"""Clase Reserva: relaciona clientes y servicios."""

from excepciones import ReservaInvalidaError, OperacionNoPermitidaError
from logs import registrar_evento, registrar_error

class Reserva:
    """Administra el ciclo de vida de una reserva."""

    def __init__(self, identificador, cliente, servicio, duracion, **parametros):
        if cliente is None or servicio is None:
            raise ReservaInvalidaError("La reserva requiere un cliente y un servicio.")
        if not isinstance(duracion, (int, float)) or duracion <= 0:
            raise ReservaInvalidaError("La duración de la reserva debe ser mayor que cero.")
        self.identificador = str(identificador)
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.parametros = parametros
        self.estado = "Pendiente"
        self.costo = 0.0
        registrar_evento(f"Reserva {self.identificador} creada en estado pendiente.")

    def procesar(self, impuesto=0.0, descuento=0.0):
        """Valida los datos y calcula el costo de la reserva."""
        try:
            if self.estado != "Pendiente":
                raise OperacionNoPermitidaError("Solo se pueden procesar reservas pendientes.")
            self.servicio.validar_parametros(**self.parametros)
            self.costo = self.servicio.calcular_costo(self.duracion, impuesto, descuento,
                                                       **({"cantidad": self.parametros["cantidad"]}
                                                          if "cantidad" in self.parametros else {}))
        except Exception as error:
            registrar_error(f"Error al procesar la reserva {self.identificador}: {error}")
            raise ReservaInvalidaError("No fue posible procesar la reserva.") from error
        else:
            self.estado = "Confirmada"
            registrar_evento(f"Reserva {self.identificador} confirmada por ${self.costo:,.2f}.")
            return self.costo
        finally:
            registrar_evento(f"Finalizó el intento de procesamiento de la reserva {self.identificador}.")

    def cancelar(self):
        """Cancela una reserva que todavía no haya sido cancelada."""
        try:
            if self.estado == "Cancelada":
                raise OperacionNoPermitidaError("La reserva ya se encuentra cancelada.")
            self.estado = "Cancelada"
            registrar_evento(f"Reserva {self.identificador} cancelada.")
        except Exception as error:
            registrar_error(f"Error al cancelar la reserva {self.identificador}: {error}")
            raise

    def obtener_informacion(self):
        return (f"Reserva {self.identificador} | Cliente: {self.cliente.nombre} | "
                f"Servicio: {self.servicio.nombre} | Estado: {self.estado} | "
                f"Costo: ${self.costo:,.2f}")
