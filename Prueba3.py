#Realiza un programa:
#1. Que extraiga los dígitos de las siguientes cadena de texto.
#2. Que los ordene de menor a mayor y los devuelva en una cadena de texto
#3. Que sume todos los dígitos y devuelva el resultado de la suma total
#4. Todos estos resultados deben ser mostrados por consola de manera simultánea


def extraerDigitos(texto):
    digitos = ""

    for digito in texto:
        if digito.isdigit():
            digitos = digitos + digito
    
    return digitos


def ordenarDigitos(digitos):
    digitosOrdenados = sorted(digitos)
    
    ordenados = ""

    for digito in digitosOrdenados:
        ordenados = ordenados + digito

    return ordenados
    


def sumaDigitos(digitosExtraidos):
    suma = 0

    for digito in digitosExtraidos:
        suma += int(digito)
    
    return "La suma de los dígitos es: " + str(suma)



if __name__ == "__main__":

    text = '3ha4sa2df3as5f3ad5a4sdf8df6'


digitos = extraerDigitos(text)

print(extraerDigitos(text))
print(ordenarDigitos(digitos))
print(sumaDigitos(digitos))