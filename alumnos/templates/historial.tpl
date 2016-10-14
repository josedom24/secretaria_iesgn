% include('header.tpl',info=info)


 <h3>Historial del Alumno</h3>
 <h4>{{info["alumno"][0].Nombre}}-{{info["alumno"][0].Unidad.Curso}}</h4>
 
 

<table class="table table-bordered">
  
    <tr><td>N.</td><td>Tipo</td><td>Fecha</td><td>Fecha fin.</td><td>Sanción</td><td>Comentario</td></tr>
    <% 
    cont=0
    for r in info["hist"]:
    cont=cont+1 %>
    <tr>
      <td>{{cont}}</td>
      % if r[1]=="A":
        % tipo="amonestacion"
        <td>Amonestación</td>
      % else:
        % tipo="sancion"
        <td>Sanción</td>
      % end     
        
      <td>{{r[0].Fecha}}</td>
      % if r[1]=="S":
        <td>{{r[0].Fecha_fin}}</td>
        <td>{{r[0].Sancion}}</td>
      %else:
        <td></td>
        <td></td>
      %end
      <td>{{r[0].Comentario}}</td>
      <td><a href="/alumnos/partes/{{info["alumno"][0].id}}/{{tipo}}/{{r[0].get_id()}}/del"><span class="glyphicon glyphicon-remove-sign" aria-hidden="true"></span></a></td>
      
      
    </tr>
    % end
    </table>

	
% include('footer.tpl',info=info)