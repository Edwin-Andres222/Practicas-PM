from logger_base import log

class Auto:
    def __init__(self,id_Auto=None,modelo=None,precio=None) -> None:
        self._id_Auto=id_Auto
        self._modelo=modelo
        self._precio = precio

    def __str__(self) -> str:
        return f'''
            ID Auto: {self._id_Auto}, modelo: {self._modelo},
            Precio: {self._precio}
        '''
    
    @property
    def idAuto(self):
        return self._id_Auto
    
    @idAuto.setter
    def idAuto(self,id_Auto):
        self._id_Auto=id_Auto

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self,model):
        self._modelo=model

    @property
    def Precio(self):
        return self._precio
    
    @Precio.setter
    def Precio(self,costo):
        self._precio=costo

if __name__ == '__main__':
    Auto1 = Auto(1,"FORD",100000.00)
    log.debug(Auto1)
