# estadisticas.py

def mediaAritmetica(datos):
    
    media = 0
    
    for item in datos:
        media +=item[1]
    return media/len(datos)

def mediana(datos):
    
    valores = [item[1] for item in datos]
    valores.sort()
    if len(valores) % 2 != 0:
        return valores[len(valores) // 2]
    
    else:
        medio1 = len(valores) // 2 - 1
        medio2 = len(valores) // 2
        return (valores[medio1] + valores[medio2]) / 2


    
    
