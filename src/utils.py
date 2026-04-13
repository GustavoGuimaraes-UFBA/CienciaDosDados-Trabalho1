import seaborn as sns
import matplotlib.pyplot as plt

def apply_custom_style():
    """Configura o look-and-feel global do projeto."""
    sns.set_theme(style="whitegrid", palette="viridis")
    plt.rcParams["figure.figsize"] = (10, 6)
    plt.rcParams["axes.titlesize"] = 16
    plt.rcParams["axes.titleweight"] = "bold"
    plt.rcParams["axes.labelsize"] = 12
    plt.rcParams["axes.labelweight"] = "bold"
    plt.rcParams["xtick.labelsize"] = 10
    plt.rcParams["ytick.labelsize"] = 10
    plt.rcParams["legend.fontsize"] = 10
    plt.rcParams["legend.title_fontsize"] = 12
    plt.rcParams["grid.alpha"] = 0.7
    plt.rcParams["grid.linestyle"] = "--"
    plt.rcParams["grid.linewidth"] = 0.5
    plt.rcParams["figure.dpi"] = 100
    plt.rcParams["savefig.dpi"] = 300
    plt.rcParams["figure.autolayout"] = True
# Exemplo de uso:
# apply_custom_style() # Chame esta função no início do seu script ou notebook para aplicar

# Funções de utilidades para o projeto:
