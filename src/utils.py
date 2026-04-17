import plotly.express as px
import plotly.io as pio
import matplotlib.pyplot as plt



def apply_custom_style():
    """Configura o look-and-feel global do projeto."""
    px.defaults.template = "seaborn"
    #px.defaults.color_continuous_scale = "Viridis"
    pio.templates[px.defaults.template]['layout']['hovermode'] = 'x unified'
    pio.renderers.default = "browser"
    pio.templates["seaborn"].update({
        "layout": {
            "title_x": 0.5,            # Títulos centralizados
            "hovermode": "x unified",  # Hover profissional
            "xaxis": dict(automargin=True),
            "yaxis": dict(automargin=True)
        }
    })

    

    
# Exemplo de uso:
# apply_custom_style()  # Chame esta função no início do seu script ou notebook para aplicar o estilo personalizado

# Funções de utilidades para o projeto:
