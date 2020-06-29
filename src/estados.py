# processa dados de granularidade estadual/regional

import pandas as pd 
import util 

def processa_estados():

	enf_uf, med_uf, hosp_uf, leitos_uf, uti_uf, uti_sus_uf, ibge_uf = util.read_uf_reg()

	# troca "-" pelo valor 0 nas celulas em que aparece
	util.dash_to_zero(enf_uf)
	util.dash_to_zero(med_uf)
	util.dash_to_zero(hosp_uf)
	util.dash_to_zero(leitos_uf)
	util.dash_to_zero(uti_uf)
	util.dash_to_zero(uti_sus_uf)

	# converte strings para valores numericos quando pertinente
	util.str_to_int(enf_uf)
	util.str_to_int(med_uf)
	util.str_to_int(hosp_uf)
	util.str_to_int(leitos_uf)
	util.str_to_int(uti_uf)
	util.str_to_int(uti_sus_uf)

	# retira linhas com informacoes desnecessarias
	util.drop(enf_uf, [-1, -1, -1])
	util.drop(med_uf, [-1, -1, -1])
	util.drop(hosp_uf, [-1, -1])
	util.drop(leitos_uf, [-1, -1])
	util.drop(uti_uf, [-1, -1])
	util.drop(uti_sus_uf, [-1, -1, -1])

	# cada bloco a seguir cria um atributo da tabela final

	nome = enf_uf["Região/Unidade da Federação"]
	# remove caracteres desnecessarios
	for i in range(len(nome)):
		nome[i] = nome[i].strip(". ")

	pop = []
	for item in ibge_uf["EST_POP_19"]:
		pop.append(item)
	# adiciona populacoes de cada regiao
	pop.insert(0, sum(ibge_uf["EST_POP_19"][0:7])) # norte
	pop.insert(8, sum(ibge_uf["EST_POP_19"][7:16])) # nordeste
	pop.insert(18, sum(ibge_uf["EST_POP_19"][16:20])) # sudeste
	pop.insert(23, sum(ibge_uf["EST_POP_19"][20:23])) # sul
	pop.insert(27, sum(ibge_uf["EST_POP_19"][23:27])) # centro-oeste

	enf_sus = enf_uf["Sim"]

	enf_nsus = enf_uf["Não"]

	enf_total = enf_uf["Total"]

	enf_sus_percent = util.percent(enf_sus, enf_total)

	enf_10k = util.pop_ratio(enf_total, 10000, pop)

	med_sus = med_uf["Sim"]

	med_nsus = med_uf["Não"]

	med_total = med_uf["Total"]

	med_sus_percent = util.percent(med_sus, med_total)

	med_10k = util.pop_ratio(med_total, 10000, pop)

	hosp_publ = []
	for i in range(len(hosp_uf)):
		hosp_publ.append(int(sum([hosp_uf["Administração Pública Federal"][i], 
						hosp_uf["Administração Pública Estadual ou Distrito Federal"][i],
						hosp_uf["Administração Pública Municipal"][i],
						hosp_uf["Administração Pública - Outros"][i],
						hosp_uf["Empresa Pública ou Sociedade de Economia Mista"][i]])))

	hosp_npubl = [] 
	for i in range(len(hosp_uf)):
		hosp_npubl.append(int(sum([hosp_uf["Demais Entidades Empresariais"][i], 
						hosp_uf["Entidades sem Fins Lucrativos"][i]])))

	hosp_total = []
	for i in range(len(hosp_uf)):
		hosp_total.append(int(hosp_publ[i] + hosp_npubl[i]))

	hosp_publ_percent = util.percent(hosp_publ, hosp_total) 

	hosp_100k = util.pop_ratio(hosp_total, 100000, pop)

	leitos_sus = []
	for i in range(len(leitos_uf)):
		leitos_sus.append(int(leitos_uf["Quantidade SUS"][i]))

	leitos_nsus = []
	for i in range(len(leitos_uf)):
		leitos_nsus.append(int(leitos_uf["Quantidade Não SUS"][i]))

	leitos_total = []
	for i in range(len(leitos_uf)):
		leitos_total.append(int(leitos_sus[i] + leitos_nsus[i]))

	leitos_sus_percent = util.percent(leitos_sus, leitos_total) 

	leitos_10k = util.pop_ratio(leitos_total, 10000, pop)

	leitos_uti_total = []
	for i in range(len(uti_uf)):
		leitos_uti_total.append(int(uti_uf["Total"][i]))

	leitos_uti_sus = uti_sus_uf["Total"]

	leitos_uti_nsus = []
	for i in range(len(leitos_uti_total)):
		leitos_uti_nsus.append(int(leitos_uti_total[i] - leitos_uti_sus[i]))

	leitos_uti_sus_percent = util.percent(leitos_uti_sus, leitos_uti_total)

	leitos_uti_10k = util.pop_ratio(leitos_uti_total, 10000, pop)

	leitos_covid_total = []
	for i in range(len(uti_uf)):
		leitos_covid_total.append(int(uti_uf["UTI adulto II COVID-19"][i] + 
							uti_uf["UTI pediátrica II COVID-19"][i]))

	leitos_covid_sus = []
	for i in range(len(uti_sus_uf)):
		leitos_covid_sus.append(int(uti_sus_uf["UTI adulto II COVID-19"][i] + 
							uti_sus_uf["UTI pediátrica II COVID-19"][i]))

	leitos_covid_nsus = []
	for i in range(len(leitos_covid_total)):
		leitos_covid_nsus.append(int(leitos_covid_total[i] - leitos_covid_sus[i]))

	leitos_covid_sus_percent = util.percent(leitos_covid_sus, leitos_covid_total)

	leitos_covid_10k = util.pop_ratio(leitos_covid_total, 10000, pop)

	dados = {'Região ou UF': nome,
		'População': pop,
		'Enfermeiros SUS': enf_sus,
		'Enfermeiros não-SUS': enf_nsus,
		'Enfermeiros - Total': enf_total,
		'%' + ' de enfermeiros SUS': enf_sus_percent,
		'Enfermeiros a cada 10k habitantes': enf_10k,
		'Médicos SUS': med_sus,
		'Médicos não-SUS': med_nsus,
		'Médicos - Total': med_total,
		'%' + ' de médicos SUS': med_sus_percent,
		'Médicos a cada 10k habitantes': med_10k,
		'Hospitais públicos': hosp_publ,
		'Hospitais não-públicos': hosp_npubl,
		'Hospitais - Total': hosp_total,
		'%' + ' de hospitais públicos': hosp_publ_percent,
		'Hospitais a cada 100k habitantes': hosp_100k,
		'Leitos (internação) SUS': leitos_sus,
		'Leitos (internação) não-SUS': leitos_nsus,
		'Leitos (internação) - Total': leitos_total,
		'%' + ' de leitos (internação) SUS': leitos_sus_percent,
		'Leitos (internação) a cada 10k habitantes': leitos_10k,
		'Leitos UTI SUS': leitos_uti_sus,
		'Leitos UTI não-SUS': leitos_uti_nsus,
		'Leitos UTI - Total': leitos_uti_total,
		'%' + ' de leitos UTI SUS': leitos_uti_sus_percent,
		'Leitos UTI a cada 10k habitantes': leitos_uti_10k,
		'Leitos UTI COVID-19 SUS': leitos_covid_sus,
		'Leitos UTI COVID-19 não-SUS': leitos_covid_nsus,
		'Leitos UTI COVID-19 - Total': leitos_covid_total,
		'%' + ' de leitos UTI COVID-19 SUS': leitos_covid_sus_percent,
		'Leitos UTI COVID-19 a cada 10k habitantes': leitos_covid_10k}

	df = pd.DataFrame(data=dados)
	util.write_to_csv(df, "Brasil - UFs e Regiões")