"""
CONSTANTE = "Variávies" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- contagem de complexidade (quanto mais longe da margem é ruim)
"""
velocidade = 61     # velocidade atual do carro
local_carro = 101   # local em que o carro está na estrada

# py não tem constantes imutaveis
RADAR_1 = 60    # velocidade máxima do radar 1
LOCAL_1 = 100   # local onde o radar 1 está
RADAR_RANGE = 1 # a distância onde o radar pega

# ainda dá para simplificar mais 
# (separar o "carro_passou_radar_1 em outras variaveis")
velocidade_excedeu_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 + RADAR_1) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and velocidade_excedeu_radar_1

if velocidade > RADAR_1:
    print('Velocidade do carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou no radar 1 dentro do limite de velocidade')

# barra invertida " \ " pode ser usado para quebra de linha
if carro_multado_radar_1:
    print('Carro foi multado em radar 1')