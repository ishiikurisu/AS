import numpy as np
import matplotlib.pylab as mpl
from scipy import signal

descricao_do_exercicio = """
Crie um vetor t para alimentar um vetor f = cos(100t). Monte o vetor w de frequencias. Plot f e a sua transformada de
Fourier. Simule uma funcao delta de Dirac, alimentando-a a funcao f. Faca Fourier com janela com tau = 100 e tau = 300.
Ha diferencas no resultado? N = 600; delta(t) = 200 se t = 300 caso contrario 0.
"""

def janela(N, tau):
    original = signal.blackman(N)
    outlet = np.zeros_like(original)

    limit = len(original)
    n = np.floor(limit/2)
    k = 0
    while (k + n < limit) and (k + tau < limit):
        outlet[tau+k] = original[n+k]
        k += 1
    k = 0
    while (k + n >= 0) and (k + tau >= 0):
        outlet[tau+k] = original[n+k]
        k -= 1

    return outlet

def exercicio():
    # Definicao do vetor f
    N = 600
    t = np.linspace(-np.pi, np.pi, N)
    f = np.cos(10*t)
    w = np.fft.fftfreq(len(t), t[1] - t[0])
    f_hat = np.fft.fft(f)

    # Colocando a delta de Dirac
    d = np.zeros_like(f)
    d[300] = 200
    f_alt = f + d
    f_alt_hat = np.fft.fft(f_alt)

    # Criando as janelas
    j_100 = janela(N, 100)
    j_300 = janela(N, 300)

    # Aplicacao das janelas
    f_100 = f_alt * j_100
    f_300 = f_alt * j_300
    f_100_hat = np.fft.fft(f_100)
    f_300_hat = np.fft.fft(f_300)

    # Fazendo os graficos
    figs = []
    axes = []
    for x in range(5):
        figs.append(mpl.figure())
        axes.append(figs[x].add_subplot(111))

    # TODO Comentar graficos
    # Grafico da funcao original
    axes[0].plot(t, f, label = 'funcao original')
    axes[0].legend()
    # Grafico da transformada de Fourier
    axes[1].plot(w, f_hat, label = 'espectro de frequencias da funcao original')
    axes[1].legend()
    # Grafico da funcao com impulso
    axes[4].plot(t, f_alt, label = 'funcao com impulso')
    axes[4].legend()
    # Mostrando as janelas
    axes[2].plot(w, f_100_hat, label = 'espetro de frequencias da funcao com delta de Dirac, janela em 100')
    axes[2].legend()
    axes[3].plot(w, f_300_hat, label = 'espetro de frequencias da funcao com delta de Dirac, janela em 300')
    axes[3].legend()

    mpl.show()

    print("""# Comentarios
O grafico com o espectro janelado em 100 esta mais proximo do que o espectro janeado em 300,
ja que a janela de 100 nao comtempla o pico contido no sinal.""")

if __name__ == '__main__':
    exercicio()
