# 📊 FIIs Ranking – Web Scraping e Análise em Python
Este projeto realiza **web scraping** dos Fundos Imobiliários (FIIs) diretamente do site [Funds Explorer](https://www.fundsexplorer.com.br/ranking), organiza os dados em tabela, aplica critérios de seleção e gera uma lista com os **Top 22 FIIs** mais relevantes. Além disso, é criado uma tabela para a visualização dos resultados utilizando **Matplotlib**.

# Sumário


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

#[4. File descriptions]
Estrutura do repositório:
fiis-rank-list/
├── LICENSE
├── README.md               
├── list_fiis.csv                  # Lista inicial de nomes dos FIIs
├── list_tabela_fiis.csv           # Tabela bruta extraída
├── main.py                        # Script principal
├── tabela_fiis_organizada.csv     # Tabela organizada e tratada
├── teste_versao_1.py              # Primeira versão do código principal
├── teste_versao_2.py              # Segunda versão do código principal
├── top_22_fiis.csv                # Ranking final dos 22 melhores FIIs

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


# [5. Referências]
- Funds Explorer – Fonte dos dados de FIIs.
- Documentação do Selenium (selenium.dev in Bing)
- Documentação do Pandas
- Documentação do Matplotlib (matplotlib.org in Bing)

  
## 🎮 Regras do Jogo
- O caça-níquel possui 3 linhas e 3 colunas.
- Os símbolos disponíveis são: `$`, `@`, `#`, `%`, com diferentes probabilidades e valores.
- O jogador aposta em até 3 linhas simultaneamente.
- Se todos os símbolos de uma linha forem iguais, o jogador ganha o valor do símbolo multiplicado pela aposta.

## 🧑‍💻 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/KauaLasco/Slot-Machine-Simulator.git

2. Entrar na pasta do projeto:
   ```bash
   cd Slot-Machine-Simulator

3. Execute o programa em Python
   ```bash
   python src/main.py
  - Esse comando roda o arquivo principal do jogo que está dentro da pasta src/.
  - Se você estiver usando Linux/Mac e tiver o Python 3 instalado, pode ser necessário usar:
   ```bash
   python3 src/main.py
   ```

---

# 🎰 Slot Machine Simulator in Python

This project is an interactive slot machine simulator via terminal, developed in Python. The player can deposit credits, choose how many lines to bet on, set the bet value per line, and spin the machine to try to get winning combinations.

## 🚀 Features
- Initial and additional credit deposit
- Choice of number of lines to bet on (up to 3)
- Setting the bet value per line (with minimum and maximum limits)
- Random generation of symbols in a 3x3 matrix
- Validation of wins per line (matching symbols)
- Calculation of winnings based on symbol values
- Automatic balance update after each round
- Continuous loop until the player decides to quit

## 🎮 Game Rules
- The slot machine has 3 rows and 3 reels.
- The available symbols are: `$`, `@`, `#`, `%`, with different probabilities and values.
- The player bets on up to 3 lines simultaneously.
- If all the symbols on a line are the same, the player wins the value of the symbol multiplied by the bet.

## 🧑‍💻 How to Run
1. Clone the repository:
```bash
git clone https://github.com/KauaLasco/Slot-Machine-Simulator.git
```

2. Enter the project folder:
```bash
cd Slot-Machine-Simulator
```

3. Run the Python program:
```bash
python src/main.py
```
- This command runs the main game file located in the src/ folder.
- If you are using Linux/Mac and have Python 3 installed, you may need to use:
```bash
python3 src/main.py
```
