import plotly.express as px
import matplotlib.pyplot as plt


def apply_custom_style():
    """Configura o look-and-feel global do projeto."""
    px.defaults.template = "plotly_white"
    px.defaults.color_continuous_scale = "Viridis"
    plt.style.use('ggplot')

    

    
# Exemplo de uso:
# apply_custom_style()  # Chame esta função no início do seu script ou notebook para aplicar o estilo personalizado

# Funções de utilidades para o projeto:
