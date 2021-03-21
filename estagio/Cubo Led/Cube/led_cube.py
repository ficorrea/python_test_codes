# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import random


class Cubo():

    delay = 0

    # Configuração dos pinos das colunas (Cátodos dos led's)
    Pin1 = 2
    Pin2 = 3
    Pin3 = 18
    Pin4 = 10
    Pin5 = 9
    Pin6 = 11
    Pin7 = 25
    Pin8 = 8
    Pin9 = 7

    # Configuração dos pinos das camadas (Base dos transistores)
    Alta = 17
    Media = 27
    Baixa = 22

    # Sequência de LEDs
    Normal = [Pin1, Pin2, Pin3, Pin4, Pin5, Pin6, Pin7, Pin8, Pin9]
    Reverso = [Pin9, Pin8, Pin7, Pin6, Pin5, Pin4, Pin3, Pin2, Pin1]
    Estrela1 = [Pin1, Pin2, Pin3, Pin6, Pin9, Pin8, Pin7, Pin4]
    Estrela2 = [Pin9, Pin8, Pin7, Pin4, Pin1, Pin2, Pin3, Pin6]
    Espiral = [Pin1, Pin2, Pin3, Pin6, Pin9, Pin8, Pin7, Pin4, Pin5]
    EspiralReverso = [Pin5, Pin4, Pin7, Pin8, Pin9, Pin6, Pin3, Pin2, Pin1]

    # Camadas
    Camadas = [Alta, Media, Baixa]

    def __init__(self):
        self.setup()
        self.delay = 0.2

    # Configuração dos pinos de I/O
    def setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Normal, GPIO.OUT)
        GPIO.setup(self.Camadas, GPIO.OUT)
        GPIO.output(self.Normal, False)
        GPIO.output(self.Camadas, True)

    # Método sequencial
    def sequencia(self, Pin):
        for i in Pin:
            GPIO.output(i, True)
            sleep(self.delay)
            GPIO.output(i, False)

    # Animações
    def randomico(self):
        camada = random.randint(0, 2)
        GPIO.output(self.Camadas[camada], True)
        led = random.randint(0, 8)
        GPIO.output(self.Normal[led], True)
        sleep(self.delay)
        GPIO.output(self.Camadas[camada], False)
        GPIO.output(self.Normal[led], False)
        sleep(self.delay)

    def random_colunas(self):
        GPIO.output(self.Camadas, True)
        self.sequencia(self.Normal)
        self.sequencia(self.Reverso)
        GPIO.output(self.Camadas, False)

    def espiral_led(self):
        GPIO.output(self.Camadas, True)
        self.sequencia(self.Espiral)
        self.sequencia(self.EspiralReverso)
        GPIO.output(self.Camadas, False)

    def random_camadas(self):
        GPIO.output(self.Alta, True)
        self.sequencia(self.Normal)
        GPIO.output(self.Alta, False)
        GPIO.output(self.Media, True)
        self.sequencia(self.Reverso)
        GPIO.output(self.Media, False)
        GPIO.output(self.Baixa, True)
        self.sequencia(self.Normal)
        GPIO.output(self.Baixa, False)

    def mix(self):
        for i in range(10):
            self.randomico()
        sleep(self.delay)
        self.random_colunas()
        sleep(self.delay)
        self.espiral_led()
        self.random_camadas()
        sleep(self.delay)
