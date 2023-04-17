import requests
from bs4 import BeautifulSoup
import tkinter as tk
import subprocess


def scrape_website():
    url = url_entry.get()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(str(soup))

def set_font_size():
    font_size = int(font_size_var.get())
    lab1.config(font=("Microsoft JhengHei", font_size))
    lab2.config(font=("Microsoft JhengHei", font_size))
    url_entry.config(font=("Microsoft JhengHei", font_size))
    btn1.config(font=("Microsoft JhengHei", font_size))
    btn2.config(font=("Microsoft JhengHei", font_size))
    btn3.config(font=("Microsoft JhengHei", font_size))
    font_size_menu.config(font=("Microsoft JhengHei", font_size))

def open_calculater():
    subprocess.call(['python', '計算機.py'])

window = tk.Tk()
window.title("網頁爬蟲")
#window.geometry('300x300')


lab1 = tk.Label(window, text="輸入網址:")
lab2 = tk.Label(window, text="字體大小:")

url_entry = tk.Entry(window)

btn1 = tk.Button(window, text="爬取", command=scrape_website,width=8)
btn2 = tk.Button(window, text="套用", command=set_font_size,width=8)
btn3 = tk.Button(window, text="計算機", command=open_calculater,width=8)

font_size_var = tk.StringVar()
font_size_var.set("10")
font_size_menu = tk.OptionMenu(window,font_size_var, *[i for i in range(10, 41, 2)])



lab1.grid(row=0,column=0,)
url_entry.grid(row=1,column=0,padx=1)
btn1.grid(row=1,column=2,padx=1)

lab2.grid(row=3,column=0,padx=1)
font_size_menu.grid(row=3,column=1,padx=1)
btn2.grid(row=3,column=2,padx=1)

btn3.grid(row=4,column=0)




window.mainloop()
