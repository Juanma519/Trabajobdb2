from config import *

class Persona(BaseModel):
    dni = IntegerField(primary_key=True) #El dni es la clave primaria de Persona
    dir_residencia = CharField()
    nombre = CharField()
    apellido = CharField()
    direccion = CharField()
    id_prop = ForeignKeyField(Propietario)

