import numpy as np
import matplotlib.pylab as mpl

descricao_do_exercicio = """
Crie um vetor t para alimentar um vetor f = cos(100t). Monte o vetor w de frequencias. Plot f e a sua transformada de
Fourier. Simule uma funcao delta de Dirac, alimentando-a a funcao f. Faca Fourier com janela com tau = 100 e tau = 300.
Ha diferencas no resultado? N = 600; delta(t) = 200 se t = 300 caso contrario 0.
"""

def exercicio():
    # Definicao do vetor f
    N = 600
    t = np.linspace(-np.pi, np.pi, N)
    f = np.cos(10*t)
    w = np.fft.fftfreq(len(t), t[1] - t[0])
    f_hat = np.fft.fft(f)

    # Colocando a delta de Dirac
    # TODO Adicionar Delta de Dirac

    # Fazendo os graficos
    figs = []
    axes = []
    for x in range(2):
        figs.append(mpl.figure())
        axes.append(figs[x].add_subplot(111))
    axes[0].plot(t, f)
    axes[1].plot(w, f_hat)
    mpl.show()

if __name__ == '__main__':
    exercicio()
