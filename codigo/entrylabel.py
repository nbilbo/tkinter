# coding: utf-8
'''
Um Frame com um label e uma entrada de texto.
A classe oferece métodos p/ acessar o texto, e definir o texto.
Também é possível acessar os widgets de label e entry, se quiser aplicar algum estilo.
'''
from tkinter import Entry, Label, Frame


class Model(object):
	def __init__(self, label, text):
		self._label = label
		self._text = text

	def label(self):
		return self._label

	def text(self):
		return self._text

	def set_label(self, label):
		self._label = label

	def set_text(self, text):
		self._text = text

	def is_empty(self):
		'''
		Retorno
		-------
		bool : Se o text possui comprimento é igual a 0(zero).
		'''
		return len(self._text.strip()) == 0


class View(Frame):
	def __init__(self, master, controller, label, width, *args, **kwargs):
		super(View, self).__init__(master, *args, **kwargs)
		self._controller = controller
		self._create_label(label, width)
		self._create_entry()

	def label(self):
		'''
		Retorno
		-------
		tkinter.Label
		'''
		return self._label

	def entry(self):
		'''
		Retorno
		-------
		tkinter.Entry
		'''		
		return self._entry

	def _create_label(self, label, width):
		self._label = Label(self, text=label)
		self._label.bind('<Double-Button-1>', lambda event: \
								self._controller.focus_entry())

		if width:
			self._label.config(width=width)

		self._label.pack(side='left')

	def _create_entry(self):
		self._entry = Entry(self)
		self._entry.bind('<KeyRelease>', lambda event: \
			self._controller.update_text(self._entry.get()))

		self._entry.pack(side='left', fill='both', expand=True)


class Controller(object):
	def __init__(self, master, label, width):
		'''
		Parametros
		----------
		master : tkinter.Widget

		label : str

		width : int
			Se widget=None, label vai ter a largura do texto.
		'''
		self._model = Model(label=label, text='')
		self._view = View(master=master, controller=self, label=label, width=width)

	def view(self):
		'''
		Retorno
		-------
		tkinter.Frame
		'''
		return self._view

	def label(self):
		'''
		Retorno
		-------
		str : o texto que esta no label.
		'''
		return self._model.label()

	def text(self):
		'''
		Retorno
		-------
		str : o texto que esta no entry.
		'''
		return self._model.text()

	def w_entry(self):
		'''
		Retorno
		-------
		tkinter.Entry
		'''
		return self._view.entry()

	def w_label(self):
		'''
		Retorno
		-------
		tkinter.Label
		'''
		return self._view.label()

	def focus_entry(self):
		'''
		O entry vai ser focado.
		'''
		self._view.entry().focus()

	def update_text(self, text):
		'''
		Atualizar o valor do texto no modelo.

		Paramatros
		----------
		text : str
		'''
		self._model.set_text(text)

	def set_text(self, text):
		'''
		Definir o texto do entry.

		Parametros
		----------
		text : str
		'''
		self._model.set_text(text)
		self._view.entry().delete(0, 'end')
		self._view.entry().insert('end', text)

	def is_empty(self):
		'''
		Retorno
		-------
		bool : Se o texto do entry possui comprimento é igual a 0(zero).
		'''
		return self._model.is_empty()


def main():
	from tkinter import Tk,  Button


	root = Tk()
	root.title('Testes entrylabel')
	root.geometry('500x500+710+160')

	# instanciando .
	label_text = 'Name'
	label_width = 10

	controle = Controller(root, label_text, label_width)
	entrylabel = controle.view()
	entrylabel.pack(fill='x')

	# definindo um valor inicial ao entry.
	controle.set_text('Hello, Entry.')

	# obtendo o texto do entry.
	print(controle.text())

	# verificando se o entry esta vazio.
	is_empty = controle.is_empty()

	# obtendo os objetos entry e label.
	obj_entry = controle.w_entry()
	obj_label = controle.w_label()

	root.mainloop()

if __name__ == '__main__':
	main()


