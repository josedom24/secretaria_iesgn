% include('header.tpl',info=info)

 <h3>Modificación</h3>
 <h4>{{info["alum"][0].Nombre+"-"+ info["alum"][0].Unidad.Curso}}</h4>
 <form action={{info["url"]}}} method="post">
  <div class="form-group">
            <label>Curso:</label>
            
                <select name="Unidad" class="form-control">
                % for c in info["cursos"]:
                % if info["alum"][0].Unidad.id==c.get_id():
                  <option selected="selected" value="{{c.get_id()}}">{{c.Curso}}</option>
                % curso=c.Curso
                % else:
                    <option value="{{c.get_id()}}">{{c.Curso}}</option>
                % end
                % end
                </select>
            
        </div>
  % titulos=["Nombre","DNI","Dirección","Código Postal","Localidad","Fecha de nacimiento","Provincia","Nombre del tutor","Apellido 1 tutor","Apellido 2 tutor","Telefono1","Telefono2"]
  % campos=["Nombre","DNI","Direccion","CodPostal","Localidad","Fecha_nacimiento","Provincia","Nomtutor","Ap1tutor","Ap2tutor","Telefono1","Telefono2"]

  % for t,c in zip(titulos,campos):
  <div class="form-group">
    <label>{{t}}:</label>
        % valor=getattr(info["alum"][0],c) if getattr(info["alum"][0],c)!=None else ""
       <input type="text" value="{{valor}}" class="form-control" name="{{c}}"/>
  </div>
  % #pattern="\d{1,2}/\d{1,2}/\d{4}"
  %end
  <div class="form-group">
    <label>Observaciones:</label>
    <textarea class="form-control" id="comentario" rows="5" name="Obs"></textarea>
  </div>

  
  <button type="submit" class="btn btn-primary">Aceptar</button>
  
</form>


	
% include('footer.tpl',info=info)

