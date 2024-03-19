import tkinter as tk
from tkinter import ttk
import os

def schedule_shutdown():
    # 獲取用戶輸入，如果輸入不是數字則預設為0
    hours = int(hours_entry.get() if hours_entry.get().isdigit() else 0)
    minutes = int(minutes_entry.get() if minutes_entry.get().isdigit() else 0)
    seconds = int(seconds_entry.get() if seconds_entry.get().isdigit() else 0)
    
    # 計算總秒數
    total_seconds = hours * 3600 + minutes * 60 + seconds
    
    # 檢查是否有設置時間
    if total_seconds > 0:
        # 安排關機
        os.system(f"shutdown -s -t {total_seconds}")
    else:
        print("請輸入有效的時間！")

# 創建主視窗
root = tk.Tk()
root.title("Windows 定時關機")

# 創建並放置小時輸入欄
tk.Label(root, text="小時:").grid(row=0, column=0)
hours_entry = tk.Entry(root)
hours_entry.grid(row=0, column=1)

# 創建並放置分鐘輸入欄
tk.Label(root, text="分鐘:").grid(row=1, column=0)
minutes_entry = tk.Entry(root)
minutes_entry.grid(row=1, column=1)

# 創建並放置秒數輸入欄
tk.Label(root, text="秒數:").grid(row=2, column=0)
seconds_entry = tk.Entry(root)
seconds_entry.grid(row=2, column=1)

# 創建並放置執行按鈕
execute_button = ttk.Button(root, text="執行", command=schedule_shutdown)
execute_button.grid(row=3, column=0, columnspan=2)

# 運行應用
root.mainloop()
