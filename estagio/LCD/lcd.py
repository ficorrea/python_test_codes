import Adafruit_CharLCD as LCD
import Adafruit_DHT
import RPi.GPIO as GPIO
import time

lcd_rs = 17
lcd_en = 27
lcd_d4 = 22
lcd_d5 = 10
lcd_d6 = 9
lcd_d7 = 11

lcd_colunas = 16
lcd_linhas = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_colunas, lcd_linhas)

botao1 = 7
botao2 = 8

sensor_atm = Adafruit_DHT.DHT11
pino_sensor_atm = 25

presenca1 = 24
presenca2 = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(botao1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(botao2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(pino_sensor_atm, GPIO.IN)
GPIO.setup(presenca1, GPIO.IN)
GPIO.setup(presenca2, GPIO.IN)

menu = 0

def delay(n):
    time.sleep(n)

def sair():
    while True:
        global menu 
        if (GPIO.input(botao1) == 1 or GPIO.input(botao2) == 1):
            lcd.clear()
            lcd.message('Saindo...')
            delay(1)
            menu = 0
            break
    
def sensores_atm():
    lcd.clear()
    lcd.message('ATMOSFERICOS\n')
    lcd.message('[1]Temp-[2]Umi')
    delay(0.5)
    umid, temp = Adafruit_DHT.read_retry(sensor_atm, pino_sensor_atm)
    t = str(temp) + str('C')
    u = str(umid) + str('%')
    while True:
        if GPIO.input(botao1) == 1:
            lcd.clear()
            lcd.message('TEMPERATURA\n')
            lcd.message(t)
            delay(0.5)
            sair()
            lcd.clear()
            break
        elif GPIO.input(botao2) == 1:
            lcd.clear()
            lcd.message('UMIDADE\n')
            lcd.message(u)
            delay(0.5)
            sair()
            lcd.clear()
            break
        
def status_presenca(sensor):
    if GPIO.input(sensor) == 1:
        lcd.message('Ativado')
    else:
        lcd.message('Desativado')        
       
def sensores_pre():
    lcd.clear()
    lcd.message('PRESENCA\n')
    lcd.message('[1]S1 - [2]S2')
    delay(0.5)
    while True:
        if GPIO.input(botao1) == 1:
            lcd.clear()
            lcd.message('Presenca 1\n')
            status_presenca(presenca1)
            delay(0.5)
            sair()
            lcd.clear()
            break
        elif GPIO.input(botao2) == 1:
            lcd.clear()
            lcd.message('Presenca 2\n')
            status_presenca(presenca2)
            delay(0.5)
            sair()
            lcd.clear()
            break
        
def main():    
    lcd.message('    SENSORES\n')
    delay(1)
    lcd.clear()
    lcd.message('[1] Atmosfericos\n')
    lcd.message('[2] Presenca')


while True:
    global menu
    while menu == 0:
        main()
        menu = 1
    if GPIO.input(botao1) == 1:
        sensores_atm()
    elif GPIO.input(botao2) == 1:
        sensores_pre()
    
    



