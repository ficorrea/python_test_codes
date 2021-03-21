# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time as tm

# Pinos
pin1 = 17
pin2 = 27
pin3 = 22
pin4 = 25

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)
GPIO.setup(pin4, GPIO.OUT)

def ligar1():
	GPIO.output(pin1, False)
	
def desligar1():
	GPIO.output(pin1, True)

def ligar2():
	GPIO.output(pin2, False)
	
def desligar2():
	GPIO.output(pin2, True)

def ligar3():
	GPIO.output(pin3, False)
	
def desligar3():
	GPIO.output(pin3, True)

def ligar4():
	GPIO.output(pin4, False)
	
def desligar4():
	GPIO.output(pin4, True)
