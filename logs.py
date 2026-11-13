"""Configuración centralizada del registro de eventos y errores."""

import logging
from pathlib import Path

# El archivo se crea automáticamente en la carpeta del proyecto.
RUTA_LOG = Path(__file__).with_name("software_fj.log")

# Se configura el registro para guardar fecha, nivel y mensaje.
logging.basicConfig(
    filename=RUTA_LOG,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger("SoftwareFJ")

def registrar_evento(mensaje):
    """Guarda un evento normal en el archivo de logs."""
    logger.info(mensaje)

def registrar_error(mensaje):
    """Guarda un error con su información correspondiente."""
    logger.exception(mensaje)
