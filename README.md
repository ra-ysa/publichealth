# publichealth

# Projeto `<Título em Português>`
# Project `<Title in English>`

# Descrição Resumida do Projeto
~~~
<Descreva resumidamente o que fará o projeto. O resumo idealmente deve: apresentar o contexto; indicar o problema; apresentar a sua solução para o problema; indicar porque a sua solução é melhor do que os esforços atuais (não obrigatório); concluir com os resultados alcançados.>
~~~

# Abstract in English
~~~
<English version of the abstract.>
~~~

# Equipe
* `<nome completo>` - `<RA>`

# Vídeo do Projeto
`<coloque um link para o vídeo apresentado o projeto.>`

# Introdução e Motivação
~~~
<Descrição do tema do projeto, incluindo motivação, contexto gerador e caracterização do problema. A introdução também pode apresentar iniciativas correlatas para lidar com o problema (não obrigatório) e deve introduzir de forma mais detalhada que o resumo a solução proposta e resultados alcançados. Aqui também são apresentadas as seções do projeto.>
~~~

## Perguntas de Pesquisa
~~~
<Perguntas de pesquisa que o projeto pretende responder ou hipóteses a serem avaliadas, enunciadas de maneira objetiva e verificável.>
~~~

## Objetivos do projeto
~~~
<Como seu projeto propôs abordar o problema apresentado.>
~~~

# Recursos e Métodos

## Bases de Dados
`<Elencar bases de dados utilizadas no projeto preferencialmente no formato da tabela a seguir.>`
Base de Dados | Endereço na Web | Resumo descritivo e uso
----- | ----- | -----
Base 1 | http://base1.org/ | `<Descrição da Base 1 e para que ela foi usada no projeto.>`
Base 2 | http://base2.org/ | `<Descrição da Base 2 e para que ela foi usada no projeto.>`

## Ferramentas

`<Elencar ferramentas utilizadas no projeto preferencialmente no formato da tabela a seguir.>`
Ferramenta | Endereço na Web | Resumo descritivo e uso
----- | ----- | -----
Ferramenta 1 | http://ferramenta1.org/ | `<Descrição da Ferramenta 1 e para que ela foi usada no projeto.>`
Ferramenta 2 | http://ferramenta2.org/ | `<Descrição da Ferramenta 2 e para que ela foi usada no projeto.>`

# Metodologia
~~~
<Abordagem/metodologia adotada, incluindo especificação de quais técnicas foram exploradas, tais como: aprendizagem de máquina, análise de redes, análise estatística, ou integração de uma ou mais técnicas.>
~~~

## Detalhamento do Projeto
~~~
<Apresente aqui detalhes da análise. Nesta seção ou na seção de Resultados podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.

Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.>
~~~

~~~python
df = pd.read_excel("/content/drive/My Drive/Colab Notebooks/dataset.xlsx");
sns.set(color_codes=True);
sns.distplot(df.Hemoglobin);
plt.show();
~~~

## Evolução do Projeto
~~~
<Relate a evolução do projeto: possíveis problemas enfrentados e possíveis mudanças de trajetória. Relatar o processo para se alcançar os resultados é tão importante quanto os resultados.>

### Seleção de dados
Rascunho:
1- selecionamos, a princípio, os seguintes dados:
IBGE - enfermeiros, médicos e leitos de UTI por estado e por município (https://mapasinterativos.ibge.gov.br/covid/saude/). São dados processados a partir de dados do CNES (Datasus), referentes a dezembro de 2019.
COFEN - Enfermeiros por estado (http://www.cofen.gov.br/enfermagem-em-numeros)
CNES (Datasus/Fiocruz), para extrair informações sobre hospitais, ainda não processadas pelo IBGE (https://bigdata-metadados.icict.fiocruz.br/dataset/cadastro-nacional-de-estabelecimentos-de-saude-cnes)
Para comparações com outros países: OCDE (https://stats.oecd.org/index.aspx?DataSetCode=HEALTH_REAC) e OMS (https://www.who.int/data/gho/data/indicators)

2- Observando com mais cuidado, notamos que:
- O Tabnet/Datasus tem dados mais atualizados que aqueles processados pelo IBGE (maio/2020). O IBGE tem como diferencial ter criado colunas com infos sobre população e densidade. Mas isso é relativamente trivial de fazer, e os dados do Datasus são suficientemente limpos e organizados. Então, optamos por pegar de lá, pela atualidade. (Pegamos, inclusive, sobre hospitais, nos permitindo dispensar os arquivos da Fiocruz, não processados, que seriam mais difíceis/custosos pra extrair infos)
- O COFEN tem infos discrepantes em relação ao Datasus. O Datasus tem dados fornecidos pelas secretarias municipais e estaduais de saúde (http://tabnet.datasus.gov.br/cgi/cnes/NT_RecursosHumanos.htm). O COFEN não especifica, mas é razoável imaginar que se trata daqueles registrados no conselho (pois seus números reportados são muito maiores que os do Datasus - ou seja, deve ter gente registrada que não necessariamente atua, ou atua mas não em estabelecimentos de saúde). Com isso, optamos por dropar os dados do COFEN e focar naqueles do Datasus. (Vale lembrar, porém, que, aparentemente, pelas quantidades, os dados reportados à OMS quanto a enfermeiros provavelmente do conselho; não sabemos como é a metodologia de report dos outros países)
Optar por usar os dados do Tabnet/Datasus pra tudo, além de facilitar, tb é importante pela consistência, então vamos focar só neles mesmo. 
- Infos da OCDE são redundantes em relação às da OMS, que são mais completas, então vamos usar só OMS
Assim, restamos com: Datasus e OMS, apenas

- Nem OMS nem OCDE têm infos globais sobre leitos de UTI especificamente, apenas "hospitals" e "hospital beds" (não sei se o último inclui leitos de UTI tb). No Datasus, dá pra separar. 

~~~

# Resultados e Discussão
~~~
<Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

A discussão dos resultados também pode ser feita aqui na medida em que os resultados são apresentados ou em seção independente. Aspectos importantes a serem discutidos: É possível tirar conclusões dos resultados? Quais? Há indicações de direções para estudo? São necessários trabalhos mais profundos?>
~~~

# Conclusões
~~~
<Apresente aqui as conclusões finais do trabalho e as lições aprendidas.>
~~~

# Trabalhos Futuros
~~~
<Indique trabalhos futuros a partir do ponto alcançado.>
~~~
