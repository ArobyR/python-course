from numeros_no_pares_excepcion import NumerosNoParesException
result = None

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    
    if a % 2 != 0 or b % 2 != 0:
        raise NumerosNoParesException("Numeros no pares")
except ZeroDivisionError as e:
    print("This is an error of", e, end="\n\n")
    print(type(e))
except TypeError as e:
    print("This is an error of", e, end="\n\n")
    print(type(e))
except Exception as e:
    print("This is an error of", e, end="\n\n")
    print(type(e))
else:
    print("Without exception")
finally:
    print("End of exception manager")

print("Continue...")
print("Result: ", result)