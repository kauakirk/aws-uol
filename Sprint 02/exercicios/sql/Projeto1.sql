-- (Query 1) Leads, vendas, receita, conversão e ticket médio por mês
-- Define dois CTEs (Common Table Expressions):
-- "leads": Contagem de visitas por mês.
-- "payments": Contagem de vendas, cálculo da receita e valores relacionados por mês.
-- Combina os CTEs para calcular leads, vendas, receita em milhares (k), conversão e ticket médio por mês.
with 
	leads as (
		select
			date_trunc('month', visit_page_date)::date as visit_page_month, -- Agrupa visitas por mês.
			count(*) as visit_page_count -- Contagem de visitas no mês.
		from sales.funnel
		group by visit_page_month
		order by visit_page_month
	),
	
	payments as (
		select
			date_trunc('month', fun.paid_date)::date as paid_month, -- Agrupa vendas por mês.
			count(fun.paid_date) as paid_count, -- Contagem de vendas no mês.
			sum(pro.price * (1+fun.discount)) as receita -- Soma a receita, considerando os descontos.
		from sales.funnel as fun
		left join sales.products as pro
			on fun.product_id = pro.product_id
		where fun.paid_date is not null -- Apenas vendas realizadas.
		group by paid_month
		order by paid_month
	)
	
select
	leads.visit_page_month as "mês", -- Mês da análise.
	leads.visit_page_count as "leads (#)", -- Contagem de leads por mês.
	payments.paid_count as "vendas (#)", -- Contagem de vendas por mês.
	(payments.receita/1000) as "receita (k, R$)", -- Receita total em milhares.
	(payments.paid_count::float/leads.visit_page_count::float) as "conversão (%)", -- Taxa de conversão (vendas/leads).
	(payments.receita/payments.paid_count/1000) as "ticket médio (k, R$)" -- Valor médio por venda, em milhares.
from leads
left join payments
	on leads.visit_page_month = paid_month -- Combina leads e vendas por mês.

-- (Query 2) Top 5 estados brasileiros com mais vendas em agosto de 2021
select
	'Brazil' as país, -- Define o país como fixo 'Brazil'.
	cus.state as estado, -- Estado do cliente.
	count(fun.paid_date) as "vendas (#)" -- Contagem de vendas.
from sales.funnel as fun
left join sales.customers as cus
	on fun.customer_id = cus.customer_id
where paid_date between '2021-08-01' and '2021-08-31' -- Limita para o mês de agosto de 2021.
group by país, estado
order by "vendas (#)" desc -- Ordena por número de vendas em ordem decrescente.
limit 5 -- Limita o resultado aos 5 estados com mais vendas.

-- (Query 3) Top 5 marcas com mais vendas em agosto de 2021
select
	pro.brand as marca, -- Nome da marca do produto.
	count(fun.paid_date) as "vendas (#)" -- Contagem de vendas por marca.
from sales.funnel as fun
left join sales.products as pro
	on fun.product_id = pro.product_id
where paid_date between '2021-08-01' and '2021-08-31' -- Limita para o mês de agosto de 2021.
group by marca
order by "vendas (#)" desc -- Ordena por número de vendas em ordem decrescente.
limit 5 -- Limita o resultado às 5 marcas mais vendidas.

-- (Query 4) Top 5 lojas com mais vendas em agosto de 2021
select
	sto.store_name as loja, -- Nome da loja.
	count(fun.paid_date) as "vendas (#)" -- Contagem de vendas por loja.
from sales.funnel as fun
left join sales.stores as sto
	on fun.store_id = sto.store_id
where paid_date between '2021-08-01' and '2021-08-31' -- Limita para o mês de agosto de 2021.
group by loja
order by "vendas (#)" desc -- Ordena por número de vendas em ordem decrescente.
limit 5 -- Limita o resultado às 5 lojas com mais vendas.

-- (Query 5) Visitas por dia da semana em agosto de 2021
select
	extract('dow' from visit_page_date) as dia_semana, -- Extrai o dia da semana (0=domingo, 6=sábado).
	case 
		when extract('dow' from visit_page_date)=0 then 'domingo'
		when extract('dow' from visit_page_date)=1 then 'segunda'
		when extract('dow' from visit_page_date)=2 then 'terça'
		when extract('dow' from visit_page_date)=3 then 'quarta'
		when extract('dow' from visit_page_date)=4 then 'quinta'
		when extract('dow' from visit_page_date)=5 then 'sexta'
		when extract('dow' from visit_page_date)=6 then 'sábado'
		else null end as "dia da semana", -- Converte o número do dia para o nome.
	count(*) as "visitas (#)" -- Contagem de visitas por dia da semana.
from sales.funnel
where visit_page_date between '2021-08-01' and '2021-08-31' -- Limita para o mês de agosto de 2021.
group by dia_semana
order by dia_semana -- Ordena pelos dias da semana (0 a 6).
