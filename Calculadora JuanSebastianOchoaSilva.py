import tkinter as tk
from tkinter import ttk

def calculadora(num1, num2, operador):

	if operador == '+':
		  resultado = num1 + num2
	elif operador == '-':
		  resultado = num1 - num2
	elif operador == '*':
		  resultado = num1 * num2
	elif operador == '/':
		  resultado = round(num1 / num2, 2)
	elif operador == 'pow':
		  resultado = num1 ** num2

	return resultado

def click_calcular(label, num1, num2, operador):
	
	#Conversacion de valores
	valor1 = float(num1)
	valor2 = float(num2)

	#Calculo dados los valores y el operador
	res = calculadora(valor1, valor2, operador)

    #Actualizacion del texto en la etiqueta
	label.configure(text = 'Resultado: ' + str(res))

def init_window():

  window = tk.Tk() #crear la pantalla
  window.title('Mi primera aplicacion') #agregar titulo a la pantalla
  # Establecer el tamanno de la pantalla (ancho: 400px y largo: 250px)
  window.geometry('400x250')

  #crear una etiqueta con fuente Arial bold y tamanno 15
  label = tk.Label(window, text='Calculadora', font=('Arial bold', 15))
  #unicar la etiqueta en la columna y fila 0 de la pantalla
  label.grid(column = 0,row = 0)


  #Agregar dos campos de texto
  entrada1 = tk.Entry(window, width=10)
  entrada2 = tk.Entry(window, width=10)

  entrada1.grid(column = 1, row = 1)
  entrada2.grid(column = 1, row = 2)

  #Agregar dos etiquetas para indicarle al usuario los valores que debe ingresar
  label_entrada1 = tk.Label(window, text = 'Ingrese primer numero:', font=('Arial bold', 10))
  label_entrada1.grid(column = 0, row = 1)

  label_entrada2 = tk.Label(window, text = 'Ingrese segundo numero:', font=('Arial bold', 10))
  label_entrada2.grid(column = 0, row = 2)

  #Crear una etiqueta para el seleccionador (combobox)
  label_operador = tk.Label(window, text = 'Escoja un operador', font=('Arial bold', 10))
  label_operador.grid(column = 0, row = 3)

  #Crear un seleccionador (combobox)
  combo_operadores = ttk.Combobox(window)
  #Asignar los valores del seleccionador a traves de su atributo values
  combo_operadores['values'] = ['+', '-', '*', '/', 'pow']
  #Asignar por defecto una opcion seleccionada: 0 es el indice de los valores
  combo_operadores.current(0) #set the selected item
  #Ubicar el seleccionador
  combo_operadores.grid(column = 1,row =3)

  #agregar etiqueta para mostrar el resultado de la operacion en pantalla
  label_resultado = tk.Label(window, text='Resultado: ', font=('Arial bold', 15))
  label_resultado.grid(column = 0, row = 5)
  
  #Boton calcular
  boton = tk. Button( window, command = lambda: click_calcular(label_resultado, entrada1.get(), entrada2.get(),	combo_operadores.get()), text = 'Calcular',	bg = 'purple', fg = 'white')
  boton.grid(column = 1, row = 4)

  window.mainloop()

init_window()