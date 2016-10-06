from bottle import app, route, template, run, static_file, error,request,response,redirect,error
import sesion
import hashlib
from gestiona import *
from beaker.middleware import SessionMiddleware
from model import *
from sys import argv

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}
app = SessionMiddleware(app(), session_opts)

@route('/')
@route('/login',method="get")
def index():
    return my_template("index.tpl")

@route('/login',method="post")
def do_login():
    
    username = request.forms.get('username')
    password = request.forms.get('password')
    usu=Usuario.select().where(Usuario.Usuario==username,Usuario.Pass==hashlib.md5(password).hexdigest())
    if usu.count()==1:  
        sesion.set("user",username)    
        sesion.set("grupo",usu[0].Perfil)
        redirect('/')
    else:
        info={"error":True}
        return my_template('index.tpl',info=info)

@route('/logout')
def do_logout():
    
    sesion.delete()
    redirect('/')

__import__("alumnos.views")





#@route('/usuarios/add',method=['get','post'])
#def add():
#    if sesion.islogin() and sesion.isprofesor():
#        if request.POST:
#            lldap=LibLDAP(sesion.get("user"),sesion.get("pass"))
#            resultados=lldap.buscar('(uidNumber=*)')
#            #

#            attrs=request.forms
#            attrs['objectclass']=["inetOrgPerson","posixAccount","top"]
#            attrs['uidNumber']=str(lista_uid(resultados))
#            path="/home/alumnos/" if attrs["gidnumber"]=="2001" else "/home/profesores/" 
#            attrs["homedirectory"]=path+attrs["uid"]
#            attrs["userpassword"]="{md5}"+base64.b64encode(binascii.unhexlify(hashlib.md5(attrs["userpassword"]).hexdigest()))
#            attrs["cn"]=attrs["givenname"]+" "+attrs["sn"]
#            lldap.add(attrs["uid"],attrs)
#            redirect('/usuarios')
#        else:
#        #

#            return my_template('add.tpl')
#    else:
#        redirect('/')#

#@route('/usuarios/borrar/<uid>',method=['get','post'])
#def borrar(uid):
#    if sesion.islogin() and sesion.isprofesor():
#        if request.POST:
#            if request.forms.get("respuesta")=="no":
#                redirect('/usuarios')
#            else:
#                lldap=LibLDAP(sesion.get("user"),sesion.get("pass"))
#                lldap.delete(uid)
#                redirect('/usuarios')
#        else:
#            info={"uid":uid}
#            return my_template('borrar.tpl',info)
#    else:
#        redirect('/')#

#@route('/usuarios/modificar/<uid>',method=['get','post'])
#def modificar(uid):
#    if sesion.islogin():
#        lldap=LibLDAP(sesion.get("user"),sesion.get("pass"))
#        busqueda='(uid=%s)'%uid
#        resultados=lldap.buscar(busqueda)
#        info=resultados[0].get_attributes()#

#        if request.POST:
#            attrs=request.forms
#            if attrs["userpassword"]=="":
#                del attrs["userpassword"]
#            else:
#                attrs["userpassword"]="{md5}"+base64.b64encode(binascii.unhexlify(hashlib.md5(attrs["userpassword"]).hexdigest()))
#            attrs["cn"]=attrs["givenname"]+" "+attrs["sn"]#

#            old={}
#            new={}
#            for key,value in attrs.items():
#                print key,value
#                if value!=info[key][0]:
#                    new[key]=value
#                    old[key]=info[key][0]
#            print new
#            print old
#            lldap.modify(attrs["uid"],new,old)
#            redirect('/usuarios')
#        else:
#            
#            
#            return my_template('modificar.tpl',info)
#    else:
#        redirect('/')#

#@route('/usuarios/tipo')
#def tipo():
#    if sesion.islogin() and sesion.isprofesor():
#        lldap=LibLDAP(sesion.get("user"),sesion.get("pass"))
#        busqueda='(givenname=*)'
#        resultados1=lldap.buscar(busqueda)
#        
#        info={"no_asignado":lista_usuarios_tipo(resultados1," ")}
#        
#        return my_template('tipo.tpl',info)#

#        
#    else:
#        redirect('/')


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')


@error(404)
def error404(error):
    return "Nada"

run(app=app,host='0.0.0.0', port=argv[1],reloader=True)
