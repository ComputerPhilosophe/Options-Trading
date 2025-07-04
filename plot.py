import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from black_scholes import call_price, put_price

def plot_option_prices():
    S = np.linspace(50, 150, 100)
    K = 100
    T = 1.0
    r = 0.05
    sigma = 0.2

    call_prices = [call_price(s, K, T, r, sigma) for s in S]
    put_prices = [put_price(s, K, T, r, sigma) for s in S]

    plt.plot(S, call_prices, label='Call')
    plt.plot(S, put_prices, label='Put')
    plt.xlabel('Preço do ativo (S)')
    plt.ylabel('Preço da opção')
    plt.title('Preço da opção vs. Preço do ativo (Black-Scholes)')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_3d_call_surface():
    S = np.linspace(50, 150, 50)
    T = np.linspace(0.01, 2.0, 50)
    S_grid, T_grid = np.meshgrid(S, T)

    K = 100
    r = 0.05
    sigma = 0.2

    Z = np.array([[call_price(s, K, t, r, sigma) for s in S] for t in T])

    fig = go.Figure(data=[go.Surface(z=Z, x=S, y=T, colorscale='Viridis')])
    fig.update_layout(
        title='Superfície de Preços de Opções Call (Black-Scholes)',
        scene=dict(
            xaxis_title='Preço do Ativo (S)',
            yaxis_title='Tempo até o Vencimento (T)',
            zaxis_title='Preço da Opção Call'
        )
    )
    fig.show()