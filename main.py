from wsgiref.simple_server import make_server
from cgi import parse_qs

from battle_field import Battlefield


def battle(num_armies):
    num_armies = int(num_armies)
    b = Battlefield(num_armies)
    return b.start()


def open_f(file, mode='r',parameter=''):
    with open(file, mode) as f:
        return f.read().format(parameter).encode('UTF-8')


def app(env, resp_start):
    route = {'battle': battle}

    resp_start('200 OK', [('content-type','text/html')])

    path = env.get('PATH_INFO')[1:]
    parts = path.split('/')
    if parts[0]:
        content_length = int(env.get('CONTENT_LENGTH'))
        post_data = env['wsgi.input'].read(content_length)
        post_data = parse_qs(post_data)
        fn = route.get(parts[0])
        if post_data[b'num_armies'][0].decode('UTF-8') > '0':
            log = fn(post_data[b'num_armies'][0].decode('UTF-8'))
            html = open_f('battle.html', 'r', log)
        else:
            html = open_f('index.html', 'r')
    else:
        html = open_f('index.html','r')

    return [html] #app  must return arr of strings


if __name__ == '__main__':
    serv = make_server('', 8080, app)
    serv.serve_forever()
