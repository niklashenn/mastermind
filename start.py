
# imports
from tkinter.ttk import * 
from tkinter import *
import sys


class Start_window:
    windowid=0
    color11 = color12 = color13 = color14 = 'white'
    ccolor11 = ccolor12 = ccolor13 = ccolor14 = 'white'

    color21 = color22 = color23 = color24 = 'white'
    ccolor21 = ccolor22 = ccolor23 = ccolor24 = 'white'

    color31 = color32 = color33 = color34 = 'white'
    ccolor31 = ccolor32 = ccolor33 = ccolor34 = 'white'

    color41 = color42 = color43 = color44 = 'white'
    ccolor41 = ccolor42 = ccolor43 = ccolor44 = 'white'

    color51 = color52 = color53 = color54 = 'white'
    ccolor51 = ccolor52 = ccolor53 = ccolor54 = 'white'

    color61 = color62 = color63 = color64 = 'white'
    ccolor61 = ccolor62 = ccolor63 = ccolor64 = 'white'

    color71 = color72 = color73 = color74 = 'white'
    ccolor71 = ccolor72 = ccolor73 = ccolor74 = 'white'

    color91 = color92 = color93 = color94 = 'white'

    spielzug = 0
    gamemode = ""
    
    def __init__(self):
        # create frame
        
        #####################################################################
        self = Tk()
        self.title("Mastermind - Start") # set frame titleµ
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
            var = StringVar()
            player_vs_computer_rb = Radiobutton(self, text="Player vs Computer", padx = 50, variable=var, value="PvC")
            player_vs_computer_rb.deselect()
            player_vs_computer_rb.grid(row = 2, column = 0, padx=5, sticky='nwse')

            # create radio button for PvP
            player_vs_player_rb = Radiobutton(self, text="Player vs Player", padx = 50, variable=var, value="PvP")
            player_vs_player_rb.deselect()
            player_vs_player_rb.grid(row = 3, column = 0, padx=5, sticky='nwse')

            # create radio button for CvP
            computer_vs_player_rb = Radiobutton(self, text="Computer vs Player", padx = 50, variable=var, value="CvP")
            computer_vs_player_rb.deselect()
            computer_vs_player_rb.grid(row = 4, column = 0, padx=5, sticky='nwse')

            
            # create exit button
            self.exit_bt = Button(self, text = "Exit", width = 6, command = self.destroy)
            #self.exit_bt.pack(side=RIGHT)
            def getgamemode():
                Start_window.gamemode = var.get()
                changewindow(1)

            # create play button
            self.play_bt = Button(self, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=lambda :getgamemode())
            self.play_bt.grid(row = 8, column = 0, pady = 5, sticky='s')

        ##########################################################################################################################################################################################
        
        def windowgame():
            if(Start_window.gamemode=="PvP"):
                Start_window.spielzug = 1

            
            self.geometry("650x950+900+300")
            self.title("Mastermind")

            self.title_lb = Label(self, text = "Mastermind", width = 20, font=("Fixedsys", 40))
            self.title_lb.grid(row = 0, column = 0, pady = 10, sticky='nwse')
            canvas()
            
        def canvas():
            canvaswidth = 455
            canvasheight = 90
            canvaspadx = 10
            canvaspady = 4
            canvasbg = "white"
            canvashbg = "black"
            canvasht = 2
            
            canvas1 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas1.grid(row=1, column=0, padx=canvaspadx, pady=canvaspady)

            canvas1.create_oval(10, 15, 70, 75, fill=Start_window.color11 , outline='black', tag="oval11")
            canvas1.tag_bind("oval11", "<Button-1>", lambda x: save_posn(11))
            
            canvas1.create_oval(90, 15, 150, 75, fill=Start_window.color12 , outline='black', tag="oval12")
            canvas1.tag_bind("oval12", "<Button-1>", lambda x: save_posn(12))

            canvas1.create_oval(170, 15, 230, 75, fill=Start_window.color13 , outline='black', tag="oval13")
            canvas1.tag_bind("oval13", "<Button-1>", lambda x: save_posn(13))

            canvas1.create_oval(250, 15, 310, 75, fill=Start_window.color14 , outline='black', tag="oval14")
            canvas1.tag_bind("oval14", "<Button-1>", lambda x: save_posn(14))

            canvas1.create_line(340, 0, 340, 100, width=5)

            canvas1.create_oval(370, 10, 400, 40, fill=Start_window.ccolor11 , outline='black', tag="control11")

            canvas1.create_oval(410, 10, 440, 40, fill=Start_window.ccolor12 , outline='black', tag="control12")

            canvas1.create_oval(370, 50, 400, 80, fill=Start_window.ccolor13 , outline='black', tag="control13")

            canvas1.create_oval(410, 50, 440, 80, fill=Start_window.ccolor14 , outline='black', tag="control14")
            
            #canvas1.bind("<Button-1>", save_posn)
    
            canvas2 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas2.grid(row=2, column=0, padx=canvaspadx, pady=canvaspady)

            canvas2.create_oval(10, 15, 70, 75, fill=Start_window.color21 , outline='black', tag="oval21")
            canvas2.tag_bind("oval21", "<Button-1>", lambda x: save_posn(21))
            
            canvas2.create_oval(90, 15, 150, 75, fill=Start_window.color22 , outline='black', tag="oval22")
            canvas2.tag_bind("oval22", "<Button-1>", lambda x: save_posn(22))

            canvas2.create_oval(170, 15, 230, 75, fill=Start_window.color23 , outline='black', tag="oval23")
            canvas2.tag_bind("oval23", "<Button-1>", lambda x: save_posn(23))

            canvas2.create_oval(250, 15, 310, 75, fill=Start_window.color24 , outline='black', tag="oval24")
            canvas2.tag_bind("oval24", "<Button-1>", lambda x: save_posn(24))

            canvas2.create_line(340, 0, 340, 100, width=5)

            canvas2.create_oval(370, 10, 400, 40, fill=Start_window.ccolor21 , outline='black', tag="control21")

            canvas2.create_oval(410, 10, 440, 40, fill=Start_window.ccolor22 , outline='black', tag="control22")

            canvas2.create_oval(370, 50, 400, 80, fill=Start_window.ccolor23 , outline='black', tag="control23")

            canvas2.create_oval(410, 50, 440, 80, fill=Start_window.ccolor24 , outline='black', tag="control24")
            

            canvas3 = Canvas(self, width=canvaswidth, height=canvasheight,  highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas3.grid(row=3, column=0, padx=canvaspadx, pady=canvaspady)

            canvas3.create_oval(10, 15, 70, 75, fill=Start_window.color31 , outline='black', tag="oval31")
            canvas3.tag_bind("oval31", "<Button-1>", lambda x: save_posn(31))
            
            canvas3.create_oval(90, 15, 150, 75, fill=Start_window.color32 , outline='black', tag="oval32")
            canvas3.tag_bind("oval32", "<Button-1>", lambda x: save_posn(32))

            canvas3.create_oval(170, 15, 230, 75, fill=Start_window.color33 , outline='black', tag="oval33")
            canvas3.tag_bind("oval33", "<Button-1>", lambda x: save_posn(33))

            canvas3.create_oval(250, 15, 310, 75, fill=Start_window.color34 , outline='black', tag="oval34")
            canvas3.tag_bind("oval34", "<Button-1>", lambda x: save_posn(34))

            canvas3.create_line(340, 0, 340, 100, width=5)
            
            canvas3.create_oval(370, 10, 400, 40, fill=Start_window.ccolor11 , outline='black', tag="control31")
            canvas3.create_oval(410, 10, 440, 40, fill=Start_window.ccolor12 , outline='black', tag="control32")
            canvas3.create_oval(370, 50, 400, 80, fill=Start_window.ccolor13 , outline='black', tag="control33")
            canvas3.create_oval(410, 50, 440, 80, fill=Start_window.ccolor14 , outline='black', tag="control34")
            

            canvas4 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas4.grid(row=4, column=0, padx=canvaspadx, pady=canvaspady)

            canvas4.create_oval(10, 15, 70, 75, fill=Start_window.color41 , outline='black', tag="oval41")
            canvas4.tag_bind("oval41", "<Button-1>", lambda x: save_posn(41))
            
            canvas4.create_oval(90, 15, 150, 75, fill=Start_window.color42 , outline='black', tag="oval42")
            canvas4.tag_bind("oval42", "<Button-1>", lambda x: save_posn(42))

            canvas4.create_oval(170, 15, 230, 75, fill=Start_window.color43 , outline='black', tag="oval43")
            canvas4.tag_bind("oval43", "<Button-1>", lambda x: save_posn(43))

            canvas4.create_oval(250, 15, 310, 75, fill=Start_window.color44 , outline='black', tag="oval44")
            canvas4.tag_bind("oval44", "<Button-1>", lambda x: save_posn(44))

            canvas4.create_line(340, 0, 340, 100, width=5)

            canvas4.create_oval(370, 10, 400, 40, fill=Start_window.ccolor11 , outline='black', tag="control41")
            canvas4.create_oval(410, 10, 440, 40, fill=Start_window.ccolor12 , outline='black', tag="control42")
            canvas4.create_oval(370, 50, 400, 80, fill=Start_window.ccolor13 , outline='black', tag="control43")
            canvas4.create_oval(410, 50, 440, 80, fill=Start_window.ccolor14 , outline='black', tag="control44")
            

            canvas5 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas5.grid(row=5, column=0, padx=canvaspadx, pady=canvaspady)

            canvas5.create_oval(10, 15, 70, 75, fill=Start_window.color51 , outline='black', tag="oval51")
            canvas5.tag_bind("oval51", "<Button-1>", lambda x: save_posn(51))
            
            canvas5.create_oval(90, 15, 150, 75, fill=Start_window.color52 , outline='black', tag="oval52")
            canvas5.tag_bind("oval52", "<Button-1>", lambda x: save_posn(52))

            canvas5.create_oval(170, 15, 230, 75, fill=Start_window.color53 , outline='black', tag="oval53")
            canvas5.tag_bind("oval53", "<Button-1>", lambda x: save_posn(53))

            canvas5.create_oval(250, 15, 310, 75, fill=Start_window.color54 , outline='black', tag="oval54")
            canvas5.tag_bind("oval54", "<Button-1>", lambda x: save_posn(54))

            canvas5.create_line(340, 0, 340, 100, width=5)

            canvas5.create_oval(370, 10, 400, 40, fill=Start_window.ccolor11 , outline='black', tag="control51")
            canvas5.create_oval(410, 10, 440, 40, fill=Start_window.ccolor12 , outline='black', tag="control52")
            canvas5.create_oval(370, 50, 400, 80, fill=Start_window.ccolor13 , outline='black', tag="control53")
            canvas5.create_oval(410, 50, 440, 80, fill=Start_window.ccolor14 , outline='black', tag="control54")
            

            canvas6 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas6.grid(row=6, column=0, padx=canvaspadx, pady=canvaspady)

            canvas6.create_oval(10, 15, 70, 75, fill=Start_window.color61 , outline='black', tag="oval61")
            canvas6.tag_bind("oval61", "<Button-1>", lambda x: save_posn(61))
            
            canvas6.create_oval(90, 15, 150, 75, fill=Start_window.color62 , outline='black', tag="oval62")
            canvas6.tag_bind("oval62", "<Button-1>", lambda x: save_posn(62))

            canvas6.create_oval(170, 15, 230, 75, fill=Start_window.color63 , outline='black', tag="oval63")
            canvas6.tag_bind("oval63", "<Button-1>", lambda x: save_posn(63))

            canvas6.create_oval(250, 15, 310, 75, fill=Start_window.color64 , outline='black', tag="oval64")
            canvas6.tag_bind("oval64", "<Button-1>", lambda x: save_posn(64))

            canvas6.create_line(340, 0, 340, 100, width=5)

            canvas6.create_oval(370, 10, 400, 40, fill=Start_window.ccolor11 , outline='black', tag="control61")
            canvas6.create_oval(410, 10, 440, 40, fill=Start_window.ccolor12 , outline='black', tag="control62")
            canvas6.create_oval(370, 50, 400, 80, fill=Start_window.ccolor13 , outline='black', tag="control63")
            canvas6.create_oval(410, 50, 440, 80, fill=Start_window.ccolor14 , outline='black', tag="control64")
            

            canvas7 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas7.grid(row=7, column=0, padx=canvaspadx, pady=canvaspady)

            canvas7.create_oval(10, 15, 70, 75, fill=Start_window.color71 , outline='black', tag="oval71")
            canvas7.tag_bind("oval71", "<Button-1>", lambda x: save_posn(71))
            
            canvas7.create_oval(90, 15, 150, 75, fill=Start_window.color72 , outline='black', tag="oval72")
            canvas7.tag_bind("oval72", "<Button-1>", lambda x: save_posn(72))

            canvas7.create_oval(170, 15, 230, 75, fill=Start_window.color73 , outline='black', tag="oval73")
            canvas7.tag_bind("oval73", "<Button-1>", lambda x: save_posn(73))

            canvas7.create_oval(250, 15, 310, 75, fill=Start_window.color74 , outline='black', tag="oval74")
            canvas7.tag_bind("oval74", "<Button-1>", lambda x: save_posn(74))

            canvas7.create_line(340, 0, 340, 100, width=5)

            canvas7.create_oval(370, 10, 400, 40, fill=Start_window.ccolor11 , outline='black', tag="control71")
            canvas7.create_oval(410, 10, 440, 40, fill=Start_window.ccolor12 , outline='black', tag="control72")
            canvas7.create_oval(370, 50, 400, 80, fill=Start_window.ccolor13 , outline='black', tag="control73")
            canvas7.create_oval(410, 50, 440, 80, fill=Start_window.ccolor14 , outline='black', tag="control74")
            
            
            canvas8 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas8.grid(row=8, column=0, padx=canvaspadx, pady=canvaspady*5)

            canvas8.create_oval(10, 15, 70, 75, fill=Start_window.color91 , outline='black', tag="oval91")
            canvas8.tag_bind("oval91", "<Button-1>", lambda x: save_posn(91))
            
            canvas8.create_oval(90, 15, 150, 75, fill=Start_window.color92 , outline='black', tag="oval92")
            canvas8.tag_bind("oval92", "<Button-1>", lambda x: save_posn(92))

            canvas8.create_oval(170, 15, 230, 75, fill=Start_window.color93 , outline='black', tag="oval93")
            canvas8.tag_bind("oval93", "<Button-1>", lambda x: save_posn(93))

            canvas8.create_oval(250, 15, 310, 75, fill=Start_window.color94 , outline='black', tag="oval94")
            canvas8.tag_bind("oval94", "<Button-1>", lambda x: save_posn(94))

            canvas8.create_line(340, 0, 340, 100, width=5)

        
        

        def save_posn(x):
            print(Start_window.spielzug*10)
            print(x)
            if(Start_window.spielzug*10<x and Start_window.spielzug*10+5>x):
                color = popup(self.winfo_pointerx(), self.winfo_pointery(),x)

            #if(Start_window.spielzug*10<x and Start_window.spielzug*10+5 > Start_window.spielzug*10 ):
                
        
            
        
        def popup(x,y,id):
            check = False
            popup = Tk()
            # set weight of rows and columns
            popup.grid_rowconfigure(8, weight=1)
            popup.grid_columnconfigure(0, weight=1)
            popup.title("Mastermind - Start") # set frame title
            popup.iconbitmap('img/icon.ico') # set frame icon
            popup.geometry("50x50+"+str(x)+"+"+str(y-80))
            def setcolor1():
                setcolor(color_cb.get(),id)
                popup.destroy()
            color_cb = Combobox(popup, values=['Gelb', 'Blau', 'Grün', 'Braun', 'Lila', 'Orange'], state="readonly")
            color_cb.current(0)
            color_cb.grid(row=0, column=0, padx=5, pady = 5)
            confirmcolor_bt = Button(popup, text = "OK", font=("Fixedsys", 14), width = 2, height=1, bg="lightgreen", command= setcolor1)
            confirmcolor_bt.grid(row = 0, column = 1, pady = 5, sticky='s')
            
        
        def setcolor(color,x):
            if(color == "Gelb"):
                color = "yellow"
            if(color == "Blau"):
                color = "blue"
            if(color == "Grün"):
                color = "green"
            if(color == "Braun"):
                color = "brown"
            if(color == "Lila"):
                color = "purple"
            if(color == "Orange"):
                color = "orange"

            if(x==11):
                Start_window.color11 = color
            if(x==12):
                Start_window.color12 = color
            if(x==13):
                Start_window.color13 = color
            if(x==14):
                Start_window.color14 = color
                    
            if(x==21):
                Start_window.color21 = color
            if(x==22):
                Start_window.color22 = color
            if(x==23):
                Start_window.color23 = color
            if(x==24):
                Start_window.color24 = color
                    
            if(x==31):
                Start_window.color31 = color
            if(x==32):
                Start_window.color32 = color
            if(x==33):
                Start_window.color33 = color
            if(x==34):
                Start_window.color34 = color
                    
            if(x==41):
                Start_window.color41 = color
            if(x==42):
                Start_window.color42 = color
            if(x==43):
                Start_window.color43 = color
            if(x==44):
                Start_window.color44 = color
                    
            if(x==51):
                Start_window.color51 = color
            if(x==52):
                Start_window.color52 = color
            if(x==53):
                Start_window.color53 = color
            if(x==54):
                Start_window.color54 = color
                    
            if(x==61):
                Start_window.color61 = color
            if(x==62):
                Start_window.color62 = color
            if(x==63):
                Start_window.color63 = color
            if(x==64):
                Start_window.color64 = color
                    
            if(x==71):
                Start_window.color71 = color
            if(x==72):
                Start_window.color72 = color
            if(x==73):
                Start_window.color73 = color
            if(x==74):
                Start_window.color74 = color

            if(x==91):
                Start_window.color91 = color
            if(x==92):
                Start_window.color92 = color
            if(x==93):
                Start_window.color93 = color
            if(x==94):
                Start_window.color94 = color
            canvas()  
            

        windowmain()
        
        
        # show everything
        
        self.mainloop()
        
        
# create new start window
start = Start_window()