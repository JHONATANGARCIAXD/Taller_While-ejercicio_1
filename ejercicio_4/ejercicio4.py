# Ejercicio 4



# input

a= int(input("Digite el valor de a: "))
b= int(input("Digite el valor de b: "))

# processing
 
if (a<b):
    cant_num=0
    a=a+1
    while (a<=b):
        r=a%5
        if r==0:
            cant_num=cant_num+1
        a=a+1         
    print("Los números multiplos de 5 que hay en este rango son:" , cant_num)              
else:
    print("a debe ser menor que b")

  