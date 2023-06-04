from persona import Persona
from cuenta import Cuenta
from peaje import Peaje
from propietario import Propietario
from vehiculo import Vehiculo
from ventanilla import Ventanilla
from obtain import *


class Remover:


    def remove_persona(dni):
        persona = Obtain.obtain_persona(dni)
        if persona:
            persona.delete_instance()
            return True
        else:
            return False
        
    def remove_cuenta(num_cuenta):
        cuenta = Obtain.obtain_cuenta(num_cuenta)
        if cuenta:
            cuenta.delete_instance()
            return True
        else:
            return False

    def remove_peaje(nomb_peaje):
        peaje = Obtain.obtain_peaje(nomb_peaje)
        if peaje:
            peaje.delete_instance()
            return True
        else:
            return False
        
    def remove_propietario (id_prop):
        propietario = Obtain.obtain_propietario(id_prop)
        if propietario:
            propietario.delete_instance()
            return True
        else:
            return False

    def remove_vehiculo(matricula):
        vehiculo = Obtain.obtain_vehiculo(matricula)
        if vehiculo:
            vehiculo.delete_instance()
            return True
        else: 
            return False
    
    def remove_ventanilla(nomb_peaje, num_ventanilla):
        ventanilla = Obtain.obtain_ventanilla(nomb_peaje, num_ventanilla)
        if ventanilla:
            ventanilla.delete_instance()
            return True
        else: 
            return False