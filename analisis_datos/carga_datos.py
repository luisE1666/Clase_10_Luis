#En este módulo se crra la lista de compras de la canasta básica
import random
def generar_lista_compras():
    canastaBasica = { "Arroz": 1800, "Azucar": 2200,
                     "Harina": 1200, "Tomate": 2500,
                     "Frijoles": 1400, "Papas": 3000,
                     "Leche": 1000, "Cerveza": 1000,
                     "Cafe": 5000, "Fideos": 800,
                     "Jabon":1500, "Huevos": 3500,
                     "Naranjas": 2500, "Sal": 800}
    
    seleccion = random.sample(list(canastaBasica.items()),k = 5)
    return seleccion
   


                           
