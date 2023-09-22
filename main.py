
import time
import serial
import struct
import threading
from time import perf_counter


# Função loop

def loop(last=[-1]):
    #threading.Timer(1.0, loop,[satellite, tvar, inv_J, sp_time]).start()
    if len(stop)>1:
        threading.Timer(0.1, loop).start()
    # ser.write(b'Francisval\r\n')
    ser.write(pacote)
    receive = ser.read_all() #.decode('ascii')

    print(receive)
    act = perf_counter()
    dur = act -last[0]    
    print('stime: {:.5f}'.format(dur))
    last[0] =act

# Código
pacote = b'STX200923214300123+001.123+003.321661ETX' # pacote a ser enviado

# ser = serial.Serial('/dev/ttyUSB0', 4800,timeout=0.01)
ser = serial.Serial('/dev/ttyS0', 4800,timeout=0.01)

stop = 'teste'

loop()

stop = input('enter to stop\n')


# Iniciando conexao serial
# ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=0.1)
# print(ser.name)         # check which port was really used
# ser.write(b'hellocasa\ncaiada\n\n')     # write a string

# bfer = ser.read_until('\n\n')
# print(bfer)
# time.sleep(0.1)
# ser.close() 