#!/usr/bin/env python3
import os, shutil, datetime

SRC = r"C:\xampp2\htdocs\Prueba5"
DEST = r"C:\Users\yoportres\Desktop\CarpetaDest"

def rename_and_copy():
    if not os.path.isdir(SRC):
        print('Source directory not found:', SRC)
        return
    os.makedirs(DEST, exist_ok=True)
    for entry in os.listdir(SRC):
        if entry.lower().endswith('.php'):
            src_path = os.path.join(SRC, entry)
            timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            new_name = f"{os.path.splitext(entry)[0]}_{timestamp}.php"
            dest_path = os.path.join(DEST, new_name)
            shutil.copy2(src_path, dest_path)
            print(f'Copied: {src_path} -> {dest_path}')

if __name__ == '__main__':
    rename_and_copy()
