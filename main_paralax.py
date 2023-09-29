import serial
import threading
from time import perf_counter
import datetime
import glob

import numpy as np
import pymap3d as pm

#pacote = b'STX200923214300123+001.123+003.321661ETX' # pacote a ser enviado

# Função loop
def loop(last=[-1]):
    global idx
    #threading.Timer(1.0, loop,[satellite, tvar, inv_J, sp_time]).start()
    if stop=='run':
        threading.Timer(0.0996, loop).start()

    now = datetime.datetime.now()

    data_hora = now.strftime("%d%m%y%H%M%S%f")[:-3]

    if fixo_traj != 'fixo':
        azim_elev = '{:+08.3f}{:+08.3f}'.format(azimute[idx], elevacao[idx])
    else:
        azim_elev = '{:+08.3f}{:+08.3f}'.format(azimute_f, elevacao_f)

    msg = 'STX'+data_hora+azim_elev+mode1+mode2+canal+'ETX' # pacote a ser enviado    
    
    pacote = bytes(msg,'ascii')    
    ser.write(pacote)
    receive = ser.read_until(b'D') #read_until(b'DS') #read_all() #.decode('ascii')

    print(receive)
    act = perf_counter()
    dur = act -last[0]    
    #print('stime: {:.5f}'.format(dur))
    print('enviado: ' + msg+ ' periodo(s): {:.5f}'.format(dur)+' tempo(s): {:.2f}'.format(idx/10.0))
    last[0] =act

    if idx<len_traj:
        idx = idx + passo
        if not idx<len_traj:
            idx=len_traj-1

    print('enter para parar')

    if stop!='run':
        ser.close()
      

# Configurações:
# ******************************************************************
fixo_traj = 'fix' # para ponto fixo: 'fixo', ou para trajetória: qualquer outro texto

# ponto fixo:
elevacao_f = 10.321321
azimute_f = 125.123122

# modo:
mode1 = '6'
mode2 = '6'

# canal:
canal = '1'

# porta Serial:
# SERIAL_PORT_NAME =  '/dev/ttyUSB0' # para teste de desenvolvimento
SERIAL_PORT_NAME =  '/dev/ttyS0' # para simulação ILT
BAUD_RATE = 4800
PARITY = 'E'

# passo da trajetória:
passo = 10  # passo da trajetória 1 - passo real, 10 - acelerado em 10x 

# instancia serial:
ser = serial.Serial(SERIAL_PORT_NAME, BAUD_RATE,timeout=0.01, parity=PARITY)

# Rampa
lat00, lon00, h00 = -5.922204, -35.161500, 32.0

#Sensor
lat0, lon0, h0 = -5.922274, -35.171978, 59.0

# fim das configurações
# ******************************************************************

# Inicialização da trajetória

txt_files = glob.glob('trn/*.trn')
sel_traj = 0

if len(txt_files) > 1:
    idx = 0
    for line in txt_files:
        print(str(idx) + "-" + line + "\n")
        idx+=1
    
    sel_traj = int(input("selecione a trajetória: "))

arr = np.loadtxt(txt_files[sel_traj],delimiter=",",skiprows=1 )
ecef_x, ecef_y, ecef_z = pm.enu2ecef(arr[:,0], arr[:,1], arr[:,2], lat00, lon00, h00)
enux, enuy, enuz = pm.ecef2enu(ecef_x, ecef_y, ecef_z, lat0, lon0, h0 )
azimute, elevacao, range = pm.enu2aer(enux, enuy, enuz, deg=True)

# inicializa variaveis
len_traj = len(azimute)
idx = 0
stop = 'run'

# chama a função do tread
loop()

# enquanto não for digitado enter solicita entrada para parar o tread
while stop == 'run':    
    stop = input('enter to stop\n')




# Iniciando conexao serial
# ser = serial.Serial('/dev/ttyUSB0', 9600,timeout=0.1)
# print(ser.name)         # check which port was really used
# ser.write(b'hellocasa\ncaiada\n\n')     # write a string

# bfer = ser.read_until('\n\n')
# print(bfer)
# time.sleep(0.1)
# ser.close() 