% include('header.tpl',info=info)

 <h3>Amonestación</h3>
 <form>

  <div class="form-group">
    <label>Fecha</label>
       <input type="text" value="{{info["dia"]}}" class="form-control" id="fecha" name="fecha" pattern="\d{1,2}/\d{1,2}/\d{4}" required autofocus>
  </div>

  <div class="form-group">
    <label>Comentario:</label>
    <textarea class="form-control" id="comentario" rows="5" name="comentario"></textarea>
  </div>

  <div class="form-group">
    <label>Profesor:</label>
    <select class="form-control" name="profesor">
      % for p in info["profesor"]:

           <option value="{{p.get_id()}}">{{p.Nombre+" "+p.Apellidos}}</option>
      % end
    </select>
  </div>



  <div class="form-group">
    <label>Hora:</label>
    <select class="form-control" id="exampleSelect1">
      <option value="1">Primera</option>
      <option value="2">Segunda</option>
      <option value="3">Tercera</option>
      <option value="4">Cuarta</option>
      <option value="5">Quinta</option>
      <option value="6">Sexta</option>
      
    </select>
  </div>
  
  <button type="submit" class="btn btn-primary">Submit</button>
</form>


	
% include('footer.tpl',info=info)

