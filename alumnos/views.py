from bottle import app, route, template, run, static_file, error,request,response,redirect,error
import sesion
import hashlib
from gestiona import *
from beaker.middleware import SessionMiddleware
from model import *

@route('/alumnos',method=['get','post'])
def alumnos():
    if sesion.islogin():
        info={}
        curso="1" if request.forms.get("curso") is None else request.forms.get("curso")
        info["params"]={"curso":curso}
        info["alumnos"]=Alumno.select().where(Alumno.Unidad==curso)
        info["cursos"]=Curso.select()    
        
        return my_template('alumnos.tpl',info=info)
    else:
        redirect('/')