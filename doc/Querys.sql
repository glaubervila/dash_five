
-- Total de Tickets
SELECT COUNT(*) FROM sale_ticket;

-- Total de Tickets Cancelados
SELECT COUNT(*) FROM sale_ticket WHERE is_canceled is TRUE;

-- Total de Vendas NAO canceladas
SELECT SUM(amount) FROM sale_ticket WHERE is_canceled is FALSE;

-- Ticket Medio (somente nao cancelados)
SELECT AVG(amount) FROM sale_ticket WHERE is_canceled is FALSE;

-- Total de Vendas canceladas
SELECT SUM(amount) FROM sale_ticket WHERE is_canceled is TRUE;

-- Total de Vendas por Loja
SELECT b.name, b.number, CONVERT(SUM(a.amount), DECIMAL(15,3)) as amount FROM sale_ticket a INNER JOIN market_store b ON (a.store_id = b.id) WHERE is_canceled is FALSE GROUP BY store_id;

-- Ticket Medio por Loja
SELECT b.name, b.number, CONVERT(AVG(a.amount), DECIMAL(15,3)) as amount FROM sale_ticket a INNER JOIN market_store b ON (a.store_id = b.id) WHERE is_canceled is FALSE GROUP BY store_id;

-- Total de descontos por Loja
SELECT b.name, b.number, CONVERT(SUM(a.discount), DECIMAL(15,3)) as discount FROM sale_ticket a INNER JOIN market_store b ON (a.store_id = b.id) WHERE is_canceled is FALSE GROUP BY store_id;

