"""Programa principal: demostración de Software FJ con diez operaciones."""

from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ErrorSistema
from logs import registrar_evento, registrar_error


def ejecutar_pruebas():
    """Ejecuta operaciones válidas e inválidas sin detener toda la aplicación."""
    clientes = []
    servicios = []
    reservas = []

    print("=" * 65)
    print("       SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
    print("=" * 65)

    # Operación 1: registro correcto de un cliente.
    try:
        cliente1 = Cliente("C001", "Andrés Sánchez", "andres@email.com", "3001234567")
        clientes.append(cliente1)
        print("\n1. Cliente registrado:", cliente1.obtener_informacion())
    except ErrorSistema as error:
        print("1. No se pudo registrar el cliente:", error)
        registrar_error("Fallo en operación 1")

    # Operación 2: intento de registro con correo inválido.
    try:
        Cliente("C002", "María López", "correo-no-valido", "3101234567")
        print("\n2. Cliente inválido registrado inesperadamente.")
    except ErrorSistema as error:
        print("\n2. Error controlado al registrar cliente:", error)
        registrar_error("Operación 2: datos de cliente inválidos")

    # Operación 3: creación correcta de una sala.
    try:
        sala = ReservaSala("S001", 50000, 12)
        servicios.append(sala)
        print("\n3. Servicio creado:", sala.describir())
    except ErrorSistema as error:
        print("\n3. Error al crear sala:", error)
        registrar_error("Fallo en operación 3")

    # Operación 4: creación de equipo con tarifa inválida.
    try:
        AlquilerEquipo("E001", -1000, "Computador")
        print("\n4. Equipo creado inesperadamente.")
    except ErrorSistema as error:
        print("\n4. Error controlado al crear servicio:", error)
        registrar_error("Operación 4: servicio con tarifa inválida")

    # Operación 5: creación de los otros servicios especializados.
    try:
        equipo = AlquilerEquipo("E002", 20000, "Computador portátil")
        asesoria = AsesoriaEspecializada("A001", 80000, "Programación")
        servicios.extend([equipo, asesoria])
        print("\n5. Servicios creados:", equipo.describir(), "y", asesoria.describir())
    except ErrorSistema as error:
        print("\n5. Error al crear servicios:", error)
        registrar_error("Fallo en operación 5")

    # Operación 6: reserva exitosa de una sala.
    try:
        reserva1 = Reserva("R001", cliente1, sala, 2, personas=8)
        costo = reserva1.confirmar(impuesto=0.19, descuento=0.10)
        reservas.append(reserva1)
        print(f"\n6. Reserva exitosa: {reserva1.obtener_informacion()}")
    except Exception as error:
        print("\n6. No se pudo realizar la reserva:", error)
        registrar_error("Operación 6: reserva de sala fallida")

    # Operación 7: reserva fallida por superar la capacidad de la sala.
    try:
        reserva2 = Reserva("R002", cliente1, sala, 2, personas=20)
        reserva2.procesar()
        reservas.append(reserva2)
        print("\n7. Reserva creada:", reserva2.obtener_informacion())
    except Exception as error:
        print("\n7. Error controlado en reserva:", error)
        registrar_error("Operación 7: cantidad de personas no válida")

    # Operación 8: reserva exitosa de varios equipos.
    try:
        reserva3 = Reserva("R003", cliente1, equipo, 3, cantidad=2)
        reserva3.confirmar(impuesto=0.19)
        reservas.append(reserva3)
        print("\n8. Reserva de equipos:", reserva3.obtener_informacion())
    except Exception as error:
        print("\n8. Error en reserva de equipos:", error)
        registrar_error("Operación 8: reserva de equipos fallida")

    # Operación 9: reserva exitosa de asesoría virtual.
    try:
        reserva4 = Reserva("R004", cliente1, asesoria, 1.5, modalidad="virtual")
        reserva4.confirmar(descuento=0.05)
        reservas.append(reserva4)
        print("\n9. Reserva de asesoría:", reserva4.obtener_informacion())
    except Exception as error:
        print("\n9. Error en asesoría:", error)
        registrar_error("Operación 9: reserva de asesoría fallida")

    # Operación 10: cancelación de una reserva confirmada.
    try:
        reserva1.cancelar()
        print("\n10. Reserva cancelada:", reserva1.obtener_informacion())
    except Exception as error:
        print("\n10. Error al cancelar reserva:", error)
        registrar_error("Operación 10: cancelación fallida")

    # Se muestra un resumen de los objetos que quedaron registrados.
    print("\n" + "-" * 65)
    print("RESUMEN DEL SISTEMA")
    print(f"Clientes registrados: {len(clientes)}")
    print(f"Servicios creados: {len(servicios)}")
    print(f"Reservas creadas correctamente: {len(reservas)}")
    print("Los eventos y errores se guardaron en software_fj.log")
    print("=" * 65)
    registrar_evento("Finalizó la ejecución de las diez operaciones de prueba.")


if __name__ == "__main__":
    # try/except general de respaldo para evitar una salida inesperada.
    try:
        ejecutar_pruebas()
    except Exception as error:
        registrar_error(f"Error inesperado en el programa principal: {error}")
        print("Ocurrió un error inesperado. Revise el archivo software_fj.log.")
