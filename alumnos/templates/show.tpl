% include('header.tpl',info=info)
% from gestiona import *

 <h3>{{info["titulo"]}}</h3>
 <h4>{{info["fecha"]}}</h4>
 
 <br/><h2>Alumnos</h2>

<table class="table table-bordered">
    % if info["tipo"]=="amonestacion":
      <tr><td>N.</td><td>Alumno</td><td>Curso</td><td>A/S</td></tr>
    % else:
      <tr><td>N.</td><td>Alumno</td><td>Curso</td><td>Sanción</td><td>Fecha</td><td>Fecha fin.</td></tr>
    % end
    <% 
    cont=0
    for r in info["alumnos"]:
    cont=cont+1 %>
    <tr>
      <td>{{cont}}</td>
      
        
        
      <td>{{r.IdAlumno.Nombre}}</td>
      <td>{{r.IdAlumno.Unidad.Curso}}</td>
      % if info["tipo"]=="amonestacion":
        <td>{{CountPartes("amonestacion",r.IdAlumno.get_id())}}/{{CountPartes("sancion",r.IdAlumno.get_id())}}</td>
      % else:
        <td>{{r.Sancion}}</td>
        <td>{{r.Fecha}}</td>
        <td>{{r.Fecha_fin}}</td>
        <td><a href="/pdf/alumnos/resumen/carta/sancion/{{r.get_id()}}"><span class="glyphicon glyphicon-list-alt" aria-hidden="true"></span></a></td>
      % end
      
    </tr>
    % end
    </table>

	
% include('footer.tpl',info=info)