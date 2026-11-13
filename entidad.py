"""Clase abstracta que representa una entidad general del sistema."""

from abc import ABC, abstractmethod

class Entidad(ABC):
    """Define los datos y comportamientos básicos de una entidad."""

    def __init__(self, identificador):
        # Se valida que la entidad tenga un identificador.
        if not identificador or not str(identificador).strip():
            raise ValueError("El identificador es obligatorio.")
        self._identificador = str(identificador).strip()

    @property
    def identificador(self):
        """Permite consultar el identificador sin modificarlo directamente."""
        return self._identificador

    @abstractmethod
    def obtener_informacion(self):
        """Cada clase hija debe definir cómo mostrar su información."""
        pass
