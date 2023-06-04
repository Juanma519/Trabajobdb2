from config import *

class Ventanilla(BaseModel):
    nomb_peaje = ForeignKeyField(Peaje, PrimaryKeyField)
    num_ventanilla = IntegerField(primary_key=True) #El numero de la ventanilla es la clave primaria de Ventanilla
    RFID_ventanilla = IntegerField()