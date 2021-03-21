# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO


class Rele():

    def __init__(self):
        # Pinos
        self.pin1 = 17
        self.pin2 = 27
        self.pin3 = 22
        self.pin4 = 23

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin1, GPIO.OUT)
        GPIO.setup(self.pin2, GPIO.OUT)
        GPIO.setup(self.pin3, GPIO.OUT)
        GPIO.setup(self.pin4, GPIO.OUT)

    def desliga(self, rele):
        if rele == 1:
            GPIO.output(self.pin1, True)
        elif rele == 2:
            GPIO.output(self.pin2, True)
        elif rele == 3:
            GPIO.output(self.pin3, True)
        elif rele == 4:
            GPIO.output(self.pin4, True)
        elif rele == 8:
            GPIO.output(self.pin1, True)
            GPIO.output(self.pin2, True)
            GPIO.output(self.pin3, True)
            GPIO.output(self.pin4, True)

    def liga(self, rele):
        if rele == 1:
            GPIO.output(self.pin1, False)
        elif rele == 2:
            GPIO.output(self.pin2, False)
        elif rele == 3:
            GPIO.output(self.pin3, False)
        elif rele == 4:
            GPIO.output(self.pin4, False)
        elif rele == 8:
            GPIO.output(self.pin1, False)
            GPIO.output(self.pin2, False)
            GPIO.output(self.pin3, False)
            GPIO.output(self.pin4, False)
