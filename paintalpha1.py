from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os

root = Tk()
root.title("PAINT ALPHA")
root.geometry("1050x570+150+50")
root.config(bg="#f2f3f5")
root.resizable(False,False)

current_x = 0
current_y = 0
color = "black"
def click_xy(event):
    global current_x, current_y
    current_x = event.x
    current_y = event.y

def addline(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y), width=get_current_value(),
                       fill=color, capstyle=ROUND, smooth=True)
    current_x, current_y = event.x, event.y

def atualizar_cor(new_color):
    global color
    color = new_color

def novo_canvas():
    canvas.delete('all')

def inserir_imagem():
    global filename
    global f_img
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file")
    f_img = PhotoImage(file=filename)
    my_img = canvas.create_image(180, 50, image=f_img)
    root.bind("<B3-Motion>", my_callback)

def my_callback(event):
    global f_img
    f_img = PhotoImage(file=filename)
    my_img = canvas.create_image(event.x, event.y, image=f_img)

############ ICONES ############
imagem_icone = PhotoImage(file="logo.png")
root.iconphoto(False, imagem_icone)

# BARRA LATERAL #
barra_lateral = PhotoImage(file="color section.png")
Label(root, image=barra_lateral, bg="#f2f3f5").place(x=10, y=20)

borracha = PhotoImage(file="eraser.png")
Button(root, image=borracha, bg="#f2f3f5", command=novo_canvas).place(x=30, y=400)

click_para_importar = PhotoImage(file="addimage.png")
Button(root, image=click_para_importar, bg="white", command=inserir_imagem).place(x=30, y=450)

################ CORES ################
colors = Canvas(root, bg="#fff", width=37, height=300, bd=0)
colors.place(x=30, y=60)

def display_palette():
    colors_list = ['black', 'red', 'gray', 'brown4', 'orange', 'yellow', 'green', 'blue', 'purple']
    buttons = []
    for i, color in enumerate(colors_list):
        x = 10
        y = 10 + i * 30
        rect = colors.create_rectangle(x, y, x + 20, y + 20, fill=color)
        colors.tag_bind(rect, '<Enter>', lambda event, r=rect: colors.itemconfig(r, width=3, outline='white'))
        colors.tag_bind(rect, '<Leave>', lambda event, r=rect: colors.itemconfig(r, width=1, outline='black'))
        colors.tag_bind(rect, '<Button-1>', lambda event, c=color: atualizar_cor(c))
        buttons.append(rect)
    return buttons


display_palette()
#### MAIN SCREEM ####
canvas = Canvas(root, width=930, height=500, background="white", cursor="hand2")
canvas.place(x=100, y=10)

# borda azul
canvas.create_rectangle(3, 3, 930, 500, outline='#0078D7', width=2)

canvas.bind('<Button-1>', click_xy)
canvas.bind('<B1-Motion>', addline)

########################Passador e sensibilidade abaixo########################
current_value = DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())

def sensi_passador(event):
    value_label.configure(text=get_current_value())

passador_sensibilidade = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=sensi_passador,
                                   variable=current_value)
passador_sensibilidade.place(x=15, y=525)

# Sensibilidade do passador #
value_label = ttk.Label(root, text=get_current_value())
value_label.place(x=27, y=550)

root.mainloop()
