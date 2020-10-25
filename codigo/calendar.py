# coding: utf-8


# imports
from tkinter import Frame, Spinbox


# constants
LABEL_WIDTH = 20


class CustomSpinbox(Frame):
    def __init__(self, master, *args, label="", minimum=0, maximum=9999, **kwargs):
        super(CustomSpinbox, self).__init__(master, *args, **kwargs)
        self.minimum = minimum
        self.maximum = maximum if maximum > minimum else minimum+1
        self.create_spinbox(label)
        self.register_filter()
        
    def create_spinbox(self, label):
        from tkinter import Label
        
        self.label = Label(self, text=label, width=LABEL_WIDTH)
        self.spinbox = Spinbox(self, from_=self.minimum, to=self.maximum)
        
        self.label.pack(side="left")
        self.spinbox.pack(side="left", fill="x", expand=True)
    
    def register_filter(self):
        tk = self.get_instance_tk(self)
        if tk:
            new_register = tk.register(self.filter_spinbox)
            self.spinbox.config(validate="key", validatecommand=(new_register, "%P"))
    
    def filter_spinbox(self, value):
        if value.isdigit() and int(value) in range(self.minimum, self.maximum+1):
            return True
        if value == "":
            return True
        return False
    
    def get_instance_tk(self, widget):
        from tkinter import Tk
        
        if isinstance(widget, Tk):
            return widget
        else:
            master=self.get_instance_tk(widget.master)
            return master
    
    def set_label(self, label):
        self.label.config(text=label)
    
    def get_value(self):
        return int(self.spinbox.get())
    
    def set_value(self, value):
        if value in range(self.minimum, self.maximum+1):
            self.spinbox.delete(0, "end")
            self.spinbox.insert("end", str(value))
        
        
class MonthOptionMenu(Frame):
    langs = {"eng":["January", "February", "March", "April", "May",
                    "June", "July", "August", "September", "October",
                    "November", "December"],
                    
             "pt-br":["Janeiro", "Fevereiro", "Março", "Abril", "Maio",
                      "Junho", "Julho", "Agosto", "Setembro", "Outubro",
                      "Novembro", "Dezembro"]}   
                
    def __init__(self, master, *args, lang="eng", **kwargs):
        super(MonthOptionMenu, self).__init__(master, *args, **kwargs)
        self.create_optionmenu()
        self.lang = lang
        self.set_lang(self.lang)
        
    def create_optionmenu(self):
        from tkinter import StringVar, IntVar, OptionMenu, Label
        
        self.label = Label(self, text="Month", width=LABEL_WIDTH)
        self.string_optionmenu = StringVar() 
        self.optionmenu = OptionMenu(self, self.string_optionmenu, [])
        
        self.label.pack(side="left")
        self.optionmenu.pack(side="left", fill="x", expand=True)
    
    def set_lang(self, lang):
        if lang in self.langs:
            self.lang = lang
            values = self.langs[lang]
            self.optionmenu.children["menu"].delete(0, "end")
            self.string_optionmenu.set(values[0])
            for value in values:
                self.optionmenu.children["menu"].add_command(label=value,
                command=lambda string=value: self.string_optionmenu.set(string))
            
    def set_value(self, value):
        if isinstance(value, int) and 0 < value <= len(self.langs[self.lang]):
            month = self.langs[self.lang][value-1]
            self.string_optionmenu.set(month)
        
        elif isinstance(value, str) and value.isdigit():
            self.set_value(int(value))
    
    def get_value(self):
        return list(self.langs[self.lang]).index(self.string_optionmenu.get())+1
    
    def set_label(self, label):
        self.label.config(text=label)
    
    
class Calendar(Frame):
    langs = {"eng":["day", "month", "year"],
             "pt-br":["dia", "mês", "ano"]}
    
    def __init__(self, master, *args, lang="eng", **kwargs):
        super(Calendar, self).__init__(master, *args, **kwargs)
        self.lang = lang
        self.create_inputs()
        self.set_lang(lang)
        self.set_value()
        
    def create_inputs(self):
        self.input_day = CustomSpinbox(self, label="Day", minimum=1, maximum=31)
        self.input_month = MonthOptionMenu(self)
        self.input_year = CustomSpinbox(self, label="Year", minimum=1, maximum=9999)
        
        self.input_day.pack(fill="x", pady=5)
        self.input_month.pack(fill="x", pady=5)
        self.input_year.pack(fill="x", pady=5)
    
    def set_lang(self, lang):
        if lang in self.langs:
            self.lang = lang
            values = self.langs[lang]
            self.input_day.set_label(values[0])
            self.input_month.set_label(values[1])
            self.input_month.set_lang(lang)
            self.input_year.set_label(values[2])
        else:
            print("LangErro, langs available:", end="")
            print([lang for lang in self.langs])
            print("\n")
    
    def set_value(self, value=None):
        from datetime import datetime
        
        value = value or datetime.now()
        if isinstance(value, datetime):
            self.input_day.set_value(value.day)
            self.input_month.set_value(value.month)
            self.input_year.set_value(value.year)
        
    def get_value(self):
        day = self.input_day.get_value()
        month = self.input_month.get_value()
        year = self.input_year.get_value()
        return datetime(year, month, day)


if __name__ == "__main__":
    from datetime import datetime
    from tkinter import Tk
    
    root = Tk()
    # creating a calendar
    calendar = Calendar(root, lang="eng")
    calendar.pack(fill="both", padx=5, pady=15)
    # set_value only works if u pass a datetime.datetime
    calendar.set_value(datetime(2021, 1, 10))
    # get_value return a datetime
    print(calendar.get_value())
    
    calendar_two = Calendar(root)
    calendar_two.set_lang("pt-br")
    calendar_two.pack(fill="both", padx=5, pady=15)
    root.mainloop()

