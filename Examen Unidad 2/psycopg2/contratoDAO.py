from contrato import contrato
from cursorDelPool import CursorDelPool
from logger_base import log

class contratoDAO:

    _SELECCIONAR= "SELECT * FROM contrato ORDER BY id"
    _INSERTAR = "INSERT INTO contrato(id, nocontrato, costo, fechainicio, fechafin) VALUES (%s, %s, %s, %s,%s)"
    _ACTUALIZAR = "UPDATE contrato SET nocontrato = %s, costo = %s, fechainicio = %s, fechafin = %s WHERE id = %s"
    _ELIMINAR = "DELETE FROM contrato WHERE id = %s"

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            contratos = []
            for r in registros:
                contrato1 = contrato(r[0],r[1],r[2],r[3],r[4])
                contratos.append(contrato1)
            return contratos
    
    @classmethod
    def insertar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.idContrato, contrato.noContrato, contrato.Costo, contrato.fechaInicio, contrato.fechaFin)
            cursor.execute(cls._INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls,contrato):
        with CursorDelPool() as cursor:
            valores = (contrato.noContrato, contrato.Costo, contrato.fechaInicio, contrato.fechaFin, contrato.idContrato)
            cursor.execute(cls._ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar (cls,contrato):
        with CursorDelPool as cursor:
            valores = (contrato.idContrato,)
            cursor.execute(cls._ELIMINAR, valores)
            return cursor.rowcount
        
if __name__ == "__main__":
    #Insertar
    contrato1 = contrato(1,"0001","100","06 de Julio 2023","06 de Agosto 2023")
    contratosInsertados = contratoDAO.insertar(contrato1)
    contrato2 = contrato(2,"0002","200","06 de Julio 2023","06 de Agosto 2023")
    contratosInsertados = contratoDAO.insertar(contrato2)
    log.debug(f"contratos Agregados: {contratosInsertados}")
    #Leer
    contrato = contratoDAO.seleccionar()
    for p in contrato:
        log.debug(p)