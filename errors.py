def dividir(dividendo,divisor):
    try:
        result = dividendo/divisor
    except ZeroDivisionError:
        print("ERROR, estas dividiendo entre cero")
    except TypeError:
        print("ERROR, estás usando STR")
    else:
        print(result)
    finally:
        print(":) Me ejecute")
print(dividir(1,0))