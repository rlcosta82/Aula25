# import pandas as pd
import polars as pl # biblioteca de manipulação de dados em larga escala
from datetime import datetime # trabalhar com o tempo


ENDERECO_DADOS = './../DADOS/BOLSA_FAMILIA/'

try:
    inicio = datetime.now()

    # Uso do Categorical para melhorar a performance da RAM
    # with StringCache() está desatualizado
    # Uso do Categorical para comparar os municípios repetidos
    df_scan = (
        pl.scan_parquet(ENDERECO_DADOS + 'bolsa_familia.parquet')
        .select(['NOME MUNICÍPIO', 'VALOR PARCELA'])
        # Convertendo município p/ categorical
        .with_columns([
            pl.col('NOME MUNICÍPIO').cast(pl.Categorical)
        ])
        .group_by('NOME MUNICÍPIO')
        .agg(pl.col('VALOR PARCELA').sum())
        .sort('VALOR PARCELA', descending=True)
    )

    # print(df_scan)
    df_bolsa_familia = df_scan.collect()
    print(df_bolsa_familia.head())
   
    final = datetime.now()
    print(f'Tempo de execução de {final - inicio}')
except Exception as e:
    print(f'Erro ao ler parquet {e}')


     