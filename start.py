# imports
from os import name
from tkinter.ttk import * 
from tkinter import *
from tkinter import messagebox
import sys
import random
import time

# 0=Gelb 1=Blau 2=Grün 3=Braun 4=Lila 5=Orange
class Mastermind:
    windowid=0

    wonwindow=True
    notwonwindow = True

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

    result = [0,0,0,0]

    verlauf = [[0 for x in range(4)] for y in range(7)] 

    show_go = True

    won = False
    notwon = False

    optioncolor = []


    poscolors = []
    betterposcolors = ["","","",""]
    
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
            self.grid_rowconfigure(6, weight=1)
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
            #player_vs_computer_rb.deselect()
            player_vs_computer_rb.grid(row = 2, column = 0, padx=5, sticky='nwse')

            # create radio button for PvP
            player_vs_player_rb = Radiobutton(self, text="Player vs Player", padx = 50, variable=var, value="PvP")
            #player_vs_player_rb.deselect()
            player_vs_player_rb.grid(row = 3, column = 0, padx=5, sticky='nwse')

            # create radio button for CvP
            computer_vs_player_rb = Radiobutton(self, text="Computer vs Player", padx = 50, variable=var, value="CvP")
            #computer_vs_player_rb.deselect()
            computer_vs_player_rb.grid(row = 4, column = 0, padx=5, sticky='nwse')

            def getgamemode():
                Mastermind.color11 = Mastermind.color12 = Mastermind.color13 = Mastermind.color14 = 'white'
                Mastermind.ccolor11 = Mastermind.ccolor12 = Mastermind.ccolor13 = Mastermind.ccolor14 = 'white'

                Mastermind.color21 = Mastermind.color22 = Mastermind.color23 = Mastermind.color24 = 'white'
                Mastermind.ccolor21 = Mastermind.ccolor22 = Mastermind.ccolor23 = Mastermind.ccolor24 = 'white'

                Mastermind.color31 = Mastermind.color32 = Mastermind.color33 = Mastermind.color34 = 'white'
                Mastermind.ccolor31 = Mastermind.ccolor32 = Mastermind.ccolor33 = Mastermind.ccolor34 = 'white'

                Mastermind.color41 = Mastermind.color42 = Mastermind.color43 = Mastermind.color44 = 'white'
                Mastermind.ccolor41 = Mastermind.ccolor42 = Mastermind.ccolor43 = Mastermind.ccolor44 = 'white'

                Mastermind.color51 = Mastermind.color52 = Mastermind.color53 = Mastermind.color54 = 'white'
                Mastermind.ccolor51 = Mastermind.ccolor52 = Mastermind.ccolor53 = Mastermind.ccolor54 = 'white'

                Mastermind.color61 = Mastermind.color62 = Mastermind.color63 = Mastermind.color64 = 'white'
                Mastermind.ccolor61 = Mastermind.ccolor62 = Mastermind.ccolor63 = Mastermind.ccolor64 = 'white'

                Mastermind.color71 = Mastermind.color72 = Mastermind.color73 = Mastermind.color74 = 'white'
                Mastermind.ccolor71 = Mastermind.ccolor72 = Mastermind.ccolor73 = Mastermind.ccolor74 = 'white'

                Mastermind.color91 = Mastermind.color92 = Mastermind.color93 = Mastermind.color94 = 'white'

                Mastermind.result = [0,0,0,0]

                Mastermind.wonwindow = True
                Mastermind.notwonwindow = True

                Mastermind.gamemode = var.get()
                Mastermind.won = False
                Mastermind.verlauf = [[0 for x in range(4)] for y in range(7)] 
                
                Mastermind.notwon = False

                Mastermind.show_go = True

                Mastermind.optioncolor = []


                Mastermind.poscolors = []
                Mastermind.betterposcolors = ["","","",""]
    

                if(Mastermind.gamemode=="PvP" or Mastermind.gamemode=="PvC" or Mastermind.gamemode=="CvP"):
                    changewindow(1)
                else:
                    messagebox.showinfo("Select gamemode", "Please select a gamemode!")
                
            
            def game_info():
                messagebox.showinfo("How to play", "Sie müssen einen Farbencode festlegen, welchen der andere Spieler erraten muss.\nDabei darf jede Farbe nur einmal verwendet werden.\n")
            
            info_bt = Button(self, text = "Info", font=("Fixedsys", 14), width = 10, height=5, bg="lightgreen", command=game_info)
            info_bt.grid(row = 5, column = 0, pady = 5)
            
            # create play button
            play_bt = Button(self, text = "Play", font=("Fixedsys", 14), width = 15, height=5, bg="lightgreen", command=lambda :getgamemode())
            play_bt.grid(row = 6, column = 0, pady = 5, sticky='s')

        ##########################################################################################################################################################################################
        
        def windowgame():
            if(Mastermind.gamemode=="PvP"):
                Mastermind.spielzug = 9
            if(Mastermind.gamemode=="PvC"):
                code = [0,1,2,3,4,5]
                random.shuffle(code)
                Mastermind.result[0]=code[0]
                Mastermind.result[1]=code[1]
                Mastermind.result[2]=code[2]
                Mastermind.result[3]=code[3]
                Mastermind.spielzug=1
            if(Mastermind.gamemode=="CvP"):
                Mastermind.spielzug = 9

            
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
            
            if(Mastermind.won==True):
                Mastermind.color91 = numbertocolor(Mastermind.result[0])
                Mastermind.color92 = numbertocolor(Mastermind.result[1])
                Mastermind.color93 = numbertocolor(Mastermind.result[2])
                Mastermind.color94 = numbertocolor(Mastermind.result[3])
                Mastermind.spielzug = 100
                wonpup()
            if(Mastermind.notwon==True):
                Mastermind.color91 = numbertocolor(Mastermind.result[0])
                Mastermind.color92 = numbertocolor(Mastermind.result[1])
                Mastermind.color93 = numbertocolor(Mastermind.result[2])
                Mastermind.color94 = numbertocolor(Mastermind.result[3])
                notwonpup()
                
                
            
            canvas1 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas1.grid(row=1, column=0, padx=canvaspadx, pady=canvaspady)

            canvas1.create_oval(10, 15, 70, 75, fill=Mastermind.color11 , outline='black', tag="oval11")
            canvas1.tag_bind("oval11", "<Button-1>", lambda x: save_posn(11))
            
            canvas1.create_oval(90, 15, 150, 75, fill=Mastermind.color12 , outline='black', tag="oval12")
            canvas1.tag_bind("oval12", "<Button-1>", lambda x: save_posn(12))

            canvas1.create_oval(170, 15, 230, 75, fill=Mastermind.color13 , outline='black', tag="oval13")
            canvas1.tag_bind("oval13", "<Button-1>", lambda x: save_posn(13))

            canvas1.create_oval(250, 15, 310, 75, fill=Mastermind.color14 , outline='black', tag="oval14")
            canvas1.tag_bind("oval14", "<Button-1>", lambda x: save_posn(14))

            canvas1.create_line(340, 0, 340, 100, width=5)
            def cvp1():
                Mastermind.color11="yellow"
                Mastermind.color12="yellow"
                Mastermind.color13="blue"
                Mastermind.color14="blue"
                canvas()
                row1()

            def cvp2():
                
                Mastermind.color21="green"
                Mastermind.color22="green"
                Mastermind.color23="brown"
                Mastermind.color24="brown"
                row2()

            def cvp3():
                
                Mastermind.color31="purple"
                Mastermind.color32="purple"
                Mastermind.color33="orange"
                Mastermind.color34="orange"
                row3()
            
            def cvp4():
                
                if(len(Mastermind.poscolors)==4):
                    Mastermind.color41=Mastermind.poscolors[0]
                    Mastermind.color42=Mastermind.poscolors[0]
                    Mastermind.color43=Mastermind.poscolors[1]
                    Mastermind.color44=Mastermind.poscolors[1]                  
                else:
                    Mastermind.color41=Mastermind.poscolors[0]
                    Mastermind.color42=Mastermind.poscolors[0]
                    Mastermind.color43=Mastermind.poscolors[1]
                    Mastermind.color44=Mastermind.poscolors[1]
                
                row4()
            
            def cvp5():
                
                cc4=[Mastermind.ccolor41,Mastermind.ccolor42,Mastermind.ccolor43,Mastermind.ccolor44]
                zaehlerred = 0
                zaehlerblack = 0 
                for x in cc4:
                    if(x=="red"):
                        zaehlerred = zaehlerred+1
                    elif(x=="black"):
                        zaehlerblack = zaehlerblack+1
                if(len(Mastermind.poscolors)==4):
                    if(zaehlerred==1 and zaehlerblack==1):
                        Mastermind.color51=Mastermind.poscolors[0]
                        Mastermind.color52=Mastermind.poscolors[0]
                        Mastermind.color53=Mastermind.poscolors[2]
                        Mastermind.color54=Mastermind.poscolors[2]
                    elif(zaehlerred==2 and zaehlerblack==0):
                        Mastermind.color51=Mastermind.poscolors[2]
                        Mastermind.color52=Mastermind.poscolors[2]
                        Mastermind.color53=Mastermind.poscolors[3]
                        Mastermind.color54=Mastermind.poscolors[3]
                        Mastermind.betterposcolors[0]=Mastermind.poscolors[1]
                        Mastermind.betterposcolors[3]=Mastermind.poscolors[0]
                    else:
                        Mastermind.color51=Mastermind.poscolors[2]
                        Mastermind.color52=Mastermind.poscolors[2]
                        Mastermind.color53=Mastermind.poscolors[3]
                        Mastermind.color54=Mastermind.poscolors[3]
                        Mastermind.betterposcolors[0]=Mastermind.poscolors[0]
                        Mastermind.betterposcolors[3]=Mastermind.poscolors[1]
                else:
                    if(zaehlerred+zaehlerblack==2):
                        print(Mastermind.optioncolor)
                        Mastermind.poscolors.append(Mastermind.optioncolor[0])
                        Mastermind.poscolors.append(Mastermind.optioncolor[1])
                        Mastermind.color51=Mastermind.poscolors[0]
                        Mastermind.color52=Mastermind.poscolors[1]
                        Mastermind.color53=Mastermind.poscolors[2]
                        Mastermind.color54=Mastermind.poscolors[3]
                    elif(zaehlerred+zaehlerblack==0):
                        Mastermind.poscolors.append(Mastermind.optioncolor[2])
                        Mastermind.poscolors.append(Mastermind.optioncolor[3])
                        Mastermind.color51=Mastermind.poscolors[0]
                        Mastermind.color52=Mastermind.poscolors[1]
                        Mastermind.color53=Mastermind.poscolors[2]
                        Mastermind.color54=Mastermind.poscolors[3]
                    else:
                        Mastermind.color51=Mastermind.poscolors[0]
                        Mastermind.color52=Mastermind.poscolors[0]
                        Mastermind.color53=Mastermind.poscolors[2]
                        Mastermind.color54=Mastermind.poscolors[2]
                row5() 
            
            def cvp6():
                
                cc5=[Mastermind.ccolor51,Mastermind.ccolor52,Mastermind.ccolor53,Mastermind.ccolor54]
                zaehlerred = 0
                zaehlerblack = 0 
                for x in cc5:
                    if(x=="red"):
                        zaehlerred = zaehlerred+1
                    elif(x=="black"):
                        zaehlerblack = zaehlerblack+1
                if(len(Mastermind.poscolors)==4):
                    print(str(zaehlerred)+ "  wddswd  "+ str(zaehlerblack))
                    
                    if(Mastermind.betterposcolors[0]==""):
                        if(zaehlerred==2 and zaehlerblack==0):
                            Mastermind.betterposcolors[0]=Mastermind.poscolors[2]
                            Mastermind.betterposcolors[2]=Mastermind.poscolors[0]
                            Mastermind.betterposcolors[3]=Mastermind.poscolors[1]
                            Mastermind.betterposcolors[1]=Mastermind.poscolors[3]
                        else:
                            Mastermind.betterposcolors[0]=Mastermind.poscolors[0]
                            Mastermind.betterposcolors[2]=Mastermind.poscolors[2]
                            Mastermind.betterposcolors[1]=Mastermind.poscolors[1]
                            Mastermind.betterposcolors[3]=Mastermind.poscolors[3]
                    else:
                        print(str(zaehlerred)+ "  swd  "+ str(zaehlerblack))
                        if(zaehlerred==2 and zaehlerblack==0):
                            Mastermind.betterposcolors[1]=Mastermind.poscolors[3]
                            Mastermind.betterposcolors[3]=Mastermind.poscolors[2]
                        else:
                            Mastermind.betterposcolors[3]=Mastermind.poscolors[3]
                            Mastermind.betterposcolors[1]=Mastermind.poscolors[2]
                    Mastermind.color61=Mastermind.betterposcolors[0]
                    Mastermind.color62=Mastermind.betterposcolors[1]
                    Mastermind.color63=Mastermind.betterposcolors[2]
                    Mastermind.color64=Mastermind.betterposcolors[3]
                else:
                    print(str(zaehlerred)+ "  "+ str(zaehlerblack))
                    if(zaehlerred+zaehlerblack==0):
                        Mastermind.poscolors.append(Mastermind.poscolors[1])
                        Mastermind.poscolors.append(Mastermind.poscolors[3])
                        Mastermind.color61=Mastermind.poscolors[0]
                        Mastermind.color62=Mastermind.poscolors[1]
                        Mastermind.color63=Mastermind.poscolors[2]
                        Mastermind.color64=Mastermind.poscolors[3]
                    else:
                        Mastermind.poscolors.append(Mastermind.poscolors[0])
                        Mastermind.poscolors.append(Mastermind.poscolors[2])
                        Mastermind.color61=Mastermind.poscolors[0]
                        Mastermind.color62=Mastermind.poscolors[1]
                        Mastermind.color63=Mastermind.poscolors[2]
                        Mastermind.color64=Mastermind.poscolors[3]

                row6()

            def cvp7():
                if(Mastermind.betterposcolors[0]!="" and Mastermind.betterposcolors[1]!="" and Mastermind.betterposcolors[2]!="" and Mastermind.betterposcolors[3]!=""):
                    Mastermind.color71=Mastermind.betterposcolors[1]
                    Mastermind.color72=Mastermind.betterposcolors[0]
                    Mastermind.color73=Mastermind.betterposcolors[3]
                    Mastermind.color74=Mastermind.betterposcolors[2]
                row7()

            def row1():
                Mastermind.verlauf[0][0]=colortonumber(Mastermind.color11)
                Mastermind.verlauf[0][1]=colortonumber(Mastermind.color12)
                Mastermind.verlauf[0][2]=colortonumber(Mastermind.color13)
                Mastermind.verlauf[0][3]=colortonumber(Mastermind.color14)
                checkverlaufandresult()
                Mastermind.spielzug = 2
                canvas()
                if(Mastermind.gamemode=="CvP"):
                    cc1=[Mastermind.ccolor11,Mastermind.ccolor12,Mastermind.ccolor13,Mastermind.ccolor14]                            
                    zaehlerred = 0
                    zaehlerblack = 0 
                    for x in cc1:
                        if(x=="red"):
                            zaehlerred = zaehlerred+1
                        elif(x=="black"):
                            zaehlerblack = zaehlerblack+1
                    if(zaehlerblack==0 and zaehlerred==0):
                        Mastermind.poscolors.append("green")
                        Mastermind.poscolors.append("brown")
                        Mastermind.poscolors.append("purple")
                        Mastermind.poscolors.append("orange")
                    elif(zaehlerred == 1 and zaehlerblack == 0 or zaehlerred == 0 and zaehlerblack == 1):
                        Mastermind.optioncolor.append("yellow")
                        Mastermind.optioncolor.append("blue")
                    elif(zaehlerred == 1 and zaehlerblack == 1 or zaehlerred == 2 and zaehlerblack == 0 or zaehlerred == 0 and zaehlerblack == 2):
                        Mastermind.poscolors.append("yellow")
                        Mastermind.poscolors.append("blue")       

                    cvp2()
            
            def checkverlaufandresult():
                redfields = 0
                blackfields = 0
                if(Mastermind.spielzug == 1):
                    workverlauf = [Mastermind.verlauf[Mastermind.spielzug-1][0],Mastermind.verlauf[Mastermind.spielzug-1][1],Mastermind.verlauf[Mastermind.spielzug-1][2],Mastermind.verlauf[Mastermind.spielzug-1][3]]
                    workverlauf = list(set(workverlauf))
                    for i in range(len(workverlauf)):
                        for j in range(0, 4):
                            if(workverlauf[i]==Mastermind.result[j]):
                                redfields=redfields+1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][0]==Mastermind.result[0]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][1]==Mastermind.result[1]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][2]==Mastermind.result[2]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][3]==Mastermind.result[3]):
                        blackfields = blackfields +1

                    if(blackfields==4):
                        Mastermind.won = True
                        Mastermind.gamemode = "PvP"

                    redfields = redfields - blackfields
                    erg = ["white","white","white","white"]
                    for i in range(0, redfields):
                        erg[i]="red"
                    for i in range(redfields, redfields+blackfields):
                        erg[i]="black"
                
                    Mastermind.ccolor11=erg[0]
                    Mastermind.ccolor12=erg[1]
                    Mastermind.ccolor13=erg[2]
                    Mastermind.ccolor14=erg[3]
                
                if(Mastermind.spielzug == 2):
                    workverlauf = [Mastermind.verlauf[Mastermind.spielzug-1][0],Mastermind.verlauf[Mastermind.spielzug-1][1],Mastermind.verlauf[Mastermind.spielzug-1][2],Mastermind.verlauf[Mastermind.spielzug-1][3]]
                    workverlauf = list(set(workverlauf))
                    for i in range(len(workverlauf)):
                        for j in range(0, 4):
                            if(workverlauf[i]==Mastermind.result[j]):
                                redfields=redfields+1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][0]==Mastermind.result[0]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][1]==Mastermind.result[1]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][2]==Mastermind.result[2]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][3]==Mastermind.result[3]):
                        blackfields = blackfields +1

                    if(blackfields==4):
                        Mastermind.won = True
                        Mastermind.gamemode = "PvP"
                
                    redfields = redfields - blackfields
                    erg = ["white","white","white","white"]
                    for i in range(0, redfields):
                        erg[i]="red"
                    for i in range(redfields, redfields+blackfields):
                        erg[i]="black"
                
                    Mastermind.ccolor21=erg[0]
                    Mastermind.ccolor22=erg[1]
                    Mastermind.ccolor23=erg[2]
                    Mastermind.ccolor24=erg[3]
                
                if(Mastermind.spielzug == 3):
                    workverlauf = [Mastermind.verlauf[Mastermind.spielzug-1][0],Mastermind.verlauf[Mastermind.spielzug-1][1],Mastermind.verlauf[Mastermind.spielzug-1][2],Mastermind.verlauf[Mastermind.spielzug-1][3]]
                    workverlauf = list(set(workverlauf))
                    for i in range(len(workverlauf)):
                        for j in range(0, 4):
                            if(workverlauf[i]==Mastermind.result[j]):
                                redfields=redfields+1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][0]==Mastermind.result[0]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][1]==Mastermind.result[1]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][2]==Mastermind.result[2]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][3]==Mastermind.result[3]):
                        blackfields = blackfields +1

                    if(blackfields==4):
                        Mastermind.won = True
                        Mastermind.gamemode = "PvP"
                
                    redfields = redfields - blackfields
                    erg = ["white","white","white","white"]
                    for i in range(0, redfields):
                        erg[i]="red"
                    for i in range(redfields, redfields+blackfields):
                        erg[i]="black"
                
                    Mastermind.ccolor31=erg[0]
                    Mastermind.ccolor32=erg[1]
                    Mastermind.ccolor33=erg[2]
                    Mastermind.ccolor34=erg[3]
                
                if(Mastermind.spielzug == 4):
                    workverlauf = [Mastermind.verlauf[Mastermind.spielzug-1][0],Mastermind.verlauf[Mastermind.spielzug-1][1],Mastermind.verlauf[Mastermind.spielzug-1][2],Mastermind.verlauf[Mastermind.spielzug-1][3]]
                    workverlauf = list(set(workverlauf))
                    for i in range(len(workverlauf)):
                        for j in range(0, 4):
                            if(workverlauf[i]==Mastermind.result[j]):
                                redfields=redfields+1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][0]==Mastermind.result[0]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][1]==Mastermind.result[1]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][2]==Mastermind.result[2]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][3]==Mastermind.result[3]):
                        blackfields = blackfields +1
                    
                    if(blackfields==4):
                        Mastermind.won = True
                        Mastermind.gamemode = "PvP"
                
                    redfields = redfields - blackfields
                    erg = ["white","white","white","white"]
                    for i in range(0, redfields):
                        erg[i]="red"
                    for i in range(redfields, redfields+blackfields):
                        erg[i]="black"
                
                    Mastermind.ccolor41=erg[0]
                    Mastermind.ccolor42=erg[1]
                    Mastermind.ccolor43=erg[2]
                    Mastermind.ccolor44=erg[3]
                
                if(Mastermind.spielzug == 5):
                    workverlauf = [Mastermind.verlauf[Mastermind.spielzug-1][0],Mastermind.verlauf[Mastermind.spielzug-1][1],Mastermind.verlauf[Mastermind.spielzug-1][2],Mastermind.verlauf[Mastermind.spielzug-1][3]]
                    workverlauf = list(set(workverlauf))
                    for i in range(len(workverlauf)):
                        for j in range(0, 4):
                            if(workverlauf[i]==Mastermind.result[j]):
                                redfields=redfields+1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][0]==Mastermind.result[0]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][1]==Mastermind.result[1]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][2]==Mastermind.result[2]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][3]==Mastermind.result[3]):
                        blackfields = blackfields +1
                    
                    if(blackfields==4):
                        Mastermind.won = True
                        Mastermind.gamemode = "PvP"
                
                    redfields = redfields - blackfields
                    erg = ["white","white","white","white"]
                    for i in range(0, redfields):
                        erg[i]="red"
                    for i in range(redfields, redfields+blackfields):
                        erg[i]="black"
                
                    Mastermind.ccolor51=erg[0]
                    Mastermind.ccolor52=erg[1]
                    Mastermind.ccolor53=erg[2]
                    Mastermind.ccolor54=erg[3]
                
                if(Mastermind.spielzug == 6):
                    workverlauf = [Mastermind.verlauf[Mastermind.spielzug-1][0],Mastermind.verlauf[Mastermind.spielzug-1][1],Mastermind.verlauf[Mastermind.spielzug-1][2],Mastermind.verlauf[Mastermind.spielzug-1][3]]
                    workverlauf = list(set(workverlauf))
                    for i in range(len(workverlauf)):
                        for j in range(0, 4):
                            if(workverlauf[i]==Mastermind.result[j]):
                                redfields=redfields+1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][0]==Mastermind.result[0]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][1]==Mastermind.result[1]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][2]==Mastermind.result[2]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][3]==Mastermind.result[3]):
                        blackfields = blackfields +1

                    if(blackfields==4):
                        Mastermind.won = True
                        Mastermind.gamemode = "PvP"
                
                    redfields = redfields - blackfields
                    erg = ["white","white","white","white"]
                    for i in range(0, redfields):
                        erg[i]="red"
                    for i in range(redfields, redfields+blackfields):
                        erg[i]="black"
                
                    Mastermind.ccolor61=erg[0]
                    Mastermind.ccolor62=erg[1]
                    Mastermind.ccolor63=erg[2]
                    Mastermind.ccolor64=erg[3]
                
                if(Mastermind.spielzug == 7):
                    workverlauf = [Mastermind.verlauf[Mastermind.spielzug-1][0],Mastermind.verlauf[Mastermind.spielzug-1][1],Mastermind.verlauf[Mastermind.spielzug-1][2],Mastermind.verlauf[Mastermind.spielzug-1][3]]
                    workverlauf = list(set(workverlauf))
                    for i in range(len(workverlauf)):
                        for j in range(0, 4):
                            if(workverlauf[i]==Mastermind.result[j]):
                                redfields=redfields+1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][0]==Mastermind.result[0]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][1]==Mastermind.result[1]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][2]==Mastermind.result[2]):
                        blackfields = blackfields +1
                    if(Mastermind.verlauf[Mastermind.spielzug-1][3]==Mastermind.result[3]):
                        blackfields = blackfields +1

                    
                    redfields = redfields - blackfields
                    erg = ["white","white","white","white"]
                    for i in range(0, redfields):
                        erg[i]="red"
                    for i in range(redfields, redfields+blackfields):
                        erg[i]="black"
                
                    Mastermind.ccolor71=erg[0]
                    Mastermind.ccolor72=erg[1]
                    Mastermind.ccolor73=erg[2]
                    Mastermind.ccolor74=erg[3]

                    if(blackfields==4):
                        Mastermind.won = True
                        Mastermind.gamemode = "PvP"
                    else:
                        Mastermind.notwon = True


                    
                    


            if(Mastermind.spielzug==1):
                if(Mastermind.gamemode!="CvP"):
                    canvas1.create_text(400, 45,text= "Check", font=("Fixedsys", 17), tag="PvPTag1")
                    canvas1.tag_bind("PvPTag1", "<Button-1>", lambda x: row1())
            else:
                canvas1.create_oval(370, 10, 400, 40, fill=Mastermind.ccolor11 , outline='black', tag="control11")
                canvas1.create_oval(410, 10, 440, 40, fill=Mastermind.ccolor12 , outline='black', tag="control12")
                canvas1.create_oval(370, 50, 400, 80, fill=Mastermind.ccolor13 , outline='black', tag="control13")
                canvas1.create_oval(410, 50, 440, 80, fill=Mastermind.ccolor14 , outline='black', tag="control14")

                
    
            canvas2 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas2.grid(row=2, column=0, padx=canvaspadx, pady=canvaspady)

            canvas2.create_oval(10, 15, 70, 75, fill=Mastermind.color21 , outline='black', tag="oval21")
            canvas2.tag_bind("oval21", "<Button-1>", lambda x: save_posn(21))
            
            canvas2.create_oval(90, 15, 150, 75, fill=Mastermind.color22 , outline='black', tag="oval22")
            canvas2.tag_bind("oval22", "<Button-1>", lambda x: save_posn(22))

            canvas2.create_oval(170, 15, 230, 75, fill=Mastermind.color23 , outline='black', tag="oval23")
            canvas2.tag_bind("oval23", "<Button-1>", lambda x: save_posn(23))

            canvas2.create_oval(250, 15, 310, 75, fill=Mastermind.color24 , outline='black', tag="oval24")
            canvas2.tag_bind("oval24", "<Button-1>", lambda x: save_posn(24))

            canvas2.create_line(340, 0, 340, 100, width=5)


            def row2():
                Mastermind.verlauf[1][0]=colortonumber(Mastermind.color21)
                Mastermind.verlauf[1][1]=colortonumber(Mastermind.color22)
                Mastermind.verlauf[1][2]=colortonumber(Mastermind.color23)
                Mastermind.verlauf[1][3]=colortonumber(Mastermind.color24)
                checkverlaufandresult()
                Mastermind.spielzug = 3
                canvas()
                if(Mastermind.gamemode=="CvP"):
                    cc2=[Mastermind.ccolor21,Mastermind.ccolor22,Mastermind.ccolor23,Mastermind.ccolor24]
                            
                    zaehlerred = 0
                    zaehlerblack = 0 
                    for x in cc2:
                        if(x=="red"):
                            zaehlerred = zaehlerred+1
                        elif(x=="black"):
                            zaehlerblack = zaehlerblack+1
                    if(zaehlerblack==0 and zaehlerred==0):
                        Mastermind.poscolors.clear()
                        Mastermind.poscolors.append("yellow")
                        Mastermind.poscolors.append("blue")
                        Mastermind.poscolors.append("purple")
                        Mastermind.poscolors.append("orange")
                    elif(zaehlerred == 1 and zaehlerblack == 0 or zaehlerred == 0 and zaehlerblack == 1):
                        Mastermind.optioncolor.append("green")
                        Mastermind.optioncolor.append("brown")
                    elif(zaehlerred == 1 and zaehlerblack == 1 or zaehlerred == 2 and zaehlerblack == 0 or zaehlerred == 0 and zaehlerblack == 2):
                        Mastermind.poscolors.append("green")
                        Mastermind.poscolors.append("brown")    

                    cvp3()
            

            if(Mastermind.spielzug==2):
                canvas2.create_text(400, 45,text= "Check", font=("Fixedsys", 17), tag="PvPTag2")
                canvas2.tag_bind("PvPTag2", "<Button-1>", lambda x: row2())
            else:
                canvas2.create_oval(370, 10, 400, 40, fill=Mastermind.ccolor21 , outline='black', tag="control21")
                canvas2.create_oval(410, 10, 440, 40, fill=Mastermind.ccolor22 , outline='black', tag="control22")
                canvas2.create_oval(370, 50, 400, 80, fill=Mastermind.ccolor23 , outline='black', tag="control23")
                canvas2.create_oval(410, 50, 440, 80, fill=Mastermind.ccolor24 , outline='black', tag="control24")
            

            canvas3 = Canvas(self, width=canvaswidth, height=canvasheight,  highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas3.grid(row=3, column=0, padx=canvaspadx, pady=canvaspady)

            canvas3.create_oval(10, 15, 70, 75, fill=Mastermind.color31 , outline='black', tag="oval31")
            canvas3.tag_bind("oval31", "<Button-1>", lambda x: save_posn(31))
            
            canvas3.create_oval(90, 15, 150, 75, fill=Mastermind.color32 , outline='black', tag="oval32")
            canvas3.tag_bind("oval32", "<Button-1>", lambda x: save_posn(32))

            canvas3.create_oval(170, 15, 230, 75, fill=Mastermind.color33 , outline='black', tag="oval33")
            canvas3.tag_bind("oval33", "<Button-1>", lambda x: save_posn(33))

            canvas3.create_oval(250, 15, 310, 75, fill=Mastermind.color34 , outline='black', tag="oval34")
            canvas3.tag_bind("oval34", "<Button-1>", lambda x: save_posn(34))

            canvas3.create_line(340, 0, 340, 100, width=5)
            
            def row3():
                Mastermind.verlauf[2][0]=colortonumber(Mastermind.color31)
                Mastermind.verlauf[2][1]=colortonumber(Mastermind.color32)
                Mastermind.verlauf[2][2]=colortonumber(Mastermind.color33)
                Mastermind.verlauf[2][3]=colortonumber(Mastermind.color34)
                checkverlaufandresult()
                Mastermind.spielzug = 4
                canvas()
                if(Mastermind.gamemode=="CvP"):
                    cc3=[Mastermind.ccolor31,Mastermind.ccolor32,Mastermind.ccolor33,Mastermind.ccolor34]
                            
                    zaehlerred = 0
                    zaehlerblack = 0 
                    for x in cc3:
                        if(x=="red"):
                            zaehlerred = zaehlerred+1
                        elif(x=="black"):
                            zaehlerblack = zaehlerblack+1
                    if(zaehlerblack==0 and zaehlerred==0):
                        Mastermind.poscolors.clear()
                        Mastermind.poscolors.append("yellow")
                        Mastermind.poscolors.append("blue")
                        Mastermind.poscolors.append("green")
                        Mastermind.poscolors.append("brown")
                    elif(zaehlerred == 1 and zaehlerblack == 0 or zaehlerred == 0 and zaehlerblack == 1):
                        Mastermind.optioncolor.append("pruple")
                        Mastermind.optioncolor.append("orange")
                    elif(zaehlerred == 1 and zaehlerblack == 1 or zaehlerred == 2 and zaehlerblack == 0 or zaehlerred == 0 and zaehlerblack == 2):
                        Mastermind.poscolors.append("purple")
                        Mastermind.poscolors.append("orange") 

                    cvp4()   

            if(Mastermind.spielzug==3):
                canvas3.create_text(400, 45,text= "Check", font=("Fixedsys", 17), tag="PvPTag3")
                canvas3.tag_bind("PvPTag3", "<Button-1>", lambda x: row3())
            else:
                canvas3.create_oval(370, 10, 400, 40, fill=Mastermind.ccolor31 , outline='black', tag="control31")
                canvas3.create_oval(410, 10, 440, 40, fill=Mastermind.ccolor32 , outline='black', tag="control32")
                canvas3.create_oval(370, 50, 400, 80, fill=Mastermind.ccolor33 , outline='black', tag="control33")
                canvas3.create_oval(410, 50, 440, 80, fill=Mastermind.ccolor34 , outline='black', tag="control34")
            

            canvas4 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas4.grid(row=4, column=0, padx=canvaspadx, pady=canvaspady)

            canvas4.create_oval(10, 15, 70, 75, fill=Mastermind.color41 , outline='black', tag="oval41")
            canvas4.tag_bind("oval41", "<Button-1>", lambda x: save_posn(41))
            
            canvas4.create_oval(90, 15, 150, 75, fill=Mastermind.color42 , outline='black', tag="oval42")
            canvas4.tag_bind("oval42", "<Button-1>", lambda x: save_posn(42))

            canvas4.create_oval(170, 15, 230, 75, fill=Mastermind.color43 , outline='black', tag="oval43")
            canvas4.tag_bind("oval43", "<Button-1>", lambda x: save_posn(43))

            canvas4.create_oval(250, 15, 310, 75, fill=Mastermind.color44 , outline='black', tag="oval44")
            canvas4.tag_bind("oval44", "<Button-1>", lambda x: save_posn(44))

            canvas4.create_line(340, 0, 340, 100, width=5)

            def row4():
                Mastermind.verlauf[3][0]=colortonumber(Mastermind.color41)
                Mastermind.verlauf[3][1]=colortonumber(Mastermind.color42)
                Mastermind.verlauf[3][2]=colortonumber(Mastermind.color43)
                Mastermind.verlauf[3][3]=colortonumber(Mastermind.color44)
                checkverlaufandresult()
                Mastermind.spielzug = 5
                
                canvas()
                if(Mastermind.gamemode=="CvP"):
                    cvp5()
            

            if(Mastermind.spielzug==4):
                canvas4.create_text(400, 45,text= "Check", font=("Fixedsys", 17), tag="PvPTag4")
                canvas4.tag_bind("PvPTag4", "<Button-1>", lambda x: row4())
            else:
                canvas4.create_oval(370, 10, 400, 40, fill=Mastermind.ccolor41 , outline='black', tag="control41")
                canvas4.create_oval(410, 10, 440, 40, fill=Mastermind.ccolor42 , outline='black', tag="control42")
                canvas4.create_oval(370, 50, 400, 80, fill=Mastermind.ccolor43 , outline='black', tag="control43")
                canvas4.create_oval(410, 50, 440, 80, fill=Mastermind.ccolor44 , outline='black', tag="control44")
            

            canvas5 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas5.grid(row=5, column=0, padx=canvaspadx, pady=canvaspady)

            canvas5.create_oval(10, 15, 70, 75, fill=Mastermind.color51 , outline='black', tag="oval51")
            canvas5.tag_bind("oval51", "<Button-1>", lambda x: save_posn(51))
            
            canvas5.create_oval(90, 15, 150, 75, fill=Mastermind.color52 , outline='black', tag="oval52")
            canvas5.tag_bind("oval52", "<Button-1>", lambda x: save_posn(52))

            canvas5.create_oval(170, 15, 230, 75, fill=Mastermind.color53 , outline='black', tag="oval53")
            canvas5.tag_bind("oval53", "<Button-1>", lambda x: save_posn(53))

            canvas5.create_oval(250, 15, 310, 75, fill=Mastermind.color54 , outline='black', tag="oval54")
            canvas5.tag_bind("oval54", "<Button-1>", lambda x: save_posn(54))

            canvas5.create_line(340, 0, 340, 100, width=5)


            def row5():
                Mastermind.verlauf[4][0]=colortonumber(Mastermind.color51)
                Mastermind.verlauf[4][1]=colortonumber(Mastermind.color52)
                Mastermind.verlauf[4][2]=colortonumber(Mastermind.color53)
                Mastermind.verlauf[4][3]=colortonumber(Mastermind.color54)
                checkverlaufandresult()
                Mastermind.spielzug = 6
                canvas()
                if(Mastermind.gamemode=="CvP"):
                    cvp6()
            

            if(Mastermind.spielzug==5):
                canvas5.create_text(400, 45,text= "Check", font=("Fixedsys", 17), tag="PvPTag5")
                canvas5.tag_bind("PvPTag5", "<Button-1>", lambda x: row5())
            else:
                canvas5.create_oval(370, 10, 400, 40, fill=Mastermind.ccolor51 , outline='black', tag="control51")
                canvas5.create_oval(410, 10, 440, 40, fill=Mastermind.ccolor52 , outline='black', tag="control52")
                canvas5.create_oval(370, 50, 400, 80, fill=Mastermind.ccolor53 , outline='black', tag="control53")
                canvas5.create_oval(410, 50, 440, 80, fill=Mastermind.ccolor54 , outline='black', tag="control54")
            

            canvas6 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas6.grid(row=6, column=0, padx=canvaspadx, pady=canvaspady)

            canvas6.create_oval(10, 15, 70, 75, fill=Mastermind.color61 , outline='black', tag="oval61")
            canvas6.tag_bind("oval61", "<Button-1>", lambda x: save_posn(61))
            
            canvas6.create_oval(90, 15, 150, 75, fill=Mastermind.color62 , outline='black', tag="oval62")
            canvas6.tag_bind("oval62", "<Button-1>", lambda x: save_posn(62))

            canvas6.create_oval(170, 15, 230, 75, fill=Mastermind.color63 , outline='black', tag="oval63")
            canvas6.tag_bind("oval63", "<Button-1>", lambda x: save_posn(63))

            canvas6.create_oval(250, 15, 310, 75, fill=Mastermind.color64 , outline='black', tag="oval64")
            canvas6.tag_bind("oval64", "<Button-1>", lambda x: save_posn(64))

            canvas6.create_line(340, 0, 340, 100, width=5)

            def row6():
                Mastermind.verlauf[5][0]=colortonumber(Mastermind.color61)
                Mastermind.verlauf[5][1]=colortonumber(Mastermind.color62)
                Mastermind.verlauf[5][2]=colortonumber(Mastermind.color63)
                Mastermind.verlauf[5][3]=colortonumber(Mastermind.color64)
                checkverlaufandresult()
                Mastermind.spielzug = 7
                canvas()
                if(Mastermind.gamemode=="CvP"):
                    cvp7()
            

            if(Mastermind.spielzug==6):
                canvas6.create_text(400, 45,text= "Check", font=("Fixedsys", 17), tag="PvPTag6")
                canvas6.tag_bind("PvPTag6", "<Button-1>", lambda x: row6())
            else:
                canvas6.create_oval(370, 10, 400, 40, fill=Mastermind.ccolor61 , outline='black', tag="control61")
                canvas6.create_oval(410, 10, 440, 40, fill=Mastermind.ccolor62 , outline='black', tag="control62")
                canvas6.create_oval(370, 50, 400, 80, fill=Mastermind.ccolor63 , outline='black', tag="control63")
                canvas6.create_oval(410, 50, 440, 80, fill=Mastermind.ccolor64 , outline='black', tag="control64")
            

            canvas7 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas7.grid(row=7, column=0, padx=canvaspadx, pady=canvaspady)

            canvas7.create_oval(10, 15, 70, 75, fill=Mastermind.color71 , outline='black', tag="oval71")
            canvas7.tag_bind("oval71", "<Button-1>", lambda x: save_posn(71))
            
            canvas7.create_oval(90, 15, 150, 75, fill=Mastermind.color72 , outline='black', tag="oval72")
            canvas7.tag_bind("oval72", "<Button-1>", lambda x: save_posn(72))

            canvas7.create_oval(170, 15, 230, 75, fill=Mastermind.color73 , outline='black', tag="oval73")
            canvas7.tag_bind("oval73", "<Button-1>", lambda x: save_posn(73))

            canvas7.create_oval(250, 15, 310, 75, fill=Mastermind.color74 , outline='black', tag="oval74")
            canvas7.tag_bind("oval74", "<Button-1>", lambda x: save_posn(74))

            canvas7.create_line(340, 0, 340, 100, width=5)

            def row7():
                Mastermind.verlauf[6][0]=colortonumber(Mastermind.color71)
                Mastermind.verlauf[6][1]=colortonumber(Mastermind.color72)
                Mastermind.verlauf[6][2]=colortonumber(Mastermind.color73)
                Mastermind.verlauf[6][3]=colortonumber(Mastermind.color74)
                checkverlaufandresult()
                Mastermind.spielzug = 8
                canvas()
            

            if(Mastermind.spielzug==7):
                canvas7.create_text(400, 45,text= "Check", font=("Fixedsys", 17), tag="PvPTag7")
                canvas7.tag_bind("PvPTag7", "<Button-1>", lambda x: row7())
            else:
                canvas7.create_oval(370, 10, 400, 40, fill=Mastermind.ccolor71 , outline='black', tag="control71")
                canvas7.create_oval(410, 10, 440, 40, fill=Mastermind.ccolor72 , outline='black', tag="control72")
                canvas7.create_oval(370, 50, 400, 80, fill=Mastermind.ccolor73 , outline='black', tag="control73")
                canvas7.create_oval(410, 50, 440, 80, fill=Mastermind.ccolor74 , outline='black', tag="control74")
            
            
            canvas8 = Canvas(self, width=canvaswidth, height=canvasheight, highlightthickness=canvasht, bg=canvasbg, highlightbackground=canvashbg)
            canvas8.grid(row=9, column=0, padx=canvaspadx, pady=canvaspady*5)

            canvas8.create_oval(10, 15, 70, 75, fill=Mastermind.color91 , outline='black', tag="oval91")
            canvas8.tag_bind("oval91", "<Button-1>", lambda x: save_posn(91))
            
            canvas8.create_oval(90, 15, 150, 75, fill=Mastermind.color92 , outline='black', tag="oval92")
            canvas8.tag_bind("oval92", "<Button-1>", lambda x: save_posn(92))

            canvas8.create_oval(170, 15, 230, 75, fill=Mastermind.color93 , outline='black', tag="oval93")
            canvas8.tag_bind("oval93", "<Button-1>", lambda x: save_posn(93))

            canvas8.create_oval(250, 15, 310, 75, fill=Mastermind.color94 , outline='black', tag="oval94")
            canvas8.tag_bind("oval94", "<Button-1>", lambda x: save_posn(94))

            canvas8.create_line(340, 0, 340, 100, width=5)

            if(Mastermind.gamemode=="PvP" or Mastermind.gamemode=="CvP"):
                if(Mastermind.show_go):
                    canvas8.create_text(400, 45,text= "Go", font=("Fixedsys", 17), tag="PvPTag")
                    canvas8.tag_bind("PvPTag", "<Button-1>", lambda x: startpvp())

            def startpvp ():
            ######################################################
                
                if(Mastermind.show_go):
                    
                    Mastermind.result[0]=colortonumber(Mastermind.color91)
                    Mastermind.result[1]=colortonumber(Mastermind.color92)
                    Mastermind.result[2]=colortonumber(Mastermind.color93)
                    Mastermind.result[3]=colortonumber(Mastermind.color94)
                    Mastermind.color91 = Mastermind.color92 = Mastermind.color93 = Mastermind.color94="white"
                    Mastermind.show_go = False
                    Mastermind.spielzug = 1
                    if(Mastermind.gamemode=="CvP"):
                        cvp1()
                    
                    canvas()
                
                


                
        def colortonumber(color):
            if(color=="yellow"):
                return 0
            if(color=="blue"):
                return 1
            if(color=="green"):
                return 2
            if(color=="brown"):
                return 3
            if(color=="purple"):
                return 4
            if(color=="orange"):
                return 5
                
        
        def numbertocolor(number):
            if(number==0):
                return "yellow"
            if(number==1):
                return "blue"
            if(number==2):
                return "green"
            if(number==3):
                return "brown"
            if(number==4):
                return "purple"
            if(number==5):
                return "orange"
            

# 0=Gelb 1=Blau 2=Grün 3=Braun 4=Lila 5=Orange


        

        def save_posn(x):
            if(Mastermind.spielzug*10<x and Mastermind.spielzug*10+5>x):
                color = popup(self.winfo_pointerx(), self.winfo_pointery(),x)

                

        def wonpup():
            if(Mastermind.wonwindow):
                Mastermind.wonwindow = False
                def backmain():
                    try:
                        changewindow(0)
                    finally:
                        wonpopup.destroy()

                wonpopup = Tk()
                wonpopup.grid_rowconfigure(1, weight=1)
                wonpopup.grid_columnconfigure(0, weight=1)
                wonpopup.title("Glückwunsch") # set frame title
                wonpopup.iconbitmap('img/icon.ico') # set frame icon
                wonpopup.geometry("390x300+1050+500")   
                title_lb = Label(wonpopup, text = "Glückwunsch, \nSie haben gewonnen!!!", font=("Fixedsys", 17))
                title_lb.grid(row=0, column=0, padx=10, pady = 5, sticky="nwse")
                back_bt = Button(wonpopup, text = "Back to\nMenu", font=("Fixedsys", 17), width = 15, height=5, bg="lightgreen",command=backmain)
                back_bt.grid(row = 1, column = 0, pady = 10, sticky='s')

            
        def notwonpup():
            if(Mastermind.notwonwindow):
                Mastermind.notwonwindow = False
                def backmain():
                    try:
                        changewindow(0)
                    finally:
                        notwonpopup.destroy()

                notwonpopup = Tk()
                notwonpopup.grid_rowconfigure(2, weight=1)
                notwonpopup.grid_columnconfigure(0, weight=1)
                notwonpopup.title("Verloren") # set frame title
                notwonpopup.iconbitmap('img/icon.ico') # set frame icon
                notwonpopup.geometry("390x300+1050+500")   
                notwonpopup.title_lb = Label(notwonpopup, text = "Schade, leider \n nicht geschafft!", font=("Fixedsys", 17))
                notwonpopup.title_lb.grid(row=0, column=0, padx=10, pady = 5, sticky="nwse")
                notwonpopup.back_bt = Button(notwonpopup, text = "Back to\nMenu", font=("Fixedsys", 17), width = 15, height=5, bg="lightgreen",command=backmain)
                notwonpopup.back_bt.grid(row = 2, column = 0, pady = 10, sticky='s')


        def popup(x,y,id):
            if(Mastermind.gamemode!="CvP" or Mastermind.spielzug==9):
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
                Mastermind.color11 = color
            if(x==12):
                Mastermind.color12 = color
            if(x==13):
                Mastermind.color13 = color
            if(x==14):
                Mastermind.color14 = color
                    
            if(x==21):
                Mastermind.color21 = color
            if(x==22):
                Mastermind.color22 = color
            if(x==23):
                Mastermind.color23 = color
            if(x==24):
                Mastermind.color24 = color
                    
            if(x==31):
                Mastermind.color31 = color
            if(x==32):
                Mastermind.color32 = color
            if(x==33):
                Mastermind.color33 = color
            if(x==34):
                Mastermind.color34 = color
                    
            if(x==41):
                Mastermind.color41 = color
            if(x==42):
                Mastermind.color42 = color
            if(x==43):
                Mastermind.color43 = color
            if(x==44):
                Mastermind.color44 = color
                    
            if(x==51):
                Mastermind.color51 = color
            if(x==52):
                Mastermind.color52 = color
            if(x==53):
                Mastermind.color53 = color
            if(x==54):
                Mastermind.color54 = color
                    
            if(x==61):
                Mastermind.color61 = color
            if(x==62):
                Mastermind.color62 = color
            if(x==63):
                Mastermind.color63 = color
            if(x==64):
                Mastermind.color64 = color
                    
            if(x==71):
                Mastermind.color71 = color
            if(x==72):
                Mastermind.color72 = color
            if(x==73):
                Mastermind.color73 = color
            if(x==74):
                Mastermind.color74 = color

            if(x==91):
                Mastermind.color91 = color
            if(x==92):
                Mastermind.color92 = color
            if(x==93):
                Mastermind.color93 = color
            if(x==94):
                Mastermind.color94 = color
            canvas()  
            

        windowmain()
        
        
        # show everything
        
        self.mainloop()
        
        
# create new start window
start = Mastermind()