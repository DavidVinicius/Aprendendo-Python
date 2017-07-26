segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
totalSegs = int(segundos)

dia   =  (totalSegs // 3600) // 24
horas = (totalSegs // 3600) % 24
segs_restantes = totalSegs % 3600
minutos   = segs_restantes // 60
segsFinal = segs_restantes % 60


print(dia," Dia",horas, " horas, ", minutos," minutos, ", segsFinal, " segundos")