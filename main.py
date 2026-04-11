#Example
from src.loader import download_csv_from_drive, load_and_clean_data, standardize_fields
from src.plotters import plot_performance_line
import matplotlib.pyplot as plt

def run_pipeline():
    # 1. Extração e download
    file_id = '1mrO2p-62uSyizW8IG3LKwOs9yMW27lVS'  # Substitua pelo ID real do arquivo
    output_path = 'data/raw/dados_projeto.csv'

    download_csv_from_drive(file_id, output_path)

    # 2. Carregamento e limpeza
    data = load_and_clean_data(output_path)

    # 3. Padronização
    data = standardize_fields(data)

    # 4. Plotagem (exemplo)
    if 'data' in data.columns and 'faturamento' in data.columns:
        fig = plot_performance_line(data, 'data', 'faturamento', 'Evolução de Vendas')

        # 5. Output
        fig.savefig('output/grafico_vendas.png', dpi=300)
        print("Gráfico gerado com sucesso!")
    else:
        print("Dados carregados e padronizados. Colunas disponíveis:", list(data.columns))

if __name__ == "__main__":
    run_pipeline()