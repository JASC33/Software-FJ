"""Excepciones personalizadas del sistema Software FJ."""

class ErrorSistema(Exception):
    """Clase base para los errores controlados de la aplicación."""

class DatoInvalidoError(ErrorSistema):
    """Se utiliza cuando un dato no cumple las validaciones."""

class ServicioNoDisponibleError(ErrorSistema):
    """Se utiliza cuando un servicio no está disponible."""

class ReservaInvalidaError(ErrorSistema):
    """Se utiliza cuando una reserva no puede realizarse."""

class OperacionNoPermitidaError(ErrorSistema):
    """Se utiliza cuando se intenta ejecutar una operación no permitida."""
