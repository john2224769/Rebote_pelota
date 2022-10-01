# Ejercicio N. 2. repeticiones: una pelota se deja caer desde una altura h, y en cada rebote sube el 10% menos del anterior. 
# hacer el diagrama de flujo y el programa en python, que lea h y que calcule e imprima en cual renbote la pelota no alcanza a subir la quita parte de la altura inicial. 

print("\n-------------------------------------------------------")
print("------------- Calculo de rebote de pelota ---------------")
print("-------------------------------------------------------\n")

#input

h=int(input("Ingrese la altura desde la cua se deja caer la pelota: "))
r=0
c=h/5

#processing 
while h>c:
    h=h-(h*0.10)
    r=r+1

print("/n La pelota no alcanza la quinta parte de la altura inicial al rebote numero "+str(r))
print(" ")
