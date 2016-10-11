# -*- coding: utf-8 -*-
from bottle import template,request
import sesion

def my_template(name,info={}):
	
	info["login"]=sesion.get("user") if sesion.islogin() else ""
	return template(name,info=info)

