from tkinter.ttk import * 
from tkinter import *

class Start_window:

    def __init__(self):
        # create frame
        self.root = Tk()
        self.root.geometry("900x700")
        self.root.title("Mastermind - Start") # set frame title
        self.root.iconbitmap('img/icon.ico')
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_columnconfigure(0, weight=3)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=3)
        
        # create title label
        self.title_lb = Label(self.root, text = "Mastermind", width = 20, font=("Fixedsys", 40))
        self.title_lb.grid(row = 0, column = 1, pady = 5, sticky='nwse')

        # create gameart label
        self.gamemode_lb = Label(self.root, text = "Gamemode", width = 20, font=("Fixedsys", 17))
        self.gamemode_lb.grid(row = 1, column = 0, padx=5, sticky='nwse')

        # create radio button for PvC
        self.player_vs_computer_rb = Radiobutton(self.root, text="Player vs Computer", padx = 50, value="PvC")
        self.player_vs_computer_rb.deselect()
        self.player_vs_computer_rb.grid(row = 2, column = 0, padx=5, sticky='nwse')

        # create radio button for PvP
        self.player_vs_player_rb = Radiobutton(self.root, text="Player vs Player", padx = 50, value="PvP")
        self.player_vs_player_rb.deselect()
        self.player_vs_player_rb.grid(row = 3, column = 0, padx=5, sticky='nwse')

        # create radio button for CvP
        self.computer_vs_player_rb = Radiobutton(self.root, text="Computer vs Player", padx = 50, value="CvP")
        self.computer_vs_player_rb.deselect()
        self.computer_vs_player_rb.grid(row = 4, column = 0, padx=5, sticky='nwse')

        # create options label
        self.options_lb = Label(self.root, text = "Options", width = 20, font=("Fixedsys", 17))
        self.options_lb.grid(row = 1, column = 2, padx=5, sticky='nwse')
        
        # create optionmenu for moves
        self.moves_cb = Combobox(self.root, values=['1', '2', '3', '4', '5', '6'])
        self.moves_cb.grid(row=2, column=2, padx=5, sticky='nwse')

        # create exit button
        self.exit_bt = Button(self.root, text = "Exit", width = 6, command = self.root.destroy)
        #self.exit_bt.pack(side=RIGHT)

        # create play button
        self.play_bt = Button(self.root, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=self.play)
        self.play_bt.grid(row = 5, column = 1, pady = 5, sticky='s')

        # show everything
        self.root.mainloop()

    def play(self): # new window definition
        play_window = Toplevel(self.root)
        play_window.title('Mastermind - Play')
        play_window.iconbitmap('img/icon.ico')
        play_window.geometry("900x700") 
        self.play_bt.config(state="disabled")

mc = Start_window()
