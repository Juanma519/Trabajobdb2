from persona import Persona
from cuenta import Cuenta
from peaje import Peaje
from propietario import Propietario
from vehiculo import Vehiculo
from ventanilla import Ventanilla
from obtain import Obtain

class Updater:
    
    def update_persona(dni, new_nombre=None, new_apellido=None, new_direccion=None):
        persona = Obtain.obtain_persona(dni)
        if persona:
            if new_nombre:
                persona.nombre = new_nombre
            if new_apellido:
                persona.apellido = new_apellido
            if new_direccion:
                persona.direccion = new_direccion
            persona.save()
            return True
        else:
            return False
        
    def update_cuenta(num_cuenta, new_saldo=None):
        cuenta = Obtain.obtain_cuenta(num_cuenta)
        if cuenta:
            if new_saldo:
                cuenta.saldo = new_saldo
            cuenta.save()
            return True
        else:
            return False
        
    def update_peaje(nomb_peaje, new_km=None, new_tel_peaje=None):
        peaje = Obtain.obtain_peaje(nomb_peaje)
        if peaje:
            if new_km:
                peaje.km = new_km
            if new_tel_peaje:
                peaje.tel_peaje = new_tel_peaje
            peaje.save()
            return True
        else:
            return False
        
    def update_propietario(id_prop, new_tipo_prop=None):
        propietario = Obtain.obtain_propietario(id_prop)
        if propietario:
            if new_tipo_prop:
                propietario.tipo_prop = new_tipo_prop
            propietario.save()
            return True
        else:
            return False

    def update_vehiculo(matricula, new_marca=None, new_color=None):
        vehiculo = Obtain.obtain_vehiculo(matricula)
        if vehiculo:
            if new_marca:
                vehiculo.marca = new_marca
            if new_color:
                vehiculo.color = new_color
            vehiculo.save()
            return True
        else:
            return False

    def update_ventanilla(nomb_peaje, num_ventanilla, new_RFID_ventanilla=None):
        ventanilla = Obtain.obtain_ventanilla(nomb_peaje, num_ventanilla)
        if ventanilla:
            if new_RFID_ventanilla:
                ventanilla.RFID_ventanilla = new_RFID_ventanilla
            ventanilla.save()
            return True
        else:
            return False
