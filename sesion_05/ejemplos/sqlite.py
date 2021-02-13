import sqlite3


def connect_to_database():
    conn = None
    try:
        conn = sqlite3.connect(':memory:')
        # conn = sqlite3.connect('db.sqlite3')
    except sqlite3.Error as err:
        print(err)
    finally:
        return conn


def disconnect_database(conn):
    conn.close()


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute(
        'CREATE TABLE peliculas(id integer PRIMARY KEY, nombre text, director text)'
    )
    conn.commit()


def create_movie(conn, name, director):
    cursor = conn.cursor()
    sql = 'INSERT INTO peliculas(nombre, director) VALUES (?, ?)'
    cursor.execute(sql, [name, director])
    conn.commit()


def get_movies(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM peliculas')
    rows = cursor.fetchall()
    movies = []
    for row in rows:
        _id, nombre, director = row
        movies.append({
            'id': _id,
            'nombre': nombre,
            'director': director
        })
    return movies


def print_movies(conn):
    print('Mis películas favoritas son:')
    for movie in get_movies(conn):
        message = '  - {} de {}'.format(movie['nombre'], movie['director'])
        print(message)


conn = connect_to_database()
create_table(conn)
create_movie(conn, 'Pulp Fiction', 'Quentin Tarantino')
create_movie(conn, 'Django', 'Quentin Tarantino')
create_movie(conn, 'The Dark Knight', 'Christopher Nolan')
print_movies(conn)
disconnect_database(conn)
