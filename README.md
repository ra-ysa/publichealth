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
* Deborah Sadetsky - 150912
* Raysa Masson Benatti - 176483

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
~~~

### Seleção de dados
Inicialmente, o conjunto de dados escolhidos para basear a análise era composto pelos seguintes datasets:
- [IBGE](https://mapasinterativos.ibge.gov.br/covid/saude/ "IBGE"): enfermeiros, médicos e leitos de UTI por estado e por município. Dados processados a partir do CNES (Cadastro Nacional de Estabelecimentos de Saúde)/Datasus, referentes a dezembro de 2019;
- [COFEN](http://www.cofen.gov.br/enfermagem-em-numeros "COFEN"): profissionais de enfermagem (enfermeiros, auxiliares, técnicos e obstetrizes) por estado, referentes a maio de 2020. A origem dos dados não é explicitada, mas pressupõe-se ser a quantidade de inscrições ativas no conselho; 
- [Fiocruz](https://bigdata-metadados.icict.fiocruz.br/dataset/cadastro-nacional-de-estabelecimentos-de-saude-cnes "Fiocruz"): CNES - tabelas detalhadas com dados referentes a todos os estabelecimentos de saúde cadastrados no país, originados do Datasus, atualizado em dezembro de 2019. A ideia inicial era usá-lo para extrair informações sobre hospitais, ainda não processadas pelo IBGE. Dados crus, não processados;
- [OCDE](https://stats.oecd.org/index.aspx?DataSetCode=HEALTH_REAC "OCDE") e [OMS](https://www.who.int/data/gho/data/indicators "OMS"): indicadores de saúde de diversos países para comparações que enriquecessem a análise.

Uma observação mais cuidadosa nos permitiu notar que:
- O portal [Tabnet/Datasus](http://www2.datasus.gov.br/DATASUS/index.php?area=02 "Tabnet Datasus") tem dados mais atualizados que aqueles processados pelo IBGE; sua última atualização é de maio de 2020. O IBGE tem como diferencial ter adicionado colunas com densidade de recursos por população e população absoluta para cada entrada (município ou estado); porém, os dados do Datasus são suficientemente limpos e organizados, e valem a pena pela atualidade e possibilidade de customização de tabulações no site, razão pela qual optamos, então, por utilizá-los no lugar das tabelas do IBGE e da Fiocruz (a última traria, ainda, dificuldades adicionais de processamento pelo tamanho). Duas tabelas do IBGE foram mantidas apenas para facilitar a extração do número de habitantes de cada estado e município (que achamos razoável julgar não ter sido atualizado entre dezembro/2019 e maio/2020);
- As informações fornecidas pelo COFEN divergem daquelas que constam no Datasus. A título de exemplo: o COFEN acusa a existência de 565458 enfermeiros no país; para o Datasus, são 282634 no mesmo mês de referência (maio/2020). Considerando que o último [reporta dados fornecidos pelas secretarias municipais e estaduais de saúde](http://tabnet.datasus.gov.br/cgi/cnes/NT_RecursosHumanos.htm "Nota Técnica"), levantamos a hipótese de que a diferença se deve à existência de profissionais registrados no Conselho sem atuar, ou atuando fora de estabelecimentos de saúde. Diante disso, e em prol da consistência na análise, optamos por descartar o dataset do COFEN, usando os do Datasus também para recuperar informações sobre profissionais de enfermagem. Ressaltamos, contudo, que os números reportados pelo país à OMS são compatíveis com os do Conselho, não com os do Datasus (e desconhecemos a metodologia de report dos demais países);
- Os dados da OCDE e os da OMS são redundantes, sendo que os da OMS são mais completos. Assim, optamos por descartar os datasets da OCDE, mantendo apenas os da OMS para comparações com outros países;
- Nem OCDE nem OMS têm informações globais sobre leitos de UTI. Tais órgãos reportam apenas estatísticas sobre hospitais e leitos de hospitais de modo geral (sem especificar, contudo, se esses leitos incluem os de UTI). Assim, a comparação desse indicador entre o Brasil (cujas informações são facilmente discrimináveis no Datasus) e outros países restaria prejudicada; há, ainda, [referências](https://github.com/ra-ysa/publichealth/blob/master/references/2012-prin-wunsch.pdf "Prin, Wunsch 2012") que questionam esse tipo de comparação em nível internacional dada a ausência de padronização nas definições referentes a <i>critical care</i> em diferentes países e regiões. Diante disso, concluímos que comparações na escala internacional considerando leitos de UTI não seriam informativas; optamos, assim, por limitar a análise desse indicador ao âmbito nacional, e efetuar comparações com outros países somente para os outros indicadores (médicos, profissionais de enfermagem e hospitais), para os quais parece existir uma homogeneidade de dados aceitável. 

Com essas ressalvas levadas em consideração, a seleção final de dados é a que se encontra descrita na seção [<b>Bases de Dados</b>](#bases-de-dados).


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
