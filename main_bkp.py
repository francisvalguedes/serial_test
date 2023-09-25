import serial
import threading
from time import perf_counter

#pacote = b'STX200923214300123+001.123+003.321661ETX' # pacote a ser enviado

# Função loop
def loop(last=[-1]):

    if stop=='run':
        threading.Timer(0.0996, loop).start()

  
    ser.write(b'STX200923214300123+001.123+003.321661ETX')

    receive = ser.read_until(b'D') #read_until(b'DS') #read_all() #.decode('ascii')
    print(receive)

    act = perf_counter()
    dur = act -last[0]    
    print('stime: {:.5f}'.format(dur))
    last[0] =act

    print('enter para parar')

    if stop!='run':
        ser.close()
      


# Configurações:
# ******************************************************************

# porta Serial:
serial_port_name =  '/dev/ttyUSB0' # para teste de desenvolvimento
#serial_port_name =  '/dev/ttyS0' # para simulação ILT

# instancia serial:
ser = serial.Serial(serial_port_name, 4800,timeout=0.01)
# ser = serial.Serial('/dev/ttyS0', 4800,timeout=0.01)

# fim das configurações
# ******************************************************************

# inicializa variaveis
stop = 'run'

# chama a função do tread
loop()

# enquanto não for digitado enter solicita entrada para parar o tread
while stop == 'run':    
    stop = input('enter to stop\n')