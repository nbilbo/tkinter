
from os.path import dirname, realpath, join
from datetime import date
from tkinter import (Tk, Frame, Button, Label, Spinbox, font, PhotoImage)


CURRENT_DIR = dirname(realpath(__file__))
CALC_PNG = join(CURRENT_DIR, 'imgs', 'calc.png')
USER_PNG = join(CURRENT_DIR, 'imgs', 'user.png')


def get_formated_date():
	current = date.today()
	#formated_date = '{}/{}/{}'.format(current.day, current.month, current.year)
	formated_date = current.strftime('%d/%m/%Y')
	return formated_date

def get_current_year():
	return date.today().year

class Program(Tk):
	BACKGROUND = '#fff'
	def __init__(self, *args, **kwargs):
		super(Program, self).__init__(*args, **kwargs)
		
		self.option_add('*Font', 'Georgia 14 normal')
		self.create_current_date_field()
		self.create_input_birth()
		self.create_button()
		self.create_output_result()
		self.settings()

	def settings(self):
		self.title('Calcular idade')
		self.geometry('550x380+0+0')
		self['background'] = self.BACKGROUND


	def execute(self):
		self.mainloop()

	def create_current_date_field(self):
		label = Label(self, background=self.BACKGROUND)
		label['text'] = get_formated_date()
		
		label.pack(side='top', padx=5, pady=5, anchor='nw')
		
	def create_input_birth(self):
		#creating frames
		main_frame = Frame(self, background=self.BACKGROUND)
		left_frame = Frame(main_frame, background=self.BACKGROUND)
		right_frame = Frame(main_frame, background=self.BACKGROUND)

		#widgets for left_frame
		label = Label(left_frame, text='Ano de nascimento', background=self.BACKGROUND)
		self.input_birth = Spinbox(left_frame, from_=0, to=9999)

		#widgets for right_frame
		img = PhotoImage(file=USER_PNG)
		label_img = Label(right_frame, image=img)
		label_img.img = img

		#packing
		label.pack(side='left', anchor='sw')
		self.input_birth.pack(side='left', anchor='sw')

		label_img.pack(side='bottom', anchor='s')

		left_frame.pack(side='left', fill='both', expand=True)
		right_frame.pack(side='left', fill='both', expand=True)
		main_frame.pack(fill='both', expand=True, padx=5, pady=5)

		left_frame.pack_propagate(False)
		right_frame.pack_propagate(False)
		main_frame.pack_propagate(False)

	def create_button(self):
		img = PhotoImage(file=CALC_PNG)

		button = Button(self, text='Calcular', image=img, compound='left')
		button.image = img
		button['background'] = '#eee'
		button['relief'] = 'raised'
		button['borderwidth'] = 4
		button['command'] = self.button_click

		button.pack(fill='x', expand=False, padx=5, pady=5)

	def create_output_result(self):
		self.output_result = Label(self, text='Resultado', background=self.BACKGROUND)
		self.output_result.pack(padx=5, pady=5)

	def button_click(self):
		user_input = self.input_birth.get()
		years_old = get_current_year() - int(user_input)
		self.output_result['text'] = f'{years_old} anos de idade.'


def main():
	program = Program()
	program.execute()
	pass

if __name__ == '__main__':
	main()

