% include('header.tpl',info=info)
% from gestiona import tipos
 <h3>Búsqueda</h3>
 <form action="/alumnos" method="post" class="form-horizontal">
        
        <div class="form-group">
            <label class="control-label col-xs-2">Curso:</label>
            <div class="col-xs-4">
                <select name="curso" class="form-control">
                % for c in info["cursos"]:
                % if info["params"].get("curso")==str(c.get_id()):
                  <option selected="selected" value="{{c.get_id()}}">{{c.Curso}}</option>
                %else:
                  <option value="{{c.get_id()}}">{{c.Curso)}}</option>
                % end
                % end
                </select>
                
        </div>
        </div>
        
        <div class="form-group">
            <div class="col-xs-offset-2 col-xs-10">
                <button type="submit" class="btn btn-primary">Buscar</button>
            </div>
        </div>
    </form>
    <hr/>
    <a href="/usuarios/add"><button type="submit" class="btn btn-primary">Nuevo usuario</button></a>
    <a href="/usuarios/tipo"><button type="submit" class="btn btn-primary">Asignar Tipo</button></a>

 <br/><h2>Alumnos</h2>

<table class="table table-bordered">
    <tr><td>N.</td><td>A/P</td><td>Usuario (Login)</td><td>Tipo</td><td>Mod.</td><td>Borrar</td></tr>
    <% 
    cont=0
    for r in info["alumnos"]:
    cont=cont+1 %>
    <tr>
      <td>{{cont}}</td>
      
        <td><span class="glyphicon glyphicon-user" aria-hidden="true"></td>
      
        <td><span class="glyphicon glyphicon-education" aria-hidden="true"></td>
        
      <td>{{r.Nombre}}</td>
      
      <td><a href="usuarios/modificar/{{r.get_id()}}"><span class="glyphicon glyphicon-pencil" aria-hidden="true"></span></a></td>
      <td><a href="usuarios/borrar/{{r.get_id()}}"><span class="glyphicon glyphicon-remove-sign" aria-hidden="true"></span></a></td>
      
    </tr>
    % end
    </table>

	
% include('footer.tpl',info=info)