# -*- coding: utf-8 -*-
import numpy
import matplotlib.pyplot
import re
from functools import reduce

SOBRE = """
Trabalho de Análise de Sinais
=============================

Aluno: Cristiano Alves da Silva Júnior
Matrícula: 13/0070629

Sobre
-----

Este trabalho visa analisar um sinal geofísico usando Python seguindo o roteiro fornecido pelo professor:

1 – Qual o é número de amostras do seu dado?
2 – Qual é a taxa de amostragem?
3 – Qual a frequência máxima que o seu sinal pode ser mostrado?
4 – Faça o gráfico do seu sinal?
5 – Apresente o sinal no domínio da frequência?
6 – Passe um filtro  passa alta que elimine 20% do sinal que é possível amostrar. p.e. a frequência máxima é 100 Hz, você deve passa um filtro passa alta que elimine 0 a 20 Hz.
7 -  Passe um filtro passa baixa que elimine 20% do sinal que é possível amostrar. p.e. a frequência máxima é 100 Hz, você deve passa um filtro passa baixe que elimine 80 a 100 Hz.

Para tanto, escolhemos o sinal identificado por "Sismologia-1.txt".

"""

def timestamp_to_integer(timestamp):
    # Example of timestamp: 2004-11-15T09:03:56.142200
    digits = map(float, re.split(':', re.split('T', timestamp)[1]))
    power = [60*60, 60, 1]
    time = sum(map(lambda x: x[0]*x[1], zip(digits, power)))

    return time

def load_signal():
    time, amplitude = [], []

    with open('Sismologia-1.txt', 'r') as fp:
        for line in fp:
            raw_data = re.split('\\s+', line)
            time.append(raw_data[0])
            amplitude.append(raw_data[1])

    time = list(map(timestamp_to_integer, time[1:]))
    amplitude = list(map(float, amplitude[1:]))
    return time, amplitude

def exercise1(time, amplitude):
    no_samples = len(amplitude)

    return 'O número de amostras é {0}'.format(no_samples)

def exercise2(time, amplitude):
    sample_rate = 1.0 / (time[1] - time[0])

    return 'A taxa de amostragem é {0} Hz'.format(sample_rate)

if __name__ == '__main__':
    time, amplitude = load_signal()
    exercises = [exercise1, exercise2]

    for item, exercise in enumerate(exercises):
        print("{0}. {1}".format(item+1, exercise(time, amplitude)))

    matplotlib.pyplot.plot(time, amplitude)
    matplotlib.pyplot.show()
