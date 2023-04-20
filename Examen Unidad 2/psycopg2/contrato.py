from logger_base import log

class contrato:
    def __init__(self,idcontrato=None,nocontrato=None,costo=None,fechainicio=None,fechafin=None) -> None:
        self._idcontrato = idcontrato
        self._nocontrato = nocontrato
        self._costo = costo
        self._fechainicio = fechainicio
        self._fechafin = fechafin

    def __str__(self) -> str:
        return f"""
            ID CONTRATO: {self._idcontrato}, NO.CONTRATO: {self._nocontrato}, COSTO: {self._costo}, 
            FECHA DE INICIO: {self._fechainicio}, FECHA DE CIERRE: {self._fechafin}
        """
    
    @property
    def idContrato(self):
        return self._idcontrato
    @idContrato.setter
    def idContrato(self, idcon):
        self._idcontrato = idcon

    @property
    def noContrato(self):
        return self._nocontrato
    @noContrato.setter
    def noContrato(self,noCon):
        self._nocontrato = noCon

    @property
    def Costo(self):
        return self._costo
    @Costo.setter
    def Costo(self,Cos):
        self._costo = Cos

    @property
    def fechaInicio(self):
        return self._fechainicio
    @fechaInicio.setter
    def fechaInicio(self,fI):
        self._fechainicio = fI

    @property
    def fechaFin(self):
        return self._fechafin
    @fechaFin.setter
    def fechaFin(self,fF):
        self._fechafin = fF

if __name__ == "__main__":
    contrato1 = contrato(1,"0001","100","06 de Julio 2023","06 de Agosto 2023")
    log.debug(contrato1)