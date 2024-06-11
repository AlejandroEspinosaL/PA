import network
import socket
from time import sleep
import machine
from machine import Pin
import utime


ssid = 'wea'
password = '12345678'

Motor_A_Adelante = Pin(16, Pin.OUT)
Motor_A_Atras = Pin(17, Pin.OUT)
Motor_B_Adelante = Pin(18, Pin.OUT)
Motor_B_Atras = Pin(19, Pin.OUT)

def mover(numero, duty):
    servo_pwm = machine.PWM(machine.Pin(numero))
    servo_pwm.freq(50)
    servo_pwm.duty_u16(duty)

def adelante():
    Motor_A_Adelante.value(1)
    Motor_B_Adelante.value(1)
    Motor_A_Atras.value(0)
    Motor_B_Atras.value(0)
    
def atras():
    Motor_A_Adelante.value(0)
    Motor_B_Adelante.value(0)
    Motor_A_Atras.value(1)
    Motor_B_Atras.value(1)

def detener():
    Motor_A_Adelante.value(0)
    Motor_B_Adelante.value(0)
    Motor_A_Atras.value(0)
    Motor_B_Atras.value(0)

def izquierda():
    Motor_A_Adelante.value(1)
    Motor_B_Adelante.value(0)
    Motor_A_Atras.value(0)
    Motor_B_Atras.value(1)

def derecha():
    Motor_A_Adelante.value(0)
    Motor_B_Adelante.value(1)
    Motor_A_Atras.value(1)
    Motor_B_Atras.value(0)


detener()
    
def conectar():
    red = network.WLAN(network.STA_IF)
    red.active(True)
    red.connect(ssid, password)
    while red.isconnected() == False:
        print('Conectando ...')
        sleep(1)
    ip = red.ifconfig()[0]
    print(f'Conectado con IP: {ip}')
    return ip
    
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def pagina_web():
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            </head>
            <body>
            <!--botones-->
            <hr>
            <h1>Controles:</h1>
            <center>
            <form action="./adelante">
            <input type="submit" value="Adelante"style="background-color: #131229;border-radius: 15px;height:120px;width:120px;border: none;color: white;padding: 16px 24px;margin: 4px 2px"  />
            </form>
            <table><tr><td><form action="./izquierda">
            <input type="submit"value="Izquierda"style="background-color: #131229;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
            </form></td>
            <td><form action="./detener">
            <input type="submit" value="Detener" style="background-color: #FF0000; border-radius: 50px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
            </form></td>
            <td><form action="./derecha">
            <input type="submit" value="Derecha" style="background-color: #131229; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
            </form></td>
            </tr></table>
            <form action="./atras">
            <input type="submit" value="Atras" style="background-color: #131229; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
            </form>
            
            <table><tr><td><form action="./motor1_0">
            <input type="submit"value="0%"style="background-color: #00FFF3;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor1_50">
            <input type="submit" value="50%" style="background-color: #00FFF3; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor1_100">
            <input type="submit" value="100%" style="background-color: #00FFF3; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
            </form></td>
            </tr></table>
            
            <table><tr><td><form action="./motor2_0">
            <input type="submit"value="0%"style="background-color: #0008FF;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor2_50">
            <input type="submit" value="50%" style="background-color: #0008FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor2_100">
            <input type="submit" value="100%" style="background-color: #0008FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
            </form></td>
            </tr></table>
            
            <table><tr><td><form action="./motor3_0">
            <input type="submit"value="0%"style="background-color: #5500FF;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor3_50">
            <input type="submit" value="50%" style="background-color: #5500FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor3_100">
            <input type="submit" value="100%" style="background-color: #5500FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
            </form></td>
            </tr></table>
            
            <table><tr><td><form action="./motor4_0">
            <input type="submit"value="0%"style="background-color: #AA00FF;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor4_50">
            <input type="submit" value="50%" style="background-color: #AA00FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor4_100">
            <input type="submit" value="100%" style="background-color: #AA00FF; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
            </form></td>
            </tr></table>
            
            <table><tr><td><form action="./motor5_0">
            <input type="submit"value="0%"style="background-color: #FF00DC;border-radius: 15px;height:120px; width:120px;border: none; color: white;padding: 16px 24px;margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor5_50">
            <input type="submit" value="50%" style="background-color: #FF00DC; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px"/>
            </form></td>
            <td><form action="./motor5_100">
            <input type="submit" value="100%" style="background-color: #FF00DC; border-radius: 15px; height:120px; width:120px; border: none; color: white; padding: 16px 24px; margin: 4px 2px" />
            </form></td>
            </tr></table>
            
            
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    while True:
        cliente = connection.accept()[0]
        peticion = cliente.recv(1024)
        peticion = str(peticion)
        try:
            peticion = peticion.split()[1]
        except IndexError:
            pass
        if peticion == '/adelante?':
            adelante()
        elif peticion =='/izquierda?':
            izquierda()
        elif peticion =='/detener?':
            detener()
        elif peticion =='/derecha?':
            derecha()
        elif peticion =='/atras?':
            atras()
        elif peticion =='/motor1_0?':
            mover(1,1000)
        elif peticion =='/motor1_50?':
            mover(1,1500)
        elif peticion =='/motor1_100?':
            mover(1,2000)
        elif peticion =='/motor2_0?':
            mover(2,900)
        elif peticion =='/motor2_50?':
            mover(2,4450)
        elif peticion =='/motor2_100?':
            mover(2,8000)
        elif peticion =='/motor3_0?':
            mover(3,1000)
        elif peticion =='/motor3_50?':
            mover(3,4000)
        elif peticion =='/motor3_100?':
            mover(3,7000)
        elif peticion =='/motor4_0?':
            mover(4,7000)
            mover(5,1000)
        elif peticion =='/motor4_50?':
            mover(4,4000)
            mover(5,4000)
        elif peticion =='/motor4_100?':
            mover(4,1000)
            mover(5,7000)
        elif peticion =='/motor5_0?':
            mover(6,1000)
        elif peticion =='/motor5_50?':
            mover(6,4500)
        elif peticion =='/motor5_100?':
            mover(6,8000)
        html = pagina_web()
        cliente.send(html)
        cliente.close()

try:
    ip = conectar()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()

       