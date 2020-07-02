# Ciência e visualização de dados em Saúde Pública: um panorama de indicadores no Brasil
## Data science and visualization in Public Health: an overview of indicators in Brazil

# Resumo
Existe uma dificuldade grande de encontrar dados de saúde pública brasileira que tenham uma visualização agradável e simples para o usuário.
Pensando nisso, decidimos buscar alguns dados, como:

- Quantidade de hospitais públicos e não públicos por estado, município e região brasileira
- Quantidade de enfermeiros do SUS ou não por estado, município e região brasileira
- Quantidade de médicos do SUS ou não por estado, município e região brasileira
- Quantidade de leitos de internação do SUS ou não por estado, município e região brasileira
- Quantidade de leitos de UTI do SUS ou não por estado, município e região brasileira
- Enfermeiros a cada 10k habitantes por estado, município e região brasileira
- Médicos a cada 10k habitantes por estado, município e região brasileira
- Hospitais a cada 100k habitantes por estado, município e região brasileira
- Leitos (internação) a cada 10k habitantes por estado, município e região brasileira
- Leitos UTI a cada 10k habitantes por estado, município e região brasileira

Com os dados em mãos, criamos visualizações em forma de *mapas de Choropleth* para conseguirmos comparar, por meio de cores as densidades de hospitais, médicos, enfermeiros, leitos e hospitais entre diferentes municípios, estados e regiões brasileras.
Além disso, também conseguimos os dados de quantidade e densidade de médicos e enfermeiros a cada 100k habitantes para diversos países, sendo possível criar uma visualização mais macro por países.

Por fim, fizemos algumas análises estatísticas com o auxílio dessas visualizações.


# Abstract
Is very difficult to find a pleasent, clean and simple visualization of brazilian public health data.
Thinking about it, we decided to look for some data, such as:

- Number of public and non-public hospitals by state, municipality and Brazilian region
- Number of SUS nurses or not by state, municipality and Brazilian region
- Number of SUS doctors or not by state, municipality and Brazilian region
- Number of SUS hospitalization beds or not by state, municipality and Brazilian region
- Number of SUS ICU beds or not by state, municipality and Brazilian region
- Nurses for every 10k inhabitants by state, municipality and Brazilian region
- Doctors for every 10k inhabitants by state, municipality and Brazilian region
- Hospitals per 100k inhabitants per state, municipality and Brazilian region
- Beds (hospitalization) for every 10k inhabitants by state, municipality and Brazilian region
- ICU beds for every 10k inhabitants by state, municipality and Brazilian region

With the data in hand, we created visualizations using * Choropleth maps* to be able to compare, through colors, the densities of hospitals, doctors, nurses, beds and hospitals between different municipalities, states and Brazilian regions.
In addition, we also obtained data of quantity and density of doctors and nurses per 100k inhabitants for different countries, making it possible to create a macro view.

Finally, using these visualizations, we made some statistical analysis.

# Equipe
* Deborah Sadetsky - 150912
* Raysa Masson Benatti - 176483

