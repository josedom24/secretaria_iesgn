% from gestiona import *

<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8">
   <style>
    @page {
        size: a4 portrait;
        @frame header_frame {           /* Static Frame */
            -pdf-frame-content: header_content;
            left: 50pt; width: 512pt; top: 20pt; height: 50pt;
            
        }
        @frame content_frame {          /* Content Frame */
            left: 50pt; width: 512pt; top: 90pt; height: 622pt;
        }
        @frame footer_frame {           /* Another static Frame */
            -pdf-frame-content: footer_content;
            left: 50pt; width: 512pt; top: 772pt; height: 20pt;
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
      % include ("header_footer.tpl")

 <h3>{{info["titulo"]}}</h3>
 <h4>Fecha: {{info["fecha"]}} - Curso: {{info["curso"]}}</h4>
 <table width="50%" border="0.2" cellspacing="0" cellpadding="4">
      <tr><td width="10%">N.</td><td>Nombre</td><td width="15%">A/S</td></tr>
    <% 
    cont=0
    for r in info["alumnos"]:
    cont=cont+1 %>
    <tr>
      <td width="10%">{{cont}}</td>
      <td>{{r.Nombre}}</td>
      <td width="15%">{{CountPartes("amonestacion",r.get_id())}}/{{CountPartes("sancion",r.get_id())}}</td>
      
      
    </tr>
    % end
    </table>

	
</body>
</html>