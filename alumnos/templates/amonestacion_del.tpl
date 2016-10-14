% include('header.tpl',info=info)


 <h4>¿Estás seguro de eliminar la {{info["tipo"]}} con fecha {{info["datos"][0].Fecha}}?</h4>
 <form action={{info["url"]}} method="post" class="form-hotizontal">
        
                
        <button  name="respuesta" type="submit" value="s" class="btn btn-primary">Si</button>
        <button  name="respuesta" type="submit" value="n" class="btn btn-primary">No</button>
    </form>
    
	
% include('footer.tpl',info=info)