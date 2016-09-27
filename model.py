# -*- coding: utf-8 -*-
from peewee import *

db = SqliteDatabase('secretaria.db')


class Departamento(Model):
	Abr = CharField(max_length=4)
	Nombre = CharField(max_length=30)

	class Meta:
		database = db 


class Profesor(Model):
	Nombre = CharField(max_length=20)
	Apellidos = CharField(max_length=30)
	Telefono = CharField(max_length=9)
	Movil = CharField(max_length=9)
	Email = CharField(max_length=50)
	Departamento = ForeignKeyField(Departamento)
	Baja = BooleanField(default=False)
	Ce = BooleanField(default=False,verbose_name="Consejo Escolar")
	Etcp = BooleanField(default=False)
	Tic = BooleanField(default=False)
	Bil = BooleanField(default=False,verbose_name="Bilingüe")

	class Meta:
		database = db 

class Curso(Model):
	Curso = CharField(max_length=30,primary_key=True)
	Tutor = ForeignKeyField(Profesor, related_name='Tutor_de',null=True)

	class Meta:
		database = db 


class Alumno(Model):
    
	Nombre = CharField(max_length=50)
	DNI = CharField(max_length=10)
	Direccion = CharField(max_length=60)
	CodPostal = CharField(max_length=5,verbose_name="Código postal")
	Localidad = CharField(max_length=30)
	Fecha_nacimiento = DateField('Fecha de nacimiento')
	Provincia = CharField(max_length=30)
	Unidad = ForeignKeyField(Curso)
	Ap1tutor = CharField(max_length=20,verbose_name="Apellido 1 Tutor")
	Ap2tutor = CharField(max_length=20,verbose_name="Apellido 2 Tutor")
	Nomtutor = CharField(max_length=20,verbose_name="Nombre tutor")
	Telefono1 = CharField(max_length=12,null=True)
	Telefono2 = CharField(max_length=12,null=True)
	Obs=TextField(verbose_name="Observaciones",null=True)

	class Meta:
		database = db 

class Usuario(Model):
    
	Usuario = CharField(max_length=50,primary_key=True)
	Nombre = CharField(max_length=50)
	Pass = CharField(max_length=32)
	Email = CharField(max_length=50)
	Perfil = CharField(max_length=1)


	class Meta:
		database = db 



