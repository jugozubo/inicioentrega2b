# main.py -- put your code here!
from machine import Pin,Timer, PWM, ADC, TouchPad  #Permite hacer otras funciones
from time import sleep,sleep_ms  #No puede hacer otras funciones
import dht


#CLAVE ARCHIVO EN LA EEPROM 
#Se hace con archivo .txt
archivo=open("clave.txt","w")
archivo.write("[7,5,3,2]")
archivo.close()

global display
display=0
medidor=dht.DHT11(Pin(4))
Pin(4,Pin.IN)
pinescatodos=[13,5]
Pin(5,Pin.OUT)
Pin(13,Pin.OUT)
              #a, b, c, d, e, f, g
pinesdisplay=[26,25,17,16,27,14,12]
for i in range(0,7):
    Pin(pinesdisplay[i],Pin.OUT)

tecla=TouchPad(Pin(32))

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
    #valor=Temp.read() 
    #leddimmer.duty(valor)
    #print(display)
    for i in range(0,7):
        Pin(pinesdisplay[i],value=valoresdisplay[display%10][i])
        Pin(5,value=1)
        Pin(13,value=0)
    sleep_ms(10)
    for i in range(0,7):
        Pin(pinesdisplay[i],value=valoresdisplay[int(display/10)][i])
        Pin(5,value=0)
        Pin(13,value=1)
    sleep_ms(10) 
    if tecla.read()<400:
        temporizador.deinit()   #Detiene el temporizador
        a=int(display)
        clave=[]
        clave.append(a)
        b=int(5)
        clave.append(b)
        c=int(3)
        clave.append(c)
        d=int(2)
        clave.append(d)
        print("la clave fue")
        print(clave)
        archivo=open("clave.txt","r")
        contenido=archivo.read()
        if str(clave)==contenido:
            print("correcto")

                #print(a)
        #print("correcto")
        try :
            
            medidor.measure()
            Temp=medidor.temperature()
            # Hum=medidor.humidity()
            # print("Temperatura=")
            print(int(Temp))
            # print("Humedad=")
            # print(Hum)
            # unidades=int(Temp%10)
            # decenas=int(Temp/10)
            # print(decenas)
            # for i in range(0,7):
            #     Pin(pinesdisplay[i],value=valoresdisplay[unidades][i])
            #     Pin(5,value=1)
            #     Pin(13,value=0)
            # sleep_ms(50)
            # for i in range(0,7):
            #     Pin(pinesdisplay[i],value=valoresdisplay[decenas][i])
            #     Pin(5,value=0)
            #     Pin(13,value=1)
            # sleep_ms(50)
        except OSError as e:
            print("sensor desconectado")
        
        
