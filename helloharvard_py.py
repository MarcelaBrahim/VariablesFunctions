# -*- coding: utf-8 -*-
"""helloharvard.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sWnO0lQiuGYFnTaMHzDVfAqrvygmIqLk
"""





from google.colab import drive
drive.mount('/content/drive')



#variables, funciones, pseudocodigo
#print("Hello World")
# comentar many lines  with #each lines or the next
"""
....
"""

#ask user for their name

###name = input("Whats is your name? ")
#remove whitespace from str
#name = name.strip()
#return the same but without spaces

#capitalize user´s name mayuscula
#name = name.title()
#capitalizo mi cpodigo ahora, sin espacios y en mayuscula
#name = name.strip().title()

#capitalizo mas aun 
name = input("Whats is your name? ").strip().title()
#Say Hello to the users
#print('Hello, ' + name)
#print('Hello, ', name)
#print('Hello, ', end='')
#print('Hello, ', name, sep='')
#print('Hello, ', end='???')
#print('Hello, ', end='???')
#print(name)
#print('Hello, "Friend"')
#print('Hello, \'Friend\'')
#print('Hello, ', {name})

#split user's into first name and last name
#first, last = name.split('')
print(f'Hello, {name}')
#print(f'Hello, {first}')

#1+1

#print('hello, world')