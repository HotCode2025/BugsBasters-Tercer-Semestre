import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')

try:
    with conexion:
        with conexion.cursor() as cursor:
        sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES (%s, &s, &s)'
        valores = ('Carlos', 'Lara', 'clara@gmial.com') # Es una tupla
        cursor.execute(sentencia, valores)   # Recuperamos todos los registros que serán una lista
        # conexion.commit()
        registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print("Ocurrió un error:", e)

finally:
    conexion.close()