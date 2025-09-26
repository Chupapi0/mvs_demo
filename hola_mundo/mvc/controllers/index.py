import web

render = web.template.render('mvc/views/')

class Index:

    def __init__(self):
        pass

    def GET(self):
        return render.index()