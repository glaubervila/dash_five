from rest_framework import serializers
from .models import Nfe
from market.models import Loja

class NfeSerializer(serializers.ModelSerializer):

    emitente = serializers.PrimaryKeyRelatedField(
        queryset=Loja.objects.all(), many=False)

    emitente_nome = serializers.SerializerMethodField()

    class Meta:
        model = Nfe
        fields = (
            'id',
            'emitente',
            'emitente_nome',
            'mod',
            'serie',
            'numero',
            'data',
            'tp_operacao',
            'id_destino',
            'tp_emissao',
            'q_item',
            'v_total',
            'v_total_tributo',
            'v_total_desconto',
        )

    def get_emitente_nome(self, obj):
        try:
            return obj.emitente.nome
        except:
            return None

# # from market.models import Store, Checkout

# class NfeSerializer(serializers.ModelSerializer):
#     # store = serializers.PrimaryKeyRelatedField(
#     #     queryset=Store.objects.all(), many=False)

#     class Meta:
#         model = Nfe
#         fields = (
#             'id',
#             # 'store',
#             # 'checkout',
#             'number',
#             'date',
#             'start_time',
#             'amount',
#             'discount',
#             'is_canceled',
#         )

# class PaymentSerializer(serializers.ModelSerializer):
#     ticket = serializers.PrimaryKeyRelatedField(
#         queryset=Ticket.objects.all(), many=False)


#     class Meta:
#         model = Payment
#         fields = (
#             'id',
#             'ticket',
#             'option',
#             'value',
#             'date_time',
#             'is_canceled',
#         )
