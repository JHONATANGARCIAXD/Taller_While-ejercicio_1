# ejercicio 6

# input

C=int(input("Digite el Capital: "))

# processing

D= 2*C
N=0

while(C<D):
    C=C+0.05*C
    N=N+1
else:
    C==D
    print(" Cuando el capital se duplique han trancurrido " + str(N) + " Meses " )