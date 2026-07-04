# import pandas as pd
import polars as pl # biblioteca de manipulação de dados em larga escala
from datetime import datetime # trabalhar com o tempo
#pip install fastparquet

ENDERECO_DADOS = './../DADOS/BOLSA_FAMILIA/'

try:
    inicio = datetime.now()

    # LENDO PARQUET - LEITURA DIRETA
    # Pandas 0:00:25.628184
    # df_bolsa_familia = pd.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    # Polars 0:00:08.014228
    df_bolsa_familia = pl.read_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')

    print(df_bolsa_familia.head())
    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet {e}')


     