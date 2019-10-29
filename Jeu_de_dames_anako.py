'''
Anaël Akouété
Créér le 21/10/2019
Module : Python
Jeu de dames
'''

from tkinter import *
from tkinter import messagebox

class Checkboard():
    CELL_SIZE = 60
    NUMBER_CELL = 10

    def __init__(self, canvas):
        self.canvas = canvas

    def drawgrid(self, canvas):
        for x in range(self.NUMBER_CELL):
            if x % 2 == 0:
                color_change = 0
            else:
                color_change = 1
            for y in range(self.NUMBER_CELL):
                if y % 2 == color_change:
                    color = 'navajowhite'
                else:
                    color = 'saddlebrown'
                canvas.create_rectangle(x * self.CELL_SIZE, y * self.CELL_SIZE,
                                        x * self.CELL_SIZE + self.CELL_SIZE,
                                        y * self.CELL_SIZE + self.CELL_SIZE, fill=color)
        self.placePawn()

    def clic(self, event):
        pass

    def placePawn(self):
        for x in range(Checkboard.NUMBER_CELL):
            for y in range(Checkboard.NUMBER_CELL):
                pawn = Pawn(self.canvas, x, y, "black")

    def clear(self, canvas):
        # Nettoyage du canevas
        clearance = messagebox.askyesno('Reset checkboard',
                                        'You are about to reset the checkboard, are you sure that\'s what you want ?')
        if clearance:
            canvas.delete("all")
            d.drawgrid(can1)


class Pawn():
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.size = 7
        self.coin = self.canvas.create_oval(self.x * Checkboard.CELL_SIZE, self.y * Checkboard.CELL_SIZE,
                                            self.x * Checkboard.CELL_SIZE + Checkboard.CELL_SIZE,
                                            self.y * Checkboard.CELL_SIZE + Checkboard.CELL_SIZE,
                                            fill = self.color)

    def become_queen(self):
        pass


class Player():
    def __init__(self, couleur):
        self.couleur = couleur


def leave():
    answer = messagebox.askyesno('Close the game',
                                 'You are about to close the game, are you sure ?')
    if answer:
        window1.quit()


# Création du widget principal
window1 = Tk()
window1.title('Checkers game')

# Création des widgets "esclaves" :
can1 = Canvas(window1, bg='dark grey', height=600, width=600)
can1.pack(side=LEFT)

# Creation du damier
d = Checkboard(can1)
d.drawgrid(can1)

# Création des boutons de controle
button1 = Button(window1, text='Close', command=leave)
button1.pack(side=BOTTOM)
button2 = Button(window1, text='Reset', command=lambda: d.clear(can1))
button2.pack()

window1.mainloop()  # démarrage du réceptionnaire d'événement
window1.destroy()  # destruction (fermeture) de la fenêtre
