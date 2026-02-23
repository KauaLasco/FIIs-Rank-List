from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

navegador = webdriver.Chrome()
navegador.get('https://www.fundsexplorer.com.br/ranking/')

#//*[@id="upTo--default-fiis-table"]/div/table/tbody/tr/td/a/text()

nomes_fiis = navegador.find_elements(By.XPATH, "//td[@class='collum-post_title']")

nomes_fiis = [element.txt for element in nomes_fiis]

list_nomes_fiis = pd.DataFrame(nomes_fiis)

print(list_nomes_fiis)

list_nomes_fiis.to_csv("list_fiis.csv", index=False, encoding="utf-8")