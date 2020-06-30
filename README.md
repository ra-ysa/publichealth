# Ciência e visualização de dados em Saúde Pública: um panorama de indicadores no Brasil
## Data science and visualization in Public Health: an overview of indicators in Brazil

# Resumo
~~~
<Descreva resumidamente o que fará o projeto. O resumo idealmente deve: apresentar o contexto; indicar o problema; apresentar a sua solução para o problema; indicar porque a sua solução é melhor do que os esforços atuais (não obrigatório); concluir com os resultados alcançados.>
~~~

# Abstract
~~~
<English version of the abstract.>
~~~

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
~~~
<Perguntas de pesquisa que o projeto pretende responder ou hipóteses a serem avaliadas, enunciadas de maneira objetiva e verificável.>
Rascunho:
HOSPITAIS
quantos % dos municípios não têm hospital at all e onde eles se concentram
% de públicos e privados em cada município/estado

LEITOS UTI
quantos % são leitos covid - país, estado e municípios
Quais municípios/estados têm maior % de leitos covid
quantos % dos municípios não têm UTI at all e onde eles se concentram
(Ver se rola: algum município tem mais leitos do que o adequado? - vide artigo)

MÉDICOS/ENFERMEIROS
quantos % atendem no sus - país, estado e municípios
Quais municípios/estados têm maior % de profissionais que não atendem sus
Razão medico:enf? Dfça entre quantos estao no sus?


TODOS
Boxplot p/ estados (quais são menos desiguais? DP nos mostra isso)
como o município se posiciona em relação à média do estado, do país, do mundo e de alguma recomendação
como o estado se posiciona em relação à média do país, do mundo e de alguma recomendação
(Ver se rola: correlação com indicadores raciais? % da pop que usa o SUS/não tem plano de saúde?)
~~~

## Objetivos do projeto
~~~
<Como seu projeto propôs abordar o problema apresentado.>
~~~

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

# Metodologia
~~~
<Abordagem/metodologia adotada, incluindo especificação de quais técnicas foram exploradas, tais como: aprendizagem de máquina, análise de redes, análise estatística, ou integração de uma ou mais técnicas.>
Análise exploratória de dados
Técnicas de estatística descritiva (quais? boxplot?)
Análise estatística? algum teste de hipótese?
Estudo bibliográfico
~~~

## Detalhamento do Projeto
~~~
<Apresente aqui detalhes da análise. Nesta seção ou na seção de Resultados podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.

Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.>
Etapas:
0- estudo bibliográfico das referências
1- seleção das bases de dados pertinentes; estudo exploratório dos dados
2- seleção de atributos de interesse e pre-processamento
3- geração de visualizações
4- definição de análises estatísticas pertinentes e realização das análises
5- compilação dos resultados

escrita do relatório: pervasiva/iterativa
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

### Escolha de indicadores
Inicialmente, o principal objetivo do trabalho era fazer uma análise comparativa de quatro indicadores entre municípios brasileiros, estados brasileiros e países em comparação com o Brasil. Os indicadores seriam: <b>médicos</b>; <b>enfermeiros</b>; <b>hospitais</b>; <b>leitos de UTI</b>. 
Após análise exploratória dos dados e estudo mais aprofundado do problema, optamos por realizar as seguintes alterações:
1) Acrescentar o indicador <b>leitos hospitalares (internação)</b> na análise nacional

A informação sobre leitos hospitalares tipo internação (ou seja, de cuidados não intensivos) é facilmente recuperada no portal do Datasus e enriquece a análise, visto que observar a quantidade de hospitais por si só, embora útil como referência, é insuficiente para informar a abrangência de acesso a atendimento hospitalar - dado que hospitais podem ter capacidades muito heterogêneas entre si. 

2) Excluir os indicadores hospitalares (<b>hospitais</b> e <b>leitos</b> de qualquer natureza) da análise mundial

