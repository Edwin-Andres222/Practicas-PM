from logger_base import log

class Bebida:
    def __init__(self,id_Bebida=None,nombre=None,precio=None) -> None:
        self._id_Bebida=id_Bebida
        self._nombre=nombre
        self._precio = precio

    def __str__(self) -> str:
        return f'''
            ID Bebida: {self._id_Bebida}, Nombre: {self._nombre},
            Precio: {self._precio}
        '''
    
    @property
    def idBebida(self):
        return self._id_Bebida
    
    @idBebida.setter
    def idBebida(self,id_Bebida):
        self._id_Bebida=id_Bebida

    @property
    def Nombre(self):
        return self._nombre
    
    @Nombre.setter
    def Nombre(self,name):
        self._nombre=name

    @property
    def Precio(self):
        return self._precio
    
    @Precio.setter
    def Precio(self,costo):
        self._precio=costo

if __name__ == '__main__':
    bebida1 = Bebida(1,"Coca Cola",45.50)
    log.debug(bebida1)
