
"""# imports
from tkinter.ttk import * 
from tkinter import *

class Start_window:

    def __init__(self):
        # create frame
        self = Tk()
        self.geometry("400x700") # set frame size
        self.title("Mastermind - Start") # set frame title
        self.iconbitmap('img/icon.ico') # set frame icon
        
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
        self.play_bt = Button(self, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=self.play)
        self.play_bt.grid(row = 8, column = 0, pady = 5, sticky='s')

        # show everything
        self.mainloop()

    # function to generate new window
    def play(self): 
        play_window = Toplevel(self) # create new window
        play_window.title('Mastermind - Play') # set title of new window
        play_window.iconbitmap('img/icon.ico') # set icon of new window
        play_window.geometry("900x700") # set size of new window
        self.play_bt.config(state="disabled") # set state of play button to "disabled" after button is clicked

        # create play button
        self.play_bt1 = Button(self, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=self.__init__)
        self.play_bt1.grid(row = 8, column = 0, pady = 5, sticky='s') 

# create new start window
start = Start_window() """

import tkinter as tk
from tkinter.constants import CURRENT
from tkinter.ttk import * 
import random


LARGE_FONT= ("Verdana", 12)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        # create title label
        title_lb = tk.Label(self, text = "Mastermind", width = 20, font=("Fixedsys", 40))
        title_lb.grid(row = 0, column = 0, pady = 10, sticky='nwse')

        # create gameart label
        gamemode_lb = tk.Label(self, text = "Gamemode", width = 20, font=("Fixedsys", 17))
        gamemode_lb.grid(row = 1, column = 0, padx=5, sticky='nwse')

        # create radio button for PvC
        var = tk.StringVar()
        player_vs_computer_rb = tk.Radiobutton(self, text="Player vs Computer", padx = 50, variable=var, value="PvC")
        player_vs_computer_rb.grid(row = 2, column = 0, padx=5, sticky='nwse')
        player_vs_computer_rb.deselect()

        # create radio button for PvP
        player_vs_player_rb = tk.Radiobutton(self, text="Player vs Player", padx = 50, variable=var, value="PvP")
        player_vs_player_rb.grid(row = 3, column = 0, padx=5, sticky='nwse')
        player_vs_player_rb.deselect()

        # create radio button for CvP
        computer_vs_player_rb = tk.Radiobutton(self, text="Computer vs Player", padx = 50, variable=var, value="CvP")
        computer_vs_player_rb.grid(row = 4, column = 0, padx=5, sticky='nwse')
        computer_vs_player_rb.deselect()

        # create options label
        options_lb = tk.Label(self, text = "", width = 1, font=("Fixedsys", 17))
        options_lb.grid(row = 5, column = 0, padx=1, sticky='nwse',pady=50)

        # create options label
        options_lb = tk.Label(self, text = "Options", width = 1, font=("Fixedsys", 17))
        options_lb.grid(row = 6, column = 0, padx=1, sticky='nwse')
        
        # create optionmenu for moves
        moves_cb = Combobox(self, values=['1', '2', '3', '4', '5', '6'])
        moves_cb.current(0)
        moves_cb.grid(row=7, column=0, padx=5, pady = 5)

        # create exit button
        exit_bt = tk.Button(self, text = "Exit", width = 6)
        #self.exit_bt.pack(side=RIGHT)
        
        btpvp = tk.Button(self, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=lambda: controller.show_frame(PageOne))
        btpvc = tk.Button(self, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=lambda: controller.show_frame(PageTwo))
        btcvp = tk.Button(self, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=lambda: controller.show_frame(PageThree))
        # create play button
        def choice():
            print(moves_cb.get())
            if(var.get()=="PvP"):
                Helper.testi =moves_cb.get()
                btpvp.invoke()
                PageOne.update(self)
                print(Helper.testi)
            elif(var.get()=="PvC"):
                vari=moves_cb.get()
                btpvc.invoke()
            elif(var.get()=="CvP"):
                vari=moves_cb.get()
                btcvp.invoke()
        

        play_bt = tk.Button(self, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=choice)
        play_bt.grid(row = 8, column = 0, pady = 5, sticky='s')



class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        title_lb = tk.Label(self, text = Helper.testi, width = 20, font=("Fixedsys", 40))
        title_lb.grid(row = 0, column = 0, pady = 10, sticky='nwse')

        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(StartPage))
        button1.grid(row = 1, column = 0, pady = 10, sticky='nwse')

        button2 = tk.Button(self, text="Page Two", command=lambda: controller.show_frame(PageTwo))
        button2.grid(row = 2, column = 0, pady = 10, sticky='nwse')


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_lb = tk.Label(self, text = "Test", width = 20, font=("Fixedsys", 40))
        title_lb.grid(row = 0, column = 0, pady = 10, sticky='nwse')

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(row = 1, column = 0, pady = 10, sticky='nwse')

        button2 = tk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button2.grid(row = 2, column = 0, pady = 10, sticky='nwse')


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title_lb = tk.Label(self, text = "Page Three", width = 20, font=("Fixedsys", 40))
        title_lb.grid(row = 0, column = 0, pady = 10, sticky='nwse')

        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button1.grid(row = 1, column = 0, pady = 10, sticky='nwse')

        button2 = tk.Button(self, text="Page One", command=lambda: controller.show_frame(PageOne))
        button2.grid(row = 2, column = 0, pady = 10, sticky='nwse')
        
class Helper():
    testi = 1


app = SeaofBTCapp()
app.mainloop()