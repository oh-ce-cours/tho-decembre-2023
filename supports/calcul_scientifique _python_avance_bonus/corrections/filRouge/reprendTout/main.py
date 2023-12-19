from tkinter import Tk
import data_access
from gui import Data

KEYS = ["id", "name", "formation_name", "note"]

root = Tk()
root.tk.call("tk", "scaling", 2.0)
d = Data(root, data_access.read_stagiaires)
root.mainloop()
