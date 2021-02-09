from tkinter import Frame, Spinbox, Scale
from tkinter.ttk import Label as LabelTtk


class Model(object):
    def __init__(self, minimum, maximum, current):
        self._minimum = minimum
        self._maximum = maximum
        self._current = current
    
    def minimum(self):
        return self._minimum

    def maximum(self):
        return self._maximum

    def current(self):
        return self._current

    def set_minimum(self, minimum):
        self._minimum = minimum
    
    def set_maximum(self, maximum):
        self._maximum = maximum
    
    def set_current(self, current):
        self._current = current


class View(Frame):
    def __init__(self, master, controller, label, width, 
            minimum, maximum, current, *args, **kwargs):
        super(View, self).__init__(master, *args, **kwargs)
        self._controller = controller
        self._create_label(label, width)
        self._create_spinbox(minimum, maximum)
        self._create_scale(minimum, maximum)
    
    def w_label(self):
        return self._label
    
    def w_spinbox(self):
        return self._spinbox

    def w_scale(self):
        return self._scale
    
    def _create_label(self, label, width):
        self._label = LabelTtk(self, text=label)
        
        if width:
            self._label.config(width=width)
            
        self._label.pack(side='left', anchor='s')
    
    def _create_spinbox(self, minimum, maximum):
        self._spinbox = Spinbox(self, from_=minimum, to=maximum)

        self._spinbox['command'] = lambda: \
            self._controller.set_current(int(self._spinbox.get()))
        
        self._spinbox.bind('<Return>', lambda e: \
            self._controller.set_current(self._spinbox.get()))
                
        self._spinbox.pack(side="left", anchor="s")        
    
    def _create_scale(self, minimum, maximum):
        self._scale = Scale(self, orient="horizontal", 
                            from_=minimum, to=maximum)
        
        self._scale['command'] = lambda e: \
            self._controller.set_current(self._scale.get())
            
        self._scale.pack(side="left", fill="x", expand=True, anchor="s")   


class Controller(object):
    def __init__(self, master, label, width, minimum, maximum, current):
        self._model = Model(minimum, maximum, current)
        self._view = View(master, self, label, width, minimum, maximum, current)
    
    def view(self):
        '''
        retorno
        -------
        tkinter.Frame
        '''        
        return self._view

    def current(self):
        '''
        retorno
        -------
        int
        '''        
        return self._model.current()

    def minimum(self):
        '''
        retorno
        -------
        int
        '''        
        return self._model.minimum()
    
    def maximum(self):
        '''
        retorno
        -------
        int
        '''
        return self._model.maximum()
         
    def set_current(self, current):
        '''
        Definir o valor atual.
        
        parametros
        ----------
        current : int
        '''
        minimum = self._model.minimum()
        maximum = self._model.maximum()
        
        # caractere númerico é convertido em inteiro.
        if isinstance(current, str) and current.isdigit():
            current = int(current)

        # caractere não númerico convertido em inteiro.
        if not isinstance(current, int):
            current = self._model.current()
        
        # current fora do range.
        if current not in range(minimum, maximum):
            current = self._model.current()
            
        self._model.set_current(current)
        self._view.w_spinbox().delete(0, 'end')
        self._view.w_spinbox().insert('end', str(current))
        self._view.w_scale().set(current)


def main():
    from tkinter import Tk
    
    
    root = Tk()
    root.geometry('500x500+355+90')
    
    # instanciando
    maximum = 797_554
    minimum = current = 0
    label = 'Ponts'
    width = 10
    
    controller = Controller(root, label, width, minimum, maximum, current)    
    slider = controller.view()
    slider.pack(fill='x')
    
    # valor inicial
    controller.set_current(20)
    
    # obter o valor
    current = controller.current()
    print(current)
    
    root.mainloop()

if __name__ == '__main__':
    main()
