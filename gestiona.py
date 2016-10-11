# -*- coding: utf-8 -*-
from bottle import template,request
from model import Amonestacion,Sancion
import sesion


def my_template(name,info={}):
	
	info["login"]=sesion.get("user") if sesion.islogin() else ""
	return template(name,info=info)

def CountAmonestaciones(id):
	return Amonestacion.select().where(Amonestacion.IdAlumno==id).count()

def CountSanciones(id):
	return Sancion.select().where(Sancion.IdAlumno==id).count()