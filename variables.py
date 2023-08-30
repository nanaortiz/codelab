# i
edad = 12
nombre = "Natalia"
estatura = 1.57
fuma = True

persona = nombre + str(edad) + str(estatura) + str(fuma)
print(persona)

# ii Python tiene precision aritmetica en los numeros enteros (int), es decir que se pueden repressentar numeros aritmeticamente grandes. La unica limitacion es la memoria.  A pesar de esto, razones históricas pueden generar ocasionalmente OverflowError para números enteros que se encuentran fuera del rango requerido.
#    los float no tienen precision infinita. No se puede representar tanta precision decimal, por ejemplo 0.999999999999999999999999999 se almacena como una aproximacion a 1. Es decir, los float tiene un malor max 1.7976931348623157e+308 si se pasa tomara la valiable un valor inf.

# iii fórmula de la suma de los primeros n números pares
# s = 2 + 4 + 6 + .....+ 40 = 420
# s = 2 + 4 + 6 + .....+ 2n
# entonces definimos n 
# 2n = 40
n = 20
print(n)
s = print(n*(n+1))