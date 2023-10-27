from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
index = env.get_template('index.html')

def english_handle_index(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'Hello, English World!']

def page_index(environ, start_response):
    # tareas = []
    # response = index.render(tareas = taresas.encode('utf-8')
    response = index.render().encode('utf-8')
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [response]

def handle_404(environ, start_response):
    status = '404 Not Found'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    return [b'Pagina no encontrada']
