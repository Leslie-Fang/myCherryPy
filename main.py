import os, os.path
import random
import string
import sqlite3

import cherrypy
import time

DB_STRING = "testDB.db"

class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return open('index.html')

@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return 'hhh'

@cherrypy.expose
class myFirstService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        with sqlite3.connect(DB_STRING) as c:
            cherrypy.session['ts'] = time.time()
            r = c.execute("SELECT * FROM STUDENT")
            print r.fetchone()
            return 'hhui'

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd()),
        },
        '/generator': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/index': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    webapp = StringGenerator()
    webapp.generator = StringGeneratorWebService()
    webapp.index = myFirstService()
   # cherrypy.quickstart(webapp, '/', conf)

    cherrypy.tree.mount(webapp, '/', conf)
    #cherrypy.tree.mount(Forum(), '/forum', forum_conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
