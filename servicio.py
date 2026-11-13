"""Clase abstracta Servicio y servicios especializados."""

from abc import ABC, abstractmethod
from entidad import Entidad
from excepciones import DatoInvalidoError, ServicioNoDisponibleError

class Servicio(Entidad, ABC):
    """Clase base para los servicios ofrecidos por Software FJ."""

    def __init__(self, identificador, nombre, tarifa_hora, disponible=True):
        super().__init__(identificador)
        if not isinstance(nombre, str) or not nombre.strip():
            raise DatoInvalidoError("El nombre del servicio es obligatorio.")
        if not isinstance(tarifa_hora, (int, float)) or tarifa_hora <= 0:
            raise DatoInvalidoError("La tarifa por hora debe ser mayor que cero.")
        self._nombre = nombre.strip()
        self._tarifa_hora = float(tarifa_hora)
        self._disponible = bool(disponible)

    @property
    def nombre(self):
        return self._nombre

    @property
    def disponible(self):
        return self._disponible

    def validar_disponibilidad(self):
        if not self._disponible:
            raise ServicioNoDisponibleError(f"El servicio {self.nombre} no está disponible.")

    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        """Calcula el costo; los parámetros opcionales permiten distintas variantes."""
        self.validar_disponibilidad()
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise DatoInvalidoError("La duración debe ser mayor que cero.")
        if not 0 <= impuesto <= 1 or not 0 <= descuento <= 1:
            raise DatoInvalidoError("Impuesto y descuento deben estar entre 0 y 1.")
        subtotal = self._tarifa_hora * horas
        return round(subtotal * (1 - descuento) * (1 + impuesto), 2)

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self, **parametros):
        pass

    def obtener_informacion(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} - Tarifa por hora: ${self._tarifa_hora:,.2f} - {estado}"


class ReservaSala(Servicio):
    """Servicio para reservar salas de reuniones o trabajo."""

    def __init__(self, identificador, tarifa_hora, capacidad, disponible=True):
        super().__init__(identificador, "Reserva de salas", tarifa_hora, disponible)
        if not isinstance(capacidad, int) or capacidad < 1:
            raise DatoInvalidoError("La capacidad de la sala debe ser un entero positivo.")
        self.capacidad = capacidad

    def describir(self):
        return f"Sala de reuniones con capacidad para {self.capacidad} personas."

    def validar_parametros(self, **parametros):
        personas = parametros.get("personas")
        if not isinstance(personas, int) or personas < 1 or personas > self.capacidad:
            raise DatoInvalidoError("La cantidad de personas supera la capacidad o no es válida.")
        return True


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos tecnológicos."""

    def __init__(self, identificador, tarifa_hora, tipo_equipo, disponible=True):
        super().__init__(identificador, "Alquiler de equipos", tarifa_hora, disponible)
        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise DatoInvalidoError("Debe indicar el tipo de equipo.")
        self.tipo_equipo = tipo_equipo.strip()

    def describir(self):
        return f"Alquiler de equipo tecnológico: {self.tipo_equipo}."

    def validar_parametros(self, **parametros):
        cantidad = parametros.get("cantidad", 1)
        if not isinstance(cantidad, int) or cantidad < 1 or cantidad > 10:
            raise DatoInvalidoError("La cantidad de equipos debe estar entre 1 y 10.")
        return True

    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0, cantidad=1):
        """Sobrescribe el cálculo para tener en cuenta la cantidad de equipos."""
        self.validar_parametros(cantidad=cantidad)
        return round(super().calcular_costo(horas, impuesto, descuento) * cantidad, 2)


class AsesoriaEspecializada(Servicio):
    """Servicio de asesoría profesional especializada."""

    def __init__(self, identificador, tarifa_hora, especialidad, disponible=True):
        super().__init__(identificador, "Asesoría especializada", tarifa_hora, disponible)
        if not isinstance(especialidad, str) or not especialidad.strip():
            raise DatoInvalidoError("Debe indicar la especialidad de la asesoría.")
        self.especialidad = especialidad.strip()

    def describir(self):
        return f"Asesoría profesional en el área de {self.especialidad}."

    def validar_parametros(self, **parametros):
        modalidad = parametros.get("modalidad", "virtual")
        if modalidad not in ("virtual", "presencial"):
            raise DatoInvalidoError("La modalidad debe ser virtual o presencial.")
        return True
