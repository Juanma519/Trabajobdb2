from config import *

class Vehiculo(BaseModel):
    matricula = IntegerField(primary_key=True) #La matricula es la clave primaria de Vehiculo
    dni_persona = ForeignKeyField(Persona)
    RUT_empresa = IntegerField()
    num_cuenta = ForeignKeyField(Cuenta)
    tipo_vehiculo = ForeignKeyField(Tipo_vehiculo, backref='Vehiculo', on_delete = 'CASCADE')
    marca = CharField()
    color = CharField()
    RFID = IntegerField()
    modelo = CharField()