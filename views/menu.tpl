<br/>
<div class="center-block btn-group-vertical" role="group" aria-label="...">
    <p class="text-center"><strong>Bienvenid@ {{info["login"]}}</strong></p>
    <p class="text-center"><strong>Menú</strong></p>
    
    
 	<a class="btn btn-default" href="/alumnos" role="button">Alumnos</a>
  	% #if info["menu"]=="alumnos":
  	<a class="btn btn-default" href="/alumnos/amonestacion/resumen" role="button">Resumen de amonestaciones</a>
  	<a class="btn btn-default" href="/alumnos/sancion/resumen" role="button">Resumen de sanciones</a>
  	% #end
  	
  	<a class="btn btn-default" href="/logout" role="button">Desconectar</a>
</div>
