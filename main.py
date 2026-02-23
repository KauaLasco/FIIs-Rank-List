#Importação das classes da biblioteca "selenium" para a execução e configuração do Chrome.
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


#Importa a biblioteca pandas para realizar a manipulação e a análise dos dados.
import pandas as pd


#Importação do módulo "time" para realizar uma pausa na execução do software.
from time import sleep


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
print(df_organizado)


#Cria um novo arquivo (.csv) com os dados da tabela de FIIs organizados.
df_organizado.to_csv("tabela_fiis_organizada.csv", encoding="utf-8", sep=";")