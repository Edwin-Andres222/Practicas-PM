from logger_base import log

class contrato_persona:
    def __init__(self,idpersona = None, idcontrato = None) -> None:
        self._idpersona = idpersona
        self._idcontrato = idcontrato

    def __str__(self) -> str:
        return f"""
            ID PERSONA: {self._idpersona}, ID CONTRATO: {self._idcontrato}
        """
    
    @property
    def idPersona(self):
        return self._idpersona
    @idPersona.setter
    def idPersona(self,idPer):
        self._idpersona = idPer

    @property
    def idContrato(self):
        return self._idcontrato
    @idContrato.setter
    def idContrato(self,idCon):
        self._idcontrato = idCon

if __name__ == "__main__":
    contrato_persona1 = contrato_persona("1","1")
    log.debug(contrato_persona1)