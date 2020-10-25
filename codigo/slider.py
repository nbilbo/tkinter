from tkinter import Frame


class Slider(Frame):
    def __init__(self, master, *args, minimum=0, maximum=100, **kwargs):
        super(Slider, self).__init__(master, *args, **kwargs)
        self.minimum = minimum
        self.maximum = maximum if maximum > minimum else minimum+1
        
        self.create_spinbox()
        self.create_scale()
        self.create_binds()
    
    def create_spinbox(self):
        from tkinter import Spinbox
        
        self.spinbox = Spinbox(self, from_=self.minimum, to=self.maximum)
        self.spinbox.pack(side="left", anchor="s")
    
    def create_scale(self):
        from tkinter import Scale
        
        self.scale = Scale(self, orient="horizontal", 
                            from_=self.minimum, to=self.maximum)
        self.scale.pack(side="left", fill="x", expand=True, anchor="s")
    
    def create_binds(self):
        self.spinbox["command"] = self.update_scale
        self.scale["command"] = self.update_spinbox
    
    def update_spinbox(self, *args):
        new_value = str(self.scale.get())
        self.spinbox.delete(0, "end")
        self.spinbox.insert("end", new_value)
    
    def update_scale(self, *args):
        new_value = self.spinbox.get()
        if new_value.isdigit():
            self.scale.set(int(new_value))
    
    def set_value(self, value):
        if isinstance(value, str) and value.isdigit():
            value = int(value)
        
        if isinstance(value, int) and value in range(self.minimum, self.maximum+1): 
            self.scale.set(value)
            
    def get_value(self):
        return self.scale.get()
  

if __name__ == "__main__":
    from tkinter import Tk
    
    root = Tk()
  
    slider1 = Slider(root)
    slider1.pack(fill="x", padx=5, pady=5)
    slider1.set_value(55)
    
    slider2 = Slider(root, minimum=155, maximum=322)
    slider2.pack(fill="x", padx=5, pady=5)
    print(slider2.get_value())
    
    root.mainloop()

