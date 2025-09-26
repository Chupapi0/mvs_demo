import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/lista_usuarios', 'mvc.controllers.usuarios.lista_usuarios.ListaUsuarios',
    '/detalles_usuarios','mvc.controllers.usuarios.detalles_usuarios.DetallesUsuarios',
    '/insertar_usuarios','mvc.controllers.usuarios.insertar_usuarios.InsertarUsuarios',
    '/lista_productos','mvc.controllers.productos.lista_productos.ListaProductos',
    '/detalles_productos','mvc.controllers.productos.detalles_productos.DetallesProductos',
    '/insertar_productos','mvc.controllers.productos.insertar_productos.InsertarProductos',
)
app = web.application(urls, globals())



if __name__ == "__main__":
    app.run()