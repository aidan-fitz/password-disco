import cherrypy

class Server(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

cherrypy.quickstart(Server())
