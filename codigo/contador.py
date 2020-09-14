#coding: utf-8

'''
Interface p/ mostrar os números gerados em um laço for.

'''


from tkinter import (Tk, Frame, Scrollbar, Scale, Label, Button, Listbox)


class Sliders(Frame):
    def __init__(self, parent,):
        super(Sliders, self).__init__(parent)
        self.create_begin()
        self.create_end()
        self.create_step()

    def create_begin(self):
        '''
        create begin slider.
        '''
        frame = Frame(self)
        label = Label(frame, text='Begin', width=10)
        self.slider_begin = Scale(frame, orient='horizontal', from_=-100, to=100, tickinterval=20)

        label.pack(side='left')
        self.slider_begin.pack(side='left', fill='x', expand=True)
        frame.pack(fill='both', expand=True)
    
    def create_end(self):
        '''
        create end slider.
        '''
        frame = Frame(self)
        label = Label(frame, text='End', width=10)
        self.slider_end = Scale(frame, orient='horizontal', from_=-100, to=100, tickinterval=20)

        label.pack(side='left')
        self.slider_end.pack(side='left', fill='x', expand=True)
        frame.pack(fill='both', expand=True, pady=0)

    def create_step(self):
        '''
        create step slider.
        '''
        frame = Frame(self)
        label = Label(frame, text='Step', width=10)
        self.slider_step = Scale(frame, orient='horizontal', from_=-100, to=100, tickinterval=20)
        self.slider_step.set(1)

        label.pack(side='left')
        self.slider_step.pack(side='left', fill='x', expand=True)
        frame.pack(fill='both', expand=True)

    def get_values(self):
        return [self.slider_begin.get(), self.slider_end.get(), self.slider_step.get()]


class Output(Frame):
    def __init__(self, parent, *args, **kwargs):
        super(Output, self).__init__(parent, *args, **kwargs)
        self.create_list()
        self.pack_propagate(False)
    
    def create_list(self):
        self.listbox = Listbox(self)
        scroll = Scrollbar(self, orient='vertical', command=self.listbox.yview)
        self.listbox.configure(yscrollcommand=scroll.set)

        self.listbox.pack(side='left', fill='both', expand=True)
        scroll.pack(side='left', fill='y')
      
    def insert(self, value):
        self.listbox.insert('end', str(value))
    
    def clear(self):
        self.listbox.delete(0, 'end')


class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.settings()
        self.create_sliders()
        self.create_output()
        
    def settings(self):
        '''
        set windows settings.
        '''
        self.geometry('630x300+0+100')
    
    def create_sliders(self):
        '''
        create the sliders and a button.
        '''
        frame = Frame(self)
        self.sliders = Sliders(frame)
        self.button = Button(frame, text='Calc', width=15, relief='raised', borderwidth=4)
        self.button['command'] = self.button_click

        self.sliders.pack(fill='both', expand=True)
        self.button.pack(padx=5, pady=5)
        frame.pack(side='left', fill='both', expand=True)
    
    def create_output(self):
        '''
        create frame with a listbox.
        '''
        self.output = Output(self, width=200)
        self.output.pack(side='left', fill='y',)
   
    def button_click(self):
        '''
        will execute a for loop to fill the listbox.
        '''
        begin, end, step = self.sliders.get_values()
        self.output.clear()

        for count in range(begin, end, step):
            self.output.insert(count)

    def execute(self):
        self.mainloop()
    

def main():
    window = Window()
    window.execute()

if __name__ == "__main__":
    main()
