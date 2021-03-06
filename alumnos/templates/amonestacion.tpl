% include('header.tpl',info=info)

 <h3>Amonestación</h3>
 <h4>{{info["alumno"].Nombre+"-"+ info["alumno"].Unidad.Curso}}</h4>
 <form action="/alumnos/partes/amonestacion/new" method="post">

  <div class="form-group">
    <label>Fecha:</label>
       <input type="text" value="{{info["dia"]}}" class="form-control" id="fecha" name="Fecha" pattern="\d{1,2}/\d{1,2}/\d{4}" required autofocus>
  </div>

  <div class="form-group">
    <label>Comentario:</label>
    <textarea class="form-control" id="comentario" rows="5" name="Comentario"></textarea>
  </div>

  <div class="form-group">
    <label>Profesor:</label>
    <select class="form-control" name="Profesor">
      % for p in info["profesor"]:

           <option value="{{p.get_id()}}">{{p.Nombre+" "+p.Apellidos}}</option>
      % end
    </select>
  </div>



  <div class="form-group">
    <label>Hora:</label>
    <select class="form-control" name="Hora">
      <option value="1">Primera</option>
      <option value="2">Segunda</option>
      <option value="3">Tercera</option>
      <option value="4">Recreo</option>
      <option value="5">Cuarta</option>
      <option value="6">Quinta</option>
      <option value="7">Sexta</option>
      
    </select>
  </div>
  
  <button type="submit" class="btn btn-primary">Aceptar</button>
  <input type="hidden" name="IdAlumno" value="{{info["id"]}}"/>
</form>


	
% include('footer.tpl',info=info)

