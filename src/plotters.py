import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


#criar uma função de plotagem de linha com a biblioteca seaborn:
def plot_performance_line(data, x_col, y_col, title=None, group_col=None, n=None):

    """
    Plota um gráfico de linha para desempenho ao longo do tempo.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados a serem plotados.
        x_col (str): Nome da coluna para o eixo x (geralmente data).
        y_col (str): Nome da coluna para o eixo y (geralmente métrica de desempenho).
        title (str): Título do gráfico.
        group_col (str, opcional): Nome da coluna para agrupar por categoria (ex: modelo). Se None, não agrupa.
        n (int, opcional): Número de categorias a exibir. Se None, exibe todas.

    Returns:
        matplotlib.figure.Figure: Objeto da figura do gráfico.
    """
    sns.set_theme(style="whitegrid")
    # Se n for fornecido, filtra os top n antes de plotar
    if n and group_col:
        top_groups = data.groupby(group_col)[y_col].mean().nlargest(n).index
        data = data[data[group_col].isin(top_groups)]
        data = data.groupby([x_col, group_col])[y_col].mean().reset_index()
    elif n:
        top_n = data.sort_values(by=y_col, ascending=False).head(n)
        data = top_n[[x_col, y_col]]
    

    plt.figure(figsize=(12, 6))
    
    # O segredo está aqui: o parâmetro hue recebe a coluna de categorias para diferenciar as linhas por cor
    sns.lineplot(data=data, x=x_col, y=y_col, hue=group_col, marker='o')
    
    plt.title(title)
    plt.xlabel(x_col.replace('_', ' ').capitalize())
    plt.ylabel(y_col.replace('_', ' ').capitalize())
    plt.xticks(rotation=45)
    plt.grid(True, which='both', linestyle='--', alpha=0.7)
    plt.legend(title=group_col.replace('_', ' ').capitalize())
    sns.move_legend(plt.gca(), "upper left", bbox_to_anchor=(1, 1))
    plt.tight_layout()
    
    return plt.gcf()

#criar uma função de plotagem de barras com a biblioteca seaborn:
def plot_performance_bar(data, x_col, y_col, title):
    """
    Plota um gráfico de barras para desempenho por categoria.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados a serem plotados.
        x_col (str): Nome da coluna para o eixo x (geralmente categoria).
        y_col (str): Nome da coluna para o eixo y (geralmente métrica de desempenho).
        title (str): Título do gráfico.

    Returns:
        matplotlib.figure.Figure: Objeto da figura do gráfico.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(data=data, x=x_col, y=y_col)
    plt.title(title)
    plt.xlabel(x_col.capitalize())
    plt.ylabel(y_col.capitalize())
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

#criar uma função de plotagem de dispersão com a biblioteca seaborn:
def plot_performance_scatter(data, x_col, y_col, title):
    """
    Plota um gráfico de dispersão para desempenho por categoria.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados a serem plotados.
        x_col (str): Nome da coluna para o eixo x (geralmente categoria).
        y_col (str): Nome da coluna para o eixo y (geralmente métrica de desempenho).
        title (str): Título do gráfico.

    Returns:
        matplotlib.figure.Figure: Objeto da figura do gráfico.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_col, y=y_col)
    plt.title(title)
    plt.xlabel(x_col.capitalize())
    plt.ylabel(y_col.capitalize())
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

#criar uma função de plotagem de área com a biblioteca seaborn:
def plot_performance_area(data, x_col, y_col, title):
    """
    Plota um gráfico de área para desempenho ao longo do tempo.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados a serem plotados.
        x_col (str): Nome da coluna para o eixo x (geralmente data).
        y_col (str): Nome da coluna para o eixo y (geralmente métrica de desempenho).
        title (str): Título do gráfico.

    Returns:
        matplotlib.figure.Figure: Objeto da figura do gráfico.
    """
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=data, x=x_col, y=y_col, marker='o')
    plt.fill_between(data[x_col], data[y_col], alpha=0.3)
    plt.title(title)
    plt.xlabel(x_col.capitalize())
    plt.ylabel(y_col.capitalize())
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt.gcf()

#criar uma função de plotagem de rosca com a biblioteca seaborn:
def plot_performance_donut(data, x_col, y_col, title):
    """
    Plota um gráfico de rosca para desempenho por categoria.

    Args:
        data (pd.DataFrame): DataFrame contendo os dados a serem plotados.
        x_col (str): Nome da coluna para as categorias.
        y_col (str): Nome da coluna para os valores.
        title (str): Título do gráfico.

    Returns:
        matplotlib.figure.Figure: Objeto da figura do gráfico.
    """
    plt.figure(figsize=(8, 8))
    plt.pie(data[y_col], labels=data[x_col], autopct='%1.1f%%', startangle=140)
    plt.title(title)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.tight_layout()
    return fig

#Exemplos de uso (substituir colunas e títulos conforme os dados específicos):
# fig_line = plot_performance_line(data, 'data', 'faturamento', 'Evolução de Vendas')
# fig_bar = plot_performance_bar(data, 'categoria', 'faturamento', 'Vendas por Categoria')
# fig_scatter = plot_performance_scatter(data, 'data', 'faturamento', 'Dispersão de Vendas')
# fig_area = plot_performance_area(data, 'data', 'faturamento', '   Evolução de Vendas (Área)')
# fig_donut = plot_performance_donut(data, 'categoria', 'faturamento', 'Participação de Vendas por Categoria')
