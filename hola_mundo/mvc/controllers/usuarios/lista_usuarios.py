import web

render = web.template.render('mvc/views/usuarios')

class ListaUsuarios:

    def __init__(self):
        pass

    def GET(self):
        return render.lista_usuarios()