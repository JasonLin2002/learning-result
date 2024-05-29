import os
import tkinter as tk
from tkinter import filedialog

def choose_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.delete(0, tk.END)  # 清除之前的文字
    folder_entry.insert(0, folder_selected)  # 插入新選擇的文字

def apply_removal():
    folder_path = folder_entry.get()
    remove_word = remove_word_entry.get()
    if not folder_path or not remove_word:
        result_label.config(text="請輸入資料夾路徑和要移除的字元")
        return

    for root, dirs, files in os.walk(folder_path):
        # 更新資料夾名稱
        for dir_name in dirs:
            if remove_word in dir_name:
                new_dir_name = dir_name.replace(remove_word, '')
                os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))
                result_label.config(text=f"已從資料夾名稱 '{dir_name}' 中移除特定字彙。")

        # 更新檔案名稱
        for file_name in files:
            if remove_word in file_name:
                new_file_name = file_name.replace(remove_word, '')
                os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))
                result_label.config(text=f"已從檔案名稱 '{file_name}' 中移除特定字彙。")

    result_label.config(text="處理完成。")

# 創建主視窗
root = tk.Tk()
root.title("資料夾選擇器")

# 創建一個標籤
folder_label = tk.Label(root, text="輸入資料夾位址:")
folder_label.pack(pady=10)

# 創建一個Entry元件，用來輸入資料夾位址
folder_entry = tk.Entry(root, width=40)
folder_entry.pack(pady=10)

# 創建一個選擇資料夾的按鈕
button_choose = tk.Button(root, text="選擇資料夾", command=choose_folder)
button_choose.pack(pady=10)

# 創建一個標籤，說明要移除的字元
remove_word_label = tk.Label(root, text="輸入要移除的字元:")
remove_word_label.pack(pady=10)

# 創建一個Entry元件，用來輸入要移除的字元
remove_word_entry = tk.Entry(root, width=40)
remove_word_entry.pack(pady=10)

# 創建一個套用按鈕，當按下時呼叫apply_removal函數
button_apply = tk.Button(root, text="套用", command=apply_removal)
button_apply.pack(pady=10)

# 創建一個標籤，顯示結果
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# 啟動主迴圈
root.mainloop()
