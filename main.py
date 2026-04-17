#Importando bibliotecas
import matplotlib.pyplot as plt
#Importando funções no repositório
from src.plotters import plot_performance_line_interactive, plot_performance_barh_interactive, plot_performance_bar_interactive, plot_correlation_heatmap, plot_scatter_interactive, plot_value_for_money, plot_area_freq_interactive, plot_donut_interactive, plot_performance_histogram_interactive

from src.loader import download_csv_from_drive, load_and_clean_data, standardize_fields

from src.utils import apply_custom_style

#aplicando template visual
apply_custom_style()

#rodando as funções nos scripts importados
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
    
    plot_value_for_money(data)

    plot_performance_line_interactive(data, 'release_year', 'intelligence_per_dollar', title='Intelligence per Dollar on models', group_col='generic_model_name',n=20)

    plot_performance_line_interactive(data, 'release_year', 'speed_per_dollar', title='Speed per Dollar on models', group_col='generic_model_name',n=20)

    plot_performance_line_interactive(data, 'release_year', 'intelligence_per_dollar', title='Intelligence per Dollar Open X Closed', group_col='is_open_source',n=20)

    plot_performance_line_interactive(data, 'release_year', 'blended_cost_usd_per_1m', title='Blended Cost per Dollar Open X Closed', group_col='provider',n=20)

    plot_performance_line_interactive(data, 'release_year', 'blended_cost_usd_per_1m', title='Blended Cost per Dollar Open X Closed', group_col='generic_model_name',n=20)
    
    #plotando histogramas
    plot_performance_histogram_interactive(data, 'provider', 'intelligence_per_dollar', n=10)
    plot_performance_histogram_interactive(data, 'clean_model_name', 'intelligence_per_dollar', n=10)
    plot_performance_histogram_interactive(data, 'provider', 'speed_per_dollar', n=10)
    plot_performance_histogram_interactive(data, 'clean_model_name', 'speed_per_dollar', n=10)

    plot_performance_histogram_interactive(data, 'provider', 'intelligence_per_dollar', n=10)

    plot_correlation_heatmap(data, ['release_year', 'aa_intelligence_index', 'time_to_first_answer_s','blended_cost_usd_per_1m', 'price_performance_ratio', ], title='Correlação entre Métricas de Desempenho e Tempo')

    plot_scatter_interactive(data, 'blended_cost_usd_per_1m', 'aa_coding_index', group_col='clean_model_name', n=20, filter=True, title='Habilidade de programação vs Custo em dólar por 1M de Tokens')

    #plotando áreas:
    plot_area_freq_interactive(data, "release_year", group_col='pricing_tier',sort_by='x', slider=False)
    #plotando áreas com possibilidade de filtrar ano a ano
    plot_area_freq_interactive(data, "release_year", group_col='pricing_tier',sort_by='x', slider=True)

    #população open source
    plot_donut_interactive(df,'model_name','is_open_source',)

    #custo open source
    plot_donut_interactive(df,'blended_cost_usd_per_1m','is_open_source',)
    
    #pricing tier dos modelos
    plot_donut_interactive(df,'model_name','pricing_tier')
    

#Mecanismo principal pra rodar o arquivo
if __name__ == "__main__":
    run_pipeline()


# EXMPLOS DE PLOTAGEM
# plot_performance_line_interactive(dataframe, x_axis, y_axis, title=None, group_col=None, n=None):
# plot_performance_barh_interactive(data, x_axis, y_axis, title=None, group_col=None, n=None, calculate='sum'):
# plot_performance_bar_interactive(data, x_axis, y_axis, title=None, group_col=None, n=None, calculate='sum'):
# plot_performance_histogram_interactive(data, x_col, y_col, title=None, group_col=None, n=None)
# plot_correlation_heatmap(data, cols, title=None):
# plot_scatter_interactive(data, x_axis, y_axis, title=None, group_col=None, n=None, filter=False):
# plot_value_for_money(data)
# plot_area_freq_interactive(data, x_axis, categories,sort_by='x',slider=True):
# plot_donut_interactive(data, measure, categories):