from config import *
from obtain import *
from creator import *

class Main:

    @classmethod
    def iniciar_aplicacion(cls):
       
        # Ejemplo de inicio de aplicación: Mostrar un menú de opciones al usuario
        while True:
            print('--- Menú Principal ---')
            print('1. Crear persona')
            print('2. Crear cuenta')
            print('3. Realizar consulta')
            print('4. Salir')

            opcion = input('Seleccione una opción: ')

            if opcion == '1':
                # Solicitar datos para crear una persona y llamar al método correspondiente en la clase Creator
                dni = input('Ingrese el DNI: ')
                nombre = input('Ingrese el nombre: ')
                apellidos = input('Ingrese los apellidos: ')
                direccion = input('Ingrese la dirección: ')
                telefono = input('Ingrese el teléfono: ')
                Creator.create_persona(dni, nombre, apellidos, direccion, telefono)
            elif opcion == '2':
                # Solicitar datos para crear una cuenta y llamar al método correspondiente en la clase Creator
                num_cuenta = input('Ingrese el número de cuenta: ')
                saldo = input('Ingrese el saldo: ')
                fecha_creacion = input('Ingrese la fecha de creación: ')
                Creator.create_cuenta(num_cuenta, saldo, fecha_creacion)
            elif opcion == '3':
                # Realizar una consulta o mostrar información según sea necesario
                # Puedes llamar a métodos en las otras clases para obtener información
                pass
            elif opcion == '4':
                # Salir del programa
                break
            else:
                print('Opción inválida')

        print('¡Hasta luego!')


    #Especificaciones para los metodos

    def comprobar_existencia_persona_y_agregarlo(dni, nombre, apellidos, direccion, telefono):

        if(Obtain.obtain_persona(dni) == None):
            Creator.create_persona(dni, nombre, apellidos, direccion, telefono)
            print("La persona fue creada exitosamente.")
        else:
            print("La persona que intenta crear ya se encuentra registrada en el sistema.")

    def comprobar_existencia_cuenta_y_agregarlo(num_cuenta, saldo, fecha_creacion):
        if(Obtain.obtain_cuenta(num_cuenta) == None):
            Creator.create_cuenta(num_cuenta,saldo, fecha_creacion)
            print("La cuenta fue creada exitosamente.")
        else:
            print("La cuenta que intenta crear ya se encuentra registrada en el sistema.")

    def comprobar_existencia_peaje_y_agregarlo():
        pass







    


# Ejecutar pruebas
#Principal.ejecutar_pruebas()

# Iniciar la aplicación
#Principal.iniciar_aplicacion()

    


    