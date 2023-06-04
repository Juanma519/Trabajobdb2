from persona import Persona
from cuenta import Cuenta
from peaje import Peaje
from propietario import Propietario
from vehiculo import Vehiculo
from ventanilla import Ventanilla
from obtain import *



class Creator:

    
    def create_persona(dni, nombre, apellidos, direccion, telefono, id_prop):
        persona = Persona.create(dni=dni, nombre=nombre, apellidos=apellidos, direccion=direccion, telefono=telefono, id_prop = id_prop)
        persona.save() #Guarda la persona en la base de datos
        
    def create_cuenta(num_cuenta, saldo, fecha_creacion):
        cuenta = Cuenta.create(num_cuenta=num_cuenta, saldo=saldo, fecha_creacion=fecha_creacion)
        cuenta.save() #Guarda la cuenta en la base de datos

    def create_peaje(nomb_peaje, km, tel_peaje, ruta, cant_ventanillas):
        peaje = Peaje.create(nomb_peaje=nomb_peaje, km=km, tel_peaje=tel_peaje, ruta=ruta, cant_ventanillas=cant_ventanillas)
        peaje.save() #Guarda el peaje en la base de datos

    def create_propietario(id_prop, tipo_prop):
        persona = Obtain.obtain_persona(obtener_dni_por_id_prop(id_prop))
        if persona:
            propietario = Propietario.create(id_prop=id_prop, tipo_prop=tipo_prop)
            propietario.save()
        else:
            return False #No se ha podido crear el propietario porque no existe la persona con ese dni

    def create_vehiculo(matricula, dni_persona, RUT_empresa, num_cuenta, tipo_vehiculo, marca, color, RFID, modelo):
        vehiculo = Vehiculo.create(matricula=matricula, dni_persona=dni_persona, RUT_empresa=RUT_empresa, num_cuenta=num_cuenta, tipo_vehiculo=tipo_vehiculo, marca=marca, color=color, RFID=RFID, modelo=modelo)
        vehiculo.save() #Guarda el vehiculo en la base de datos

    def create_ventanilla(nomb_peaje, num_ventanilla, RFID_ventanilla):
        ventanilla = Ventanilla.create(nomb_peaje=nomb_peaje, num_ventanilla=num_ventanilla, RFID_ventanilla=RFID_ventanilla)
        ventanilla.save() #Guarda la ventanilla en la base de datos



    #Funcion auxiliar para encontrar el dni de la persona a traves del id_prop
    def obtener_dni_por_id_prop(id_prop):
        propietario = Propietario.get_or_none(Propietario.id_prop == id_prop)
        if propietario:
            persona = propietario.id_prop  # Acceder a la instancia de Persona a través de la relación en Propietario
            dni = persona.dni  # Acceder al atributo "dni" de Persona
            return dni
        else:
            return None #No se ha encontrado el propietario con ese id_prop