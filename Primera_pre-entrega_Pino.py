#-----------------------------------------BADE DE DATOS-------------------------------------------------------------------
#Creamos un diccionario donde se van a almacenar los registros-
mi_data = {}

#-----------------------------------------FUNCIONES-----------------------------------------------------------------------
#Creamos la función para registrar usuarios-
def registrar_usuario(almacenamiento):
    #Esta funcion recibe como parámetro el diccionario donde guardaremos los registros. Pide que ingresen un usuario y verifica si se encuentra en el diccionario, si no exite, nos pide además una contraseña para almacenarlo en el diccionario. Si el usuario ya existe, nos aclara que debemos ingresar uno distinto.
    usuario = input("Igrese usuario: ").lower()
    if usuario not in almacenamiento:
        contraseña = input("Ingrese contraseña: ")
        mi_data[usuario] = contraseña
        print(" * Ha sido registrado correctamente.")
    else:
        print(" * El usuario ingresado ya existe en la base de datos. Debe ingresar uno distinto.")

#Creamos la función para leer los registros-
def leer_registros(almacenamiento):
    #Esta función recibe como parámetro un diccionario e imprime la clave y valor de éste, usando un bucle for e items()
    print("* La información almacenada en la base de datos es:")
    for clave, valor in almacenamiento.items():
        print(f"Usuario: {clave} | Contraseña: {valor}")

#Creamos la función para almacenar los datos en un archivo.txt
def guardar_archivo_txt(almacenamiento):
    #Esta función implementa lo dado en la clase 8. Recibe como parámetro un diccionario y guarda todo lo que hayamos registrado hasta el momento en un archivo.txt-
    f = open("./archivo.txt", "w")
    f.write(f"{almacenamiento}")
    f.close()
    print("El archivo se guardo correctamente.")

#Creamos la función para inicio de sesion-
def login(almacenamiento):
    #Esta funcion simula el login de una cuenta, pide que ingresemos un usuario, primero verifica si el usuario ingresado se encuentra en el diccionario (si no se encuentra nos avisa que no existe en la basde de datos), si se encuentra, nos va pedir que ingresemos la contraseña y verifica si corresponde a la guardada. 
    usuario = input("Ingrese su usuario: ").lower()
    if usuario in almacenamiento:
        contraseña = input("Ingrese su contraseña: ")
        if contraseña == almacenamiento[usuario]:
            print(" * Ha ingresado correctamente!")
        else:
            print(" * Contraseña incorrecta.")
    else:
        print(" * El usuario ingresado no existe en la base de datos.")

#-----------------------------------------MENU P/ USUARIO-----------------------------------------------------------------

#Usamos un bucle while y armamos un menu para que el usuario elija lo que quiera hacer, para ello usamos estructura de flujo condicionales (if, elif, else) y tambien excepciones (try, except)-
while True:
    print(" Ingrese la opción que desea realizar:")
    print(" 1. Registrar usuario nuevo")
    print(" 2. Leer los registros")
    print(" 3. Iniciar sesión")
    print(" 4. Guardar los datos en un archivo.txt")
    print(" 5. Terminar programa")
    try:
        opcion = int(input("==>"))
        if opcion == 1:
            registrar_usuario(mi_data)
        elif opcion == 2:
            leer_registros(mi_data)
        elif opcion == 3:
            login(mi_data)
        elif opcion == 4:
            guardar_archivo_txt(mi_data)
        elif opcion == 5:
            print("Finalizó el programa. Hasta la próxima!")
            break
        else:
            print(" * El número ingresado no corresponde a las opciones. Por favor vuelva a intentarlo.")
    except:
        print(" * Opción inválida. Debe ingresar un número entero.")
