<br/>
<div class="center-block btn-group-vertical" role="group" aria-label="...">
    <p class="text-center"><strong>Bienvenid@ {{info["login"]}}</strong></p>
    <p class="text-center"><strong>Menú</strong></p>
    
    
 	<a class="btn btn-default" href="/alumnos" role="button">Alumnos</a>
  	
  	% if info.has_key("menu") and info["menu"]=="alumnos":
  	<a class="btn btn-default" href="/alumnos/partes/amonestacion/resumen" role="button">Resumen de amonestaciones</a>
  	<a class="btn btn-default" href="/alumnos/partes/sancion/resumen" role="button">Resumen de sanciones</a>
  	<a class="btn btn-default" href="/pdf/alumnos/partes/{{info["curso"]}}" role="button">Imprimir</a>
  	% end

  	% if info.has_key("menu") and info["menu"]=="amonestacion":
  	
  	<a class="btn btn-default" href="/pdf/alumnos/resumen/{{info["tipo"]}}/{{info["fecha"]}}" role="button">Imprimir resumen</a>
  	<a class="btn btn-default" href="/pdf/alumnos/resumen/cartas/{{info["tipo"]}}/{{info["fecha"]}}" role="button">Imprimir cartas</a>
  	% end

    % if info.has_key("menu") and info["menu"]=="sancion":
    
    <a class="btn btn-default" href="/pdf/alumnos/resumen/{{info["tipo"]}}/{{info["fecha"]}}" role="button">Imprimir resumen</a>
    
    % end
  	<a class="btn btn-default" href="/profesores" role="button">Profesores</a>
  	<a class="btn btn-default" href="/logout" role="button">Desconectar</a>
</div>
