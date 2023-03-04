# Programa que determina si los dos últimos dígitos son iguales 

print("-----------------------------------------------")
print("----------------últimos iguales----------------")
print("-----------------------------------------------")

# Input

n=int(input("Dígite un número entero: "))

# Processing y output

if n<0:
    n=n*-1
else:
    n=n

y=n%10
x=n//10
z=x%10

if z==y:
    print("-----------------------------------------------")
    print("Los dos últimos dígitos son iguales")
    print("-----------------------------------------------")
else:
    print("-----------------------------------------------")
    print("Los dos últimos dígitos no son iguales")
    print("-----------------------------------------------")