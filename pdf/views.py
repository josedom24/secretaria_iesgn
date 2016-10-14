# -*- coding: utf-8 -*-
from bottle import app, route, template, run, static_file, error,request,response,redirect,error
import bottle
import os
from gestiona import *


from xhtml2pdf import pisa
from cStringIO import StringIO
import sesion
from model import *


base_path = os.path.abspath(os.path.dirname(__file__))
pdf_path = os.path.join(base_path, 'templates')
bottle.TEMPLATE_PATH.insert(0, pdf_path)

@route("/pdf")
def pdf():
	response.headers['Content-Type'] = 'application/pdf; charset=UTF-8'
	response.headers['Content-Disposition'] = 'attachment; filename="test1.pdf"'
	
	id="32"
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
	pdf_data= my_template('historial2.tpl',info=info)

	
	pdf = StringIO()
	pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
	pdf.reset()
	
	return pdf.readlines()
