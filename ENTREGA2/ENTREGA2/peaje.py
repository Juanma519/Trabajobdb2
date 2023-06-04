from config import *

class Peaje(BaseModel):
    nomb_peaje = PrimaryKeyField()      #El nombre del peaje es la clave primaria de Peaje
    km = IntegerField()
    tel_peaje = IntegerField()
    ruta = IntegerField()
    cant_ventanillas = IntegerField()