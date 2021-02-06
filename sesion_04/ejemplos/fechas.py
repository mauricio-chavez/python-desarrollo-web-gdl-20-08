import datetime

fecha1 = datetime.date(1975, 12, 20)
fecha2 = datetime.date(1975, 12, 23)
diferencia_entre_fechas = fecha2 - fecha1

diferencia_24_dias = datetime.timedelta(days=24)
print(fecha1 + diferencia_24_dias)
