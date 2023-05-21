import tkinter as tk
import hashlib
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import sys
import subprocess

kiemtra_windows = tk.Tk()
kiemtra_windows.title("Chữ Ký Số")
kiemtra_windows.geometry("800x400")
kiemtra_windows.config(bg="#00768c")


#setup su kien=====================


def layfile():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()
    text_noidung1.delete('1.0', END)
    text_noidung1.insert(END, file_content)

def layfile1():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()
    text_noidung2.delete('1.0', END)
    text_noidung2.insert(END, file_content)


def compare_integrity():
    text1 = text_noidung1.get("1.0", "end-1c")  # Lấy nội dung từ ô text1
    text2 = text_noidung2.get("1.0", "end-1c")  # Lấy nội dung từ ô text2

    if hash(text1) == hash(text2):
        messagebox.showinfo("Thông báo", "Hai đoạn văn bản có tính toàn vẹn giống nhau.")
    else:
        messagebox.showinfo("Thông báo", "Hai đoạn văn bản không có tính toàn vẹn giống nhau.")



#def calculate_hash(text):
 #   text_bytes = text.encode("utf-8")
  #  hash_object = hashlib.sha256(text_bytes)
    #hash_value = hash_object.hexdigest()
    #return hash_value



def quoaylai():
    # Gọi lệnh để chạy tệp child.py
    subprocess.Popen(['python', 'Main.py'])
    sys.exit()


#lable_tieude = tk.Label(kiemtra_windows,text="Kiểm tra tính toàn vẹn!",bg="#D3D3D3", width=18, height=2)
#lable_tieude.place(x=320, y=5)
lable_tieude = tk.Label(kiemtra_windows,text="Kiểm tra tính toàn vẹn!",bg="red", fg="white", width=25, height=2)
lable_tieude.place(x=320, y=5)

lable_noidung1 = tk.Label(kiemtra_windows,bg="#D3D3D3",width=13,height=2, text="Văn bản 1:")
lable_noidung1.place(x=3, y=50)
text_noidung1 = tk.Text(kiemtra_windows, width=75, height=2, borderwidth=0)
text_noidung1.place(x=105, y=50)

lable_noidung2 = tk.Label(kiemtra_windows,bg="#D3D3D3",width=13,height=2, text="Văn bản 2:")
lable_noidung2.place(x=3, y=130)
text_noidung2 = tk.Text(kiemtra_windows, width=75, height=2, borderwidth=0)
text_noidung2.place(x=105, y=130)




#===========setup button

button_chonfile1 = tk.Button(kiemtra_windows, text="Chọn File", bg="#D3D3D3", width=10, command=layfile)
button_chonfile1.place(x=710, y=54)

button_chonfile2 = tk.Button(kiemtra_windows, text="Chọn File", bg="#D3D3D3", width=10,command=layfile1)
button_chonfile2.place(x=710, y=134)

button_kiemtra = tk.Button(kiemtra_windows, text="Kiểm Tra", bg="#D3D3D3", width=20, height=2,command=compare_integrity)
button_kiemtra.place(x=220, y=250)


buttom_quoaylai = tk.Button(kiemtra_windows, text="Quoay lại", bg="#D3D3D3", width=20, height=2, command=quoaylai)
buttom_quoaylai.place(x=440, y=250)

kiemtra_windows.mainloop()