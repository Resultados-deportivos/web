from jinja2 import Environment, FileSystemLoader
import os

env = Environment(loader=FileSystemLoader('templates'))
#env2 = Environment(loader=FileSystemLoader('static'))
#env3 = Environment(loader=FileSystemLoader('static/img'))
index = env.get_template('index.html')
competiciones = env.get_template('competiciones.html')
equipos = env.get_template('equipos.html')
partidos = env.get_template('partidos.html')
error = env.get_template('error.html')
login = env.get_template('login.html')


def page_index(environ, start_response):
    publicaciones = [
        ('img1.jpg', 'Mate espectacular de Michael Jordan', 'Reviviendo uno de los míticos mates de MJ.'),
        ('img2.jpg', 'LeBron gana su cuarto campeonato', 'El Rey consigue otro anillo de campeón.'),
        ('img3.jpg', 'Homenaje a la leyenda Kobe Bryant', 'Recordando la carrera de Kobe en la NBA.'),
        ('img4.jpg', 'Nuevo récord de puntos en un partido',
         'Un jugador supera el récord de anotación en un solo partido.'),
        ('img5.jpg', 'Increíble jugada de baloncesto', 'Una jugada asombrosa que dejó a todos sorprendidos.')
    ]

    response = index.render(publicaciones=publicaciones).encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def page_competiciones(environ, start_response):
    response = competiciones.render().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def page_equipos(environ, start_response):
    response = equipos.render().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def page_partidos(environ, start_response):
    response = partidos.render().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def page_login(environ, start_response):
    response = login.render().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]


def serve_static(environ, start_response, path):
    # Set the appropriate content type for CSS
    if path.endswith('.css'):
        content_type = 'text/css'
    else:
        content_type = 'text/plain'  # Set a default content type for other static files

    try:
        with open('.' + path, 'rb') as file:
            response_body = file.read()
        status = '200 OK'
    except FileNotFoundError:
        response_body = b'File Not Found'
        status = '404 Not Found'

    response_headers = [('Content-type', content_type)]
    start_response(status, response_headers)
    return [response_body]


def serve_static_img(environ, start_response, path):
    # Set the appropriate content type for CSS
    if path.endswith('.png'):
        content_type = 'image/png'
    else:
        content_type = 'text/plain'  # Set a default content type for other static files

    try:
        with open('.' + path, 'rb') as file:
            response_body = file.read()
        status = '200 OK'
    except FileNotFoundError:
        response_body = b'File Not Found'
        status = '404 Not Found'

    response_headers = [('Content-type', content_type)]
    start_response(status, response_headers)
    return [response_body]


def serve_static_js(environ, start_response, path):
    # Set the appropriate content type for JavaScript files
    if path.endswith('.js'):
        content_type = 'application/javascript'
    else:
        content_type = 'text/plain'  # Set a default content type for other static files

    try:
        with open('.' + path, 'rb') as file:
            response_body = file.read()
        status = '200 OK'
    except FileNotFoundError:
        response_body = b'File Not Found'
        status = '404 Not Found'

    response_headers = [('Content-type', content_type)]
    start_response(status, response_headers)
    return [response_body]


def handle_404(environ, start_response):
    response = error.render().encode('utf-8')
    status = '404 Not Found'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]
