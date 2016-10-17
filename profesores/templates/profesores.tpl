% include('header.tpl',info=info)
% from gestiona import *



 <h3>Búsqueda</h3>
 <form action="/profesores" method="post" class="form-hotizontal">
        
        <div class="form-group">
            <label class="control-label col-xs-2">Departamento:</label>
            <div class="col-xs-4">
              <select name="departamento" class="form-control">
                % if info["departamento"]=="-1":
                %  departamento=""
                  <option selected="selected" value="-1"></option>
                % else:
                  <option  value="-1"></option>
                % end 
                % for c in info["departamentos"]:

                % if info["departamento"]==str(c.get_id()):
                  <option selected="selected" value="{{c.get_id()}}">{{c.Nombre}}</option>
                % departamento="- "+c.Nombre
                % else:
                    <option value="{{c.get_id()}}">{{c.Nombre}}</option>
                % end
                % end
                </select>
            </div>
        </div>
        <button  type="submit" class="btn btn-primary">Buscar</button>
    </form>
    <hr/>
    <!--<a href="/usuarios/add"><button type="submit" class="btn btn-primary">Nuevo usuario</button></a>
    <a href="/usuarios/tipo"><button type="submit" class="btn btn-primary">Asignar Tipo</button></a>-->

 <br/><h2>Gestión de profesores {{departamento}}</h2>

<table class="table table-bordered">
    <tr><td>N.</td><td>Nombre</td><td>Teléfono</td><td>Movil</td><td>Tutor</td><td>Dep.</td><td>CE</td><td>ETCP</td><td>Bil</td><td>Mod.</td><td>Borrar</td></tr>
    <% 
    cont=0
    for r in info["profesores"]:
    cont=cont+1 %>
    <tr>
      <td>{{cont}}</td>
      
        
        
      <td>{{r.Apellidos}},{{r.Nombre}}</td>
      <td><small>{{r.Telefono}}</small></td>
      <td><small>{{r.Movil}}</small></td>
      <td><small>{{profesor_curso(r.get_id())}}</small></td>
      <td><small>{{r.Departamento.Abr}}</small></td>
      <% lista=["Ce","Etcp","Bil"]
         for tipo in lista:
         if not getattr(r,tipo):
            color="red"
            operacion="on"
        else:
            color="green"
            operacion="off"
        end
      %>
      <td><a href="/profesores/{{tipo}}/{{r.get_id()}}/{{operacion}}"><span class="glyphicon glyphicon-user" style="color:{{color}}" aria-hidden="true"></span></a></td>
         
         % end
      <td><a href="/profesores/update/{{r.get_id()}}"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span></a></td>
      <td><a href="/profesores/del/{{r.get_id()}}"><span class="glyphicon glyphicon-remove-sign" aria-hidden="true"></span></a></td>

      
    </tr>
    % end
    </table>

	
% include('footer.tpl',info=info)