from config import *

class Cuenta(BaseModel):
    num_cuenta = IntegerField(primary_key=True) #El numero de la cuenta es la clave primaria de Cuenta
    saldo = IntegerField()
    fecha_creacion = DateTimeField()   