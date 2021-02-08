# coding: utf-8
'''
Um menu onde é possivel definir as opções e obter a opção atual.
Tabém é possível atualizar os valores sempre que quiser.
'''
from tkinter import OptionMenu, Frame, StringVar


# model
class Model(object):
	def __init__(self, options):
		self._options = options
		self._current = options[0]
		
	def options(self):
		return self._options

	def current(self):
		return self._current

	def set_options(self, options):
		self._options = options

	def set_current(self, current):
		self._current= current


# view
class View(Frame):
	def __init__(self, master, options, *args, **kwargs):
		super(View, self).__init__(master, *args, **kwargs)
		self._menuvar = StringVar()
		self._create_dropdown(self._menuvar, options)

	def menuvar(self):
		return self._menuvar

	def dropdown(self):
		'''
		retorno
		-------
		tkinter.OptionMenu
		'''
		return self._dropdown

	def show_option(self, option):
		'''
		Mostrar uma opção no dropdown.

		parametros
		----------
		option : str
		'''
		self._menuvar.set(option)

	def show_options(self, options):
		'''
		Atualiza as opções disponivies no menu.

		parametros
		----------
		options : list
		'''
		menu = self._dropdown['menu']
		menu.delete(0, 'end')

		for option in options:
			menu.add_command(label=option, command=lambda opt=option: \
												self._menuvar.set(opt))

	def _create_dropdown(self, stringvar, options):
		self._dropdown = OptionMenu(self, stringvar, *options)
		self._dropdown.pack(fill='both', expand=True)


# controller
class Controller(object):
	def __init__(self, master, options):
		'''
		parametros
		----------
		master : tkinter.Widget

		options : list
		'''
		self._model = Model(options)
		self._view = View(master, options)

	def view(self):
		'''
		retorno
		-------
		tkinter.Frame
		'''
		return self._view

	def w_dropdown(self):
		'''
		retorno
		-------
		tkinter.OptionMenu
		'''
		return self._view.dropdown()

	def current(self):
		'''
		retorno
		-------
		str : A opção atualemente selecionada no dropdown.
		'''
		current = self._view.menuvar().get()
		self._model.set_current(current)

		return current

	def options(self):
		'''
		retorno
		-------
		list : Lista com todas as opções do dropdown.
		'''
		return self._model.options()

	def set_current(self, current):
		'''
		Definir a opção que ficara selecionado no dropdown.

		parametros
		----------
		current ; str
		'''
		self._model.set_current(current)
		self._view.show_option(current)

	def set_options(self, options):
		'''
		Atualizar as opções do dropdwon.

		parametros
		----------
		options : list
		'''
		self._model.set_options(options)
		self._view.show_options(options)
		self.set_current(options[0])


def main():
	from tkinter import Tk, Button


	root = Tk()
	root.title('Teste DropDown')
	root.geometry('500x500+710+180')

	# instanciando
	options = ['apple', 'potato', 'orange']
	controle = Controller(root, options)
	dropdown = controle.view()
	dropdown.pack(fill='x')

	# alterando as opcoes
	others = ['book', 'notebook', 'facebook']
	controle.set_options(others)

	# definindo a opcao atual
	controle.set_current('door')

	# obtendo o objeto dropdown
	obj_dropdown = controle.w_dropdown()

	# obtendo a opção atualemente selecionada.
	print(controle.current())

	btn = Button(root, text='click')
	btn['command'] = lambda: print(controle.current())
	btn.pack()


	root.mainloop()

if __name__ == '__main__':
	main()
