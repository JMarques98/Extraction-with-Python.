#!/usr/bin/env python
# coding: utf-8

# In[127]:


import os
#Module os to access Operating System functionalities, access directories, read and write files.
import os.path
#os submodule, to access functionalities related to file and directory path names.
from PyPDF2 import PdfFileReader, PdfFileWriter
# PyPDF2 is a library for working with PDF documents.
#PdfFileReader class of PyPDF2 to get pdf content

os.getcwd()
#Returns a string representing the current working directory 

losarchivos = []
#The list where we are going to put the files is created and declared.

for file in os.listdir("."):
    #All folders and files on the desktop are listed and we go through them one by one.
    if file.lower().endswith('.pdf'):
        #We tell you that if you find a file ending with the extension .pdf, add the name to the list of "losarchivos".
        losarchivos.append(file)

for i in range(len(losarchivos)):
    
    #We run through the length of the list and extract the text from each file.
    
    valor = str(losarchivos[i])
    pdf = PdfFileReader(valor)

    number_of_pages = pdf.getNumPages()

        
    print('El número de páginas de' + ' ' + valor + ' ' + 'es' + ' ' + str(number_of_pages))
    
    #we print by screen the number of pages detected in each file
    
    i = 0
    
    while i < number_of_pages:
        page = pdf.getPage(i)
        print(page.extractText())
        i = i + 1
       


