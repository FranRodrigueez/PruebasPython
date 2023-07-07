# PRUEBA TÉCNICA #

# En la variable 'text' dispones de una cadena de texto
# Debes contar las palabras y devolver cuantas veces se repiten cada una de ellas
#Ejemplo --> 'nadie' aparece dos veces

text = "Creo que a veces es la gente de la que nadie espera nada, la que hace cosas que nadie puede imaginar"

def tolower(text):

    lowerText = text.lower()

    return lowerText

def cleaningText(text):    

    cleanedText = text.replace(',', "")

    return cleanedText

def countWords(text):

    TextArray = text.split()
    dictionary = {}

    for word in TextArray:
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1

    diccionario_ordenado = dict(sorted(dictionary.items(), key=lambda item: item[1]), reverse = True)

    return diccionario_ordenado

lowerText = tolower(text)

cleanedText = cleaningText(lowerText)

print(countWords(cleanedText))
