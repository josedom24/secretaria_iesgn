% include('header.tpl',info=info)
% from gestiona import *

 <h3>{{info["titulo"]}}</h3>
 <h4>{{info["fecha"]}}</h4>
 
 <br/><h2>Alumnos</h2>

<table class="table table-bordered">
    <tr><td>N.</td><td>Alumno</td><td>Curso</td><td>A/S</td></tr>
    <% 
    cont=0
    for r in info["alumnos"]:
    cont=cont+1 %>
    <tr>
      <td>{{cont}}</td>
      
        
        
      <td>{{r.IdAlumno.Nombre}}</td>
      <td>{{r.IdAlumno.Unidad.Curso}}</td>
      <td>{{CountPartes("amonestacion",r.IdAlumno.get_id())}}/{{CountPartes("sancion",r.IdAlumno.get_id())}}</td>
      
      
    </tr>
    % end
    </table>

	
% include('footer.tpl',info=info)