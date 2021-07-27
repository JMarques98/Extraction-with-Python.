#!/usr/bin/env python
# coding: utf-8

# In[127]:


import os
#Modulo os para acceder a funcionalidades del Sistema Operativo,acceder a directorios,leer y escribir arhivos.
import os.path
#Submodulo de os, para acceder a funcionalidades relacionadas con los nombres de las rutas de archivos y directorios.
from PyPDF2 import PdfFileReader, PdfFileWriter
# PyPDF2 es una libreria para trabajar con documentos PDF
#PdfFileReader clase de PyPDF2 para obtener contenido del pdf

os.getcwd()
#Devuelve una cadena que representa el directorio de trabajo actual 

losarchivos = []
#Se crea y se declara la lista donde vamos a meter los archivos

for file in os.listdir("."):
    #Se listan todas las carpetas y archivos que tenemos en el escritorio y recorremos una por una
    if file.lower().endswith('.pdf'):
        #Le decimos que si encuentra un archivo que termine con la extensión .pdf, añada el nombre a la lista de "losarchivos"
        losarchivos.append(file)

for i in range(len(losarchivos)):
    
    #Recorremos la longitud de la lista y vamos extrayendo el texto de cada archivo
    
    valor = str(losarchivos[i])
    pdf = PdfFileReader(valor)

    number_of_pages = pdf.getNumPages()

        
    print('El número de páginas de' + ' ' + valor + ' ' + 'es' + ' ' + str(number_of_pages))
    
    #imprimimos por pantalla el número de paginas que se detecta en cada archivo
    
    i = 0
    
    while i < number_of_pages:
        page = pdf.getPage(i)
        print(page.extractText())
        i = i + 1
       


# In[ ]:




