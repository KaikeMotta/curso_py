velocidade = 59
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

car_multado =  local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1

if velocidade > RADAR_1:
    print('Ele passou a velocidade do radar 1')

if local_carro and LOCAL_1:
    print('carro passou pelo radar')

if car_multado:
    print('carro foi multado em radar 1')