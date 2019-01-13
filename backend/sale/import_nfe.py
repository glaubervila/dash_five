import xmltodict
import pprint
import json

from market.models import Loja
from stock.models import Produto
from sale.models import Nfe, NfProduto, NfPagamento


class ImportNF():

    def import_xml(self, filepath):

        print(filepath)

        # Ler o xml
        nf = self.xml_to_dict(filepath)
        # print(json.dumps(nf))

        # Emitente
        dEmitente = nf['nfeProc']['NFe']['infNFe']['emit']
        emitente = self.get_loja(dEmitente)

        # Dados da Nota Fiscal
        inf_nfe = nf['nfeProc']['NFe']['infNFe']['ide']
        
        # Totais
        inf_total = nf['nfeProc']['NFe']['infNFe']['total']['ICMSTot']

        # Items  
        inf_items = nf['nfeProc']['NFe']['infNFe']['det']

        # Verificar se tem mais de um item 
        if not isinstance(inf_items, list):
            inf_items = list([inf_items])
        
        # Pagamentos
        inf_pagamentos = nf['nfeProc']['NFe']['infNFe']['pag']['detPag']

        # Verificar se tem mais de um pagamento 
        if not isinstance(inf_pagamentos, list):
            inf_pagamentos = list([inf_pagamentos])
        

        self.debug_xml(inf_pagamentos)

        # Criar Model da Nota
        nota_fiscal, created = Nfe.objects.update_or_create(
            emitente=emitente,
            mod=inf_nfe['mod'],
            serie=inf_nfe['serie'],
            numero=inf_nfe['nNF'],
            defaults={
                'data': inf_nfe['dhEmi'], 
                'tp_operacao': inf_nfe['tpNF'],
                'id_destino': inf_nfe['idDest'],
                'tp_emissao': inf_nfe['tpEmis'],
                'chave_acesso': inf_nfe['cNF'],
                'chave_acesso_dv': inf_nfe['cDV'],
                'q_item': len(inf_items),
                'v_total': inf_total['vNF'],
                'v_total_tributo': inf_total['vTotTrib'],
                'v_total_desconto': inf_total['vDesc'],
            }
        )

        nota_fiscal.save()

        for inf_item in inf_items:
            inf_prod = inf_item['prod']
            inf_imposto = inf_item['imposto']

            # Identificar o Produto 
            prod = Produto.objects.get(codigo=inf_prod['cProd'])

            item, created = NfProduto.objects.update_or_create(
                nf = nota_fiscal,
                produto = prod,
                n_item = inf_item['@nItem'],
                defaults={
                    'ean': inf_prod['cEAN'],
                    'descricao': inf_prod['xProd'],
                    'ncm': inf_prod['NCM'],
                    'cfop': inf_prod['CFOP'],
                    'unidade': inf_prod['uCom'],
                    'quantidade': inf_prod['qCom'],
                    'v_unitario': inf_prod['vUnCom'],
                    'v_bruto_total': inf_prod['vProd'],
                    'u_tributavel': inf_prod['uTrib'],
                    'q_tributavel': inf_prod['qTrib'],
                    'v_unit_tributacao': inf_prod['vUnTrib'],
                    'v_total_tributo': inf_imposto['vTotTrib'],
                    'flag_total': inf_prod['indTot'],
                }
            )
            item.save()

        for inf_pagamento in inf_pagamentos:

            pagamento, create = NfPagamento.objects.update_or_create(
                nf = nota_fiscal,
                f_pagamento = inf_pagamento['tPag'],
                defaults={
                    'valor': inf_pagamento['vPag'],
                }
            )

            pagamento.save()

        return dict({
            # 'xml': nf
            'loja': emitente.nome,
            'nf': inf_pagamentos
        })

    def get_loja(self, emitente):
        # self.debug_xml(emitente)

        cnpj = emitente['CNPJ']

        lj = Loja.objects.get(cnpj=cnpj)

        return lj




    def xml_to_dict(self, filepath):
        with open(filepath) as fd:
            doc = xmltodict.parse(fd.read())
            return doc


    def debug_xml(self, xml):
        print(json.dumps(xml, indent=4))