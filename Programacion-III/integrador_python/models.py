# models.py
from datetime import datetime
from config import DatabaseConfig
from mysql.connector import Error

class Paciente:
    def __init__(self, id_paciente=None, nombre=None, apellido=None, 
                 fecha_nacimiento=None, genero=None, telefono=None, 
                 email=None, direccion=None):
        self.id_paciente = id_paciente
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
    
    @staticmethod
    def crear_paciente(paciente_data):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO pacientes 
                          (nombre, apellido, fecha_nacimiento, genero, 
                           telefono, email, direccion) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, (
                    paciente_data['nombre'],
                    paciente_data['apellido'],
                    paciente_data['fecha_nacimiento'],
                    paciente_data['genero'],
                    paciente_data['telefono'],
                    paciente_data['email'],
                    paciente_data['direccion']
                ))
                connection.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error al crear paciente: {e}")
                return None
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def obtener_todos_pacientes():
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM pacientes WHERE estado = TRUE"
                cursor.execute(query)
                return cursor.fetchall()
            except Error as e:
                print(f"Error al obtener pacientes: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def obtener_paciente_por_id(id_paciente):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM pacientes WHERE id_paciente = %s AND estado = TRUE"
                cursor.execute(query, (id_paciente,))
                return cursor.fetchone()
            except Error as e:
                print(f"Error al obtener paciente: {e}")
                return None
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def actualizar_paciente(id_paciente, paciente_data):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """UPDATE pacientes SET 
                          nombre=%s, apellido=%s, fecha_nacimiento=%s, 
                          genero=%s, telefono=%s, email=%s, direccion=%s 
                          WHERE id_paciente=%s"""
                cursor.execute(query, (
                    paciente_data['nombre'],
                    paciente_data['apellido'],
                    paciente_data['fecha_nacimiento'],
                    paciente_data['genero'],
                    paciente_data['telefono'],
                    paciente_data['email'],
                    paciente_data['direccion'],
                    id_paciente
                ))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al actualizar paciente: {e}")
                return False
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def eliminar_paciente(id_paciente):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE pacientes SET estado = FALSE WHERE id_paciente = %s"
                cursor.execute(query, (id_paciente,))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al eliminar paciente: {e}")
                return False
            finally:
                cursor.close()
                connection.close()

class Medico:
    def __init__(self, id_medico=None, nombre=None, apellido=None, 
                 especialidad=None, telefono=None, email=None, 
                 horario_trabajo=None, fecha_contratacion=None):
        self.id_medico = id_medico
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.telefono = telefono
        self.email = email
        self.horario_trabajo = horario_trabajo
        self.fecha_contratacion = fecha_contratacion
    
    @staticmethod
    def crear_medico(medico_data):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO medicos 
                          (nombre, apellido, especialidad, telefono, 
                           email, horario_trabajo, fecha_contratacion) 
                          VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(query, (
                    medico_data['nombre'],
                    medico_data['apellido'],
                    medico_data['especialidad'],
                    medico_data['telefono'],
                    medico_data['email'],
                    medico_data['horario_trabajo'],
                    medico_data['fecha_contratacion']
                ))
                connection.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error al crear médico: {e}")
                return None
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def obtener_todos_medicos():
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM medicos WHERE estado = TRUE"
                cursor.execute(query)
                return cursor.fetchall()
            except Error as e:
                print(f"Error al obtener médicos: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def obtener_medico_por_id(id_medico):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = "SELECT * FROM medicos WHERE id_medico = %s AND estado = TRUE"
                cursor.execute(query, (id_medico,))
                return cursor.fetchone()
            except Error as e:
                print(f"Error al obtener médico: {e}")
                return None
            finally:
                cursor.close()
                connection.close()

class Cita:
    def __init__(self, id_cita=None, id_paciente=None, id_medico=None,
                 fecha_cita=None, motivo=None, estado='Programada'):
        self.id_cita = id_cita
        self.id_paciente = id_paciente
        self.id_medico = id_medico
        self.fecha_cita = fecha_cita
        self.motivo = motivo
        self.estado = estado
    
    @staticmethod
    def crear_cita(cita_data):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO citas 
                          (id_paciente, id_medico, fecha_cita, motivo, estado) 
                          VALUES (%s, %s, %s, %s, %s)"""
                cursor.execute(query, (
                    cita_data['id_paciente'],
                    cita_data['id_medico'],
                    cita_data['fecha_cita'],
                    cita_data['motivo'],
                    cita_data['estado']
                ))
                connection.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error al crear cita: {e}")
                return None
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def obtener_todas_citas():
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """SELECT c.*, 
                          CONCAT(p.nombre, ' ', p.apellido) as paciente_nombre,
                          CONCAT(m.nombre, ' ', m.apellido) as medico_nombre,
                          m.especialidad
                          FROM citas c
                          JOIN pacientes p ON c.id_paciente = p.id_paciente
                          JOIN medicos m ON c.id_medico = m.id_medico
                          WHERE c.estado != 'Cancelada'
                          ORDER BY c.fecha_cita DESC"""
                cursor.execute(query)
                return cursor.fetchall()
            except Error as e:
                print(f"Error al obtener citas: {e}")
                return []
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def obtener_cita_por_id(id_cita):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """SELECT c.*, 
                          CONCAT(p.nombre, ' ', p.apellido) as paciente_nombre,
                          CONCAT(m.nombre, ' ', m.apellido) as medico_nombre
                          FROM citas c
                          JOIN pacientes p ON c.id_paciente = p.id_paciente
                          JOIN medicos m ON c.id_medico = m.id_medico
                          WHERE c.id_cita = %s"""
                cursor.execute(query, (id_cita,))
                return cursor.fetchone()
            except Error as e:
                print(f"Error al obtener cita: {e}")
                return None
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def actualizar_estado_cita(id_cita, estado):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = "UPDATE citas SET estado = %s WHERE id_cita = %s"
                cursor.execute(query, (estado, id_cita))
                connection.commit()
                return True
            except Error as e:
                print(f"Error al actualizar cita: {e}")
                return False
            finally:
                cursor.close()
                connection.close()

class Factura:
    @staticmethod
    def crear_factura(factura_data):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO facturacion 
                          (id_cita, concepto, monto, estado_pago) 
                          VALUES (%s, %s, %s, %s)"""
                cursor.execute(query, (
                    factura_data['id_cita'],
                    factura_data['concepto'],
                    factura_data['monto'],
                    factura_data['estado_pago']
                ))
                connection.commit()
                return cursor.lastrowid
            except Error as e:
                print(f"Error al crear factura: {e}")
                return None
            finally:
                cursor.close()
                connection.close()
    
    @staticmethod
    def obtener_facturas_paciente(id_paciente):
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                query = """SELECT f.*, c.fecha_cita, 
                          CONCAT(p.nombre, ' ', p.apellido) as paciente_nombre
                          FROM facturacion f
                          JOIN citas c ON f.id_cita = c.id_cita
                          JOIN pacientes p ON c.id_paciente = p.id_paciente
                          WHERE c.id_paciente = %s"""
                cursor.execute(query, (id_paciente,))
                return cursor.fetchall()
            except Error as e:
                print(f"Error al obtener facturas: {e}")
                return []
            finally:
                cursor.close()
                connection.close()