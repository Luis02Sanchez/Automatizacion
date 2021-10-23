import xml.etree.cElementTree as et

root = et.Element("Edificio_2_TI")

se = et.SubElement(root,"Especialidad_1_TI")
et.SubElement(se,"Matricula").text = "18040095"
et.SubElement(se,"Carrera").text = "Redes_Inteligentes_y_Ciberseguridad"
et.SubElement(se,"Nombre").text = "Luis_Angel_Sanchez_Ortiz"

et.SubElement(se,"Matricula").text = "18040096"
et.SubElement(se,"Carrera").text = "Redes_Inteligentes_y_Ciberseguridad"
et.SubElement(se,"Nombre").text = "Reyna_Argelia_Sanchez_Ortiz"

et.SubElement(se,"Matricula").text = "18040097"
et.SubElement(se,"Carrera").text = "Redes_Inteligentes_y_Ciberseguridad"
et.SubElement(se,"Nombre").text = "Irasu_Bellalit_Sanchez_Ortiz"

et.SubElement(se,"Matricula").text = "18040098"
et.SubElement(se,"Carrera").text = "Redes_Inteligentes_y_Ciberseguridad"
et.SubElement(se,"Nombre").text = "Cesareo_Duarte_Sanchez"

et.SubElement(se,"Matricula").text = "18040099"
et.SubElement(se,"Carrera").text = "Redes_Inteligentes_y_Ciberseguridad"
et.SubElement(se,"Nombre").text = "Celia_Ortiz_Perez"

et.SubElement(se,"Matricula").text = "18040100"
et.SubElement(se,"Carrera").text = "Redes_Inteligentes_y_Ciberseguridad"
et.SubElement(se,"Nombre").text = "Greisy_Bellalit_Muñoz_Sanchez"

se = et.SubElement(root,"Especialidad_2_TI")
et.SubElement(se,"Matricula").text = "18040075"
et.SubElement(se,"Carrera").text = "Entornos_Virtuales"
et.SubElement(se,"Nombre").text = "Karla_Berenice_Zamora_Mata"

et.SubElement(se,"Matricula").text = "1804076"
et.SubElement(se,"Carrera").text = "Entornos_Virtuales"
et.SubElement(se,"Nombre").text = "Eliud_Gloria_Ledezma"

et.SubElement(se,"Matricula").text = "18040077"
et.SubElement(se,"Carrera").text = "Entornos_Virtuales"
et.SubElement(se,"Nombre").text = "Cinthya_Carolina_Zavala_Rodriguez"

et.SubElement(se,"Matricula").text = "18040078"
et.SubElement(se,"Carrera").text = "Entornos_Virtuales"
et.SubElement(se,"Nombre").text = "Reyna_Cecilia_Suarez_Arguello"

et.SubElement(se,"Matricula").text = "18040079"
et.SubElement(se,"Carrera").text = "Etornos_Virtuales"
et.SubElement(se,"Nombre").text = "Jair_Maximo_Duran_Rodriguez"

se = et.SubElement(root,"Especialidad_3_TI")
et.SubElement(se,"Matricula").text = "1804085"
et.SubElement(se,"Carrera").text = "Desarrollo_Multiplataforma"
et.SubElement(se,"Nombre").text = "Adrana_Guadalupe_Hernandez_Ramirez"

et.SubElement(se,"Matricula").text = "18040086"
et.SubElement(se,"Carrera").text = "Desarrollo_Multiplataforma"
et.SubElement(se,"Nombre").text = "Isidro_Mendez_Jaramillo"

et.SubElement(se,"Matricula").text = "1804087"
et.SubElement(se,"Carrera").text = "Desarrollo_Multiplataforma"
et.SubElement(se,"Nombre").text = "Andrea_Gudalupe_Rojas_Lopez"

et.SubElement(se,"Matricula").text = "18040088"
et.SubElement(se,"Carrera").text = "Desarrollo_Multiplataforma"
et.SubElement(se,"Nombre").text = "Xochitl_Anahi_Ovalle_Macias"

et.SubElement(se,"Matricula").text = "1804089"
et.SubElement(se,"Carrera").text = "Desarrollo_Multiplataforma"
et.SubElement(se,"Nombre").text = "Nadia_Itzel_Villanueva_Cortes"

tree = et.ElementTree(root)
tree.write("Edificio_2_TI.xml", xml_declaration=True)
