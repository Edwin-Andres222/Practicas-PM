from contrato_persona import contrato_persona
from cursorDelPool import CursorDelPool
from logger_base import log

class contrato_personaDAO:

    _SELECCIONAR= "SELECT * FROM contrato_persona ORDER BY idpersona"
    _INSERTAR = "INSERT INTO contrato_persona(idpersona, idcontrato) VALUES (%s, %s)"


    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato1 = contrato_persona(r[0],r[1])
                contratos.append(contrato1)
            return contratos
    
    @classmethod
    def insertar(cls,contrato_persona):
        with CursorDelPool() as cursor:
            valores =  (contrato_persona.idPersona, contrato_persona.idContrato)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    
        
if __name__ == "__main__":
    #Insertar
    contrato_persona1 = contrato_persona("1","1")
    contratosInsertados = contrato_personaDAO.insertar(contrato_persona1)
    contrato_persona2 = contrato_persona("2","2")
    contratosInsertados = contrato_personaDAO.insertar(contrato_persona2)
    log.debug(f"contratos Agregados: {contratosInsertados}")
    #Leer
    contrato = contrato_personaDAO.seleccionar()
    for p in contrato:
        log.debug(p)