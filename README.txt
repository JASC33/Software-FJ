PROYECTO: SOFTWARE FJ
Sistema Integral de Gestión de Clientes, Servicios y Reservas

REQUISITOS
- Python 3.9 o superior.
- Visual Studio Code (recomendado).

ARCHIVOS
- main.py: ejecuta las diez operaciones de demostración.
- entidad.py: clase abstracta general.
- cliente.py: clase Cliente y validaciones.
- servicio.py: clase abstracta Servicio y tres servicios especializados.
- reserva.py: creación, procesamiento y cancelación de reservas.
- excepciones.py: excepciones personalizadas.
- logs.py: registro de eventos y errores.

CÓMO EJECUTAR
1. Extraiga la carpeta Software_FJ.
2. Abra Visual Studio Code.
3. Seleccione Archivo > Abrir carpeta y elija Software_FJ.
4. Abra main.py.
5. Abra la terminal en Visual Studio Code.
6. Ejecute: python main.py
   Si ese comando no funciona en Windows, pruebe: py main.py
7. Revise la salida de la terminal y el archivo software_fj.log.

NOTAS
- El proyecto no utiliza bases de datos.
- Los datos se manejan en objetos y listas durante la ejecución.
- El archivo software_fj.log se crea automáticamente.
- El método calcular_costo utiliza parámetros opcionales y una versión
  sobrescrita para el alquiler de equipos, mostrando distintas variantes
  de cálculo en Python.
