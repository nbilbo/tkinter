try:
    from tkinter import Tk, Frame, Label, Scrollbar, Canvas
    from tkinter.ttk import Style, Label as ttkLabel, Entry as ttkEntry, Treeview
    print("python 3x")

except ImportError:
    from Tkinter import Tk, Frame, Label, Scrollbar, Canvas
    from ttk import Style, Label as ttkLabel, Entry as ttkEntry, Treeview
    print("python 2x")


#---------------------------- FrameEntry ---------------------
class FrameEntry(Frame):
    def __init__(self, parent, text = "L", **kwargs):
        Frame.__init__(self, parent, **kwargs)
        
        #estilo
        style = Style()
        style.configure("TLabel", font = (None, 12, "bold"))
        
        #criando os widgets
        self.label = ttkLabel(self, text = text)
        self.entry = ttkEntry(self, font = (None, 12, "bold"))
        
        #posicioanando
        self.label.pack(side = "left", padx = 1, pady = 1)
        self.entry.pack(side = "left", fill = "x", expand = True)
        
        #comandos
        self.label.bind("<Button-1>", lambda event: self.entry.focus())
    
    def setColorLabel(self, background = "#ffffff", foreground = "#000000"):
        self.label.configure(background = background, foreground = foreground)
    
    def setColorEntry(self, background = "#ffffff", foreground = "#000000"):
        self.entry.configure(background = background, foreground = foreground)
        
    def posicionar(self):
        self.pack(side = "top", fill = "x", padx = 5, pady = 5)
        
        
#---------------- TreeWithScroll -----------------------------
class TreeWithScroll(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        
        #largura do scroll
        self.widthScrollY = 16
        self.heightScrollX = 16
        
        #estilo
        self.configure(
        background = "blue"
        )
        
        #criando os widgets
        self.createTree()
        self.createScrollX()
        self.createScrollY()
        
        #configurando o scroll
        self.configureScroll()
        
    def createTree(self):
        self.tree = Treeview(self)
    
    def createScrollX(self):
        self.frameX = Frame(self, height = self.heightScrollX)
        self.scrollX = Scrollbar(self.frameX, orient = "horizont" )
        
    def createScrollY(self):
        self.frameY = Frame(self, bg = "red", width = self.widthScrollY)
        self.scrollY = Scrollbar(self.frameY, orient = "vertical")
    
    def configureScroll(self):
        self.tree.configure(
        xscrollcommand = self.scrollX.set,
        yscrollcommand = self.scrollY.set
        )
        self.scrollX.configure(command = self.tree.xview)
        self.scrollY.configure(command = self.tree.yview)
         
    def posicionar(self):
        self.pack(side = "top", fill = "both", expand = True, padx = 5, pady = 5)
        self.pack_propagate(False)
        
        self.tree.pack(side = "left", fill = "both", expand = True)
        self.frameY.pack(side = "left", fill = "y")
        self.scrollY.pack(side = "top", fill = "y", expand = True)
        
        
class TreeWithTwoScroll(TreeWithScroll):
    def __init__(self, parent, *args, **kwargs):
        TreeWithScroll.__init__(self, parent, *args, **kwargs)
        
    def posicionar(self):
        self.pack(side = "top", fill = "both", expand = True, padx = 5, pady = 5)
        self.pack_propagate(False)
        
        self.frameX.pack(side = "bottom", fill = "x")
        self.scrollX.pack(side = "left", fill = "x", expand = True)
        
        self.tree.pack(side = "left", fill = "both", expand = True)
        
        self.frameY.pack(side = "left", fill = "y")
        self.scrollY.pack(side = "top", fill = "y", expand = True)


#---------- FrameWithScroll -------------------------------
class FrameWithScroll(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        
        #estilo
        self.configure(
        background = "blue"
        )
  
        #criando os widgets
        self.createContainer()
    
    def createContainer(self):
        self.canvas = Canvas(self)
        scroll = Scrollbar(self, command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = scroll.set)
        
        self.container = Frame(self.canvas)
        self.windowsCanvas = self.canvas.create_window((0, 0), window = self.container, anchor = "nw")
        
        self.canvas.pack(side = "left", fill = "both", expand = True)
        scroll.pack(side = "left", fill = "y")
        
        self.container.bind("<Configure>", lambda event: self.canvas.configure(scrollregion = self.canvas.bbox("all")))
 
    def posicionar(self):
        self.pack(fill = "both", expand = True, padx = 5, pady = 5)


def main():
    pass

if __name__ == "__main__":
    main()
