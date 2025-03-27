# Proyecto: [Clase 10 - Fundamentos de python]
# Estudiante: {[Luis Chacón]
# Fecha de Inicio: [2024/03/26]
# Fecha de Entrega: [dd/mm/aaaa]
# Descripción: Este archivo contiene el punto de entrada principal del proyecto.
# Recuerda incluir tu nombre completo, la fecha en la que iniciaste el proyecto y la fecha estimada de entrega.
# Esto ayuda a mantener un registro claro del trabajo realizado.


#from analisis_datos.carga_datos import generar_lista_compras
#from analisis_datos.estadisticas import mediaAritmetica, mediana
from analisis_datos import *

lista_compra = generar_lista_compras()
print(lista_compra)

print(f"La media es {mediaAritmetica(lista_compra)}")
print(f"La mediana es {mediana(lista_compra)}")
