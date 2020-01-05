import tkinter as tk


class Visualization(tk.Frame):
    """
        visualize the board on the screen

        Parameters
        ----------
        d: int
            size of the board
        loc: list
            the locations of sheep and sheep dogs in every step
    """

    def __init__(self, d, loc):
        tk.Frame.__init__(self)
        self.master.title("SheepDog")
        self.d = d
        self.pack(expand=tk.NO, fill=tk.BOTH)
        self.label_matrix = []
        self.cnt = 0
        self.l = tk.Label(text='step: ' + str(self.cnt))
        self.loc = loc
        self.init_step()

    def click_reset(self):
        self.label_matrix[self.loc[self.cnt][0][0]][self.loc[self.cnt][0][1]].configure(text=' ')
        self.label_matrix[self.loc[self.cnt][1][0]][self.loc[self.cnt][1][1]].configure(text=' ', fg='black')
        self.label_matrix[self.loc[self.cnt][2][0]][self.loc[self.cnt][2][1]].configure(text=' ', fg='black')
        self.cnt = 0
        self.label_matrix[self.loc[0][0][0]][self.loc[0][0][1]].configure(text='S')
        self.label_matrix[self.loc[0][1][0]][self.loc[0][1][1]].configure(text='D', fg='blue')
        self.label_matrix[self.loc[0][2][0]][self.loc[0][2][1]].configure(text='D', fg='red')
        self.l.configure(text='step: ' + str(self.cnt))

    def click_next(self):
        if self.cnt < len(self.loc) - 1:
            self.label_matrix[self.loc[self.cnt][0][0]][self.loc[self.cnt][0][1]].configure(text=' ')
            self.label_matrix[self.loc[self.cnt][1][0]][self.loc[self.cnt][1][1]].configure(text=' ', fg='black')
            self.label_matrix[self.loc[self.cnt][2][0]][self.loc[self.cnt][2][1]].configure(text=' ', fg='black')
            self.cnt += 1
            self.label_matrix[self.loc[self.cnt][0][0]][self.loc[self.cnt][0][1]].configure(text='S')
            self.label_matrix[self.loc[self.cnt][1][0]][self.loc[self.cnt][1][1]].configure(text='D', fg='blue')
            self.label_matrix[self.loc[self.cnt][2][0]][self.loc[self.cnt][2][1]].configure(text='D', fg='red')
            self.l.configure(text='step: ' + str(self.cnt))
        else:
            print("end")


    def init_step(self):
        frame1 = tk.Frame(bg='black')
        for i in range(self.d):
            label_list = []
            for j in range(self.d):
                label_list.append(tk.Label(frame1, text=" ", width=2, height=1, font=('Arial', 15)))
                label_list[j].grid(row=i, column=j, padx=1, pady=1)
            self.label_matrix.append(label_list)
        self.label_matrix[self.loc[0][0][0]][self.loc[0][0][1]].configure(text='S')
        self.label_matrix[self.loc[0][1][0]][self.loc[0][1][1]].configure(text='D', fg='blue')
        self.label_matrix[self.loc[0][2][0]][self.loc[0][2][1]].configure(text='D', fg='red')
        frame1.pack()
        frame2 = tk.Frame()
        self.next_button = tk.Button(frame2, text = 'next', width = 6, height = 1, command = self.click_next).pack(side='left')
        self.reset_button = tk.Button(frame2, text = 'reset', width = 6, height = 1, command = self.click_reset).pack(side='left')
        frame2.pack()
        self.l.pack()

