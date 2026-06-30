# main.py
import os
from datetime import datetime

from models import Paciente, Medico, Cita, Factura

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    print("=" * 50)
    print("          SISTEMA DE GESTIÓN CLÍNICA DE SALUD")
    print("=" * 50)
    print("1. Gestión de Pacientes")
    print("2. Gestión de Médicos")
    print("3. Gestión de Citas")
    print("4. Gestión de Facturación")
    print("5. Reportes")
    print("6. Salir")
    print("-" * 50)
    return input("Seleccione una opción: ")

def menu_pacientes():
    while True:
        limpiar_pantalla()
        print("=" * 40)
        print("          GESTIÓN DE PACIENTES")
        print("=" * 40)
        print("1. Registrar Nuevo Paciente")
        print("2. Ver Todos los Pacientes")
        print("3. Buscar Paciente por ID")
        print("4. Actualizar Paciente")
        print("5. Eliminar Paciente")
        print("6. Volver al Menú Principal")
        print("-" * 40)
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            ver_pacientes()
        elif opcion == "3":
            buscar_paciente()
        elif opcion == "4":
            actualizar_paciente()
        elif opcion == "5":
            eliminar_paciente()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Presione Enter para continuar...")
            input()

def registrar_paciente():
    limpiar_pantalla()
    print("=" * 40)
    print("          REGISTRAR NUEVO PACIENTE")
    print("=" * 40)
    
    paciente_data = {
        'nombre': input("Nombre: "),
        'apellido': input("Apellido: "),
        'fecha_nacimiento': input("Fecha de Nacimiento (YYYY-MM-DD): "),
        'genero': input("Género (M/F/Otro): "),
        'telefono': input("Teléfono: "),
        'email': input("Email: "),
        'direccion': input("Dirección: ")
    }
    
    id_paciente = Paciente.crear_paciente(paciente_data)
    if id_paciente:
        print(f"Paciente registrado exitosamente con ID: {id_paciente}")
    else:
        print("Error al registrar paciente. Verifique los datos.")
    
    input("Presione Enter para continuar...")

def ver_pacientes():
    limpiar_pantalla()
    print("=" * 40)
    print("          LISTA DE PACIENTES")
    print("=" * 40)
    
    pacientes = Paciente.obtener_todos_pacientes()
    if pacientes:
        print(f"{'ID':<5} {'Nombre':<30} {'Teléfono':<15} {'Email':<25}")
        print("-" * 75)
        for paciente in pacientes:
            nombre_completo = f"{paciente['nombre']} {paciente['apellido']}"
            print(f"{paciente['id_paciente']:<5} {nombre_completo:<30} "
                  f"{paciente['telefono'] or 'N/A':<15} {paciente['email'] or 'N/A':<25}")
    else:
        print("No hay pacientes registrados.")
    
    input("Presione Enter para continuar...")

def buscar_paciente():
    limpiar_pantalla()
    print("=" * 40)
    print("          BUSCAR PACIENTE")
    print("=" * 40)
    
    try:
        id_paciente = int(input("ID del Paciente: "))
        paciente = Paciente.obtener_paciente_por_id(id_paciente)
        
        if paciente:
            print(f"\nID: {paciente['id_paciente']}")
            print(f"Nombre: {paciente['nombre']} {paciente['apellido']}")
            print(f"Fecha de Nacimiento: {paciente['fecha_nacimiento']}")
            print(f"Género: {paciente['genero']}")
            print(f"Teléfono: {paciente['telefono']}")
            print(f"Email: {paciente['email']}")
            print(f"Dirección: {paciente['direccion']}")
            print(f"Fecha de Registro: {paciente['fecha_registro']}")
        else:
            print("Paciente no encontrado.")
    except ValueError:
        print("ID inválido.")
    
    input("Presione Enter para continuar...")

