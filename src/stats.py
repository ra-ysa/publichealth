# gera estatisticas a partir dos dados de entrada 
import pandas as pd 
import matplotlib.pyplot as plt

# lista de indices que representam as regioes brasileiras em dataset_uf
indices_regioes = [0, 8, 18, 23, 27]
# lista de indices que representam os estados brasileiros em dataset_uf
indices_estados = [1, 2, 3, 4, 5, 6, 7,
					9, 10, 11, 12, 13, 14, 15, 16, 17,
					19, 20, 21, 22,
					24, 25, 26,
					28, 29, 30, 31]

def stats_municipios(dataset_mun):
	print("ok1")

def stats_estados(dataset_uf_reg):
	# extrai apenas regioes
	dataset_reg = dataset_uf_reg.loc[[0, 8, 18, 23, 27], :]
	dataset_uf = dataset_uf_reg.loc[[1, 2, 3, 4, 5, 6, 7,
					9, 10, 11, 12, 13, 14, 15, 16, 17,
					19, 20, 21, 22,
					24, 25, 26,
					28, 29, 30, 31], :]

	# plota % de enfermeiros e medicos sus vs regiao
	x = dataset_reg["Região ou UF"]
	y1 = dataset_reg["%" + " de enfermeiros SUS"]
	y2 = dataset_reg["%" + " de médicos SUS"]

	fig, ax = plt.subplots()
	ax.scatter(x, y1, linewidth=2, label="Enfermeiros")
	ax.scatter(x, y2, linewidth=2, label="Médicos")
		
	ax.set_ylim(bottom=0, top=100)
	fig.autofmt_xdate()
	ax.set_title("%" + " de médicos e enfermeiros que atendem no SUS por região, em relação ao total de sua categoria")
	ax.set_ylabel("%")
	plt.legend(loc="lower right")
	plt.show()

	# plota % de hospitais públicos por região
	x = dataset_reg["Região ou UF"]
	y = dataset_reg["%" + " de hospitais públicos"]

	fig, ax = plt.subplots()
	ax.scatter(x, y, linewidth=2)
		
	ax.set_ylim(bottom=0, top=100)
	fig.autofmt_xdate()
	ax.set_title("%" + " de hospitais públicos por região")
	ax.set_ylabel("%")
	plt.show()

	# plota excesso/deficit de profissionais de saude por estado
	dataset_uf.sort_values("Déficit ou excesso de médicos/enfermeiros", inplace=True)
	x = dataset_uf["Região ou UF"]
	y = dataset_uf["Déficit ou excesso de médicos/enfermeiros"]

	fig, ax = plt.subplots()
	ax.barh(x, y, align="center")
		
	fig.autofmt_xdate()
	ax.set_title("Déficit ou excesso absoluto de médicos/enfermeiros por estado")
	plt.show()

def stats_paises(dataset_paises):
	print("ok3") 



