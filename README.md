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


TODOS
Boxplot p/ estados (quais são menos desiguais? DP nos mostra isso)
como o município se posiciona em relação à média do estado, do país, do mundo e de alguma recomendação
como o estado se posiciona em relação à média do país, do mundo e de alguma recomendação
(Ver se rola: correlação com indicadores raciais?)
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
Datasus - CNES - Recursos Humanos a partir de 2007 | https://bit.ly/380TRfF | `<Descrição da Base 1 e para que ela foi usada no projeto.>`
Datasus - CNES - Estabelecimentos | https://bit.ly/3fSAMz1 | `<Descrição da Base 2 e para que ela foi usada no projeto.>`
Datasus - CNES - Recursos Físicos | https://bit.ly/2NucsY4 | `<Descrição da Base 2 e para que ela foi usada no projeto.>`
IBGE - Limites Territoriais 2019 - UF | https://bit.ly/2NriFUL | `<Descrição da Base 2 e para que ela foi usada no projeto.>`
IBGE - Limites Territoriais 2019 - Municípios | https://bit.ly/2Yt8gxU | `<Descrição da Base 2 e para que ela foi usada no projeto.>`
WHO/Global Health Observatory - Hospital bed density | https://bit.ly/2BaJjP5 | `<Descrição da Base 2 e para que ela foi usada no projeto.>`
WHO/Global Health Observatory - Health infrastructure | https://bit.ly/2Yttyf0 | `<Descrição da Base 2 e para que ela foi usada no projeto.>`
WHO/Global Health Observatory - Medical doctors | https://bit.ly/2NvJrek | `<Descrição da Base 2 e para que ela foi usada no projeto.>`
WHO/Global Health Observatory - Nursing and midwifery personnel | https://bit.ly/2Z4c7Rm | `<Descrição da Base 2 e para que ela foi usada no projeto.>`

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
- O portal [Tabnet/Datasus](http://www2.datasus.gov.br/DATASUS/index.php?area=02 "Tabnet Datasus") tem dados mais atualizados que aqueles processados pelo IBGE; sua última atualização é de maio de 2020. O IBGE tem como diferencial ter adicionado colunas com densidade de recursos por população e população absoluta para cada entrada (município ou estado); porém, os dados do Datasus são suficientemente limpos e organizados, e valem a pena pela atualidade e possibilidade de customização de tabulações no site, razão pela qual optamos, então, por utilizá-los no lugar das tabelas do IBGE e da Fiocruz (a última traria, ainda, dificuldades adicionais de processamento pelo tamanho). O número de habitantes de cada estado e município foi extraído de outras duas tabelas do IBGE, que trazem estimativas feitas para dezembro de 2019 (dado que o último censo oficial é de 2010);
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