Embora a OMS compile dados sobre [estabelecimentos de saúde](https://apps.who.int/gho/data/view.main.30000 "Health infrastructure by country") e [leitos](https://apps.who.int/gho/data/view.main.HS07v "Hospital bed density by country"), optamos por não incluí-los na análise pelos seguintes fatores:
- Não há informações globais sobre disponibilidade de leitos de UTI: bancos de dados da OCDE e da OMS não fazem essa distinção, reportando apenas estatísticas sobre leitos de hospitais de modo geral (sem especificar, contudo, a natureza dos leitos). Tampouco parece haver tal informação sistematizada em outros bancos de dados públicos, existindo somente dados esparsos sobre países ou regiões específicos em artigos acadêmicos. Assim, a comparação de leitos hospitalares entre o Brasil (cujas informações são facilmente discrimináveis no Datasus) e outros países restaria prejudicada se confrontássemos os dados nacionais com os mundiais. Há, ainda, [referências](https://github.com/ra-ysa/publichealth/blob/master/references/2012-prin-wunsch.pdf "Prin, Wunsch 2012") que questionam esse tipo de comparação em nível internacional dada a ausência de padronização nas definições referentes a <i>critical care</i> em diferentes países e regiões;
- Esses dados trouxeram dificuldades adicionais de pré-processamento e limpeza em relação aos demais, diminuindo o benefício em relação ao custo de agregá-los na análise.

Diante dessas ponderações, concluímos que comparações na escala internacional considerando os indicadores hospitalares não seriam informativas; optamos, assim, por limitar a análise deles ao âmbito nacional, com os dados do Datasus, e efetuar comparações com outros países somente para os indicadores de recursos humanos (médicos e profissionais de enfermagem), para os quais parece existir uma homogeneidade de dados aceitável (ainda que [imperfeita](#dificuldades-e-limitações)). 

### Seleção de dados
Inicialmente, o conjunto de dados escolhidos para basear a análise era composto pelos seguintes datasets:
- [IBGE](https://mapasinterativos.ibge.gov.br/covid/saude/ "IBGE"): enfermeiros, médicos e leitos de UTI por estado e por município. Dados processados a partir do CNES (Cadastro Nacional de Estabelecimentos de Saúde)/Datasus, referentes a dezembro de 2019;
- [COFEN](http://www.cofen.gov.br/enfermagem-em-numeros "COFEN"): profissionais de enfermagem (enfermeiros, auxiliares, técnicos e obstetrizes) por estado, referentes a maio de 2020. A origem dos dados não é explicitada, mas pressupõe-se ser a quantidade de inscrições ativas no conselho; 
- [Fiocruz](https://bigdata-metadados.icict.fiocruz.br/dataset/cadastro-nacional-de-estabelecimentos-de-saude-cnes "Fiocruz"): CNES - tabelas detalhadas com dados referentes a todos os estabelecimentos de saúde cadastrados no país, originados do Datasus, atualizado em dezembro de 2019. A ideia inicial era usá-lo para extrair informações sobre hospitais, ainda não processadas pelo IBGE. Dados crus, não processados;
- [OCDE](https://stats.oecd.org/index.aspx?DataSetCode=HEALTH_REAC "OCDE") e [OMS](https://www.who.int/data/gho/data/indicators "OMS"): indicadores de saúde de diversos países para comparações que enriquecessem a análise.

Uma observação mais cuidadosa nos permitiu notar que:
- O portal [Tabnet/Datasus](http://www2.datasus.gov.br/DATASUS/index.php?area=02 "Tabnet Datasus") tem dados mais atualizados que aqueles processados pelo IBGE; sua última atualização é de maio de 2020. O IBGE tem como diferencial ter adicionado colunas com densidade de recursos por população e população absoluta para cada entrada (município ou estado); porém, os dados do Datasus são suficientemente limpos e organizados, e valem a pena pela atualidade e possibilidade de customização de tabulações no site, razão pela qual optamos, então, por utilizá-los no lugar das tabelas do IBGE e da Fiocruz (a última traria, ainda, dificuldades adicionais de processamento computacional pelo tamanho). O número de habitantes de cada estado e município foi extraído de outras duas tabelas do IBGE, que trazem estimativas feitas para dezembro de 2019 (dado que o último censo oficial é de 2010);
- As informações fornecidas pelo COFEN divergem daquelas que constam no Datasus. A título de exemplo: o COFEN acusa a existência de 565458 enfermeiros no país; para o Datasus, são 282634 no mesmo mês de referência (maio/2020). Considerando que o último [reporta dados fornecidos pelas secretarias municipais e estaduais de saúde](http://tabnet.datasus.gov.br/cgi/cnes/NT_RecursosHumanos.htm "Nota Técnica"), levantamos a hipótese de que a diferença se deve à existência de profissionais registrados no Conselho sem atuar, ou atuando fora de estabelecimentos de saúde. Diante disso, e em prol da consistência na análise, optamos por descartar o dataset do COFEN, usando os do Datasus também para recuperar informações sobre profissionais de enfermagem;
- Os dados da OCDE e os da OMS são redundantes, sendo que os da OMS são mais completos. Assim, optamos por descartar os datasets da OCDE, mantendo apenas os da OMS para comparações com outros países;
- Para gerar as visualizações, seria necessário incluir, ainda, informações espaciais sobre os municípios, estados e países analisados. (Os datasets do IBGE têm atributos tipo <i>shape</i>, que optamos por não usar por demandarem processamento em softwares de GIS (sistema de informação geográfica), que não dominamos.)

Com essas ressalvas levadas em consideração, a seleção final de dados é a que se encontra descrita na seção [<b>Bases de Dados</b>](#bases-de-dados).

### Dificuldades e limitações
Ao longo do trabalho, além das mudanças relatadas acima, outras dificuldades emergiram e algumas limitações se revelaram. Destacamo-las abaixo.

- <b>Pré-processamento e limpeza de dados</b>: Não houve dificuldades de processamento computacional, considerando que o tamanho dos dados era adequado para as máquinas utilizadas; houve, contudo, algumas dificuldades algorítmicas para efetuar o pré-processamento/limpeza adequadamente. Deixar os dados em um formato amigável para sua utilização na geração de visualizações e análises estatísticas exigiu concatená-los, em cada uma das granularidades (municipal, estadual e nacional), de modo que fizesse sentido; isso exigiu a escolha de atributos pertinentes e a adequação de diversas tabelas, além de processos tradicionais de limpeza (exclusão de linhas, remoção ou edição de caracteres inválidos, adaptações de tipos de variáveis, tratamento de casos especiais etc.). Tais dificuldades foram superadas com persistência e estudo das ferramentas, além de readequação do projeto quando necessário, conforme descrito nesta seção. A atividade de pré-processamento/limpeza foi, provavelmente, a que mais demandou tempo e trabalho do grupo;
- <b>Geração de visualizaçeõs</b>: @debs explicar dificuldades encontradas no processo;
- <b>Limitações dos dados utilizados</b>: Algumas limitações são intrísecas aos dados - seja por sua disponibilização, método de coleta ou outros aspectos. Um conjunto de dados é, afinal, um recorte da realidade, e não é factível esperar que seja possível expressá-la integralmente através deles. Abaixo, destacamos as limitações com as quais nos esbarramos no que diz respeito aos dados.

<b>1)</b> Dados sobre hospitais brasileiros: no Datasus, é possível selecionar hospitais usando diversos atributos; contudo, a vinculação (ou não) do estabelecimento ao SUS não é um deles. Ou seja: ao contrário do que ocorre com os outros indicadores analisados, não é possível, pelo Datasus, saber se um hospital atende pacientes do SUS, de convênios médicos, particulares ou uma combinação destes. É possível, no entanto, selecioná-los pela sua esfera jurídica (pública ou privada); em razão disso, nossa análise considera hospitais públicos (administração pública estadual, municipal, do Distrito Federal ou outras; empresa pública ou sociedade de economia mista) versus não-públicos (entidades sem fins lucrativos; demais entidades empresariais). Lembramos, porém, que essa classificação não implica vinculação ao tipo de atendimento prestado: hospitais de natureza jurídica privada, por exemplo, podem atender pacientes do SUS; há hospitais que atendem pacientes de serviços diversos etc. 

<b>2)</b> Dados da Organização Mundial da Saúde - temporalidade: a OMS compila os dados reportados por cada país para diferentes anos. Não há, contudo, homogeneidade temporal entre os países ou entre os atributos. Na etapa de pré-processamento, removemos todas as entradas que não fossem do último ano reportado; assim, a tabela final tem o dado mais recente disponível por país segundo a OMS - mas o ano de referência não é o mesmo para todos. Por exemplo, a informação mais recente sobre quantidade de médicos em Cuba é de 2018; em Mônaco, é de 2016. Os dados mais recentes sobre quantidades de profissionais de enfermagem no Afeganistão são de 2017; sobre quantidades de médicos, para o mesmo país, são de 2016. 

<b>3)</b> Dados da Organização Mundial da Saúde - consistência: a própria instituição [reconhece](https://github.com/ra-ysa/publichealth/blob/master/references/2016-who-health-workforce.pdf "WHO 2016") que, em suas análises, utiliza dados reportados por cada país, o que pode gerar inconsistências com outros bancos de dados (por exemplo, datasets nacionais) em razão de diferenças de definição de atributos e possibilidades múltiplas de fontes de informação. De fato, isso foi observado para o caso brasileiro: a quantidade de médicos mais recente reportada ao órgão, de 2018, é cerca de 14% maior que a quantidade registrada no Datasus para dezembro do mesmo ano. No caso de profissionais de enfermagem ([enfermeiros/obstetrizes e profissionais associados, como técnicos e auxiliares](https://www.ilo.org/public/english/bureau/stat/isco/docs/resol08.pdf "ILO - International Standard Classification of Occupations"), segundo o [critério](https://www.who.int/data/gho/data/indicators/indicator-details/GHO/nursing-and-midwifery-personnel-(number) "Nursing and midwifery personnel - metadata") usado pelo órgão internacional nesse banco de dados), a discrepância é ainda maior: segundo a OMS, o Brasil tinha mais que o dobro (2119620) da quantidade desses profissionais em 2018 que o número que consta no Datasus (957739) para o mês de dezembro. Diante disso, em prol da consistência, optamos por comparar países somente com os dados da OMS, usando os dados nacionais do Brasil apenas para análises dentro do próprio território e em relação a [padrões de referência internacionais definidos com métodos estatísticos](https://github.com/ra-ysa/publichealth/blob/master/references/2016-who-health-workforce.pdf "WHO 2016"). (Lembramos, ainda, que tanto esses padrões de referência quanto nossa análise nacional não consideram profissionais de enfermagem associados, somente enfermeiros.)

# Resultados e Discussão
~~~
<Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

A discussão dos resultados também pode ser feita aqui na medida em que os resultados são apresentados ou em seção independente. Aspectos importantes a serem discutidos: É possível tirar conclusões dos resultados? Quais? Há indicações de direções para estudo? São necessários trabalhos mais profundos?>

Vale lembrar q rolam algumas limitações dos próprios dados q não podem ser esquecidas; não invalida a análise, mas é importante deixar essas limitações claras (citar reportagem da nature q fala disso)
~~~

# Conclusões
~~~
<Apresente aqui as conclusões finais do trabalho e as lições aprendidas.>
~~~

# Trabalhos Futuros
~~~
<Indique trabalhos futuros a partir do ponto alcançado.>
~~~
