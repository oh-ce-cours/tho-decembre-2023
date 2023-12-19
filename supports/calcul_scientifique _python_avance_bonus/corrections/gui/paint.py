from tkinter import Tk, Canvas, Frame, Menu, filedialog


class Mycanvas():
    def __init__(self, master):
        self.last_pos = ()
        self.current_color = "black"

        self.w = Canvas(master, width=500, height=500)
        self.w.pack()
        self.w.bind("<Button-1>", self.onclick)
        self.w.bind("<B1-Motion>", self.onmove)
        self.w.bind("<ButtonRelease-1>", self.onmove)

    def draw(self, last, current):
        if not last:
            return

        self.w.create_line(*last, *current, fill=self.current_color)

    def onclick(self, event):
        self.last_pos = (event.x, event.y)

    def onmove(self, event):
        current_pos = (event.x, event.y)
        self.draw(self.last_pos, current_pos)
        self.last_pos = current_pos

    def onrelease(self, event):
        current_pos = ()

    def clear(self):
        self.w.delete("all")

    def save(self):
        file_selected = filedialog.asksaveasfilename()
        self.w.postscript(file=file_selected, colormode='color')
        print("saved", file_selected)

    def set_color(self, color):
        self.current_color = color


master = Tk()
c = Mycanvas(master)

menubar = Menu(master)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=c.clear)
filemenu.add_command(label="Save as...", command=c.save)
filemenu.add_separator()
filemenu.add_command(label="Close", command=master.destroy)
menubar.add_cascade(label="File", menu=filemenu)

color_menu = Menu(menubar, tearoff=0)
color_menu.add_command(label="Red", command=lambda: c.set_color("red"))
color_menu.add_command(label="Black", command=lambda: c.set_color("black"))
color_menu.add_command(label="Blue", command=lambda: c.set_color("blue"))
color_menu.add_command(label="Green", command=lambda: c.set_color("green"))
menubar.add_cascade(label="Colors", menu=color_menu)


master.config(menu=menubar)
master.mainloop()