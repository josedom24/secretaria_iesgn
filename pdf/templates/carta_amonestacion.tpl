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
{{!info["contenido"]}}
   
   
<body>

	
</body>
</html>