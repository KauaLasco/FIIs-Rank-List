# 📊 FIIs Ranking – Web Scraping e Análise em Python
Este projeto realiza **web scraping** dos Fundos Imobiliários (FIIs) diretamente do site [Funds Explorer](https://www.fundsexplorer.com.br/ranking), organiza os dados em tabela, aplica critérios de seleção e gera uma lista com os **Top 22 FIIs** mais relevantes. Além disso, é criado uma tabela para a visualização dos resultados utilizando **Matplotlib**.

# Sumário
- [1. Instalação]
- [2. Funcionalidades]
- [3. Objetivo do Projeto]
- [4. Descrição dos arquivos]
- [5. Como executar]
- [6. Referências]
- [7. Agradecimentos]

# [1. Instalação] 
Para executar este projeto, é necessário instalar as seguintes bibliotecas: 
- Python 3.8+
- Selenium
- Pandas
- Time (módulo nativo do Python)
- Matplotlib

# [2. Funcionalidades]
- Coleta automática dos FIIs via web scraping.
- Limpeza e conversão dos dados para tipos numéricos.
- Aplicação de múltiplos critérios de seleção.
- Cálculo de **score total** para ranqueamento dos fundos.
- Exportação dos resultados em **CSV**.
- Visualização dos dados em formato de **tabela com Matplotlib**.

# [3. Objetivo do Projeto]
O objetivo deste projeto é automatizar a coleta e análise de dados dos FIIs, aplicando critérios quantitativos para identificar os fundos mais atrativos.

Critérios utilizados:
- Liquidez Diária (R$)
- P/VP
- Dividend Yield
- Variação de Preço
- Patrimônio Líquido
- Número de Cotistas

A partir desses indicadores, o projeto calcula um score total e seleciona os Top 22 FIIs que melhor atendem aos critérios, exportando os resultados em CSV e exibindo uma tabela visual.

# [4. Descrição dos arquivos]
Estrutura do repositório:
fiis-rank-list/
- LICENSE
- README.md
- list_fiis.csv                  # Lista inicial de nomes dos FIIs
- list_tabela_fiis.csv           # Tabela bruta extraída
- main.py                        # Script principal
- tabela_fiis_organizada.csv     # Tabela organizada e tratada
- teste_versao_1.py              # Primeira versão do código principal
- teste_versao_2.py              # Segunda versão do código principal
- top_22_fiis.csv                # Ranking final dos 22 melhores FIIs

# [5. Como executar] 
Clone este repositório: 
## 1. Clone este repositório:
```bash
git clone https://github.com/KauaLasco/FIIs-Rank-List.git
```

## 2. Instale as dependências:
```bash
pip install selenium pandas matplotlib
```

## 3. Execute o código principal:
```bash
python fiis_ranking.py
```

## 4. O projeto irá:
- Abrir o navegador Chrome via Selenium.
- Extrair os dados da tabela de FIIs do Funds Explorer.
- Organizar e limpar os dados com Pandas.
- Aplicar os critérios de seleção e calcular o score.
- Exportar os resultados em arquivos .csv.
- Exibir uma tabela visual com Matplotlib.

# [6. Referências]
- [Funds Explorer](https://www.fundsexplorer.com.br/ranking?utm_source=copilot.com) – Fonte dos dados de FIIs.
- [Documentação do Selenium](https://www.selenium.dev/documentation/)
- [Documentação do Pandas](https://pandas.pydata.org/docs/)
- [Documentação do Matplotlib](https://matplotlib.org/stable/index.html)

# [7. Agradecimentos]
Agradeço a Jesus Cristo, pois abriu minha mente e me deu forças nessas 12h seguidas de desenvolvimento do projeto!

---

# 📊 FIIs Ranking – Web Scraping and Analysis in Python
This project performs web scraping of Real Estate Investment Funds (FIIs) directly from the Funds Explorer website (https://www.fundsexplorer.com.br/ranking), organizes the data into a table, applies selection criteria, and generates a list of the Top 22 most relevant FIIs. Additionally, a table is created for visualizing the results using Matplotlib.

# Summary
- [1. Installation]
- [2. Functionalities]
- [3. Project Objective]
- [4. File Description]
- [5. How to Run]
- [6. References]
- [7. Acknowledgments]

# [1. [Installation]

To run this project, you need to install the following libraries:

- Python 3.8+
- Selenium
- Pandas
- Time (native Python module)
- Matplotlib

# [2. Features]
- Automatic collection of REITs via web scraping.

- Data cleaning and conversion to numeric types.

- Application of multiple selection criteria.

- Calculation of **total score** for fund ranking.

- Export of results in **CSV** format.

- Data visualization in **table format with Matplotlib**.

# [3. Project Objective]
The objective of this project is to automate the collection and analysis of REIT data, applying quantitative criteria to identify the most attractive funds.

Criteria used:

- Daily Liquidity (R$)
- P/VP (Price-to-Book Ratio)
- Dividend Yield
- Price Variation
- Net Worth
- Number of Shareholders

Based on these indicators, the project calculates a total score and selects the Top 22 REITs that best meet the criteria, exporting the results in CSV format and displaying a visual table.

# [4. [File Description]
Repository Structure:
fiis-rank-list/
- LICENSE
- README.md
- list_fiis.csv # Initial list of FII names
- list_tabela_fiis.csv # Raw extracted table
- main.py # Main script
- tabela_fiis_organizada.csv # Organized and processed table
- teste_versao_1.py # First version of the main code
- teste_versao_2.py # Second version of the main code
- top_22_fiis.csv # Final ranking of the 22 best FIIs

# [5. How to run]
Clone this repository:

## 1. Clone this repository:
```bash
git clone https://github.com/KauaLasco/FIIs-Rank-List.git
```

## 2. Install the dependencies:
```bash
pip install selenium pandas matplotlib
```

## 3. Run the main code:
```bash
python fiis_ranking.py
```

## 4. The project will:

- Open the Chrome browser via Selenium.

- Extract the data from the FIIs table in Funds Explorer.

- Organize and clean the data with Pandas.

- Apply the selection criteria and calculate the score.

- Export the results to .csv files.

- Display a visual table with Matplotlib.

# [6. [References]
- [Funds Explorer](https://www.fundsexplorer.com.br/ranking?utm_source=copilot.com) – Source of FII data.
- [Selenium Documentation](https://www.selenium.dev/documentation/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)

# [7. Acknowledgments]
I thank Jesus Christ, for opening my mind and giving me strength during those 12 consecutive hours of project development!

