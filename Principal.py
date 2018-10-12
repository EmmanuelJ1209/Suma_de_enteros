__Author__ ='Emmanuel Palacios Aureoles'

def sumar (n):
    if n==2:
        return 2;
    else:
        return n + sumar(n-2)


n= int(input("ingrese el numero que se desea sumar"))
print(sumar(n))
