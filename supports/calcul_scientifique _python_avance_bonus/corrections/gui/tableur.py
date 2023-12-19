from tkinter import Tk, Entry, Frame, END, Label, N, S, W, E, Scale, OptionMenu, StringVar

import random

def debug(event):
    print(event)

FIELDS = ["id", "name", "age"]

data = (
    (1, "Matthieu", random.randint(5, 100)),
    (2, "Paul", random.randint(5, 100)),
    (3, "Yves", random.randint(5, 100)),
    (4, "Jacques", random.randint(5, 100)),
    (5, "Matthieu", random.randint(5, 100)),
    (6, "Paul", random.randint(5, 100)),
    (7, "Yves", random.randint(5, 100)),
    (8, "Jacques", random.randint(5, 100)),
    (9, "Matthieu", random.randint(5, 100)),
    (10, "Paul", random.randint(5, 100)),
    (11, "Yves", random.randint(5, 100)),
    (12, "Jacques", random.randint(5, 100)),
    (13, "Matthieu", random.randint(5, 100)),
    (14, "Paul", random.randint(5, 100)),
    (15, "Yves", random.randint(5, 100)),
    (16, "Jacques", random.randint(5, 100)),
)


def get_unique_names(data):
    return sorted(set([i[1] for i in data]), key=lambda row: row[1])

def filter_by_name(data, name):
    return [i for i in filter(lambda row: row[1] == name, data)]


def filter_by_max_age(data, age):
    return [row for row in data if row[2] > int(age)]


class Data:
    def __init__(self, root, data):
        self.root = root
        self.data = data

        self.current_data = []

        self.frame_control = Frame(root)
        self.frame_control.grid(row=1, sticky=N+S+E+W)
        self.init_control(self.data)

        self.frame_data = Frame(root)
        self.frame_data.grid(row=2, sticky=N+S+E+W)

        self.update_display(self.data)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)



    def init_control(self, data):
        Label(self.frame_control, text="Age max").grid(column=1, row=0)
        self.age_scale = Scale(self.frame_control, orient="horizontal", command=self.update_data_age)
        self.age_scale.grid(column=2, row=0)


        Label(self.frame_control, text="Name").grid(column=3, row=0)
        names = get_unique_names(self.data)
        self.selected_name = StringVar(self.frame_control)
        self.selected_name.set(names[0]) # default value
        self.name_option = OptionMenu(self.frame_control, self.selected_name, *names, command=self.update_data_name)
        self.name_option.grid(column=4, row=0)

    def update_data_name(self, name):
        data = filter_by_name(self.data, name)
        self.last_name = name
        self.update_display(data)
        self.selected_name = name

    def update_data_age(self, age):
        data = filter_by_max_age(self.data, age)
        self.update_display(data)

    def update_display(self, data):
        # poor man caching key
        if len(data) == len(self.current_data) and self.selected_name == self.last_name:
            return

        self.current_data = data

        for widget in self.frame_data.winfo_children():
            # from : https://stackoverflow.com/questions/15781802/python-tkinter-clearing-a-frame
            widget.destroy()


        # header
        for index, field in enumerate(FIELDS):
            Label(self.frame_data, text=field).grid(column=index, row=0)

        # data
        for index_row, user in enumerate(data, 1):
            print(user)
            id_ = user[0]
            for index_col, (field, name) in enumerate(zip(user, FIELDS)):
                entry = Entry(self.frame_data)
                entry.insert(0, str(field))
                entry.grid(column=index_col, row=index_row, sticky=N+S+E+W)
                entry.__field_name = name
                entry.__id = id_

        self.init_grid_responsive()

    def init_grid_responsive(self):
        for column in range(len(FIELDS)):
            self.frame_data.columnconfigure(column, weight=1)


if __name__ == "__main__":
    root = Tk()
    root.tk.call('tk', 'scaling', 2.0)
    d = Data(root, data)
    root.mainloop()