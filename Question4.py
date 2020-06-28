from tkinter import *



class Calculator(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        btns = [
            ['MC','M+','M-','MR'],
        	['C','√','x²','+'],
        	['7','8','9','-'],
        	['4','5','6','*'],
        	['1','2','3','/'],
        	['0','.','+-','=']
        ]
    
        e1 = Entry(self,                
                   bg="Grey",
                   width=31)
        e1.grid(row=0, columnspan=4)
        
        for r in range(6):
            for c in range(4):
                btn = Button(self,
                               width=3,
                               relief=RAISED,
                               padx=7,
                               text=btns[r][c])
                btn.grid(row=r+1, column=c)
        
    def get(self):
        return self.entry.get()

class Mortage(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        
        la = Label(self, text="Loan Amount")
        la.grid(row=0,column=0,padx=5)        
        lat = Entry(self)
        lat.grid(row=0,column=1,padx=5)
        
        
        la1 = Label(self, text="Interest Rate")
        la1.grid(row=1,column=0,padx=5)        
        lat1 = Entry(self)
        lat1.grid(row=1,column=1,padx=5)
        
        
        la2 = Label(self, text="Loan Terms")
        la2.grid(row=2,column=0,padx=5)        
        lat2 = Entry(self)
        lat2.grid(row=2,column=1,padx=5)
        
        btn = Button(self, text="Compute Mortgage")
        btn.grid(row=3,column=0,padx=5)
        cm = Entry(self)
        cm.grid(row=3,column=1,padx=5)
        
    def get(self):
        return self.entry.get()
    
    
class MainApp(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.e1 = Calculator(self)
        self.e2 = Mortage(self)
        
        self.e2.grid(row=0, column=0, sticky="ew")
        self.e1.grid(row=0, column=1, sticky="ew")
        
        #self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(2, weight=1)
    
if __name__ == "__main__":
    root = Tk()
    root.geometry("460x185")
    MainApp(root).place(x=0, y=0)
    root.mainloop()
    #mortgage = Mortgage()
    #app = Calculator()
