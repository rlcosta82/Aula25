# import pandas as pd
import polars as pl # biblioteca de manipulação de dados em larga escala
from datetime import datetime # trabalhar com o tempo


ENDERECO_DADOS = './../DADOS/BOLSA_FAMILIA/'

try:
    inicio = datetime.now()

    # LENDO PARQUET - LEITURA *PREGUIÇOSA_SCAN_PARQUET
 
    # Polars 0:00:09.819229
    # scan_parquet gera um plano de execução. Não tras os dados
    df_scan = pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
    print(df_scan)  # printa o plano de execução

    # pré-processamento ...

    # Collect executa o plano, carregando os dados p/a memória
    df_bolsa_familia = df_scan.collect()
    print(df_bolsa_familia.head())

    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet {e}')


     