"""Calculette en TKinter.

Met en avant les notions de :
 * grid layout
 * gestion des événements (2 approches, method et bind)

Ne se concentre pas sur le parsing et le calcul de l'expression.
On pourrait utiliser l'algo de Shunting-yard
(https://en.wikipedia.org/wiki/Shunting-yard_algorithm).
A la place on utilise eval.
"""

from tkinter import Frame, Button, Label, Tk, Entry, N, S, E, W


def add_button_value_to_compute(event):
    value = event.widget["text"]
    if result.empty:
        result["text"] = ""
        result.empty = False
    result["text"] += value


def compute():
    input_ = result["text"]
    try:
        value = eval(input_)
    except ZeroDivisionError:
        result["text"] = "La division par zero n'est pas définie"
    except SyntaxError:
        result["text"] = "Erreur de syntaxe"
    else:
        result["text"] = str(value)
    result.empty = True

def erase():
    result["text"] = ""
    result.empty = True



def init_grid_responsive(root):
    for row in range(5):
        root.rowconfigure(row, weight=1)

    for column in range(1, 6):
        root.columnconfigure(column, weight=1)


root = Tk()
init_grid_responsive(root)

result = Label(root, text="Entrer une opération")
result.empty = True
result.grid(row=0, columnspan=6, sticky=N)

# on pourrait améliorer la mise en place des boutons avec une boucle...
buttons = []
buttons.append(Button(root, text="1"))
buttons[-1].grid(row=1, column=1, sticky=N+S+E+W) # sticky pour le responsive, jouer avec pour voir l'impact
buttons.append(Button(root, text="2"))
buttons[-1].grid(row=1, column=2, sticky=N+S+E+W)
buttons.append(Button(root, text="3"))
buttons[-1].grid(row=1, column=3, sticky=N+S+E+W)

buttons.append(Button(root, text="4"))
buttons[-1].grid(row=2, column=1, sticky=N+S+E+W)
buttons.append(Button(root, text="5"))
buttons[-1].grid(row=2, column=2, sticky=N+S+E+W)
buttons.append(Button(root, text="6"))
buttons[-1].grid(row=2, column=3, sticky=N+S+E+W)

buttons.append(Button(root, text="7"))
buttons[-1].grid(row=3, column=1, sticky=N+S+E+W)
buttons.append(Button(root, text="8"))
buttons[-1].grid(row=3, column=2, sticky=N+S+E+W)
buttons.append(Button(root, text="9"))
buttons[-1].grid(row=3, column=3, sticky=N+S+E+W)

buttons.append(Button(root, text="0"))
buttons[-1].grid(row=4, column=1, sticky=N+S+E+W)
buttons.append(Button(root, text="."))
buttons[-1].grid(row=4, column=2, sticky=N+S+E+W)

actions = []
actions.append(Button(root, text="+"))
actions[-1].grid(row=1, column=4, sticky=N+S+E+W)
actions.append(Button(root, text="-"))
actions[-1].grid(row=2, column=4, sticky=N+S+E+W)
actions.append(Button(root, text="*"))
actions[-1].grid(row=3, column=4, sticky=N+S+E+W)
actions.append(Button(root, text="/"))
actions[-1].grid(row=4, column=4, sticky=N+S+E+W)


for button in buttons+actions:
    button.bind('<Button-1>', add_button_value_to_compute)


action_delete = Button(root, text="Effacer", command=erase)
action_delete.grid(row=1, column=5, columnspan=2, sticky=N+S+E+W)
action_compute = Button(root, text="Calculer", command=compute)
action_compute.grid(row=2, column=5, columnspan=2, rowspan=3, padx=2, pady=2, sticky=W+E+N+S)




if __name__ == "__main__":
    root.mainloop()