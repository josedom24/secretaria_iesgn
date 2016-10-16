# -*- coding: utf-8 -*-
from bottle import app, route, template, run, static_file, error,request,response,redirect,error
import bottle
import os
from gestiona import *


from xhtml2pdf import pisa
from cStringIO import StringIO
import sesion
import time
from model import *
from gestiona import *


base_path = os.path.abspath(os.path.dirname(__file__))
pdf_path = os.path.join(base_path, 'templates')
bottle.TEMPLATE_PATH.insert(0, pdf_path)

@route("/pdf/alumnos/partes/<curso>")
def alumnos_partes(curso):
	if sesion.islogin():
		response.headers['Content-Type'] = 'application/pdf; charset=UTF-8'
		response.headers['Content-Disposition'] = 'attachment; filename="partes.pdf"'
		
		info={}
		info["curso"]=Curso.select().where(Curso.id==curso)[0].Curso
		info["alumnos"]=Alumno.select().where(Alumno.Unidad==curso)
		info["titulo"]="Resumen de Amonestaciones/Sanciones"
		info["fecha"]=time.strftime("%d/%m/%Y")

		pdf_data= my_template('listado.tpl',info=info)	
		pdf = StringIO()
		pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
		pdf.reset()
		return pdf.readlines()
	else:
		redirect("/")

@route("/pdf/alumnos/resumen/amonestacion/<day:int>/<month:int>/<year:int>")
def alumnos_resumen_amonestacion(day,month,year):
	if sesion.islogin():
		response.headers['Content-Type'] = 'application/pdf; charset=UTF-8'
		response.headers['Content-Disposition'] = 'attachment; filename="amonestacion.pdf"'
		
		info={}
		info["fecha"]="%s/%s/%s"%(day,month,year)
		info["titulo"]="Resumen de amonestaciones"
		info["alumnos"]=Amonestacion.select().where(Amonestacion.Fecha==info["fecha"])

		pdf_data= my_template('resumen_amonestacion.tpl',info=info)	
		pdf = StringIO()
		pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
		pdf.reset()
		return pdf.readlines()
	else:
		redirect("/")
@route("/pdf/alumnos/resumen/cartas/amonestacion/<day:int>/<month:int>/<year:int>")
def carta_amonestacion(day,month,year):
	response.headers['Content-Type'] = 'application/pdf; charset=UTF-8'
	response.headers['Content-Disposition'] = 'attachment; filename="cartas_amonestacion.pdf"'
	info={}
	contenido=""
	info["fecha"]="%s/%s/%s"%(day,month,year)
	info["alumnos"]=Amonestacion.select().where(Amonestacion.Fecha==info["fecha"])

	for i in info["alumnos"]:
		info2={}
		info2["alumno"]=i
		info2["num_amon"]=CountPartes("amonestacion",i.IdAlumno.get_id())
		contenido=contenido+my_template('contenido_carta_amonestacion.tpl',info=info2)
		if i.id!=info["alumnos"][-1].id:
			contenido=contenido+"<pdf:nextpage>"
	info["contenido"]=contenido

	pdf_data= my_template('carta_amonestacion.tpl',info=info)	
	pdf = StringIO()
	pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
	pdf.reset()
	return pdf.readlines()


@route("/pdf/alumnos/resumen/sancion/<day:int>/<month:int>/<year:int>")
def alumnos_resumen_sancion(day,month,year):
	if sesion.islogin():
		response.headers['Content-Type'] = 'application/pdf; charset=UTF-8'
		response.headers['Content-Disposition'] = 'attachment; filename="sancion.pdf"'
		
		info={}
		info["fecha"]="%s/%s/%s"%(day,month,year)
		info["titulo"]="Resumen de sanciones"
		info["alumnos"]=Sancion.select().where(Sancion.Fecha==info["fecha"])

		pdf_data= my_template('resumen_sancion.tpl',info=info)	
		pdf = StringIO()
		pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
		pdf.reset()
		return pdf.readlines()
	else:
		redirect("/")

@route("/pdf/alumnos/resumen/carta/sancion/<id:int>")
def carta_sancion(id):
	response.headers['Content-Type'] = 'application/pdf; charset=UTF-8'
	response.headers['Content-Disposition'] = 'attachment; filename="carta_sancion.pdf"'
	info={}
	contenido=""
	
	info["alumno"]=Sancion.select().where(Sancion.id==id)[0]
	info["fecha"]={}
	info["fecha"]["dia"]=time.strftime('%d')
	info["fecha"]["mes"]=time.strftime('%B')
	info["fecha"]["ano"]=time.strftime('%Y')
	info["fecha"]["hora"]=time.strftime('%H')+":00"
	

	pdf_data= my_template('contenido_carta_sancion.tpl',info=info)	
	pdf = StringIO()
	pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
	pdf.reset()
	return pdf.readlines()