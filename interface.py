from tkinter import *
from tkinter import filedialog, messagebox
from autocorrelation import *


class Application:

    def __init__(self, master):
        self.master = master
        self.file_path1 = StringVar(master)
        self.file_path2 = StringVar(master)

        master.title('3D Навігація')
        self.master.geometry('750x300')

    def get_image_url1(self):
        filename1 = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("all files", "*.*"),
                                                          ("jpeg files", "*.jpg"),
                                                          ("png files", "*.png")))
        if filename1:
            self.file_path1.set(str(filename1))

    def get_image_url2(self):
        filename2 = filedialog.askopenfilename(initialdir="/", title="Select file",
                                               filetypes=(("all files", "*.*"),
                                                          ("jpeg files", "*.jpg"),
                                                          ("png files", "*.png")))
        if filename2:
            self.file_path2.set(str(filename2))


class EstimationHeight(Application):

    def __init__(self, master):
        Application.__init__(self, master)

        self.blank_label = Label(master, text="\n")
        self.blank_label.grid()
        self.top_label = Label(master, text="ВИЗНАЧЕННЯ ВИСОТИ ТА МАСШТАБУ", anchor=CENTER, font=('Arial', 13), width=50)
        self.top_label.grid(row=0, column=0)
        self.blank_label = Label(master, text="\n")
        self.blank_label.grid()

        self.label_etalon_scale = Label(master, text='Масштаб еталонного зображення (м/пікс): ', font=('Arial', 10), anchor='w')
        self.etalon_scale = Entry(master)
        self.label_etalon_scale.grid(row=2, column=0)
        self.etalon_scale.grid(row=2, column=1)
        self.blank_label = Label(master, text="\n")
        self.blank_label.grid()

        self.label_etalon_height = Label(master, text='Висота зйомки еталонного зображення (м): ', font=('Arial', 10), anchor='w')
        self.etalon_height = Entry(master)
        self.label_etalon_height.grid(row=4, column=0)
        self.etalon_height.grid(row=4, column=1)
        self.blank_label = Label(master, text="\n")
        self.blank_label.grid()

        self.label_get_image1 = Label(master, text='Еталонне зображення: ', font=('Arial', 10))
        self.label_get_image1.grid(row=6, column=0)
        self.get_image_button1 = Button(master, text='Пошук', command=self.get_image_url1)
        self.get_image_button1.grid(row=6, column=1)
        self.blank_label = Label(master, text="\n")
        self.blank_label.grid()

        self.label_get_image2 = Label(master, text='Вхідне зображення: ', font=('Arial', 10))
        self.label_get_image2.grid(row=8, column=0)
        self.get_image_button2 = Button(master, text='Пошук', command=self.get_image_url2)
        self.get_image_button2.grid(row=8, column=1)
        self.blank_label = Label(master, text="\n")
        self.blank_label.grid()

        self.submit_button = Button(master, text="Виконати", command=self.calculation,  fg='GREEN', font=('Arial', 10))
        self.submit_button.grid(row=10, column=1)

    def show_result(self, height, scale):
        messagebox.showinfo('Результати', 'Висота = {0:.2f} м\n\n '
                                          'Масштаб = {1:.2f} м/пікс'.format(height, scale))

        return 0

    def calculation(self):

        height, relation = estimation_height(str(self.file_path1.get()), str(self.file_path2.get()),
                                             float(self.etalon_height.get()))

        scale = float(self.etalon_scale.get())*relation

        self.show_result(height, scale)

    def __str__(self):
        return self.file_path1, self.file_path2


root = Tk()
my_gui = EstimationHeight(root)
root.mainloop()