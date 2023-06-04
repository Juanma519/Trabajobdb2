from persona import Persona
from cuenta import Cuenta
from peaje import Peaje
from propietario import Propietario
from vehiculo import Vehiculo
from ventanilla import Ventanilla


class Obtain:


    def obtain_persona (dni):
        persona = Persona.get_or_none(Persona.dni == dni)
        return persona  

    def obtain_cuenta (num_cuenta):
        cuenta = Cuenta.get_or_none(Cuenta.num_cuenta == num_cuenta)
        return cuenta
    
    def obtain_peaje(nomb_peaje):
        peaje = Peaje.get_or_none(Peaje.nomb_peaje == nomb_peaje)
        return peaje
    
    def obtain_propietario (id_prop):
        propietario = Propietario.get_or_none(Propietario.id_prop == id_prop)
        return propietario
    
    def obtain_vehiculo(matricula):
        vehiculo = Vehiculo.get_or_none(Vehiculo.matricula == matricula)
        return vehiculo

    def obtain_ventanilla(nomb_peaje, num_ventanilla):
        ventanilla = Ventanilla.get_or_none(Ventanilla.nomb_peaje == nomb_peaje, Ventanilla.num_ventanilla == num_ventanilla)
        return ventanilla