# -*- coding: utf-8 -*-
from bottle import app, route, template, run, static_file, error,request,response,redirect,error
import bottle
import os
import sesion
from beaker.middleware import SessionMiddleware
from model import *
from gestiona import *


base_path = os.path.abspath(os.path.dirname(__file__))
profesores_path = os.path.join(base_path, 'templates')
bottle.TEMPLATE_PATH.insert(0, profesores_path)

@route('/profesores',method=['get','post'])
def profesores():
    if sesion.islogin():
        info={}
        info["profesores"]=Profesor.select().order_by(Profesor.Apellidos)
        info["menu"]="profesores"   
        return my_template('profesores.tpl',info=info)
    else:
        redirect('/')