def actualizar_paciente():
    limpiar_pantalla()
    print("=" * 40)
    print("          ACTUALIZAR PACIENTE")
    print("=" * 40)
    
    try:
        id_paciente = int(input("ID del Paciente a actualizar: "))
        paciente = Paciente.obtener_paciente_por_id(id_paciente)
        
        if paciente:
            print("\nDeje en blanco para mantener el valor actual:")
            paciente_data = {
                'nombre': input(f"Nombre ({paciente['nombre']}): ") or paciente['nombre'],
                'apellido': input(f"Apellido ({paciente['apellido']}): ") or paciente['apellido'],
                'fecha_nacimiento': input(f"Fecha de Nacimiento ({paciente['fecha_nacimiento']}): ") or paciente['fecha_nacimiento'],
                'genero': input(f"Género ({paciente['genero']}): ") or paciente['genero'],
                'telefono': input(f"Teléfono ({paciente['telefono']}): ") or paciente['telefono'],
                'email': input(f"Email ({paciente['email']}): ") or paciente['email'],
                'direccion': input(f"Dirección ({paciente['direccion']}): ") or paciente['direccion']
            }
            
            if Paciente.actualizar_paciente(id_paciente, paciente_data):
                print("Paciente actualizado exitosamente.")
            else:
                print("Error al actualizar paciente.")
        else:
            print("Paciente no encontrado.")
    except ValueError:
        print("ID inválido.")
    
    input("Presione Enter para continuar...")

def eliminar_paciente():
    limpiar_pantalla()
    print("=" * 40)
    print("          ELIMINAR PACIENTE")
    print("=" * 40)
    
    try:
        id_paciente = int(input("ID del Paciente a eliminar: "))
        confirmar = input(f"¿Está seguro de eliminar al paciente ID {id_paciente}? (s/n): ")
        
        if confirmar.lower() == 's':
            if Paciente.eliminar_paciente(id_paciente):
                print("Paciente eliminado exitosamente.")
            else:
                print("Error al eliminar paciente.")
        else:
            print("Operación cancelada.")
    except ValueError:
        print("ID inválido.")
    
    input("Presione Enter para continuar...")

def menu_medicos():
    while True:
        limpiar_pantalla()
        print("=" * 40)
        print("          GESTIÓN DE MÉDICOS")
        print("=" * 40)
        print("1. Registrar Nuevo Médico")
        print("2. Ver Todos los Médicos")
        print("3. Buscar Médico por ID")
        print("4. Volver al Menú Principal")
        print("-" * 40)
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_medico()
        elif opcion == "2":
            ver_medicos()
        elif opcion == "3":
            buscar_medico()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Presione Enter para continuar...")
            input()

def registrar_medico():
    limpiar_pantalla()
    print("=" * 40)
    print("          REGISTRAR NUEVO MÉDICO")
    print("=" * 40)
    
    medico_data = {
        'nombre': input("Nombre: "),
        'apellido': input("Apellido: "),
        'especialidad': input("Especialidad: "),
        'telefono': input("Teléfono: "),
        'email': input("Email: "),
        'horario_trabajo': input("Horario de Trabajo: "),
        'fecha_contratacion': input("Fecha de Contratación (YYYY-MM-DD): ")
    }
    
    id_medico = Medico.crear_medico(medico_data)
    if id_medico:
        print(f"Médico registrado exitosamente con ID: {id_medico}")
    else:
        print("Error al registrar médico. Verifique los datos.")
    
    input("Presione Enter para continuar...")

def ver_medicos():
    limpiar_pantalla()
    print("=" * 40)
    print("          LISTA DE MÉDICOS")
    print("=" * 40)
    
    medicos = Medico.obtener_todos_medicos()
    if medicos:
        print(f"{'ID':<5} {'Nombre':<30} {'Especialidad':<25} {'Teléfono':<15}")
        print("-" * 75)
        for medico in medicos:
            nombre_completo = f"{medico['nombre']} {medico['apellido']}"
            print(f"{medico['id_medico']:<5} {nombre_completo:<30} "
                  f"{medico['especialidad']:<25} {medico['telefono'] or 'N/A':<15}")
    else:
        print("No hay médicos registrados.")
    
    input("Presione Enter para continuar...")

def buscar_medico():
    limpiar_pantalla()
    print("=" * 40)
    print("          BUSCAR MÉDICO")
    print("=" * 40)
    
    try:
        id_medico = int(input("ID del Médico: "))
        medico = Medico.obtener_medico_por_id(id_medico)
        
        if medico:
            print(f"\nID: {medico['id_medico']}")
            print(f"Nombre: {medico['nombre']} {medico['apellido']}")
            print(f"Especialidad: {medico['especialidad']}")
            print(f"Teléfono: {medico['telefono']}")
            print(f"Email: {medico['email']}")
            print(f"Horario de Trabajo: {medico['horario_trabajo']}")
            print(f"Fecha de Contratación: {medico['fecha_contratacion']}")
        else:
            print("Médico no encontrado.")
    except ValueError:
        print("ID inválido.")
    
    input("Presione Enter para continuar...")

