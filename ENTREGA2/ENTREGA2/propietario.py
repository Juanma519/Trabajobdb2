from config import *

class Propietario(BaseModel):
    id_prop = IntegerField(primary_key=True) #El id del propietario es la clave primaria de Propietario
    tipo_prop = CharField()