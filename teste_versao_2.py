from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pandas as pd

from time import sleep

opcoes = Options()
opcoes.add_experimental_option('detach', True)

navegador = Chrome(options=opcoes)

navegador.get('https://www.fundsexplorer.com.br/ranking')

dados = {}

sleep(10)


nomes_fiis = navegador.find_elements('css selector', '#upTo--default-fiis-table > div > table > tbody > tr > td')
setor_fiis = navegador.find_elements('css selector', 'collum-setor')
liquidez_diaria_fiis = navegador.find_elements('css selector', 'collum-liquidezmediadiaria')
pvp_fiis = navegador.find_elements('css selector', 'collum-pvp')
dy_fiis = navegador.find_elements('css selector', 'collum-yeld')
valor_patrimonial_fiis = navegador.find_elements('css selector', 'collum-patrimonio')
numero_cotistas_fiis = navegador.find_elements('css selector', 'collum-numero_cotista')

nomes_fiis = [element.text for element in nomes_fiis]

list_fiis = pd.DataFrame(nomes_fiis)

print(list_fiis)

list_fiis.to_csv("list_fiis.csv", index=False, encoding="utf-8")