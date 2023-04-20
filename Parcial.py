# Mensaje de bienvenida.
print("COMIENZA EL CODIGO")

numero = -1

while numero <= 0:

    try:
        numero = int(input("\nDefina con un número para realizar la serie de datos. -> "))

        if numero > 0:
            break
        
        print("\033[1m"+"\nNo es posible ingresar la cantidad de datos escrita, por favor vuelva a intentarlo."+"\033[0m")

    except ValueError:
        print("\033[1m"+"\nUsted ingresó un valor que no es un número entero. Por favor ingrese un valor valido."+"\033[0m")

totalSuma = 1
para = 1

while para < numero:
    totalSuma += 1/(1+para)
    para +=1