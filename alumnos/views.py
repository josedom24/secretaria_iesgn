# -*- coding: utf-8 -*-
from bottle import app, route, template, run, static_file, error,request,response,redirect,error
import bottle
import os
import sesion
import hashlib
import time
import calendar
from datetime import datetime
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

        curso=sesion.get("curso") if sesion.get("curso")!="" else "1" 
        curso=curso if request.forms.get("curso") is None else request.forms.get("curso")
        sesion.set("curso",curso)
        print curso
        info["curso"]=curso
        info["alumnos"]=Alumno.select().where(Alumno.Unidad==curso)
        info["cursos"]=Curso.select() 
        info["menu"]="alumnos"   
        
        
        return my_template('alumnos.tpl',info=info)
    else:
        redirect('/')

@route('/alumnos/partes/<tipo>/<id:int>',method='get')
def amonestacion(tipo,id):
    if sesion.islogin():
        info={}
        info["id"]=id
        info["dia"]=time.strftime('%d/%m/%Y')
        info["profesor"]=Profesor.select() 
        info["alumno"]=Alumno.get(Alumno.id==id)
        info["menu"]="alumnos"
        return my_template(tipo+'.tpl',info=info)
    else:
        redirect('/')

@route('/alumnos/partes/<tipo>/new',method='post')
def amonestacion_new(tipo):
    if sesion.islogin():
        if tipo=="amonestacion":
            Amonestacion.create(**request.forms)
        elif tipo=="sancion":
            Sancion.create(**request.forms)    
        redirect('/alumnos')
    else:
        redirect('/')


@route('/alumnos/partes/<tipo>/resumen',method='get')
def amonestacion_resumen(tipo):
    if sesion.islogin():
        redirect('/alumnos/partes/'+tipo+'/resumen/%s/%s'%(time.strftime('%Y'),time.strftime('%m')))
    else:
        redirect('/')

@route('/alumnos/partes/<tipo>/resumen/<year:int>/<month:int>',method='get')
def amonestacion_resumen2(tipo,year,month):
    if sesion.islogin() and (month>=1 and month<=12):
        
        info={}
        info["tipo"]=tipo
        info["proxmes"]=month+1
        info["prevmes"]=month-1
        info["proxano"]=year
        info["prevano"]=year
        if(info["proxmes"]>12):
            info["proxmes"]=1
            info["proxano"]=year+1
        if(info["prevmes"]<1):
            info["prevmes"]=12
            info["prevano"]=year-1
        c = calendar.HTMLCalendar(calendar.MONDAY)
        info["cal"]=c.formatmonth(int(year),int(month))
        info["cal"]=info["cal"].replace('class="month"','class="table-condensed table-bordered table-striped"')

        hoy=datetime.now()
        primerdia="01/%s/%s" % (hoy.month,hoy.year)
        ultimodia="%s/%s/%s" % (calendar.monthrange(hoy.year-1, hoy.month-1)[1],hoy.month,hoy.year)
        if tipo=="amonestacion":
            info["titulo"]="Resumen de amonestaciones"
            sql=Amonestacion.select(Amonestacion.Fecha).where(Amonestacion.Fecha>=primerdia ,Amonestacion.Fecha<=ultimodia)
        elif tipo=="sancion":
            info["titulo"]="Resumen de sanciones"
            sql=Sancion.select(Sancion.Fecha).where(Sancion.Fecha>=primerdia ,Sancion.Fecha<=ultimodia)
            
        
        fechas=[]
        for f in sql:
            fechas.append(f.Fecha)
        fechas=set(fechas)
        ult_dia=calendar.monthrange(hoy.year-1, hoy.month-1)[1]
        for dia in xrange(1,int(ult_dia)+1):
            fecha="%s/%s/%s" % (dia,month,year)
            if fecha in fechas:
                info["cal"]=info["cal"].replace(">"+str(dia)+"<",'><a href="/alumnos/partes/%s/show/%s/%s/%s"><strong>%s</strong></a><'%(tipo,dia,month,year,dia))


        return my_template('amonestacion_resumen.tpl',info=info)
    else:
        redirect('/')

