-- Obtém o número de leads (clientes potenciais) por gênero
select
	case
		when ibge.gender = 'male' then 'homens' -- Renomeia gênero masculino para 'homens'
		when ibge.gender = 'female' then 'mulheres' -- Renomeia gênero feminino para 'mulheres'
	end as "gênero",
	count(*) as "leads (#)" -- Conta o número total de leads por gênero

from sales.customers as cus
left join temp_tables.ibge_genders as ibge
	on lower(cus.first_name) = lower(ibge.first_name) -- Relaciona os primeiros nomes ignorando diferenciação de maiúsculas/minúsculas
group by ibge.gender -- Agrupa por gênero para a contagem


-- Calcula a porcentagem de leads por status profissional
select
	case
		when professional_status = 'freelancer' then 'freelancer' -- Renomeia status para português
		when professional_status = 'retired' then 'aposentado(a)'
		when professional_status = 'clt' then 'clt'
		when professional_status = 'self_employed' then 'autônomo(a)'
		when professional_status = 'other' then 'outro'
		when professional_status = 'businessman' then 'empresário(a)'
		when professional_status = 'civil_servant' then 'funcionário(a) público(a)'
		when professional_status = 'student' then 'estudante'
	end as "status profissional",
	(count(*)::float)/(select count(*) from sales.customers) as "leads (%)" -- Calcula a porcentagem de leads

from sales.customers
group by professional_status -- Agrupa por status profissional
order by "leads (%)" -- Ordena pela porcentagem de leads


-- Calcula a distribuição de leads por faixa etária
select
	case
		when datediff('years', birth_date, current_date) < 20 then '0-20' -- Faixa etária de 0 a 20 anos
		when datediff('years', birth_date, current_date) < 40 then '20-40' -- Faixa etária de 20 a 40 anos
		when datediff('years', birth_date, current_date) < 60 then '40-60' -- Faixa etária de 40 a 60 anos
		when datediff('years', birth_date, current_date) < 80 then '60-80' -- Faixa etária de 60 a 80 anos
		else '80+' -- Faixa etária acima de 80 anos
	end "faixa etária",
	count(*)::float/(select count(*) from sales.customers) as "leads (%)" -- Calcula a porcentagem de leads

from sales.customers
group by "faixa etária" -- Agrupa por faixa etária
order by "faixa etária" desc -- Ordena decrescentemente pela faixa etária


-- Calcula a distribuição de leads por faixa salarial
select
	case
		when income < 5000 then '0-5000' -- Faixa salarial de 0 a 5000
		when income < 10000 then '5000-10000'
		when income < 15000 then '10000-15000'
		when income < 20000 then '15000-20000'
		else '20000+' -- Faixa salarial acima de 20000
	end "faixa salarial",
	count(*)::float/(select count(*) from sales.customers) as "leads (%)", -- Calcula a porcentagem de leads
	case
		when income < 5000 then 1 -- Ordena faixas salariais numericamente
		when income < 10000 then 2
		when income < 15000 then 3
		when income < 20000 then 4
		else 5
	end "ordem"

from sales.customers
group by "faixa salarial", "ordem" -- Agrupa por faixa salarial e ordem
order by "ordem" desc -- Ordena decrescentemente pela ordem


-- Classifica veículos como novos ou seminovos com base na idade do modelo
with
	classificacao_veiculos as (
		select
			fun.visit_page_date,
			pro.model_year,
			extract('year' from visit_page_date) - pro.model_year::int as idade_veiculo, -- Calcula a idade do veículo
			case
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 2 then 'novo' -- Veículo com até 2 anos é novo
				else 'seminovo' -- Veículo com mais de 2 anos é seminovo
			end as "classificação do veículo"

		from sales.funnel as fun
		left join sales.products as pro
			on fun.product_id = pro.product_id -- Relaciona produtos e funil de vendas
	)
select
	"classificação do veículo",
	count(*) as "veículos visitados (#)" -- Conta os veículos visitados por classificação
from classificacao_veiculos
group by "classificação do veículo" -- Agrupa por classificação de veículo



-- Classifica veículos em faixas etárias com porcentagem e ordem
with
	faixa_de_idade_dos_veiculos as (
		select
			fun.visit_page_date,
			pro.model_year,
			extract('year' from visit_page_date) - pro.model_year::int as idade_veiculo, -- Calcula a idade do veículo
			case
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 2 then 'até 2 anos'
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 4 then 'de 2 à 4 anos'
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 6 then 'de 4 à 6 anos'
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 8 then 'de 6 à 8 anos'
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 10 then 'de 8 à 10 anos'
				else 'acima de 10 anos' -- Faixa etária acima de 10 anos
			end as "idade do veículo",
			case
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 2 then 1 -- Ordenação
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 4 then 2
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 6 then 3
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 8 then 4
				when (extract('year' from visit_page_date) - pro.model_year::int) <= 10 then 5
				else 6
			end as "ordem"

		from sales.funnel as fun
		left join sales.products as pro
			on fun.product_id = pro.product_id -- Relaciona produtos e funil de vendas
	)
select
	"idade do veículo",
	count(*)::float/(select count(*) from sales.funnel) as "veículos visitados (%)", -- Calcula a porcentagem
	ordem
from faixa_de_idade_dos_veiculos
group by "idade do veículo", ordem -- Agrupa por idade e ordem
order by ordem -- Ordena pela ordem

-- Lista marcas e modelos de veículos mais visitados
select
	pro.brand, -- Marca do veículo
	pro.model, -- Modelo do veículo
	count(*) as "visitas (#)" -- Conta as visitas por marca e modelo

from sales.funnel as fun
left join sales.products as pro
	on fun.product_id = pro.product_id -- Relaciona produtos e funil de vendas
group by pro.brand, pro.model -- Agrupa por marca e modelo
order by pro.brand, pro.model, "visitas (#)" -- Ordena por marca, modelo e número de visitas






