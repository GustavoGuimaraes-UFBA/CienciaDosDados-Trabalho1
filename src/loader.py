#Importa o arquivo base
import os
import gdown
import pandas as pd


def download_csv_from_drive(file_id: str, output_path: str) -> None:
    """
    Baixa um arquivo CSV do Google Drive usando gdown.

    Args:
        file_id (str): ID do arquivo no Google Drive.
        output_path (str): Caminho onde salvar o arquivo baixado.
    """
    # Cria a pasta se não existir
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Sempre baixa o arquivo, sobrescrevendo se necessário
    url = f'https://drive.google.com/uc?id={file_id}'
    gdown.download(url, output_path, quiet=False)
    print(f"Arquivo baixado para {output_path} com sucesso.")


def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV e realiza limpeza básica dos dados.

    Args:
        filepath (str): Caminho para o arquivo CSV.

    Returns:
        pd.DataFrame: DataFrame limpo.
    """
    df = pd.read_csv(filepath)
    
    # Exemplo: remover nulos, converter tipos de dados, etc.
    # Converter tipos de dados para os mais apropriados automaticamente
    df = df.convert_dtypes()
    # Remover linhas com valores nulos em colunas críticas
    df = df.dropna(how='all') #incluir subset=['coluna1', 'coluna2'] para especificar colunas que não podem ser nulas

    return df


def standardize_fields(df: pd.DataFrame) -> pd.DataFrame:
    """
    Padroniza campos do DataFrame para uso em plotagem ou outras funções.

    Args:
        df (pd.DataFrame): DataFrame a ser padronizado.

    Returns:
        pd.DataFrame: DataFrame com campos padronizados.
    """
    # Exemplo: converter tipos, renomear colunas, etc.
    # Ajuste conforme os dados específicos
    df = df.copy()
    # Converter colunas numéricas
    numeric_cols = df.select_dtypes(include=['str']).columns
    for col in numeric_cols:
        try:
            df[col] = pd.to_numeric(df[col], errors='ignore')
        except:
            pass
    # Padronizar nomes de colunas para lowercase
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def save_dataframe(df: pd.DataFrame, output_path: str) -> None:
    """
    Salva um DataFrame em um arquivo CSV.

    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        output_path (str): Caminho onde salvar o arquivo CSV.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"DataFrame salvo em {output_path} com sucesso.")

# Exemplo de uso:
# file_id = '1A2B3C4D5E6F7G8H9I0J_ID_USER' # Substitua pelo ID real do arquivo
# output = 'data/raw/dados_projeto.csv' # Caminho onde o arquivo será salvo
# download_csv_from_drive(file_id, output) # Baixa o arquivo do Google Drive
# df = load_and_clean_data(output) # Carrega e limpa os dados
# df = standardize_fields(df) # Padroniza os campos do DataFrame