@route('/alumnos/partes/<tipo>/show/<day:int>/<month:int>/<year:int>',method='get')
def show(tipo,day,month,year):
    if sesion.islogin():
        info={}
        info["fecha"]="%s/%s/%s"%(day,month,year)
        if tipo=="amonestacion":
            info["titulo"]="Resumen de amonestaciones"
            info["alumnos"]=Amonestacion.select().where(Amonestacion.Fecha==info["fecha"])
        elif tipo=="sancion":
            info["titulo"]="Resumen de sanciones"
            info["alumnos"]=Sancion.select().where(Sancion.Fecha==info["fecha"])

        

        
        return my_template('show.tpl',info=info)
    else:
        redirect('/')

@route('/alumnos/historial/alumno/<id:int>',method='get')
def historial(id):
    if sesion.islogin():
        info={}
        alum=Alumno.select().where(Alumno.id==id)
        amon=Amonestacion.select().where(Amonestacion.IdAlumno==id).order_by('Fecha')
        sanc=Sancion.select().where(Sancion.IdAlumno==id).order_by('Fecha')
        historial=list(amon)+list(sanc)
        historial=sorted(historial, key=lambda x: x.Fecha, reverse=False)
    
        tipo=[]
        for h in historial:
            tipo.append(str(type(h)).split(".")[1][0])
        hist=zip(historial,tipo)
        
        info["hist"]=hist
        info["alumno"]=alum
        
           
        return my_template('historial.tpl',info=info)
    else:
        redirect('/')

@route('/alumnos/partes/<alum:int>/<tipo>/<id:int>/del',method='get')
def amonestacion_del_get(alum,tipo,id):
    if sesion.islogin():
        info={}
        info["url"]="/alumnos/partes/%s/%s/%s/del"%(alum,tipo,id)
        info["alum"]=Alumno.select().where(Alumno.id==alum)
        if tipo=="amonestacion":
            info["tipo"]="Amonestación"
            info["datos"]=Amonestacion.select().where(Amonestacion.id==id)
        elif tipo=="sancion":
            info["tipo"]="Sanción"
            info["datos"]=Sancion.select().where(Sancion.id==id)
        return my_template('amonestacion_del.tpl',info=info)
    else:
        redirect('/')

@route('/alumnos/partes/<alum:int>/<tipo>/<id:int>/del',method='post')
def amonestacion_del_post(alum,tipo,id):
    if sesion.islogin():
        if request.forms.get("respuesta")=="s":
            if tipo=="amonestacion":
                sql=Amonestacion.delete().where(Amonestacion.id==id)
                sql.execute()
            elif tipo=="sancion":
                sql=Sancion.delete().where(Sancion.id==id)
                sql.execute()
        redirect('/alumnos/historial/alumno/'+str(alum))
        

    else:
        redirect('/')

@route('/alumnos/del/<id:int>',method='get')
def alumno_del_get(id):
    if sesion.islogin():
        info={}
        info["url"]="/alumnos/del/%s"%id
        info["alum"]=Alumno.select().where(Alumno.id==id)
        return my_template('alumno_del.tpl',info=info)
    else:
        redirect('/')


@route('/alumnos/del/<id:int>',method='post')
def alumno_del_post(id):
    if sesion.islogin():
        if request.forms.get("respuesta")=="s":
            sql=Alumno.delete().where(Alumno.id==id)
            sql.execute()
            sql=Amonestacion.delete().where(Amonestacion.IdAlumno==id)
            sql.execute()
            sql=Sancion.delete().where(Sancion.IdAlumno==id)
            sql.execute()
        redirect('/alumnos')
    else:
        redirect('/')
