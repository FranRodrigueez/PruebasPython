
#Haz una función multiplicar que no utilice el símnbolo multiplicación

def multiply(num1, num2):

    result = 0

    for rep in range(num1):
        result += num2

    return result

total = multiply(6,5)

print(total)
