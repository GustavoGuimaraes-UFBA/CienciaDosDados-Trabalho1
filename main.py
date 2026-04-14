#Example
from src.loader import download_csv_from_drive, load_and_clean_data, standardize_fields
from src.plotters import plot_performance_line, plot_performance_bar, plot_performance_scatter, plot_performance_area
from src.utils import apply_custom_style
import matplotlib.pyplot as plt

apply_custom_style()

def run_pipeline():
    # 1. Extração e download
    file_id = '1Ki8nvHJx91LM_vTZ7motgNhCF9fjyfGg'  # Substitua pelo ID real do arquivo
    output_path = 'data/raw/dados_projeto.csv'

    download_csv_from_drive(file_id, output_path)

    # 2. Carregamento e limpeza
    data = load_and_clean_data(output_path)

    # 3. Padronização
    data = standardize_fields(data)

    # 4. Plotagem (exemplo)
    fig = plot_performance_line(data, x_col='release_year', y_col='aa_intelligence_index', title='Inteligência por Ano de Lançamento', group_col='model_name', n=5)
    plt.show()
    

if __name__ == "__main__":
    run_pipeline()