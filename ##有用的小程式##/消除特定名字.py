import os

# 指定資料夾路徑和要移除的特定字彙
folder_path = r'D:\照片\H漫\分類'
common_word = '- 捷徑'

# 遍歷指定的資料夾及其內容
for root, dirs, files in os.walk(folder_path):
    # 更新資料夾名稱
    for dir_name in dirs:
        new_dir_name = dir_name.replace(common_word, '')
        os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))
        print(f"已從資料夾名稱 '{dir_name}' 中移除特定字彙。")

    # 更新檔案名稱
    for file_name in files:
        new_file_name = file_name.replace(common_word, '')
        os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))
        print(f"已從檔案名稱 '{file_name}' 中移除特定字彙。")

print("處理完成。")
