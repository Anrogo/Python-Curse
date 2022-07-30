select concat(nombre,' ',apellido) as Nombre_Completo, email, concat(calle,' ',no_calle, ', ', pais) as Direccion 
from personas_persona p join personas_domicilio d on p.domicilio_id = d.id