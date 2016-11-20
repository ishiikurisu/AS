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

    # Fazendo os graficos
    figs = []
    axes = []
    for x in range(4):
        figs.append(mpl.figure())
        axes.append(figs[x].add_subplot(111))

    # Grafico da funcao original
    axes[0].plot(t, f)
    # Grafico da transformada de Fourier
    axes[1].plot(w, f_hat)
    # Mostrando as janelas
    axes[2].plot(t, j_100)
    axes[3].plot(t, j_300)

    mpl.show()

if __name__ == '__main__':
    exercicio()
