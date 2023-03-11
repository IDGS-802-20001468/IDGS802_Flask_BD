from db import get_connection

'''
try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consultar_alumnos()')
        resultset = cursor.fetchall()
        for row in resultset:
            print(row)
except Exception as ex:
    print('ERROR')
'''

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consultar_alumno(%s)', (2,))
        resultset = cursor.fetchall()
        print(resultset)
except Exception as ex:
    print('ERROR')


'''
try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call agregar_alumno(%s, %s, %s)', ('Arturo','Alba', 'alba@gmail.com'))

        connection.commit()
        connection.close()
except Exception as ex:
    print('ERROR')

'''

