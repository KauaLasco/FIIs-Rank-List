#Importação das classes da biblioteca "selenium" para a execução e configuração do Chrome.
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


#Importa a biblioteca pandas para realizar a manipulação e a análise dos dados.
import pandas as pd


#Importação do módulo "time" para realizar uma pausa na execução do software.
from time import sleep


#Importa a biblioteca "matplotlib" para gerar a tabela com os dados finais.
import matplotlib.pyplot as plt


#Configuração do Chrome
opcoes = Options()
opcoes.add_experimental_option('detach', True)


#Realiza a inicialização do navegador com as configurações definidas e abre o link.
navegador = Chrome(options=opcoes)
navegador.get('https://www.fundsexplorer.com.br/ranking')


#Pausa para que a página seja carregada e os dados extraidos.
sleep(1)


#Realiza a abertura da URL e a localização da tabela para extrair os dados da mesma.
nomes_fiis = navegador.find_elements('css selector', '#upTo--default-fiis-table > div > table > tbody > tr > td > a')
tabela_fiis = navegador.find_elements('css selector', '#upTo--default-fiis-table > div > table > tbody > tr > td')


#Realiza a conversão de todos os valores para texto.
nomes_fiis = [element.text for element in nomes_fiis]
tabela_fiis = [element.text for element in tabela_fiis]


#Utiliza a biblioteca "panda" e a estrutura de dados "DataFrame" do próprio "panda" para listar tudo.
list_nome_fiis = pd.DataFrame(nomes_fiis)
list_tabela_fiis = pd.DataFrame(tabela_fiis)


#Salva os dados em um arquivos ".csv".
list_nome_fiis.to_csv("list_fiis.csv", index=False, encoding="utf-8")
list_tabela_fiis.to_csv("list_tabela_fiis.csv", index=False, encoding="utf-8")


#Variável para armazenar o objeto DataFrame.
#Realiza a leitura do arquivo CSV como somente uma coluna. (Mantém os valores "N/A")
df = pd.read_csv("list_tabela_fiis.csv", header=None, skiprows=1, keep_default_na=False)


#Removendo valores vazios e transformando em lista.
valores_lista = [v for v in df[0].tolist() if v != ""]


#Quebrando a linha a cada 8 valores (em blocos de 8).
linhas = [valores_lista[i:i+8] for i in range(0, len(valores_lista), 8)]


#Organizando o DataFrame.
df_organizado = pd.DataFrame(linhas, columns=["Fundos", "Setor", "Liquidez Diária (R$)", "P/VP", "Dividend Yield", "Variação de Preço", "Patrimônio Líquido", "Num. Cotistas"])


#Realizando a definição da primeira coluna como o índice da tabela.
df_organizado.set_index("Fundos", inplace=True)


#Exibe a lista com os dados na tela.
#print(df_organizado)


#Cria um novo arquivo (.csv) com os dados da tabela de FIIs organizados.
df_organizado.to_csv("tabela_fiis_organizada.csv", encoding="utf-8", sep=";")


#Realiza a leitura do arquivo (.csv) da tabela com os dados dos FIIs, tendo como índice a coluna "Fundos".
df_organizado = pd.read_csv("tabela_fiis_organizada.csv", sep=";", index_col="Fundos")


#Remove pontos e vírgulas para realizar a converção de "str" para "float".
df_organizado["Liquidez Diária (R$)"] = (df_organizado["Liquidez Diária (R$)"].str.replace(".", "", regex=False).str.replace(",", ".", regex=False).astype(float))

df_organizado["P/VP"] = df_organizado["P/VP"].str.replace(",", ".", regex=False).astype(float)

df_organizado["Dividend Yield"] = (df_organizado["Dividend Yield"].str.replace("%", "", regex=False).str.replace(",", ".", regex=False).str.replace(".", "", regex=False).str.strip().astype(float) / 100)

df_organizado["Variação de Preço"] = (df_organizado["Variação de Preço"].str.replace("%", "", regex=False).str.replace(",", ".", regex=False).str.replace(".", "", regex=False).str.strip().astype(float) / 100)

df_organizado["Patrimônio Líquido"] = (df_organizado["Patrimônio Líquido"].str.replace(".", "", regex=False).str.replace(",", ".", regex=False).astype(float))

df_organizado["Num. Cotistas"] = (df_organizado["Num. Cotistas"].str.replace(".", "", regex=False).astype(int))


#Realiza a seleçãos dos FIIs que atendem aos critérios.
top_liquidez = df_organizado.nlargest(547, "Liquidez Diária (R$)")
top_pvp = df_organizado.nsmallest(547, "P/VP")
top_dyield = df_organizado.nlargest(547, "Dividend Yield")
top_vpreco = df_organizado.nsmallest(547, "Variação de Preço")
top_valor_patrimonial = df_organizado.nlargest(547, "Patrimônio Líquido")
top_cotistas = df_organizado.nlargest(547, "Num. Cotistas")


#Aplicando todos os critérios para que seja possível realizar o filtro na tabela.
criterio_filtro_fiis = (set(top_liquidez.index) & set(top_pvp.index) & set(top_dyield.index) & set(top_vpreco.index) & set(top_valor_patrimonial.index) & set(top_cotistas.index))


#Realização do filtro com todos os critérios.
top_fiis_filtrados = df_organizado.loc[list(criterio_filtro_fiis)]


#Realiza a criação de um Score para realizar a ordenação e seleção dos melhores FIIs.
top_fiis_filtrados["score_total"] = (top_fiis_filtrados["Liquidez Diária (R$)"].rank(ascending=False) + top_fiis_filtrados["P/VP"].rank(ascending=True) + top_fiis_filtrados["Dividend Yield"].rank(ascending=False) + top_fiis_filtrados["Variação de Preço"].rank(ascending=True) + top_fiis_filtrados["Patrimônio Líquido"].rank(ascending=False) + top_fiis_filtrados["Num. Cotistas"].rank(ascending=False))


#Realiza a ordenação dos FIIs pelo Score e seleciona os 22 melhores.
top_22_fiis = top_fiis_filtrados.sort_values("score_total").head(22)


#Exibição dos TOP 22 FIIs que atendem a todos os critérios.
print("Top 22 FIIs com base no P/VP, DY, LD, Var%, PL e Nº de Cotistas")
print(top_22_fiis)


#Criação do arquivo dos TOP 22 FIIs.
top_22_fiis.head(22).to_csv("top_22_fiis.csv", sep=";", encoding="utf-8")


#Leitura do Arquivo final dos TOPs FIIs.
top_22_fiis = pd.read_csv("top_22_fiis.csv", sep=";", encoding="utf-8-sig", index_col="Fundos")


#Criação da figura e dos eixos.
figura, eixo = plt.subplots(figsize=(14,7))
eixo.axis("tight")
eixo.axis("off")


#Criando a tabela visual com os dados do arquivo (.csv) final.
tabela = eixo.table(cellText=top_22_fiis.values, colLabels=top_22_fiis.columns, rowLabels=top_22_fiis.index, loc="center")


#Edição da fonte e escala da tabela.
tabela.auto_set_font_size(False)
tabela.set_fontsize(5)
tabela.scale(1.2, 1.2)


#Nomeação do título da tabela e exibição.
plt.title("Top 22 FIIs com base no P/VP, DY, LD, Var%, PL e Nº de Cotistas", fontsize=12)
plt.show()