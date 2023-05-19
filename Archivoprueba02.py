contador=0
while(contador<=10):
    print(f"el contador esta en {contador}")
    contador+=1
#    if contador >6:
 #       break

    """
    este es 
    un bloque de
    codigo
    comentado
    """

    #Comentario por defecto, Explicacion
    #! Comentario con bettercommment ROJO --> IMPORTANTE
    #? Comentario con bettercomment AZUL --> Instruccion
    #// Comentario con bettercomment Gris  --> Codigo Borrado/cambiado
    #* Comentario con bettercomment --> Explicacion
    #todo Comentario con bettercomment Naranja --> Otros



import pandas as pd
import matplotlib.pyplot as plt
datos = pd.DataFrame({"manzanas": [3, 2], "peras": [4, 1]}, index=["juan", "pablo"])
datos
datos.plot.bar()
plt.show()




paises = {"Peru": 100, "Argentina": 200, 
          "Ecuador": 160}
print(paises)


import pandas as pd
from urllib.parse import quote
from IPython.display import display

url = 'https://es.wikipedia.org/wiki/Copa_Mundial_de_Fútbol_de_2022'
url_encoded = quote(url, safe=':/')

tablas = pd.read_html(url_encoded)
tabla_corregida = tablas[9]

display(tabla_corregida)

