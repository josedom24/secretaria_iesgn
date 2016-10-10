from bottle import app, route, template, run, static_file, error,request,response,redirect,error
import bottle
import os
import sesion
import hashlib
from gestiona import *
from beaker.middleware import SessionMiddleware
from model import *

base_path = os.path.abspath(os.path.dirname(__file__))
alumnos_path = os.path.join(base_path, 'templates')
bottle.TEMPLATE_PATH.insert(0, alumnos_path)

@route('/alumnos',method=['get','post'])
def alumnos():
    if sesion.islogin():
        info={}
        curso="1" if request.forms.get("curso") is None else request.forms.get("curso")
        info["params"]={"curso":curso}
        info["alumnos"]=Alumno.select().where(Alumno.Unidad==curso)
        info["cursos"]=Curso.select()    
        print bottle.TEMPLATE_PATH
        
        return my_template('alumnos.tpl',info=info)
    else:
        redirect('/')