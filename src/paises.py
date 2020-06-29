# processa dados de granularidade nacional

import pandas as pd 
import util 

def processa_paises():

	who_doctors, who_nurses = util.read_pais()

	# remove duplicatas, deixando apenas os dados mais recentes
	util.drop_pais_dupl(who_doctors, "Country")
	util.drop_pais_dupl(who_nurses, "Country")
	
	# cada bloco a seguir cria um atributo da tabela final

	# a lista de paises nao eh igual entre os datasets
	# para igualar, concatenamos e fazemos os ajustes pertinentes
	nome = []
	nome_aux = pd.concat([who_doctors["Country"], who_nurses["Country"]], join='inner', ignore_index=True)
	nome_aux.drop_duplicates(inplace=True)
	nome_series = nome_aux.reset_index() # reseta indices
	nome_series.drop(["index"], axis=1, inplace=True) # remove indices antigos
	for i in range(len(nome_series)):
		nome.append(nome_series["Country"][i])
	nome.sort(key=str.lower) # organiza em ordem alfabetica 

	med_total = util.match(nome, who_doctors, "Medical doctors (number)", "Country")

	med_10k = util.match(nome, who_doctors, "Medical doctors (per 10 000 population)", "Country")

	enf_total = util.match(nome, who_nurses, "Nursing and midwifery personnel  (number)", "Country")

	enf_10k = util.match(nome, who_nurses, "Nursing and midwifery personnel (per 10 000 population)", "Country")

	dados = {'País': nome,
		'Profissionais de enfermagem - Total': enf_total,
		'Profissionais de enfermagem a cada 10k habitantes': enf_10k,
		'Médicos - Total': med_total,
		'Médicos a cada 10k habitantes': med_10k}

	df = pd.DataFrame(data=dados)
	util.write_to_csv(df, "Mundo (OMS)")