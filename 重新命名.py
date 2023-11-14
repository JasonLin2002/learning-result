import os

def rename_files_in_folder(folder_path, start_index):
    files = os.listdir(folder_path)

    for i, file_name in enumerate(files, start=start_index):
        _, file_extension = os.path.splitext(file_name)
        new_name = f"{i:03d}{file_extension}"
        
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)

if __name__ == "__main__":
    # 設定第一個資料夾路徑和起始索引
    folder1_path = r"C:\Users\jk121\Documents\臨時下載\[ポロリビスタ] 煽り男 file 1-8 [中国翻訳]"
    start_index_folder1 = 1

    # 設定第二個資料夾路徑和起始索引
    folder2_path = r"C:\Users\jk121\Documents\臨時下載\[ポロリビスタ] 煽り男9 (COMIC クリベロン DUMA 2023年8月号 Vol.51) [中国翻訳]"
    start_index_folder2 = 219

    # 重命名第一個資料夾中的圖檔
    rename_files_in_folder(folder1_path, start_index_folder1)

    # 重命名第二個資料夾中的圖檔
    rename_files_in_folder(folder2_path, start_index_folder2)
