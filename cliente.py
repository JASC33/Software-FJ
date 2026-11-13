"""Clase Cliente con encapsulación y validación de datos."""

import re
from entidad import Entidad
from excepciones import DatoInvalidoError

class Cliente(Entidad):
    """Representa a una persona registrada en Software FJ."""

    def __init__(self, identificador, nombre, correo, telefono):
        super().__init__(identificador)
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 2:
            raise DatoInvalidoError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor.strip().title()

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", valor):
            raise DatoInvalidoError("El correo electrónico no tiene un formato válido.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        numero = str(valor).strip()
        if not numero.isdigit() or len(numero) < 7 or len(numero) > 15:
            raise DatoInvalidoError("El teléfono debe contener entre 7 y 15 dígitos.")
        self._telefono = numero

    def obtener_informacion(self):
        return f"Cliente: {self.nombre} | Correo: {self.correo} | Teléfono: {self.telefono}"
