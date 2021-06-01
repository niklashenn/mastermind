
# imports
from tkinter.ttk import * 
from tkinter import *
import sys


class Start_window:
    windowid=0
    color1= 'white'
    color2 = 'white'
    
    def __init__(self):
        # create frame
        
        #####################################################################
        self = Tk()
        self.title("Mastermind - Start") # set frame title
        self.iconbitmap('img/icon.ico') # set frame icon

        def clear_frame():
            for widgets in self.winfo_children():
                widgets.destroy()

        def changewindow(id):
            clear_frame()
            if(id==1):
                windowgame()
            if(id==0):
                windowmain()
        
        ##########################################################################################################################################################################################
        def windowmain():
            self.geometry("400x700") # set frame size
            # set weight of rows and columns
            self.grid_rowconfigure(8, weight=1)
            self.grid_columnconfigure(0, weight=1)
        
            # create title label
            self.title_lb = Label(self, text = "Mastermind", width = 20, font=("Fixedsys", 40))
            self.title_lb.grid(row = 0, column = 0, pady = 10, sticky='nwse')

            # create gameart label
            self.gamemode_lb = Label(self, text = "Gamemode", width = 20, font=("Fixedsys", 17))
            self.gamemode_lb.grid(row = 1, column = 0, padx=5, sticky='nwse')

            # create radio button for PvC
            var = IntVar()
            self.player_vs_computer_rb = Radiobutton(self, text="Player vs Computer", padx = 50, variable=var, value="PvC")
            self.player_vs_computer_rb.deselect()
            self.player_vs_computer_rb.grid(row = 2, column = 0, padx=5, sticky='nwse')

            # create radio button for PvP
            self.player_vs_player_rb = Radiobutton(self, text="Player vs Player", padx = 50, variable=var, value="PvP")
            self.player_vs_player_rb.deselect()
            self.player_vs_player_rb.grid(row = 3, column = 0, padx=5, sticky='nwse')

            # create radio button for CvP
            self.computer_vs_player_rb = Radiobutton(self, text="Computer vs Player", padx = 50, variable=var, value="CvP")
            self.computer_vs_player_rb.deselect()
            self.computer_vs_player_rb.grid(row = 4, column = 0, padx=5, sticky='nwse')

            # create options label
            self.options_lb = Label(self, text = "", width = 1, font=("Fixedsys", 17))
            self.options_lb.grid(row = 5, column = 0, padx=1, sticky='nwse',pady=50)

            # create options label
            self.options_lb = Label(self, text = "Options", width = 1, font=("Fixedsys", 17))
            self.options_lb.grid(row = 6, column = 0, padx=1, sticky='nwse')
            
            # create optionmenu for moves
            self.moves_cb = Combobox(self, values=['1', '2', '3', '4', '5', '6'])
            self.moves_cb.grid(row=7, column=0, padx=5, pady = 5)

            # create exit button
            self.exit_bt = Button(self, text = "Exit", width = 6, command = self.destroy)
            #self.exit_bt.pack(side=RIGHT)

            # create play button
            self.play_bt = Button(self, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=lambda :changewindow(1))
            self.play_bt.grid(row = 8, column = 0, pady = 5, sticky='s')

        ##########################################################################################################################################################################################
        
        def windowgame():
            self.geometry("600x1250")
            self.title("Mastermind")

            self.title_lb = Label(self, text = "Mastermind", width = 20, font=("Fixedsys", 40))
            self.title_lb.grid(row = 0, column = 0, pady = 10, sticky='nwse')
            canvas()
            
        def canvas():
            canvaswidth = 455
            canvasheight = 90
            canvaspadx = 50
            canvaspady = 4
            canvasbg = "white"
            canvashbg = "black"
            canvasht = 2
            
            canvas1 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas1.grid(row=1, column=0, padx=canvaspadx, pady=canvaspady)

            canvas1.create_oval(10, 10, 50, 50, fill=Start_window.color1 , outline='black', tag="oval1")
            canvas1.tag_bind("oval1", "<Button-1>", lambda x: save_posn(1))
            
            canvas1.create_oval(60, 10, 100, 50, fill=Start_window.color2 , outline='black', tag="oval2")
            canvas1.tag_bind("oval2", "<Button-1>", lambda x: save_posn(2))
            
            #canvas1.bind("<Button-1>", save_posn)
    
            canvas2 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas2.grid(row=2, column=0, padx=canvaspadx, pady=canvaspady)

            canvas3 = Canvas(self, width=canvaswidth, height=canvasheight,  highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas3.grid(row=3, column=0, padx=canvaspadx, pady=canvaspady)

            canvas4 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas4.grid(row=4, column=0, padx=canvaspadx, pady=canvaspady)

            canvas5 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas5.grid(row=5, column=0, padx=canvaspadx, pady=canvaspady)

            canvas6 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas6.grid(row=6, column=0, padx=canvaspadx, pady=canvaspady)

            canvas7 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas7.grid(row=7, column=0, padx=canvaspadx, pady=canvaspady)

            canvas8 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas8.grid(row=8, column=0, padx=canvaspadx, pady=canvaspady)

            canvas9 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas9.grid(row=9, column=0, padx=canvaspadx, pady=canvaspady)

            canvas10 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas10.grid(row=10, column=0, padx=canvaspadx, pady=canvaspady)
            
            canvas11 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas11.grid(row=11, column=0, padx=canvaspadx, pady=canvaspady*5)

        
            
        def save_posn(x):    
            popup()
            if(x==1):
                Start_window.color1 = 'black'
            if(x==2):
                Start_window.color2 = 'black'
            canvas()
        
        def popup():
            self = Tk()
            self.title("Mastermind - Start") # set frame title
            self.iconbitmap('img/icon.ico') # set frame icon
            self.geometry("50x50")

            #newWindow = Toplevel(self)
            #labelExample = Label(self.newWindow, text = "New Window")
            #buttonExample = Button(self.newWindow, text = "New Window button")


        windowgame()
        
        # show everything
        
        self.mainloop()
        
        
# create new start window
start = Start_window()