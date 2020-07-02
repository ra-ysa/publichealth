# gera estatisticas a partir dos dados de entrada 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

# lista de indices que representam as regioes brasileiras em dataset_uf
indices_regioes = [0, 8, 18, 23, 27]
# lista de indices que representam os estados brasileiros em dataset_uf
indices_estados = [1, 2, 3, 4, 5, 6, 7,
					9, 10, 11, 12, 13, 14, 15, 16, 17,
					19, 20, 21, 22,
					24, 25, 26,
					28, 29, 30, 31]

# plota distribuicao dos recursos selecionados
def barh_discrete(resultados, categorias):
	labels = list(resultados.keys())
	data = np.array(list(resultados.values()))
	data_cum = data.cumsum(axis=1)
	category_colors = plt.get_cmap('RdYlGn')(
        np.linspace(0.15, 0.85, data.shape[1]))
	fig, ax = plt.subplots(figsize=(12, 6.5))
	ax.invert_yaxis()
	#ax.xaxis.set_visible(False)
	ax.set_xlim(0, np.sum(data, axis=1).max())
	for i, (colname, color) in enumerate(zip(categorias, category_colors)):
		widths = data[:, i]
		starts = data_cum[:, i] - widths
		ax.barh(labels, widths, left=starts, height=0.5,
                label=colname, color=color)
		xcenters = starts + widths / 2
		r, g, b, _ = color
		text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
		for y, (x, c) in enumerate(zip(xcenters, widths)):
			ax.text(x, y, str(int(c)), ha='center', va='center',
                    color=text_color)
	ax.set_xlabel("% por região", labelpad = 20)
	ax.legend(ncol=len(categorias), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small')

# devolve lista com % do recurso selecionado em relacao ao total
def recurso_percent(recurso, dataset):
	recurso_percent = []
	total = dataset[recurso].sum()
	for i in range(len(dataset)):
		percent = (dataset[recurso].iloc[i] / total) * 100
		recurso_percent.append(percent)
	return recurso_percent

# devolve n maiores elementos para um recurso escolhido
def recurso_nmax(n, recurso, nome, dataset):
    df = dataset.nlargest(n, recurso)
    df = df[[nome, recurso]]
    return df

# devolve n menores elementos para um recurso escolhido
def recurso_nmin(n, recurso, nome, dataset):
	# no dataset mundial, 0->sem dado
	# vamos filtrar essas linhas
	if(nome == "País"):
		dataset = dataset[dataset[recurso] > 0]
	df = dataset.nsmallest(n, recurso)
	df = df[[nome, recurso]]
	return df

# devolve boxplot 
def boxplot(recurso, dataset):
	pass  

# devolve % de municipios que nao possuem um determinado recurso (valor==0)
def percent_zero(dataset, recurso):
	tam_df = len(dataset)
	sem_recurso = dataset[dataset[recurso] == 0]
	tam_sem_recurso = len(sem_recurso)
	porcentagem = (tam_sem_recurso / tam_df)*100
	return round(porcentagem, 2)

# devolve a densidade (quantidade a cada 10k ou 100k habitantes) do recurso selecionado para o Brasil todo
def densidade_geral(dataset, recurso):
	denominador = 10000
	# para hospitais, usamos 100k em vez de 10k
	if("Hospitais" in recurso):
		denominador = 100000
	pop_rel_sum = dataset["População"].sum() / denominador
	recurso_sum = dataset[recurso].sum()
	densidade = recurso_sum / pop_rel_sum 
	qtd_pessoas_para_1 = denominador / densidade 
	return round(densidade, 2), round(qtd_pessoas_para_1, 2)

def stats_municipios(dataset_mun):
	print(recurso_nmax(5, "Médicos a cada 10k habitantes", "Município", dataset_mun))
	print(recurso_nmin(5, "Enfermeiros - Total", "Município", dataset_mun))
	print(percent_zero(dataset_mun, "Hospitais - Total"))
	print(densidade_geral(dataset_mun, "Enfermeiros - Total"))

def stats_estados(dataset_uf_reg):
	# extrai apenas regioes
	dataset_reg = dataset_uf_reg.loc[[0, 8, 18, 23, 27], :]
	# extrai apenas estados 
	dataset_uf = dataset_uf_reg.loc[[1, 2, 3, 4, 5, 6, 7,
					9, 10, 11, 12, 13, 14, 15, 16, 17,
					19, 20, 21, 22,
					24, 25, 26,
					28, 29, 30, 31], :]

	# plota % de enfermeiros e medicos sus vs regiao
	x = dataset_reg["Região ou UF"]
	y1 = dataset_reg["%" + " de enfermeiros SUS"]
	y2 = dataset_reg["%" + " de médicos SUS"]

	fig, ax = plt.subplots(figsize=(10, 6.5))
	ax.scatter(x, y1, linewidth=2, label="Enfermeiros")
	ax.scatter(x, y2, linewidth=2, label="Médicos")
		
	ax.set_ylim(bottom=0, top=100)
	fig.autofmt_xdate()
	ax.set_title("%" + " de médicos e enfermeiros que atendem no SUS por região, em relação ao total de sua categoria")
	ax.set_ylabel("%")
	plt.legend(loc="lower right")
	plt.savefig("../assets/gráficos/%_enfmed_sus.png")

	# plota % de hospitais públicos por região
	x = dataset_reg["Região ou UF"]
	y = dataset_reg["%" + " de hospitais públicos"]

	fig, ax = plt.subplots()
	ax.scatter(x, y, linewidth=2)
		
	ax.set_ylim(bottom=0, top=100)
	fig.autofmt_xdate()
	ax.set_title("%" + " de hospitais públicos por região")
	ax.set_ylabel("%")
	plt.savefig("../assets/gráficos/%_hosp_publ.png")

	# plota excesso/deficit de profissionais de saude por estado
	dataset_uf.sort_values("Déficit ou excesso de médicos/enfermeiros", inplace=True)
	x = dataset_uf["Região ou UF"]
	y = dataset_uf["Déficit ou excesso de médicos/enfermeiros"]

	fig, ax = plt.subplots(figsize=(13, 6))
	ax.barh(x, y, align="center")
		
	fig.autofmt_xdate()
	ax.set_title("Déficit (-) ou excesso (+) absoluto de médicos/enfermeiros por estado*")
	ax.set_xlabel("*Densidade de referência: 44.5 profissionais (médicos + enfermeiros)/10k habitantes (OMS, 2016)",
					labelpad=30)
	plt.savefig("../assets/gráficos/deficit_excesso.png")

	# plota % de recursos por região
	categorias = dataset_reg["Região ou UF"]
	populacao = recurso_percent("População", dataset_reg)
	medicos = recurso_percent("Médicos - Total", dataset_reg)
	enfermeiros = recurso_percent("Enfermeiros - Total", dataset_reg)
	hospitais = recurso_percent("Hospitais - Total", dataset_reg)
	leitos_internacao = recurso_percent("Leitos (internação) - Total", dataset_reg)
	leitos_uti = recurso_percent("Leitos UTI - Total", dataset_reg)
	leitos_covid = recurso_percent("Leitos UTI COVID-19 - Total", dataset_reg)
	resultados = {'População': populacao,
				'Médicos': medicos,
				'Enfermeiros': enfermeiros,
				'Hospitais': hospitais,
				'Leitos internação': leitos_internacao,
				'Leitos UTI': leitos_uti,
				'Leitos UTI Covid-19': leitos_covid}
	barh_discrete(resultados, categorias)
	plt.savefig("../assets/gráficos/%_recursos_geral.png")

def stats_paises(dataset_paises):
	print(recurso_nmax(5, "Profissionais de enfermagem - Total", "País", dataset_paises))
	print(recurso_nmin(5, "Profissionais de enfermagem - Total", "País", dataset_paises))
	print(recurso_nmax(5, "Profissionais de enfermagem a cada 10k habitantes", "País", dataset_paises))
	print(recurso_nmin(5, "Profissionais de enfermagem a cada 10k habitantes", "País", dataset_paises))
	print(recurso_nmax(5, "Médicos - Total", "País", dataset_paises))
	print(recurso_nmin(5, "Médicos - Total", "País", dataset_paises))
	print(recurso_nmax(5, "Médicos a cada 10k habitantes", "País", dataset_paises))
	print(recurso_nmin(5, "Médicos a cada 10k habitantes", "País", dataset_paises))