# Vídeo do Projeto
O vídeo introdutório do projeto, gravado em 10/05/2020, pode ser acessado [aqui](http://shorturl.at/eNP39 "Vídeo") (visível a pessoas logadas em e-mail com domínio Unicamp).

# Introdução e Motivação
~~~
<Descrição do tema do projeto, incluindo motivação, contexto gerador e caracterização do problema. A introdução também pode apresentar iniciativas correlatas para lidar com o problema (não obrigatório) e deve introduzir de forma mais detalhada que o resumo a solução proposta e resultados alcançados. Aqui também são apresentadas as seções do projeto.>
~~~

## Perguntas de Pesquisa
O trabalho foi guiado tendo como principal pergunta de pesquisa: <b>no contexto de avaliação de adequação da oferta de recursos essenciais em saúde pública, quão próximos estamos, no Brasil, das melhores práticas?</b>
Essa pergunta se desdobra nas seguintes questões específicas:
- Identificação das melhores práticas
  - Tendo em vista os indicadores <b>médicos</b>, <b>enfermeiros</b>, <b>hospitais</b> e <b>leitos hospitalares (inclusive de UTI)</b> e sua oferta para a população, quais são as melhores práticas e como elas são identificadas?
- Panorama da situação brasileira
  - Como é a distribuição desses recursos nos municípios, estados e regiões brasileiros? 
  - Se há desigualdade na distribuição desses recursos no país, qual é sua magnitude e quais são os lugares mais afetados por ela? 
  - Como o Brasil se compara com o resto do mundo na disponibilidade de médicos e enfermeiros à população?

## Objetivos do projeto
Além do objetivo principal de responder às perguntas de pesquisa, o trabalho se desdobra nos seguintes objetivos específicos: trazer opções para visualizar grandes quantidades de dados de saúde pública, de forma simples e didática; realizar análises estatísticas descritivas a partir dos dados coletados; criar visualizações dessas análises.

# Recursos e Métodos

## Bases de Dados

Base de Dados | Endereço na Web | Resumo descritivo e uso
----- | ----- | -----
Datasus - CNES - Recursos Humanos a partir de 2007 | https://bit.ly/380TRfF | Base de dados de recursos humanos em saúde registrados no Brasil, usada para extrair indicadores sobre recursos selecionados
Datasus - CNES - Estabelecimentos | https://bit.ly/3fSAMz1 | Base de dados de estabelecimentos de saúde registrados no Brasil, usada para extrair indicadores sobre estabelecimentos selecionados
Datasus - CNES - Recursos Físicos | https://bit.ly/2NucsY4 | Base de dados de recursos físicos em saúde registrados no Brasil, usada para extrair indicadores sobre recursos selecionados
IBGE - Limites Territoriais 2019 - UF | https://bit.ly/2NriFUL | Base de dados de informações básicas oficiais sobre cada UF brasileira, usada para extrair indicadores estaduais
IBGE - Limites Territoriais 2019 - Municípios | https://bit.ly/2Yt8gxU | Base de dados de informações básicas oficiais sobre cada município brasileiro, usada para extrair indicadores municipais
WHO/Global Health Observatory - Medical doctors | https://bit.ly/2NvJrek | Base de dados de quantidade e densidade de médicos registrados por país, para os países com dados disponíveis, usada para extrair indicadores mundiais
WHO/Global Health Observatory - Nursing and midwifery personnel | https://bit.ly/2Z4c7Rm | Base de dados de quantidade e densidade de profissionais de enfermagem registrados por país, para os países com dados disponíveis, usada para extrair indicadores mundiais
GISMAPS - GeoJSON das Grandes Regiões do Brasil 2019 | https://bit.ly/3eRAw3a | Arquivo Geojson com o mapa das Grandes Regiões do Brasil, usado para plotar visualizações
Plotly Datasets - 2014 World Gdp With Codes | https://bit.ly/31A0MLB | Base de dados com os Codes dos países, usada para auxiliar nas plotagens de visualizações
Github Sandeco - GeoJSON dos Estados brasileiros | https://bit.ly/31zk2c1 | Arquivo Geojson com o mapa das Estados do Brasil, usado para plotar visualizações
Github tbrugz - GeoJSONS dos Municípios brasileiros por estado | https://bit.ly/2NNjJlP | Arquivos Geojson com os perímetros dos municípios brasileiros dividido por estado, usados para plotar visualizações

- Os arquivos Geojson foram todos salvos no formato .json.
- Os dados da Organização Mundial da Saúde e do IBGE foram obtidos diretamente, sem filtragens, pelo download das tabelas em formato .csv.
- Os dados do Tabnet/Datasus foram obtidos selecionando-se as tabulações desejadas no formato de colunas separadas por ";", em plain text; esse conteúdo foi transferido para uma planilha em LibreOffice Calc e salvo no formato .csv, ajustando-se a codificação de caracteres para Unicode UTF-8. O ajuste foi necessário pois a exportação automática para arquivos .csv oferecida pelo site resulta em arquivos com caracteres corrompidos, devido a uma incompatibilidade na codificação.  
As tabulações escolhidas foram as seguintes:

1) CNES - Recursos Humanos a partir de 2007 > Profissionais > Brasil por Região, UF e Município > Linha: Região/UF / Coluna: Atende no SUS / Conteúdo: Quantidade / Período: Maio/2020 / Seleção: Médicos > Médico Anestesiologista, Médico Cirurgião Geral, Médico Clínico, Médico Generalista Alopata, Médico Ginecologista Obstetra, Médico da estratégia de Saúde da Família, Médico de família e comunidade, Médico Pediatra, Médico psiquiatra, Médico em radiologia e diagnóstico por imagem, Médico sanitarista, Médico acupunturista, Médico alergista e imunologista, Médico anatomopatologista, Médico angiologista, Médico broncoesofalogista, Médico Cardiologista Intervencionista, Médico cancerologista cirúrgico, Médico cancerologista clínico, Médico cancerologista pediátrico, Médico cardiologista, Médico cirurgião cardiovascular, Médico cirurgião da mão, Médico cirurgião de cabeça e pescoço, Médico cirurgião do aparelho digestivo, Médico cirurgião pediátrico, Médico cirurgião plástico, Médico cirurgião torácico, Médico cirurgião vascular, Médico citopatologista, Médico coloproctologista, Médico dermatologista, Médico do trabalho, Médico em cirurgia vascular, Médico em eletroencefalografia, Médico em endoscopia, Médico em medicina de tráfego, Médico em medicina intensiva, Médico em medicina nuclear, Médico em medicina preventiva e social, Médico endocrinologista e metabologista, Médico fisiatra, Médico foniatra, Médico gastroenterologista, Médico geneticista, Médico geriatra, Médico hansenologista, Médico hematologista, Médico hemoterapeuta, Médico hiperbarista, Médico homeopata, Médico infectologista, Médico legista, Médico mastologista, Médico nefrologista, Médico neurocirurgião, Médico neurofisiologista clínico, Médico neurologista, Médico nutrologista, Médico oftalmologista, Médico oncologista, Médico oncologista clínico, Médico ortopedista e traumatologista, Médico otorrinolaringologista, Médico patologista, Médico patologista clínico / medicina laboratorial, Médico perito, Médico pneumologista, Médico radioterapeuta, Médico residente, Médico reumatologista, Médico urologista
2) CNES - Recursos Humanos a partir de 2007 > Profissionais > Brasil por Região, UF e Município > Linha: Município / Coluna: Atende no SUS / Conteúdo: Quantidade / Período: Maio/2020 / Seleção: Médicos > Médicos (idem)
3) CNES - Recursos Humanos a partir de 2007 > Profissionais > Brasil por Região, UF e Município > Linha: Região/UF / Coluna: Atende no SUS / Conteúdo: Quantidade / Período: Maio/2020 / Seleção: Ocupações de nível superior > Outros enfermeiros, Enfermeiro, Enfermeiro Estomaterapeuta, Enfermeiro auditor, Enfermeiro da estratégia de agente comunitário de \[saúde]\, Enfermeiro da estratégia de saúde da família, Enfermeiro de bordo, Enfermeiro de centro cirúrgico, Enfermeiro de terapia intensiva, Enfermeiro do trabalho, Enfermeiro nefrologista, Enfermeiro neonatologista, Enfermeiro obstétrico, Enfermeiro psiquiátrico, Enfermeiro puericultor e pediátrico, Enfermeiro sanitarista, Enfermeiro saúde da familia
4) CNES - Recursos Humanos a partir de 2007 > Profissionais > Brasil por Região, UF e Município > Linha: Município / Coluna: Atende no SUS / Conteúdo: Quantidade / Período: Maio/2020 / Seleção: Ocupações de nível superior > Enfermeiros (idem)
5) CNES - Estabelecimentos > Tipos de Estabelecimentos > Brasil por Região, UF e Município > Linha: Região/UF / Coluna: Esfera Jurídica / Conteúdo: Quantidade / Período: Maio/2020 / Seleção: Tipo de Estabelecimento > HOSPITAL ESPECIALIZADO, HOSPITAL GERAL, HOSPITAL DIA
6) CNES - Estabelecimentos > Tipos de Estabelecimentos > Brasil por Região, UF e Município > Linha: Município / Coluna: Esfera Jurídica / Conteúdo: Quantidade / Período: Maio/2020 / Seleção: Tipo de Estabelecimento > HOSPITAL ESPECIALIZADO, HOSPITAL GERAL, HOSPITAL DIA
7) CNES - Recursos Físicos > Hospitalar - Leitos Internação > Brasil por Região, UF e Município > Linha: Região/UF / Coluna: Não ativa / Conteúdo: Quantidade SUS, Quantidade Não SUS / Período: Maio/2020 / Seleção: Nenhuma
8) CNES - Recursos Físicos > Hospitalar - Leitos Internação > Brasil por Região, UF e Município > Linha: Município / Coluna: Não ativa / Conteúdo: Quantidade SUS, Quantidade Não SUS / Período: Maio/2020 / Seleção: Nenhuma
9) CNES - Recursos Físicos > Hospitalar - Leitos Complementares > Brasil por Região, UF e Município > Linha: Região/UF / Coluna: Leitos complementares / Conteúdo: Quantidade existente / Período: Maio/2020 / Seleção: Nenhuma
10) CNES - Recursos Físicos > Hospitalar - Leitos Complementares > Brasil por Região, UF e Município > Linha: Município / Coluna: Leitos complementares / Conteúdo: Quantidade existente / Período: Maio/2020 / Seleção: Nenhuma
11) CNES - Recursos Físicos > Hospitalar - Leitos Complementares > Brasil por Região, UF e Município > Linha: Região/UF / Coluna: Leitos complementares / Conteúdo: Quantidade SUS / Período: Maio/2020 / Seleção: Nenhuma
12) CNES - Recursos Físicos > Hospitalar - Leitos Complementares > Brasil por Região, UF e Município > Linha: Município / Coluna: Leitos complementares / Conteúdo: Quantidade SUS / Período: Maio/2020 / Seleção: Nenhuma

