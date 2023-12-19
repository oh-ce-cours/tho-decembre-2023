from tkinter import Frame, Button, Label, Tk, Entry, LEFT, RIGHT, TOP, BOTTOM, Scale, END


NB_A_TROUVER = 43

def game(guess):
    if guess == NB_A_TROUVER:
        result_label["text"] = "BRAVO !"

    if guess < NB_A_TROUVER:
        result_label["text"] = "C'est plus !"

    if guess > NB_A_TROUVER:
        result_label["text"] = "C'est moins !"



def update_input(value):
    """ Gère la mise à jour de l'entry.

    Appelé depuis le scale dès qu'on le déplace
    """
    input_number.delete(0,END)
    input_number.insert(0,str(value))
    print("update", value)


def update_scale(value_dans_le_scale):
    """Gère la mise à jour de la scale.

    Gère à la fois :

      * la validation que ce qui est entré est bien un nombre
      * la mise à jour de la scale
      * la mise à jour du jeu

    Appelé depuis le Entry."""
    value = value_dans_le_scale

    if value == "":
        return True

    print("update scale", value)
    try:
        value = int(value)
    except:
        return False
    print(value)

    if not (0 < value < 100):
        return False

    scale.set(value)
    game(value)
    return True


def on_release_scale(event):
    """ Callback appellée quand on fini l'interaction avec le scale.

    Gère le déroulement du jeu.
    """
    guess = scale.get()
    game(guess)


# racine de l'arbre de widgets
root = Tk()

# frame qui contient le label et le input
input_frame = Frame(root)
label = Label(input_frame, text='Entrer un nombre (entre 0 et 100)')
tcl_function_update_scale = (input_frame.register(update_scale), "%P")
input_number = Entry(input_frame, validate="key", validatecommand=tcl_function_update_scale)

# label à gauche / input à droite / frame en haut
label.pack(side=LEFT)
input_number.pack(side=RIGHT)
input_frame.pack(anchor="n")

# scale de gauche à droite, entre 0 et 100
scale = Scale(root, orient="horizontal", from_=1, to=99, command=update_input)
scale.bind("<ButtonRelease-1>", on_release_scale) # callback quand on lache le bouton gauche
# positionnéee en bas de la frame
scale.pack(anchor="s")

# label de résultats
result_label = Label(root, text="C'est plus !")
# positionné en bas de la scale
result_label.pack(anchor="s")



root.mainloop()

