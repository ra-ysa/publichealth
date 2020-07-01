# processa dados de granularidade municipal

import pandas as pd 
import util 
import stats 

def processa_municipios():

	enf_mun, med_mun, hosp_mun, leitos_mun, uti_mun, uti_sus_mun, ibge_mun = util.read_mun()

	# troca "-" pelo valor 0 nas celulas em que aparece
	util.dash_to_zero(enf_mun)
	util.dash_to_zero(med_mun)
	util.dash_to_zero(hosp_mun)
	util.dash_to_zero(leitos_mun)
	util.dash_to_zero(uti_mun)
	util.dash_to_zero(uti_sus_mun)

	# converte strings para valores numericos quando pertinente
	util.str_to_int(enf_mun)
	util.str_to_int(med_mun)
	util.str_to_int(hosp_mun)
	util.str_to_int(leitos_mun)
	util.str_to_int(uti_mun)
	util.str_to_int(uti_sus_mun)

	# retira linhas com informacoes desnecessarias
	util.drop(enf_mun, [-1, -1, -1])
	util.drop(med_mun, [-1, -1, -1])
	util.drop(hosp_mun, [-1, -1, -1])
	util.drop(leitos_mun, [-1, -1, -1])
	util.drop(uti_mun, [-1, -1, -1])
	util.drop(uti_sus_mun, [-1, -1, -1])
	util.drop_mun(enf_mun)
	util.drop_mun(med_mun)
	util.drop_mun(hosp_mun)
	util.drop_mun(leitos_mun)
	util.drop_mun(uti_mun)
	util.drop_mun(uti_sus_mun)

	# adiciona informacao sobre sigla correspondente a cada codigo uf
	siglas_uf = util.cod_to_uf(ibge_mun)
	ibge_mun["NM_UF"] = siglas_uf

	# remove ultimo digito do codigo municipal do dataset do ibge
	# o objetivo eh igualar ao codigo municipal dos datasets do datasus
	for i in range(len(ibge_mun)):
		ibge_mun.at[i, "CD_MUN"] = ibge_mun["CD_MUN"][i]//10

	# cada bloco a seguir cria um atributo da tabela final

	cod = []
	for i in range(len(enf_mun)):
		cod.append(int(enf_mun["Município"][i][0:7])) # primeiros seis digitos

	nome = []
	for i in range(len(enf_mun)):
		nome.append(enf_mun["Município"][i][7:]) # todos os digitos menos 7 primeiros (6 do codigo + espaco)

	pop = []
	# insere na ordem dos datasets do datasus
	for i in range(len(cod)):
		# pop_cod = populacao registrada para a linha em que cd_mun == cod[i]
		pop_cod = ibge_mun["EST_POP_19"][ibge_mun["CD_MUN"] == cod[i]].iloc[0]
		pop.append(pop_cod)
	
	uf = []
	# insere na ordem dos datasets do datasus
	for i in range(len(cod)):
		# uf_cod = sigla da uf registrada para a linha em que cd_mun == cod[i]
		uf_cod = ibge_mun["NM_UF"][ibge_mun["CD_MUN"] == cod[i]].iloc[0]
		uf.append(uf_cod)

	enf_sus = enf_mun["Sim"]

	enf_nsus = enf_mun["Não"]

	enf_total = enf_mun["Total"]

	enf_sus_percent = util.percent(enf_sus, enf_total)

	enf_10k = util.pop_ratio(enf_total, 10000, pop)

	med_sus = med_mun["Sim"]

	med_nsus = med_mun["Não"]

	med_total = med_mun["Total"]

	med_sus_percent = util.percent(med_sus, med_total)

	med_10k = util.pop_ratio(med_total, 10000, pop)

	hosp_publ = []
	for i in range(len(hosp_mun)):
		hosp_publ.append(int(sum([hosp_mun["Administração Pública Federal"][i], 
						hosp_mun["Administração Pública Estadual ou Distrito Federal"][i],
						hosp_mun["Administração Pública Municipal"][i],
						hosp_mun["Administração Pública - Outros"][i],
						hosp_mun["Empresa Pública ou Sociedade de Economia Mista"][i]])))

	hosp_npubl = [] 
	for i in range(len(hosp_mun)):
		hosp_npubl.append(int(sum([hosp_mun["Demais Entidades Empresariais"][i], 
						hosp_mun["Entidades sem Fins Lucrativos"][i]])))

	hosp_total = []
	for i in range(len(hosp_mun)):
		hosp_total.append(int(hosp_publ[i] + hosp_npubl[i]))

	hosp_publ_percent = util.percent(hosp_publ, hosp_total) 

	hosp_100k = util.pop_ratio(hosp_total, 100000, pop)

	leitos_sus = leitos_mun["Quantidade SUS"]

	leitos_nsus = leitos_mun["Quantidade Não SUS"]

	leitos_total = []
	for i in range(len(leitos_mun)):
		leitos_total.append(int(leitos_sus[i] + leitos_nsus[i]))

	leitos_sus_percent = util.percent(leitos_sus, leitos_total) 

	leitos_10k = util.pop_ratio(leitos_total, 10000, pop)

	leitos_uti_total = uti_mun["Total"]

	leitos_uti_sus = uti_sus_mun["Total"]

	leitos_uti_nsus = []
	for i in range(len(leitos_uti_total)):
		leitos_uti_nsus.append(int(leitos_uti_total[i] - leitos_uti_sus[i]))

	leitos_uti_sus_percent = util.percent(leitos_uti_sus, leitos_uti_total)

	leitos_uti_10k = util.pop_ratio(leitos_uti_total, 10000, pop)

	leitos_covid_total = []
	for i in range(len(uti_mun)):
		leitos_covid_total.append(int(uti_mun["UTI adulto II COVID-19"][i] + 
							uti_mun["UTI pediátrica II COVID-19"][i]))

	leitos_covid_sus = []
	for i in range(len(uti_sus_mun)):
		leitos_covid_sus.append(int(uti_sus_mun["UTI adulto II COVID-19"][i] + 
							uti_sus_mun["UTI pediátrica II COVID-19"][i]))

	leitos_covid_nsus = []
	for i in range(len(leitos_covid_total)):
		leitos_covid_nsus.append(int(leitos_covid_total[i] - leitos_covid_sus[i]))

	leitos_covid_sus_percent = util.percent(leitos_covid_sus, leitos_covid_total)

	leitos_covid_10k = util.pop_ratio(leitos_covid_total, 10000, pop)

	# deficit ou excesso de profissionais de saude no municipio
	# em relacao a densidade populacional
	# considerando referencia oms (health workforce requirements, 2016)
	# recomendado = 44.5 medicos/enfs a cada 10k habitantes 
	rel_prof_saude_recomend = []
	recomend = 44.5
	for i in range(len(enf_total)):
		med_e_enf_10k = med_10k[i] + enf_10k[i]
		dfca = med_e_enf_10k - recomend # valor pos indica excesso; valor neg indica deficit
		rel_prof_saude_recomend.append(round((dfca*pop[i])/10000, 2))


	dados = {'Código Municipal': cod,
		'Município': nome,
		'População': pop,
		'UF': uf,
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
		'Déficit ou excesso de médicos/enfermeiros': rel_prof_saude_recomend,
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
	util.write_to_csv(df, "Brasil - Municípios")
	stats.stats_municipios(df)