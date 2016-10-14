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

        curso=sesion.get("curso") if sesion.get("curso")!=""<    else "1" 
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

@route('/alumnos/<tipo>/<id:int>',method='get')
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

@route('/alumnos/<tipo>/new',method='post')
def amonestacion_new(tipo):
    if sesion.islogin():
        if tipo=="amonestacion":
            Amonestacion.create(**request.forms)
        elif tipo=="sancion":
            Sancion.create(**request.forms)    
        redirect('/alumnos')
    else:
        redirect('/')


@route('/alumnos/<tipo>/resumen',method='get')
def amonestacion_resumen(tipo):
    if sesion.islogin():
        redirect('/alumnos/'+tipo+'/resumen/%s/%s'%(time.strftime('%Y'),time.strftime('%m')))
    else:
        redirect('/')

@route('/alumnos/<tipo>/resumen/<year:int>/<month:int>',method='get')
def amonestacion_resumen2(tipo,year,month):
    if sesion.islogin() and (month>=1 and month<=12):
        
        info={}
        
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
                info["cal"]=info["cal"].replace(">"+str(dia)+"<",'><a href="/alumnos/amonestacion/show/%s/%s/%s"><strong>%s</strong></a><'%(dia,month,year,dia))


        return my_template('amonestacion_resumen.tpl',info=info)
    else:
        redirect('/')

@route('/alumnos/<tipo>/show/<day:int>/<month:int>/<year:int>',method=['get','post'])
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