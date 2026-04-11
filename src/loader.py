#Importa o arquivo base
import os
import gdown
import pandas as pd


#Exemplo:
#def load_clean_data(filepath: str) -> pd.DataFrame:
    #df = pd.read_csv(filepath)
    # Exemplo: converter datas e remover nulos
    #df['data'] = pd.to_datetime(df['data'])
    #return df.dropna()

#file_id = '1A2B3C4D5E6F7G8H9I0J_SEU_ID_AQUI'
#url = f'https://google.com{file_id}'
#output = 'data/raw/dados_projeto.csv'
#
## Cria a pasta se não existir
#os.makedirs('data/raw', exist_ok=True)
#
## Baixa apenas se o arquivo ainda não existir localmente
#if not os.path.exists(output):
#    gdown.download(url, output, quiet=False)
#
#df = pd.read_csv(output)