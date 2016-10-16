% from gestiona import *

<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8">
   <style>
    @page {
        size: a4 landscape;
        @frame header_frame {           /* Static Frame */
            -pdf-frame-content: header_content;
            left: 50pt; width: 700pt; top: 20pt; height: 50pt;
            
            
        }
        @frame content_frame {          /* Content Frame */
            left: 50pt; width: 700pt; top: 90pt; height: 470pt;
            
        }
        @frame footer_frame {           /* Another static Frame */
            -pdf-frame-content: footer_content;
            left: 50pt; width: 700pt; top: 572pt; height: 20pt;
            
        }

    }
    
    #header_content p
    {
      font-size: 65%;
      margin-bottom: 0px;
      margin-top: 0 px;
      
    }
    #header_content h3
    {
      font-size: 85%;
      margin-bottom: 5px;
      margin-top: 2px;
    }
    
    </style>
</head>


   
<body>
      
<div id="header_content">
      <table cellspacing="0" cellpadding="4" width="50%">
        <tr>
          <td width="25%"><img width="50%"  alt="" src="https://secretaria-iesgn.rhcloud.com/img/contraportada.jpg" /></td>
          <td>
      <h3>IES Gonzalo Nazareno</h3>
      <p>C/Las Botijas,10</p>
      <p>41710 - Dos Hermanas (Sevilla)</p>
      <p>Tfno: 955839911 - Fax: 955839915</p>
    </td>
  </table>
    </div>
 <div id="footer_content"><pdf:pagenumber> / <pdf:pagecount>
    </div>
 <h3>{{info["titulo"]}}</h3>
 <h4>Fecha: {{info["fecha"]}}</h4>

 <table border="0.2" cellspacing="0" cellpadding="4">
      <tr><td>N.</td><td>Alumno</td><td>Curso</td><td>Sanción</td><td>Fecha</td><td>Fecha fin.</td></tr>
    <% 
    cont=0
    for r in info["alumnos"]:
    cont=cont+1 %>
    <tr>
      <td width="10%">{{cont}}</td>
      <td>{{r.IdAlumno.Nombre}}</td>
      <td width="15%">{{r.IdAlumno.Unidad.Curso}}</td>
      <td>{{r.Sancion}}</td>
      <td width="15%">{{r.Fecha}}</td>
      <td width="15%">{{r.Fecha_fin}}</td>
      
      
    </tr>
    % end
    </table>

	
</body>
</html>