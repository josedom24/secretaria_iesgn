% include('header.tpl',info=info)


 <h3>{{info["titulo"]}}</h3>
 <table>
                    <tr>
                      <th colspan="7" >
                        <a href="/alumnos/partes/{{info["tipo"]}}/resumen/{{info["prevano"]}}/{{info["prevmes"]}}" class="btn"><i class="glyphicon glyphicon-chevron-left"></i></a>
                        
                        <a href="/alumnos/partes/{{info["tipo"]}}/resumen/{{info["proxano"]}}/{{info["proxmes"]}}" class="btn"><i class="glyphicon glyphicon-chevron-right"></i></a>
                      </th>
                    </tr>
                    <tr>
  </table>
 {{!info["cal"]}}
	
% include('footer.tpl',info=info)