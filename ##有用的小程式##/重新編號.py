import os
import tkinter as tk
from tkinter import filedialog

def choose_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)  # 清除之前的文字
    folder_entry.insert(0, folder_selected)  # 插入新選擇的文字

def apply_rename():
    folder_path = folder_entry.get()
    start_index = int(start_index_entry.get())  # 從新的 Entry 中取得數字
    rename_files_in_folder(folder_path, start_index)

def rename_files_in_folder(folder_path, start_index):
    files = os.listdir(folder_path)

    for i, file_name in enumerate(files, start=start_index):
        _, file_extension = os.path.splitext(file_name)
        new_name = f"{i:03d}{file_extension}"
        
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

# 創建主視窗
root = tk.Tk()
root.title("資料夾選擇器")

# 創建一個標籤
label = tk.Label(root, text="輸入資料夾位址:")
label.pack(pady=10)

# 創建一個Entry元件，用來輸入資料夾位址
folder_entry = tk.Entry(root, width=40)
folder_entry.pack(pady=10)

label = tk.Label(root, text="重新命名編號:")
label.pack(pady=10)

# 創建一個數字限制的Entry元件，用來輸入起始索引
start_index_entry = tk.Entry(root, width=10, validate="key", validatecommand=(root.register(lambda char: char.isdigit() or char == ""), "%S"))
start_index_entry.pack(pady=10)
start_index_entry.insert(0, "1")  # 預設起始索引為1

# 創建一個按鈕，當按下時呼叫choose_folder函數
button_choose = tk.Button(root, text="選擇資料夾", command=choose_folder)
button_choose.pack(pady=10)

# 創建一個套用按鈕，當按下時呼叫apply_rename函數
button_apply = tk.Button(root, text="套用", command=apply_rename)
button_apply.pack(pady=10)

# 啟動主迴圈
root.mainloop()