def menu_citas():
    while True:
        limpiar_pantalla()
        print("=" * 40)
        print("          GESTIÓN DE CITAS")
        print("=" * 40)
        print("1. Programar Nueva Cita")
        print("2. Ver Todas las Citas")
        print("3. Buscar Cita por ID")
        print("4. Actualizar Estado de Cita")
        print("5. Volver al Menú Principal")
        print("-" * 40)
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            programar_cita()
        elif opcion == "2":
            ver_citas()
        elif opcion == "3":
            buscar_cita()
        elif opcion == "4":
            actualizar_estado_cita()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Presione Enter para continuar...")
            input()

def programar_cita():
    limpiar_pantalla()
    print("=" * 40)
    print("          PROGRAMAR CITA")
    print("=" * 40)
    
    # Mostrar pacientes para referencia
    print("\nPacientes disponibles:")
    pacientes = Paciente.obtener_todos_pacientes()
    if pacientes:
        for p in pacientes:
            print(f"ID: {p['id_paciente']} - {p['nombre']} {p['apellido']}")
    else:
        print("No hay pacientes registrados. Primero debe registrar un paciente.")
        input("Presione Enter para continuar...")
        return
    
    # Mostrar médicos para referencia
    print("\nMédicos disponibles:")
    medicos = Medico.obtener_todos_medicos()
    if medicos:
        for m in medicos:
            print(f"ID: {m['id_medico']} - {m['nombre']} {m['apellido']} ({m['especialidad']})")
    else:
        print("No hay médicos registrados. Primero debe registrar un médico.")
        input("Presione Enter para continuar...")
        return
    
    try:
        cita_data = {
            'id_paciente': int(input("\nID del Paciente: ")),
            'id_medico': int(input("ID del Médico: ")),
            'fecha_cita': input("Fecha y Hora de la Cita (YYYY-MM-DD HH:MM:SS): "),
            'motivo': input("Motivo de la Cita: "),
            'estado': 'Programada'
        }
        
        id_cita = Cita.crear_cita(cita_data)
        if id_cita:
            print(f"Cita programada exitosamente con ID: {id_cita}")
        else:
            print("Error al programar cita. Verifique los datos.")
    except ValueError:
        print("Datos inválidos.")
    
    input("Presione Enter para continuar...")

def ver_citas():
    limpiar_pantalla()
    print("=" * 40)
    print("          LISTA DE CITAS")
    print("=" * 40)
    
    citas = Cita.obtener_todas_citas()
    if citas:
        print(f"{'ID':<5} {'Paciente':<20} {'Médico':<20} {'Fecha':<20} {'Estado':<12}")
        print("-" * 77)
        for cita in citas:
            print(f"{cita['id_cita']:<5} {cita['paciente_nombre']:<20} "
                  f"{cita['medico_nombre']:<20} {cita['fecha_cita']:<20} {cita['estado']:<12}")
    else:
        print("No hay citas programadas.")
    
    input("Presione Enter para continuar...")

def buscar_cita():
    limpiar_pantalla()
    print("=" * 40)
    print("          BUSCAR CITA")
    print("=" * 40)
    
    try:
        id_cita = int(input("ID de la Cita: "))
        cita = Cita.obtener_cita_por_id(id_cita)
        
        if cita:
            print(f"\nID de Cita: {cita['id_cita']}")
            print(f"Paciente: {cita['paciente_nombre']}")
            print(f"Médico: {cita['medico_nombre']}")
            print(f"Fecha y Hora: {cita['fecha_cita']}")
            print(f"Motivo: {cita['motivo']}")
            print(f"Estado: {cita['estado']}")
        else:
            print("Cita no encontrada.")
    except ValueError:
        print("ID inválido.")
    
    input("Presione Enter para continuar...")

def actualizar_estado_cita():
    limpiar_pantalla()
    print("=" * 40)
    print("          ACTUALIZAR ESTADO DE CITA")
    print("=" * 40)
    
    try:
        id_cita = int(input("ID de la Cita: "))
        print("\nEstados disponibles: Programada, Completada, Cancelada, En Espera")
        nuevo_estado = input("Nuevo Estado: ")
        
        estados_validos = ['Programada', 'Completada', 'Cancelada', 'En Espera']
        if nuevo_estado in estados_validos:
            if Cita.actualizar_estado_cita(id_cita, nuevo_estado):
                print("Estado de la cita actualizado exitosamente.")
            else:
                print("Error al actualizar estado de la cita.")
        else:
            print("Estado no válido.")
    except ValueError:
        print("ID inválido.")
    
    input("Presione Enter para continuar...")

