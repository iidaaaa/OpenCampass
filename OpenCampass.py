import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from playsound import playsound

global tk_img
global tk_img2
global wav1
global wav2
import pathlib

here = pathlib.Path(__file__).parent
print(here)

def wav(wav_gene):
    playsound(wav_gene)

def combo_selected(event):
    global tk_img
    global wav1
    img = Image.open(str(here) + "/img/" + combo.get() + ".jpg")        # 画像ファイルを開き、ファイル情報取得。text.jpgは任意に設定
    img = img.resize((img.width // 8, img.height // 8))
    wav1 = combo.get()
    tk_img = ImageTk.PhotoImage(img)

    canvas = tk.Canvas(app, width=200, height=200)        # 画像表示エリアの作成
    canvas.place(x=10, y=0)
    canvas.create_image(0, 0 , anchor = tk.NW, image=tk_img)        # 画像表示

def fnc_do_1(event):
    global wav1, wav2
    wav_gene = "from_" + wav1 + "_to_" + wav2 + "_sa1.wav"
    wav(str(here) + "/img/" + wav_gene)

def combo_selected2(event):
    print(combo2.get(),"が選択されました")
    print('111')
    global tk_img2
    global wav2
    img = Image.open(str(here) + "/img/" + combo2.get() + ".jpg")        # 画像ファイルを開き、ファイル情報取得。text.jpgは任意に設定
    img = img.resize((img.width // 8, img.height // 8))
    wav2 = combo2.get()
    tk_img2 = ImageTk.PhotoImage(img)


    canvas2.create_image(0, 0 , anchor = tk.NW, image=tk_img2)        # 画像表示

app = tk.Tk()
app.geometry("550x400")
# img = Image.open('sa1.jpg')        # 画像ファイルを開き、ファイル情報取得。text.jpgは任意に設定
# img = img.resize((img.width // 8, img.height // 8))
# tk_img = ImageTk.PhotoImage(img)

option = ["01M", "02M", "04M", "05F", "08F", "12M"] 
variable = tk.StringVar()
combo=ttk.Combobox(app,values=option,textvariable=variable)
combo.bind("<<ComboboxSelected>>",combo_selected)
combo.pack()
combo.place(x=50, y=200)



combo2=ttk.Combobox(app,values=option,textvariable=variable)
combo2.bind("<<ComboboxSelected>>",combo_selected2)
combo2.pack()
combo2.place(x=320, y=200)

canvas2 = tk.Canvas(app, width=200, height=200)        # 画像表示エリアの作成
canvas2.place(x=300, y=0)


btn = ttk.Button(app, text="変換")
 
# ボタン表示
btn.place(x=170, y=230, width=150, height=40)
 
# ボタンに関数をbind
btn.bind("<Button-1>", fnc_do_1)



app.mainloop()