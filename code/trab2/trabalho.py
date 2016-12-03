# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot
import re

SOBRE = """
Trabalho de Análise de Sinais
=============================

Aluno: Cristiano Alves da Silva Júnior
Matrícula: 13/0070629

Sobre
-----

Este trabalho visa analisar um sinal geofísico usando Python seguindo o roteiro fornecido pelo professor:

1 – Qual é o número de amostras do seu dado?
2 – Qual é a taxa de amostragem?
3 – Qual a frequência máxima que o seu sinal pode ser mostrado?
4 – Faça o gráfico do seu sinal?
5 – Apresente o sinal no domínio da frequência?
6 – Passe um filtro  passa alta que elimine 20% do sinal que é possível amostrar. p.e. a frequência máxima é 100 Hz, você deve passar um filtro passa alta que elimine 0 a 20 Hz.
7 -  Passe um filtro passa baixa que elimine 20% do sinal que é possível amostrar. p.e. a frequência máxima é 100 Hz, você deve passar um filtro passa baixe que elimine 80 a 100 Hz.
"""

######################
# Auxiliar functions #
######################

def get_sample_rate(time):
    return 1.0 / (time[1] - time[0])

def fourier_transform(time, amplitude):
    frequency = numpy.fft.fft(amplitude)
    frequencies = numpy.fft.fftfreq(len(time), time[1] - time[0])
    return frequencies, frequency

#############
# Exercises #
#############

def exercise1(time, amplitude):
    """Esta função calcula o número de amostras do sinal."""
    no_samples = len(amplitude)
    return 'O número de amostras é {0}'.format(no_samples)

def exercise2(time, amplitude):
    """Aqui temos o procedimento para se calcular a taxa de amostragem do sinal."""
    sample_rate = 1.0 / (time[1] - time[0])
    return 'A taxa de amostragem é {0} Hz'.format(sample_rate)

def exercise3(time, amplitude):
    """Esta função busca calcular a frequência de Nyquist do sinal; isto é, a maior frequência amostrável do sinal."""
    nyquist_frequency = get_sample_rate(time) / 2
    return 'A frequência de Nyquist deste sinal é de {0}'.format(nyquist_frequency)

def exercise4(time, amplitude):
    """Demonstração do sinal no domínio do tempo."""
    matplotlib.pyplot.plot(time, amplitude, label = 'Gráfico 1: representação gráfica do sinal')
    matplotlib.pyplot.show()
    return 'Veja o gráfico 1'

def exercise5(time, amplitude):
    """Plota o sinal no domínio da frequência"""
    freqs, freq = fourier_transform(time, amplitude)
    matplotlib.pyplot.plot(freqs, freq, label = 'Gráfico 2: representação do espectro de frequências')
    matplotlib.pyplot.show()
    return 'Veja o gráfico 2'

def exercise6(time, amplitude):
    """Passa um filtro passa-alta no sinal, sobrando somente as 20% frequências superiores amostráveis do sinal
    e mostra o resultado da filtragem no domínio do tempo."""
    nyquist_frequency = get_sample_rate(time) / 2
    frequencies, frequency = fourier_transform(time, amplitude)
    cutoff_frequency = 0.2 * nyquist_frequency
    cutoff_frequencies = list(map(lambda f: 1 if abs(f) > cutoff_frequency else 0, frequencies))
    filtered_frequencies = frequency * cutoff_frequencies
    filtered_amplitude = numpy.fft.ifft(filtered_frequencies)

    matplotlib.pyplot.plot(time, filtered_amplitude, label = 'Gráfico 3: representação do sinal filtrado')
    matplotlib.pyplot.show()

    return 'Veja o gráfico 3'

def exercise7(time, amplitude):
    """Passa um filtro passa baixa no sinal, deixando passar somente as 80% frequências inferiores do sinal. Por fim,
    mostra o sinal filtrado no domínio do tempo."""
    nyquist_frequency = get_sample_rate(time) / 2
    frequencies, frequency = fourier_transform(time, amplitude)
    cutoff_frequency = 0.8 * nyquist_frequency
    cutoff_frequencies = list(map(lambda f: 0 if abs(f) > cutoff_frequency else 1, frequencies))
    filtered_frequencies = frequency * cutoff_frequencies
    filtered_amplitude = numpy.fft.ifft(filtered_frequencies)

    matplotlib.pyplot.plot(time, filtered_amplitude, label = 'Gráfico 4: representação do sinal filtrado')
    matplotlib.pyplot.show()
    return 'Veja o gráfico 4'

def main(load_signal):
    time, amplitude = load_signal()
    exercises = [exercise1, exercise2, exercise3, exercise4, exercise5, exercise6, exercise7]

    for item, exercise in enumerate(exercises):
        print("{0}. {1}".format(item+1, exercise(time, amplitude)))
