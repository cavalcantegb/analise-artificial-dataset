from random import seed
from random import random
from random import gauss
from random import randint
import csv

seed(23)
numeroLinhas = 5000000
with open('Merged_HT101.csv', 'w', newline='') as f:
    theWriter = csv.writer(f)
    theWriter.writerow(['Date','Weight','Temperature','DewPoint','Pressure','WindSpeed','Class'])


    random_walk_peso = random_walk_temperatura = list()
    random_walk_dew_point = random_walk_pressao = list()
    random_walk_vento = list()

    random_walk_peso.append(20.0)
    random_walk_temperatura.append(27.0)
    random_walk_dew_point.append(8.0)
    random_walk_pressao.append(1011.0)
    random_walk_vento.append(5.0)

    for i in range(1, numeroLinhas):
        # Peso
        peso = random_walk_peso[i-1] + gauss(0,1)
        peso = 11.0 if peso < 11.0 else peso
        peso = 30.0 if peso > 30.0 else peso
        random_walk_peso.append(peso)

        # Temperatura
        temperatura = random_walk_temperatura[i-1] + gauss(0, 1)
        temperatura = 20 if temperatura < 20 else temperatura
        temperatura = 35 if temperatura > 35 else temperatura
        random_walk_temperatura.append(temperatura)

        # Dew Point
        dewPoint = random_walk_dew_point[i-1] + gauss(0, 1)
        dewPoint = -7 if dewPoint < -7 else dewPoint
        dewPoint = 26 if dewPoint > 26 else dewPoint
        random_walk_dew_point.append(dewPoint)

        # Pressao
        pressao = random_walk_pressao[i-1] + gauss(0,1)*0.7
        pressao = 1000 if pressao < 1000 else pressao
        pressao = 1030 if pressao > 1030 else pressao
        random_walk_pressao.append(pressao)

        # Vento
        vento = random_walk_vento[i-1] + (gauss(0,1) * random() * 1.1)
        vento = 0.65 if vento < 0.65 else vento
        vento = 7.00 if vento > 7.00 else vento
        random_walk_vento.append(vento)

        # Class
        classe = randint(0,3)

        theWriter.writerow(['2017-04-04 00:00:00', peso, temperatura, dewPoint, pressao, vento, classe])
