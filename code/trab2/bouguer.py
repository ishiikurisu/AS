# -*- coding: utf-8 -*-
import re
from trabalho import *

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

Este é o processamento do arquivo "Bouguer-1.txt". Nota-se que estamos relacionando a distância com a medida Bouguer para que as questões façam sentido neste caso, já que o dado encontra-se no espaço 3D.
"""

#####################
# Loading functions #
#####################

def load_signal():
    time, amplitude = [], []

    with open('Bouguer-1.txt', 'r') as fp:
        for line in fp:
            raw_data = re.split('\\s+', line)
            time.append(raw_data[0])
            amplitude.append(raw_data[3])

    time = list(map(float, time[1:]))
    amplitude = list(map(float, amplitude[1:]))
    return time, amplitude

if __name__ == '__main__':
    main(load_signal)
