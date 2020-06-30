# ferramentas de processamento de dados pertinentes ao projeto

import pandas as pd 

# leem arquivos de dados pertinentes a cada uma das granularidades
# devolvem como dataframes 

def read_pais():
	who_doctors = pd.read_csv("../data/external/who-medical-doctors-per-country.csv")
	who_nurses = pd.read_csv("../data/external/who-nursing-personnel-per-country.csv")
	return who_doctors, who_nurses 

def read_uf_reg():
	enf_uf = pd.read_csv("../data/external/Datasus - Enfermeiros por estado.csv")
	med_uf = pd.read_csv("../data/external/Datasus - Médicos por estado.csv")
	hosp_uf = pd.read_csv("../data/external/Datasus - Hospitais por estado.csv")
	leitos_uf = pd.read_csv("../data/external/Datasus - Leitos internação por estado.csv")
	uti_uf = pd.read_csv("../data/external/Datasus - Leitos UTI por estado.csv")
	uti_sus_uf = pd.read_csv("../data/external/Datasus - Leitos UTI SUS por estado.csv")
	ibge_uf = pd.read_csv("../data/external/IBGE - Limites territoriais 2019 - UFs.csv")
	return enf_uf, med_uf, hosp_uf, leitos_uf, uti_uf, uti_sus_uf, ibge_uf

def read_mun():
	enf_mun = pd.read_csv("../data/external/Datasus - Enfermeiros por município.csv")
	med_mun = pd.read_csv("../data/external/Datasus - Médicos por município.csv")
	hosp_mun = pd.read_csv("../data/external/Datasus - Hospitais por município.csv")
	leitos_mun = pd.read_csv("../data/external/Datasus - Leitos internação por município.csv")
	uti_mun = pd.read_csv("../data/external/Datasus - Leitos UTI por município.csv")
	uti_sus_mun = pd.read_csv("../data/external/Datasus - Leitos UTI SUS por município.csv")
	ibge_mun = pd.read_csv("../data/external/IBGE - Limites territoriais 2019 - Municípios.csv") 
	return enf_mun, med_mun, hosp_mun, leitos_mun, uti_mun, uti_sus_mun, ibge_mun 

# salva o dataset como arquivo .csv no diretorio correto
def write_to_csv(dataset, nome):
	nome_csv = "../data/interim/" + nome + ".csv"
	dataset.to_csv(nome_csv)

# dicionario de codigos uf e suas respectivas siglas (ibge)
ufs = {12: "AC", 27: "AL", 16: "AP", 13: "AM", 29: "BA",
		23: "CE", 53: "DF", 32: "ES", 52: "GO", 21: "MA",
		51: "MT", 50: "MS", 31: "MG", 15: "PA", 25: "PB",
		41: "PR", 26: "PE", 22: "PI", 24: "RN", 43: "RS",
		33: "RJ", 11: "RO", 14: "RR", 42: "SC", 35: "SP",
		28: "SE", 17: "TO"}

# retira linhas desnecessarias ou sem informacao de um dataset (ex: UF desconhecida)
def drop(dataset, index_list):
	for i in range(len(index_list)):
		dataset.drop(dataset.index[index_list[i]], inplace=True)
	return dataset 

# retira linhas tipo "municipio ignorado"
def drop_mun(dataset):
	for i in range(dataset.shape[0]):
		if("ignorado" in dataset["Município"][i]):
			dataset.drop(i, inplace=True)
	dataset.reset_index(inplace=True)
	dataset.drop(["index"], axis=1, inplace=True) # remove indices antigos
	return dataset

# retira informacoes duplicadas, deixando apenas as linhas com os dados mais recentes
def drop_pais_dupl(dataset, atributo):
	dataset.drop_duplicates(subset=atributo, keep='first', inplace=True)
	dataset.reset_index(inplace=True)
	dataset.drop(["index"], axis=1, inplace=True) # remove indices antigos
	return dataset

# devolve a lista de um atributo, ordenada por um atributo ordenador
# (conforme match feito entre lista_nomes e o dataset original)
def match(lista_nomes, dataset, atributo, ordenador):
	r = []
	for i in range(len(lista_nomes)):
		if(dataset[ordenador].str.contains(lista_nomes[i], regex=False).any()):
			# valor = valor registrado para a linha em que ordenador == lista_nomes[i]
			valor = dataset[atributo][dataset[ordenador] == lista_nomes[i]].iloc[0]
			if(isinstance(valor, float)):
				r.append(round(valor, 2))
			else:
				r.append(valor)
		else:
			r.append("-")
	return r 

# converte codigo estadual para a sigla correspondente
def cod_to_uf(dataset):
	siglas_uf = []
	for i in range(len(dataset)):
		cod = dataset.at[i, "COD_UF"]
		sigla_uf = ufs.get(cod)
		siglas_uf.append(sigla_uf)
	return siglas_uf 

# substitui "-" pelo valor numerico zero
def dash_to_zero(dataset):
	for i in range(dataset.shape[0]): # para cada linha
		for j in range(dataset.shape[1]): # para cada coluna
			if(dataset.iat[i, j] == '-'):
				dataset.iat[i, j] = 0
	return dataset

# converte strings para valores numericos quando pertinente
def str_to_int(dataset):
	for i in range(dataset.shape[0]): # para cada linha
		for j in range(1, dataset.shape[1]): # para cada coluna a partir da segunda
			if(type(dataset.iat[i, j]) == str):
				dataset.iat[i, j] = int(dataset.iat[i, j])
	return dataset

# devolve lista com porcentagem de um atributo (parte) em relacao a outro (total)
def percent(parte, total):
	p = []
	for i in range(len(total)):
		if(total[i] != 0):
			p.append(round((parte[i] / total[i])*100, 2))
		else:
			p.append(0)
	return p

# devolve lista com taxa de um atributo (parte) 
# em relacao a uma determinada quantidade (denominador) da populacao (pop)
def pop_ratio(parte, denominador, pop):
	r = []
	for i in range(len(pop)):
		r.append(round((parte[i] * denominador)/pop[i], 2))
	return r