def menu_facturacion():
    while True:
        limpiar_pantalla()
        print("=" * 40)
        print("          GESTIÓN DE FACTURACIÓN")
        print("=" * 40)
        print("1. Crear Nueva Factura")
        print("2. Ver Facturas por Paciente")
        print("3. Volver al Menú Principal")
        print("-" * 40)
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_factura()
        elif opcion == "2":
            ver_facturas_paciente()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Presione Enter para continuar...")
            input()

def crear_factura():
    limpiar_pantalla()
    print("=" * 40)
    print("          CREAR FACTURA")
    print("=" * 40)
    
    try:
        factura_data = {
            'id_cita': int(input("ID de la Cita: ")),
            'concepto': input("Concepto: "),
            'monto': float(input("Monto: ")),
            'estado_pago': input("Estado de Pago (Pendiente/Pagado/Cancelado): ")
        }
        
        estados_validos = ['Pendiente', 'Pagado', 'Cancelado']
        if factura_data['estado_pago'] not in estados_validos:
            print("Estado de pago no válido.")
            input("Presione Enter para continuar...")
            return
        
        id_factura = Factura.crear_factura(factura_data)
        if id_factura:
            print(f"Factura creada exitosamente con ID: {id_factura}")
        else:
            print("Error al crear factura. Verifique los datos.")
    except ValueError:
        print("Datos inválidos.")
    
    input("Presione Enter para continuar...")

def ver_facturas_paciente():
    limpiar_pantalla()
    print("=" * 40)
    print("          FACTURAS POR PACIENTE")
    print("=" * 40)
    
    try:
        id_paciente = int(input("ID del Paciente: "))
        facturas = Factura.obtener_facturas_paciente(id_paciente)
        
        if facturas:
            print(f"\n{'ID':<5} {'Concepto':<30} {'Monto':<12} {'Estado':<12} {'Fecha':<20}")
            print("-" * 79)
            total = 0
            for factura in facturas:
                print(f"{factura['id_factura']:<5} {factura['concepto']:<30} "
                      f"${factura['monto']:<11.2f} {factura['estado_pago']:<12} "
                      f"{factura['fecha_emision']}")
                if factura['estado_pago'] == 'Pagado':
                    total += factura['monto']
            print("-" * 79)
            print(f"Total Pagado: ${total:.2f}")
        else:
            print("No hay facturas para este paciente.")
    except ValueError:
        print("ID inválido.")
    
    input("Presione Enter para continuar...")

def menu_reportes():
    limpiar_pantalla()
    print("=" * 40)
    print("          REPORTES")
    print("=" * 40)
    print("1. Estadísticas Generales")
    print("2. Volver al Menú Principal")
    print("-" * 40)
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        mostrar_estadisticas()
    elif opcion == "2":
        pass

def mostrar_estadisticas():
    limpiar_pantalla()
    print("=" * 40)
    print("          ESTADÍSTICAS GENERALES")
    print("=" * 40)
    
    pacientes = Paciente.obtener_todos_pacientes()
    medicos = Medico.obtener_todos_medicos()
    citas = Cita.obtener_todas_citas()
    
    print(f"\nTotal de Pacientes: {len(pacientes)}")
    print(f"Total de Médicos: {len(medicos)}")
    print(f"Total de Citas: {len(citas)}")
    
    # Contar citas por estado
    estados = {'Programada': 0, 'Completada': 0, 'Cancelada': 0, 'En Espera': 0}
    for cita in citas:
        if cita['estado'] in estados:
            estados[cita['estado']] += 1
    
    print("\nCitas por Estado:")
    for estado, cantidad in estados.items():
        print(f"  {estado}: {cantidad}")
    
    input("\nPresione Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            menu_pacientes()
        elif opcion == "2":
            menu_medicos()
        elif opcion == "3":
            menu_citas()
        elif opcion == "4":
            menu_facturacion()
        elif opcion == "5":
            menu_reportes()
        elif opcion == "6":
            print("¡Gracias por usar el Sistema de Gestión de Clínica de Salud!")
            break
        else:
            print("Opción no válida. Presione Enter para continuar...")
            input()

if __name__ == "__main__":
    main()