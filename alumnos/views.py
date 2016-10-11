from bottle import app, route, template, run, static_file, error,request,response,redirect,error
import bottle
import os
import sesion
import hashlib
import time
import calendar
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

@route('/alumnos/amonestacion/<id>',method='get')
def amonestacion(id):
    if sesion.islogin():
        info={}
        info["id"]=id
        info["dia"]=time.strftime('%d/%m/%Y')
        info["profesor"]=Profesor.select() 
        info["alumno"]=Alumno.get(Alumno.id==id)
        info["menu"]="alumnos"
        return my_template('amonestacion.tpl',info=info)
    else:
        redirect('/')

@route('/alumnos/amonestacion/new',method='post')
def amonestacion_new():
    if sesion.islogin():
        Amonestacion.create(**request.forms)
        redirect('/alumnos')
    else:
        redirect('/')

@route('/alumnos/sancion/<id>',method='get')
def sancion(id):
    if sesion.islogin():
        info={}
        info["id"]=id
        info["dia"]=time.strftime('%d/%m/%Y')
        info["profesor"]=Profesor.select() 
        info["alumno"]=Alumno.get(Alumno.id==id)
        info["menu"]="alumnos"
        return my_template('sancion.tpl',info=info)
    else:
        redirect('/')

@route('/alumnos/sancion/new',method='post')
def sancion_new():
    if sesion.islogin():
        Sancion.create(**request.forms)
        redirect('/alumnos')
    else:
        redirect('/')


@route('/alumnos/amonestacion/resumen',method='get')
def amonestacion_resumen():
    if sesion.islogin():
        info={}
        c = calendar.HTMLCalendar(calendar.MONDAY)
        info["cal"]=c.formatmonth(int(time.strftime('%Y')),int(time.strftime('%m')))
        return my_template('amonestacion_resumen.tpl',info=info)
    else:
        redirect('/')
