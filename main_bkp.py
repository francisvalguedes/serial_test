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
#SERIAL_PORT_NAME =  '/dev/ttyUSB0' # para teste de desenvolvimento
SERIAL_PORT_NAME =  '/dev/ttyS0' # para simulação ILT
BAUD_RATE = 4800
PARITY = 'E'

# instancia serial:
ser = serial.Serial(SERIAL_PORT_NAME, BAUD_RATE,timeout=0.01, parity=PARITY)

# fim das configurações
# ******************************************************************

# inicializa variaveis
stop = 'run'

# chama a função do tread
loop()

# enquanto não for digitado enter solicita entrada para parar o tread
while stop == 'run':    
    stop = input('enter to stop\n')