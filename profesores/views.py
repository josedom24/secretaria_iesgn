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
    	departamento=sesion.get("departamento") if sesion.get("departamento")!="" else str(Departamento.select()[0].get_id())
        departamento=departamento if request.forms.get("departamento") is None else request.forms.get("departamento")
        sesion.set("departamento",departamento)
        info["departamento"]=departamento
        if departamento=="-1":
        	info["profesores"]=Profesor.select().order_by(Profesor.Apellidos)
        else:
        	info["profesores"]=Profesor.select().where(Profesor.Departamento==departamento).order_by(Profesor.Apellidos)
        info["departamentos"]=Departamento.select()
        info["menu"]="profesores"   
        return my_template('profesores.tpl',info=info)
    else:
        redirect('/')

@route("/profesores/<campo>/<id:int>/<operacion>")
def actualizar_campo(campo,id,operacion):
	
	valor={campo:True} if operacion=="on" else {campo:False}
	Profesor.update(**valor).where(Profesor.id==id).execute()
	redirect("/profesores")

@route('/profesores/del/<id:int>',method='get')
def profesor_del_get(id):
    if sesion.islogin():
        info={}
        info["url"]="/profesores/del/%s"%id
        info["profe"]=Profesor.select().where(Profesor.id==id)
        return my_template('profesor_del.tpl',info=info)
    else:
        redirect('/')


@route('/profesores/del/<id:int>',method='post')
def profesor_del_post(id):
    if sesion.islogin():
        if request.forms.get("respuesta")=="s":
        	curso=profesor_curso(id)
        	if curso!="":
        		Curso.update(Tutor=None).where(Curso.Curso==curso).execute()
        	sql=Profesor.delete().where(Profesor.id==id)
        	sql.execute()
            
        redirect('/profesores')
    else:
        redirect('/')