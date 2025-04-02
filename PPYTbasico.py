import random
computadora = random.randint(0,4)

print ("Escoge tu arma")
print ("piedra(1)","papel(2)","tijera(3)","lagarto(4)","spok(5)")
usuario = int(input())
usuario=usuario-1

def armas (escoge):
    opciones = ["piedra","papel","tijera","lagarto","spok"]
    objeto = opciones[escoge]
    return objeto

def fuerza (num):
    valores = [15,8,16,14,20]
    poder = valores[num]
    return poder

obj_compu = armas(computadora)
val_compu = fuerza(computadora)
obj_usuario= armas(usuario)
val_usuario= fuerza(usuario)
resultado= val_usuario - val_compu

print ("Yo pedi "+ obj_compu + ", tu escogiste " + obj_usuario +". El resultado es:")

if resultado == 0: print ("empate")

elif resultado ==1 or resultado==4 or resultado==6 or resultado==-2 or resultado==-5 or resultado==-12 or resultado==8 or resultado==-7:
    print ("Ganaste")
else:
    print ("Gane")
