# main.py -- put your code here!
from machine import Pin,Timer, PWM, ADC  #Permite hacer otras funciones
from time import sleep  #No puede hacer otras funciones

global display
display=0
pinesdisplay=[26,25,17,16,27,14,12]
for i in range(0,7):
    Pin(pinesdisplay[i],Pin.OUT)

valoresdisplay=[[0,0,0,0,0,0,1],
                [1,0,0,1,1,1,1],
                [0,0,1,0,0,1,0],
                [0,0,0,0,1,1,0],
                [1,0,0,1,1,0,0],
                [0,1,0,0,1,0,0],
                [0,1,0,0,0,0,0],
                [0,0,0,1,1,1,1],
                [0,0,0,0,0,0,0],
                [0,0,0,0,1,0,0]]
def contador(timer):
    global display
    display=display+1
Pin(35,Pin.IN)
leddimmer=PWM(Pin(2),freq=10000)
Temp=ADC(Pin(35))
Temp.atten(ADC.ATTN_11DB)
Temp.width(ADC.WIDTH_10BIT)
temporizador=Timer(1)
temporizador.init(period=1000,mode=Timer.PERIODIC,callback=contador)

while True:
    valor=Temp.read() 
    leddimmer.duty(valor)
    print(display)
    for i in range(0,7):
        Pin(pinesdisplay[i],value=valoresdisplay[display][i])
