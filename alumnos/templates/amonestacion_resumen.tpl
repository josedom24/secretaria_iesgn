% include('header.tpl',info=info)


 <h3>Resumen de amonestaciones</h3>
 <table>
                    <tr>
                      <th colspan="7" >
                        <a href="/alumnos/amonestacion/resumen/{{info["prevano"]}}/{{info["prevmes"]}}" class="btn"><i class="glyphicon glyphicon-chevron-left"></i></a>
                        
                        <a href="/alumnos/amonestacion/resumen/{{info["proxano"]}}/{{info["proxmes"]}}" class="btn"><i class="glyphicon glyphicon-chevron-right"></i></a>
                      </th>
                    </tr>
                    <tr>
  </table>
 {{!info["cal"]}}
	
% include('footer.tpl',info=info)