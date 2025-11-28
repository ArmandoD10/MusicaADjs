def calculador():
    print("Ojo no se aceptan ni letras ni caracteres!")
    num1 = int(input("Digite un numero: "))
    num2 = int(input("Digite un numero: "))
    print(f"Suma: {num1 + num2} \n Resta: {num1 - num2} \n Division: {num1 / num2} \n Multiplicacion: {num1 * num2}")
    print("Tus resultados!")
    

def agregar():
    lista = []

    for i in range(5):
        dato = input("Digite caracter: (5)")
        lista.append(dato)

    print("Tu lista: !")
    print(lista)


correo = "armandodiaz1020158@gmail.com"
contrasena = "1020158ad"
cont = 0

while True:
    cor = input("Ingrese correo....")
    pas = input("Ingrese contrasena....")

    if (cor == correo) and (pas == contrasena):
        print("Acceso consedido !")
        print("Bienvenido al sistema Armando")
        respuesta = int(input("Seleccione una opcion: \n 1 = Calcular \n 2 = Agregar Lista"))

        if respuesta == 1:
            calculador()
        elif respuesta == 2:
            agregar()
        else:
            print("Caracter inavlido saliendo del sistema!")
            break

    else:
        print("Contrasena incorrecta, Intente de nuevo")
        cont += 1

        if(cont == 5):
            print("Has obtenido demasiados intentos, Vuelva mas tarde")
            print("Saliendo del sistema!")
            print("Derechos reservados por ADCode.com")
            break


