% include('header.tpl',info=info)

 <h3>Búsqueda</h3>
 <form action="/alumnos" method="post" class="form-hotizontal">
        
        <div class="form-group">
            <label class="control-label col-xs-1">Curso:</label>
            <div class="col-xs-4">
                <select name="curso" class="form-control">
                % for c in info["cursos"]:
                % if info["params"].get("curso")==str(c.get_id()):
                  <option selected="selected" value="{{c.get_id()}}">{{c.Curso}}</option>
                % curso=c.Curso
                % else:
                    <option value="{{c.get_id()}}">{{c.Curso}}</option>
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

 <br/><h2>Alumnos - {{curso}}</h2>

<table class="table table-bordered">
    <tr><td>N.</td><td>Alumno</td><td>A/S</td><td>A</td><td>S</td><td>Mod.</td><td>Borrar</td></tr>
    <% 
    cont=0
    for r in info["alumnos"]:
    cont=cont+1 %>
    <tr>
      <td>{{cont}}</td>
      
        
        
      <td>{{r.Nombre}}</td>
      <td>0/0</td>
      <td><a href="usuarios/amonestacion/{{r.get_id()}}"><span class="glyphicon glyphicon-thumbs-down" aria-hidden="true"></span></a></td>
      <td><a href="usuarios/sancion/{{r.get_id()}}"><span class="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span></a></td>
      <td><a href="usuarios/historial/{{r.get_id()}}"><span class="glyphicon glyphicon-list-alt" aria-hidden="true"></span></a></td>
      <td><a href="usuarios/modificar/{{r.get_id()}}"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span></a></td>
      <td><a href="usuarios/borrar/{{r.get_id()}}"><span class="glyphicon glyphicon-remove-sign" aria-hidden="true"></span></a></td>
      
    </tr>
    % end
    </table>

	
% include('footer.tpl',info=info)