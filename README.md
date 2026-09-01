# Cálculo II — Algoritmo de Simpson

Trabalho da disciplina de Cálculo II (UFAPE) — Grupo 2.

**Integrantes:**
Allan José Marinho Silva de Moura, Emerson Morais de Araujo, José Walter de Melo Sobral Filho, Letícia de Melo Sobral e Maísa Lins de Melo Ciriaco.

**Método:** Regra de Simpson 1/3 composta.

## Arquivos

| Arquivo | Descrição |
| --- | --- |
| `Implementação_equação.ipynb` | Implementação do método aplicada ao caso analítico f(x) = eˣ em [0,1] (validação e análise de convergência O(h⁴)) |
| `implementação_densidade.ipynb` | Aplicação do método ao banco de dados de densidade linear (kg/m) ao longo da posição (m) |
| `bancos_dados_integracao_numerica.xlsx - Densidade.csv` | Banco de dados de densidade utilizado |

## Como executar

1. Instale as dependências:
   ```bash
   pip install numpy pandas matplotlib jupyter
   ```
2. Abra os notebooks no Jupyter:
   ```bash
   jupyter notebook
   ```
3. Execute as células na ordem em que aparecem.

> Obs.: o notebook de densidade carrega o CSV diretamente do repositório (URL no GitHub), portanto requer conexão com a internet.
