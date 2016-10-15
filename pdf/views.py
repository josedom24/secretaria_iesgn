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