## Ferramentas

Ferramenta | Endereço na Web | Resumo descritivo e uso
----- | ----- | -----
Python | https://www.python.org/ | Linguagem de programação interpretada de alto nível, usada para processar os dados, efetuar análises estatísticas e gerar visualizações.
Pandas | https://pandas.pydata.org/ | Biblioteca de manipulação e análise de dados, usada para auxiliar nas tarefas performadas em linguagem Python.
Plotly | https://plotly.com/python/ | Biblioteca de análise e visualização de dados on-line.
Jupyter | https://jupyter.org/ | Aplicação web para "desenvolver software de código aberto, padrões abertos e serviços para computação interativa em dezenas de linguagens de programação".
Matplotlib | https://matplotlib.org/ | Biblioteca de visualização, usada para produzir gráficos em linguagem Python.
NumPy | https://numpy.org/ | Biblioteca de computação científica, usada para auxiliar nas tarefas de visualização performadas em linguagem Python.

# Metodologia
A metodologia adotada no trabalho baseou-se nas seguintes estratégias:
- Estudo bibliográfico: as [referências](https://github.com/ra-ysa/publichealth/tree/master/references "Referências") foram estudadas para compreender quais são os padrões esperados de cada indicador escolhido;
- Análise exploratória dos dados: a exploração manual, com eventual auxílio das [ferramentas](#ferramentas), foi necessária para selecionar os dados adequados, processá-los e escolher o que destacar deles; 
- Análise estatística: baseada, principalmente, em técnicas de estatística descritiva e visualização. Para extrair conhecimento dos dados, foram gerados gráficos de diferentes tipos (boxplot, barra, scatter plot) e visualizações geoespaciais, com mapas coropléticos. 

## Detalhamento do Projeto
~~~
<Apresente aqui detalhes da análise. Nesta seção ou na seção de Resultados podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.

Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.>

escrita do relatório: pervasiva/iterativa
~~~
O percurso do trabalho se deu conforme as etapas descritas nesta seção.
### 0. Estudo bibliográfico das referências
As referências bibliográficas selecionadas para embasar o trabalho ajudaram-nos a entender melhor os indicadores escolhidos e como obter padrões de referência para cada um deles quando se trata de analisar como eles interferem na adequação da assistência à saúde.

- <b>Indicadores hospitalares</b>

[Ravaghi et al](https://github.com/ra-ysa/publichealth/blob/master/references/2020-ravaghi-etal.pdf "Ravaghi et al, 2020") (2020) fazem uma revisão sistemática sobre modelos e métodos para determinação de números ótimos de leitos hospitalares; [Pinto e Campos](https://github.com/ra-ysa/publichealth/blob/master/references/2014-pinto-campos.pdf "Pinto, Campos, 2015") (2015), por sua vez, propõem modelos para estimar a quantidade ideal de leitos hospitalares para a cidade de Belo Horizonte. 

[Wunsch](https://github.com/ra-ysa/publichealth/blob/master/references/2012-wunsch.pdf "Wunsch, 2012") (2012) tenta compreender se é possível determinar uma curva de Frank-Starling para estimar uma quantidade ótima de leitos de cuidado intensivo; [Prin e Wunsch](https://github.com/ra-ysa/publichealth/blob/master/references/2012-prin-wunsch.pdf "Prin, Wunsch 2012") (2012) avaliam a possibilidade de comparar diferentes países ou regiões em relação a esse indicador. 

- <b>Indicadores de recursos humanos</b>

Para indicadores de recursos humanos, estudamos um [relatório de 2016](https://github.com/ra-ysa/publichealth/blob/master/references/2016-who-health-workforce.pdf "OMS, 2016") da OMS, que apresenta o resultado de estudos sobre requisitos mínimos de recursos humanos para cobertura universal em saúde conforme os [Objetivos de Desenvolvimento Sustentável](https://en.wikipedia.org/wiki/Sustainable_Development_Goals "SDGs"). 

### 1. Seleção das bases de dados pertinentes / Estudo exploratório dos dados
A seleção de bases partiu de um [conjunto inicial](#seleção-de-dados) que foi refinado conforme aumentaram a compreensão sobre os dados, sobre o que gostaríamos de extrair deles e sobre o que seria necessário para tal (em termos de ferramentas, processamento computacional, habilidades e tempo de trabalho). 

A seleção final é aquela que se encontra na seção [<b>Bases de Dados</b>](#bases-de-dados).

### 2. Seleção de atributos de interesse e pré-processamento/limpeza
Com os dados em mãos, passamos à seleção de quais atributos seriam extraídos de cada um. Definimos três conjuntos de atributos:

<b>1) Municípios:</b>

- Código municipal;
- Nome; 
- População estimada em 2019 (IBGE);
- UF correspondente;
- Quantidade de enfermeiros que atendem no SUS;
- Quantidade de enfermeiros que não atendem no SUS;
- Quantidade total de enfermeiros;
- Porcentagem de enfermeiros que atendem no SUS em relação ao total de enfermeiros;
- Enfermeiros a cada 10.000 habitantes;
- Quantidade de médicos que atendem no SUS;
- Quantidade de médicos que não atendem no SUS;
- Quantidade total de médicos;
- Porcentagem de médicos que atendem no SUS em relação ao total de médicos;
- Médicos a cada 10.000 habitantes;
- Déficit ou excesso absoluto de médicos/enfermeiros*;
- Quantidade de hospitais públicos;
- Quantidade de hospitais não-públicos;
- Quantidade total de hospitais; 
- Porcentagem de hospitais públicos em relação ao total de hospitais;
- Hospitais a cada 100.000 habitantes;
- Quantidade de leitos de internação SUS;
- Quantidade de leitos de internação não-SUS;
- Quantidade total de leitos de internação;
- Porcentagem de leitos de internação SUS em relação ao total de leitos dessa natureza;
- Leitos de internação a cada 10.000 habitantes;
- Quantidade de leitos complementares (isto é, de cuidado intensivo/UTI ou intermediário/UCI) SUS;
- Quantidade de leitos complementares não-SUS;
- Quantidade total de leitos complementares;
- Porcentagem de leitos complementares SUS em relação ao total de leitos dessa natureza;
- Leitos complementares a cada 10.000 habitantes;
- Quantidade de leitos de UTI dedicados a COVID-19 SUS;
- Quantidade de leitos de UTI dedicados a COVID-19 não-SUS;
- Quantidade total de leitos de UTI dedicados a COVID-19;
- Porcentagem de leitos de UTI dedicados a COVID-19 SUS em relação ao total de leitos dessa natureza;
- Leitos de UTI dedicados a COVID-19 a cada 10.000 habitantes.

* Esse atributo corresponde à quantidade faltante - ou extra - de profissionais (médicos e enfermeiros) em relação a um valor de referência para a região selecionada. Segundo [relatório da OMS](https://github.com/ra-ysa/publichealth/blob/master/references/2016-who-health-workforce.pdf "OMS, 2016") (2016), seriam necessários 44.5 médicos e enfermeiros/obstetrizes (somados) a cada 10.000 habitantes para garantir cobertura de saúde adequada em uma população. Embora arbitrário em algum grau, esse valor representa uma referência útil para entender o posicionamento de uma região de interesse - no nosso caso, o Brasil - em relação ao que é estabelecido como padrão internacional. [Aqui](#melhores-práticas), explicamos como esse número é obtido e algumas de suas limitações; maiores detalhes podem ser compreendidos pela leitura do relatório.

<b>2) Estados:</b>

Conjunto idêntico ao de atributos para os municípios (exceto pelo código municipal e UF correspondente).

<b>3) Países:</b>

- Nome;
- Quantidade total de profissionais de enfermagem;
- Profissionais de enfermagem a cada 10.000 habitantes;
- Quantidade total de médicos;
- Médicos a cada 10.000 habitantes. 

Para cada um desses conjuntos, os dados originais foram pré-processados e limpos de modo que uma nova tabela, com os atributos descritos acima, foi gerada, pronta para ser usada nas análises de interesse. O processo resultou, assim, em três [tabelas](https://github.com/ra-ysa/publichealth/tree/master/data/processed "Dados processados"): ``Brasil - Municípios.csv``, ``
Brasil - UFs e Regiões.csv `` e ``Mundo (OMS).csv``. 

### 3. Geração de visualizações

- <b>Mapas</b>: Os mapas foram [gerados](https://github.com/ra-ysa/publichealth/tree/master/notebooks "Notebooks") usando Jupyter Notebook, a partir de dados processados por [município](https://github.com/ra-ysa/publichealth/tree/master/data/processed/dados_municipios_por_estado "Dados municipais por estado"), [estado](https://github.com/ra-ysa/publichealth/tree/master/data/processed/dados_por_estado "Dados estaduais"), [região](https://github.com/ra-ysa/publichealth/tree/master/data/processed/dados_por_regiao "Dados regionais") e [país](https://github.com/ra-ysa/publichealth/tree/master/data/processed/dados_por_pais "Dados mundiais"). 

### 4. Definição e realização de análises estatísticas pertinentes

### 5. Compilação dos resultados

### 6. Atividades pervasivas
Ao longo do projeto, algumas atividades foram realizadas de maneira pervasiva, em todas as etapas, iterativamente com adequações conforme o trabalho evoluía. Fazem parte desse grupo as atividades de escrita/revisão do relatório e realização de testes de código. 

## Evolução do Projeto
Nesta seção, apresentamos aspectos do trabalho que passaram por mudanças significativas. 

### Seleção de dados
Inicialmente, o conjunto de dados escolhidos para basear a análise era composto pelos seguintes datasets:
- [IBGE](https://mapasinterativos.ibge.gov.br/covid/saude/ "IBGE"): enfermeiros, médicos e leitos de UTI por estado e por município. Dados processados a partir do CNES (Cadastro Nacional de Estabelecimentos de Saúde)/Datasus, referentes a dezembro de 2019;
- [COFEN](http://www.cofen.gov.br/enfermagem-em-numeros "COFEN"): profissionais de enfermagem (enfermeiros, auxiliares, técnicos e obstetrizes) por estado, referentes a maio de 2020. A origem dos dados não é explicitada, mas pressupõe-se ser a quantidade de inscrições ativas no conselho; 
- [Fiocruz](https://bigdata-metadados.icict.fiocruz.br/dataset/cadastro-nacional-de-estabelecimentos-de-saude-cnes "Fiocruz"): CNES - tabelas detalhadas com dados referentes a todos os estabelecimentos de saúde cadastrados no país, originados do Datasus, atualizado em dezembro de 2019. A ideia inicial era usá-lo para extrair informações sobre hospitais, ainda não processadas pelo IBGE. Dados crus, não processados;
- [OCDE](https://stats.oecd.org/index.aspx?DataSetCode=HEALTH_REAC "OCDE") e [OMS](https://www.who.int/data/gho/data/indicators "OMS"): indicadores de saúde de diversos países para comparações que enriquecessem a análise.

Uma observação mais cuidadosa nos permitiu notar que:
- O portal [Tabnet/Datasus](http://www2.datasus.gov.br/DATASUS/index.php?area=02 "Tabnet Datasus") tem dados mais atualizados que aqueles processados pelo IBGE; sua última atualização é de maio de 2020. O IBGE tem como diferencial ter adicionado colunas com densidade de recursos por população e população absoluta para cada entrada (município ou estado); porém, os dados do Datasus são suficientemente limpos e organizados, e valem a pena pela atualidade e possibilidade de customização de tabulações no site, razão pela qual optamos, então, por utilizá-los no lugar das tabelas do IBGE e da Fiocruz (a última traria, ainda, dificuldades adicionais de processamento computacional pelo tamanho). O número de habitantes de cada estado e município foi extraído de outras duas tabelas do IBGE, que trazem estimativas feitas para dezembro de 2019 (dado que o último censo oficial é de 2010);
- As informações fornecidas pelo COFEN divergem daquelas que constam no Datasus. A título de exemplo: o COFEN acusa a existência de 565458 enfermeiros no país; para o Datasus, são 282634 no mesmo mês de referência (maio/2020). Considerando que o último [reporta dados fornecidos pelas secretarias municipais e estaduais de saúde](http://tabnet.datasus.gov.br/cgi/cnes/NT_RecursosHumanos.htm "Nota Técnica"), levantamos a hipótese de que a diferença se deve à existência de profissionais registrados no Conselho sem atuar, ou atuando fora de estabelecimentos de saúde. Diante disso, e em prol da consistência na análise, optamos por descartar o dataset do COFEN, usando os do Datasus também para recuperar informações sobre profissionais de enfermagem;
- Os dados da OCDE e os da OMS são redundantes, sendo que os da OMS são mais completos. Assim, optamos por descartar os datasets da OCDE, mantendo apenas os da OMS para comparações entre países;
- Para gerar as visualizações, seria necessário incluir, ainda, informações espaciais sobre os municípios, estados e países analisados. (Os datasets do IBGE têm atributos tipo <i>shape</i>, que optamos por não usar por demandarem processamento em softwares de GIS (sistema de informação geográfica), que não dominamos.)

Com essas ressalvas levadas em consideração, a seleção final de dados é a que se encontra descrita na seção [<b>Bases de Dados</b>](#bases-de-dados).

### Escolha de indicadores
Inicialmente, o principal objetivo do trabalho era fazer uma análise comparativa de quatro indicadores entre municípios brasileiros, estados brasileiros e países em comparação com o Brasil. Os indicadores seriam: <b>médicos</b>; <b>enfermeiros</b>; <b>hospitais</b>; <b>leitos de UTI</b>. 
Após análise exploratória dos dados e estudo mais aprofundado do problema, optamos por realizar as seguintes alterações:
1) Acrescentar o indicador <b>leitos hospitalares (internação)</b> na análise nacional

A informação sobre leitos hospitalares tipo internação (ou seja, de cuidados não intensivos) é facilmente recuperada no portal do Datasus e enriquece a análise, visto que observar a quantidade de hospitais por si só, embora útil como referência, é insuficiente para informar a abrangência de acesso a atendimento hospitalar - dado que hospitais podem ter capacidades muito heterogêneas entre si. 

2) Excluir os indicadores hospitalares (<b>hospitais</b> e <b>leitos</b> de qualquer natureza) da análise mundial

Embora a OMS compile dados sobre [estabelecimentos de saúde](https://apps.who.int/gho/data/view.main.30000 "Health infrastructure by country") e [leitos](https://apps.who.int/gho/data/view.main.HS07v "Hospital bed density by country"), optamos por não incluí-los na análise pelos seguintes fatores:
- Não há informações globais sobre disponibilidade de leitos de UTI: bancos de dados da OCDE e da OMS não fazem essa distinção, reportando apenas estatísticas sobre leitos de hospitais de modo geral (sem especificar, contudo, a natureza dos leitos). Tampouco parece haver tal informação sistematizada em outros bancos de dados públicos, existindo somente dados esparsos sobre países ou regiões específicos em artigos acadêmicos. Há, ainda, [referências](https://github.com/ra-ysa/publichealth/blob/master/references/2012-prin-wunsch.pdf "Prin, Wunsch 2012") que questionam esse tipo de comparação em nível internacional dada a ausência de padronização nas definições referentes a <i>critical care</i> em diferentes países e regiões;
- Esses dados trouxeram dificuldades adicionais de pré-processamento e limpeza em relação aos demais, diminuindo o benefício em relação ao custo de agregá-los na análise.

Diante dessas ponderações, optamos por por limitar a análise desses indicadores ao âmbito nacional, com os dados do Datasus, e efetuar comparações entre países somente para os indicadores de recursos humanos (médicos e profissionais de enfermagem), para os quais houve menos dificuldades de pré-processamento e parece existir uma homogeneidade de dados aceitável (ainda que [imperfeita](#dificuldades-e-limitações)). 

### Dificuldades e limitações
Ao longo do trabalho, além das mudanças relatadas acima, outras dificuldades emergiram e algumas limitações se revelaram. Destacamo-las abaixo.

- <b>Pré-processamento e limpeza de dados</b>: Não houve dificuldades de processamento computacional, considerando que o tamanho dos dados era adequado para as máquinas utilizadas; houve, contudo, algumas dificuldades algorítmicas para efetuar o pré-processamento/limpeza adequadamente. Deixar os dados em um formato amigável para sua utilização na geração de visualizações e análises estatísticas exigiu concatená-los, em cada uma das granularidades (municipal, estadual e nacional), de modo que fizesse sentido; isso exigiu a escolha de atributos pertinentes e a adequação de diversas tabelas, além de processos tradicionais de limpeza (exclusão de linhas, remoção ou edição de caracteres inválidos, adaptações de tipos de variáveis, tratamento de casos especiais etc.). Tais dificuldades foram superadas com persistência e estudo das ferramentas, além de readequação do projeto quando necessário, conforme descrito nesta seção. A atividade de pré-processamento/limpeza foi, provavelmente, a que mais demandou tempo e trabalho do grupo;

- <b>Geração de visualizaçeõs</b>: 
  - Houve dificuldade para encontrar os perímetros dos municípios e dos estados no formato necessário para utilização da biblioteca [Choropleth](https://plotly.com/python/choropleth-maps/ "Choropleth");
  - Existiam várias divergências entre os nomes dos municípios e dos países presentes nos dois arquivos utilizados na plotagem dos mapas (banco de dados e .json ou arquivo dos códigos dos países). Devido a essas divergências, uma análise minuciosa foi feita para padronização dos nomes e acabamos descobrindo algumas curiosidades sobre os nomes dos municípios brasileiros (estão descritas nos [notebooks de visualização](https://github.com/ra-ysa/publichealth/tree/master/notebooks "Notebooks"));
  - Um desafio interessante foi pensar em como visualizar tantos dados de forma limpa e plotar gráficos pouco poluído (cores utilizadas, disponibilização das informações, tamanho da imagem e da fonte etc.);
  - Uma ideia que surgiu da necessidade de fazer gráficos não poluídos foi a presença de botões de seleção. Também foi uma dificuldade entender como utilizá-los corretamente, interligando com os dados disponibilizados nos mapas;

- <b>Limitações dos dados utilizados</b>: Algumas limitações são intrísecas aos dados - seja por sua disponibilização, método de coleta ou outros aspectos. Um conjunto de dados é, afinal, um recorte da realidade, e não é factível esperar que seja possível expressá-la integralmente através deles. Abaixo, destacamos as limitações com as quais nos esbarramos no que diz respeito aos dados.

<b>1)</b> Dados sobre hospitais brasileiros: no Datasus, é possível selecionar hospitais usando diversos atributos; contudo, a vinculação (ou não) do estabelecimento ao SUS não é um deles. Ou seja: ao contrário do que ocorre com os outros indicadores analisados, não é possível, pelo Datasus, saber se um hospital atende pacientes do SUS, de convênios médicos, particulares ou uma combinação destes. É possível, no entanto, selecioná-los pela sua esfera jurídica (pública ou privada); em razão disso, nossa análise considera hospitais públicos (administração pública estadual, municipal, do Distrito Federal ou outras; empresa pública ou sociedade de economia mista) versus não-públicos (entidades sem fins lucrativos; demais entidades empresariais). Lembramos, porém, que essa classificação não implica vinculação ao tipo de atendimento prestado: hospitais de natureza jurídica privada, por exemplo, podem atender pacientes do SUS; há hospitais que atendem pacientes de serviços diversos etc.; 

<b>2)</b> Dados da Organização Mundial da Saúde - atualidade: a OMS compila os dados reportados por cada país para diferentes anos. Não há, contudo, homogeneidade temporal entre os países ou entre os atributos. Na etapa de pré-processamento, removemos todas as entradas que não fossem do último ano reportado; assim, a tabela final tem o dado mais recente disponível por país segundo a OMS - mas o ano de referência não é o mesmo para todos. Por exemplo, a informação mais recente sobre quantidade de médicos em Cuba é de 2018; em Mônaco, é de 2016. Os dados mais recentes sobre quantidades de profissionais de enfermagem no Afeganistão são de 2017; sobre quantidades de médicos, para o mesmo país, são de 2016; 

<b>3)</b> Dados da Organização Mundial da Saúde versus dados nacionais - consistência: a própria instituição [reconhece](https://github.com/ra-ysa/publichealth/blob/master/references/2016-who-health-workforce.pdf "WHO 2016") que, em suas análises, utiliza dados reportados por cada país, o que pode gerar inconsistências com outros bancos de dados (por exemplo, datasets nacionais) em razão de diferenças de definição de atributos e possibilidades múltiplas de fontes de informação. De fato, isso foi observado para o caso brasileiro: a quantidade de médicos mais recente reportada ao órgão, de 2018, é cerca de 14% maior que a quantidade registrada no Datasus para dezembro do mesmo ano. No caso de profissionais de enfermagem ([enfermeiros/obstetrizes e profissionais associados, como técnicos e auxiliares](https://www.ilo.org/public/english/bureau/stat/isco/docs/resol08.pdf "ILO - International Standard Classification of Occupations"), segundo o [critério](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/nursing-and-midwifery-personnel-(number) "Nursing and midwifery personnel - metadata") usado pelo órgão internacional nesse banco de dados), a discrepância é ainda maior: segundo a OMS, o Brasil tinha mais que o dobro (2119620) da quantidade desses profissionais em 2018 que o número que consta no Datasus (957739) para o mês de dezembro. Diante disso, em prol da consistência, optamos por comparar países somente com os dados da OMS, usando os dados nacionais do Brasil apenas para análises dentro do próprio território e em relação a [padrões de referência internacionais definidos com métodos estatísticos](https://github.com/ra-ysa/publichealth/blob/master/references/2016-who-health-workforce.pdf "WHO 2016"). (Lembramos, ainda, que tanto esses padrões de referência quanto nossa análise nacional não consideram profissionais de enfermagem associados, somente enfermeiros.)

# Resultados e Discussão
~~~
<Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

A discussão dos resultados também pode ser feita aqui na medida em que os resultados são apresentados ou em seção independente. Aspectos importantes a serem discutidos: É possível tirar conclusões dos resultados? Quais? Há indicações de direções para estudo? São necessários trabalhos mais profundos?>

Vale lembrar q rolam algumas limitações dos próprios dados q não podem ser esquecidas; não invalida a análise, mas é importante deixar essas limitações claras (citar reportagem da nature q fala disso)
~~~
## Melhores práticas
Para realizar análises sobre os dados coletados, uma das preocupações levantadas foi a definição de quais valores de referência devem ser usados como padrão aceitável em cada um dos indicadores escolhidos. Para tanto, recorremos à literatura. 

[Ravaghi et al](https://github.com/ra-ysa/publichealth/blob/master/references/2020-ravaghi-etal.pdf "Ravaghi et al, 2020") (2020) concluem, a partir de uma revisão sistemática sobre modelos e métodos para determinação de números ótimos de leitos hospitalares, que não há como obter um padrão universal para esse valor sem considerar fatores que variam conforme o contexto regional ou hospitalar, como mudanças demográficas, tempo de estada do paciente, taxas de admissão e taxas de ocupação; ressaltam, ainda, a importância da atenção básica, da assistência integral à saúde e da colaboração e coordenação entre provedores de saúde como fatores que podem diminuir a demanda por recursos hospitalares. [Pinto e Campos](https://github.com/ra-ysa/publichealth/blob/master/references/2014-pinto-campos.pdf "Pinto, Campos, 2015") (2015) propõem modelos para estimar a quantidade ideal de leitos hospitalares para a cidade de Belo Horizonte; as estimativas variam entre 2.4 e 2.95 leitos para cada mil habitantes. 

[Wunsch](https://github.com/ra-ysa/publichealth/blob/master/references/2012-wunsch.pdf "Wunsch, 2012") (2012) tenta compreender se é possível determinar uma curva de Frank-Starling para estimar uma quantidade ótima de leitos de cuidado intensivo; segundo propõe, o excesso de leitos pode ser prejudicial na medida em que aumenta a quantidade de intervenções desnecessárias e o custo total do sistema de saúde, mas a falta deles é potencialmente fatal, atrasando ou impedindo atendimentos imprescindíveis para manutenção da vida. A autora identifica fatores que influenciam o cálculo de um suposto padrão ótimo: incidência e gravidade de doenças crônicas na população; disponibilidade de outros serviços, como leitos hospitalares comuns; quanto de espaço/recursos há para deixar "folgas" no sistema. Adverte, porém, que também para esse indicador não há um único padrão universal a ser observado, sendo que cada sistema de saúde deve ser guiado por avaliações do seu próprio contexto e necessidades. [Prin e Wunsch](https://github.com/ra-ysa/publichealth/blob/master/references/2012-prin-wunsch.pdf "Prin, Wunsch 2012") (2012) destacam, ainda, que comparar diferentes países ou regiões em relação a esse indicador pode não ser muito informativo, considerando que não há consenso entre eles sobre a definição de <i>critical care</i>. 

Para indicadores de recursos humanos, contudo, parece ser mais factível encontrar padrões de referência que ajudem a garantir a cobertura mínima necessária. Em [relatório de 2016](https://github.com/ra-ysa/publichealth/blob/master/references/2016-who-health-workforce.pdf "OMS, 2016"), a OMS apresenta o resultado de estudos sobre requisitos mínimos de recursos humanos para cobertura universal em saúde conforme os [Objetivos de Desenvolvimento Sustentável](https://en.wikipedia.org/wiki/Sustainable_Development_Goals "SDGs"). Atualizando estudos anteriores feitos a respeito, novos fatores entraram no cálculo, e o valor de 4.45 médicos e enfermeiros/obstetrizes (somados) a cada mil habitantes (ou 44.5 a cada dez mil) foi obtido como o mínimo necessário para chegar à mediana (25%) do que é definido como uma alta cobertura em saúde (80% ou mais de adequação aos indicadores selecionados, que incluem cuidado pré-natal, cobertura a doenças infecciosas e crônicas, imunização, planejamento familiar e acesso a saneamento básico). O órgão destaca que se trata de uma referência apenas, dentre outras possíveis, e que há outros fatores importantes a considerar na formulação de políticas públicas em saúde - por exemplo, especificidades locais/regionais, qualidade do atendimento prestado, integração entre diferentes profissionais de saúde e variabilidade na formação e habilidades desses profissionais. Ainda assim, é uma referência útil para entender o posicionamento de uma região de interesse - no nosso caso, o Brasil - em relação ao que é estabelecido como padrão internacional.

Com isso, identificamos que, para os indicadores hospitalares, estabelecer padrões universais é difícil, o que aumenta a importância de considerar o contexto local/regional e fazer comparações entre pares de mesma granularidade ou características similares - por exemplo, entre municípios ou estados. Para a avaliação sobre recursos humanos, o contexto local/regional e as comparações também são essenciais, mas a existência de um valor de referência fornece um elemento a mais de análise. 

## Panorama brasileiro

# Conclusões
~~~
<Apresente aqui as conclusões finais do trabalho e as lições aprendidas.>
~~~
- processamento leva mais tempo que o esperado
- fazer boas visualizaçoes nao eh trivial
- apesar dos probleminhas, datasus eh uma plataforma mto massa (referenciar relatorio)
- o ideal pra informar politicas publicas eh evidencias (que vêm de dados) + conhecimento do domínio. dados sozinhos, sem que a gt saiba o que queremos deles, nao dizem mta coisa

# Trabalhos Futuros
A partir dos dados processados neste trabalho, obtivemos estatísticas e geramos visualizações com informações úteis para entender o panorama de alguns indicadores de saúde pública no Brasil. Contudo, a quantidade de análises que podem ser feitas, informação que pode ser obtida e produtos que podem ser gerados usando os mesmos dados é imensa. Além disso, outros dados podem ser obtidos e informar novas análises em combinação com esta. Nesta seção, destacamos algumas possibilidades para trabalhos futuros.

## Dados 
- O Tabnet/Datasus tem diversos dados que não foram utilizados neste trabalho, mas podem ser úteis em análises sobre a assistência à saúde no país: indicadores sobre a rede assistencial (estabelecimentos, recursos físicos, recursos humanos, equipes de saúde); indicadores básicos de saúde e assistência à saúde; dados epidemiológicos e de morbidade; dados demográficos e socioeconômicos e outros;
- O repositório [Global Health Observatory](https://apps.who.int/gho/data/view.main "GHO") (OMS) traz, também, inúmeros dados interessantes sobre saúde no mundo, e pode ser explorado para informar futuras análises sobre o tema.

## Visualização
Em relação às visualizações, identificamos atributos que poderiam ser adicionados ou melhorados em trabalhos futuros, em relação àquelas que produzimos aqui:
- Com o intuito de divulgar esse trabalho, seria possível hospedar todas as visualizações contruídas em um servidor. Para tanto, algumas ideias são:
  - Dar para o usuário a escolha de um 'Dark Mode' ou 'Light Mode' por meio de botões (as duas opções de mapas já foram contruídas);
  - Interligar os diferentes mapas se seguinte forma: a tela inicial seria com o mapa dos países. Assim, conforme clicamos no Brasil, existiria uma animação "zoom in" para o mapa das grandes regiões. Da mesma forma, acessaríamos os mapas dos estados e dos municípios - a granularidade seria refinada com o "zoom in";
  - Criar uma página (como um dashboard, por exemplo) com as análises resultantes dos dados coletados. Poderia ser permitida, ainda, a seleção de indicadores de interesse (como 'Município com maior densidade de médicos no Brasil') para visualização de resultados.

## Indicadores e Análises
Para além do que já foi extraído neste trabalho, sugerimos alguns indicadores e análises que poderiam ser estudados em trabalhos futuros - alguns dos quais, inclusive, podem ser levantados a partir do próprio código do projeto, com poucas adaptações:
- Indicadores hospitalares
  - Discriminar, com mais detalhes, cada um dos grupos de leitos hospitalares;
  - Incluir outros estabelecimentos de saúde para efetuar comparações;
- Indicadores de recursos humanos
  - Enriquecer o estudo de diferenças entre médicos e enfermeiros (por exemplo, diferença na % de cada categoria que atende pelo SUS) com testes de hipóteses;
  - Acrescentar demais profissionais de saúde na análise;
  - Estudar as proporções entre profissionais de saúde (por exemplo, enfermeiros:médicos);
- Todos os indicadores
  - Aumentar ou mudar a granularidade das análises - identificando, por exemplo, como um (ou mais) município(s) de interesse se posiciona(m) em relação à média do estado, do país, da região e do mundo, dentre outras combinações possíveis;
  - Enriquecer algumas das comparações com testes de hipóteses; 
- Outros indicadores (sugestões)
  - Indicadores sociodemográficos - por exemplo, raciais, de renda ou de gênero - podem ser combinados a indicadores de saúde, com o objetivo de verificar a existência de correlações relevantes (ainda que não haja relação automática de causalidade a partir de uma correlação, esta pode indicar um caminho interessante para o qual olhar e, aliada a conhecimento do domínio, fortalecer ou rejeitar hipóteses de causalidade); 
  - Podem ser incluídos indicadores detalhados sobre quais parcelas da população usam diferentes tipos de prestadores (ex: pessoas que usam exclusivamente o SUS, pessoas que têm convênios de saúde etc.).
