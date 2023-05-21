import tkinter as tk
from tkinter import filedialog
from tkinter import *
import random
from math import gcd
import sys
import subprocess
import os




#=================setup cua so===

main_windows = tk.Tk()
main_windows.title("Chữ Ký Số")
main_windows.geometry("800x650")
main_windows.config(bg="#00768c")




def kiemtra():
    # Gọi lệnh để chạy tệp child.py
    subprocess.Popen(['python', 'kiemtra.py'])
    sys.exit()


#================Backend========
def layfile():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()
    text_noidung.delete('1.0', END)
    text_noidung.insert(END, file_content)

def layfile1():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r', encoding="utf-8") as file:
        file_content = file.read()
    text_vanbangocc.delete('1.0', END)
    text_vanbangocc.insert(END, file_content)




# sinh số ngẫu nhiên cho p và q
def prime_number():
    while True:
        #ramdon so ngau nhien
        number = random.randint(1, 150)
        if is_prime(number):
            return number
def is_prime(n):
    if n <= 1:
        return False
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def sinhkhoangaunhien():
    p = prime_number()
    q = prime_number()
    text_p.delete(0, tk.END)
    text_p.insert(tk.END, str(p))
    text_q.delete(0, tk.END)
    text_q.insert(tk.END, str(q))
#============================================================================

# khi có 2 số nguyên tố p và q ta tiền hành sinh khóa

def generate_rsa_key():
    p = int(text_p.get())
    q = int(text_q.get())

    n = p * q
    phi = (p - 1) * (q - 1)
    e = find_coprime(phi)
    d = find_mod_inverse(e, phi)
    public_key = (n, e)
    private_key = (n, d)

    text_key.delete(0, tk.END)
    text_key.insert(tk.END, str(public_key))

    text_keyy.delete(0, tk.END)
    text_keyy.insert(tk.END, str(private_key))

def find_coprime(phi):
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            return e

def find_mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

def encrypt_message():
    message = text_noidung.get("1.0", "end-1c")  # Lấy thông điệp từ đối tượng Text
    public_key = text_keyy.get()  # Lấy khóa công khai từ ô nhập liệu
    public_key = public_key.replace("(", "").replace(")", "")  # Xóa dấu ngoặc đơn trong khóa công khai
    n, e = map(int, public_key.split(','))  # Chuyển đổi khóa công khai thành e và n
    encrypted_message = [pow(ord(char), e, n) for char in message]  # Mã hóa thông điệp
    encrypted_text = ' '.join(map(str, encrypted_message))  # Chuyển đổi thành chuỗi số nguyên
    text_noidungdaky.delete("1.0", "end")  # Xóa nội dung cũ trong đối tượng Text
    text_noidungdaky.insert("1.0", encrypted_text)  # Hiển thị số nguyên mã hóa lên đối tượng Text


def decrypt_message():
    encrypted_text = text_vanbangocc.get("1.0", "end-1c")  # Lấy số nguyên mã hóa từ đối tượng Text
    encrypted_message = list(map(int, encrypted_text.split()))  # Chuyển đổi số nguyên mã hóa thành danh sách
    private_key = text_key.get()  # Lấy khóa riêng tư từ ô nhập liệu
    private_key = private_key.replace("(", "").replace(")", "")  # Xóa dấu ngoặc đơn trong khóa riêng tư
    n, d = map(int, private_key.split(','))  # Chuyển đổi khóa riêng tư thành n và d
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]  # Giải mã từng số nguyên
    decrypted_text = ''.join(decrypted_message)  # Chuyển đổi thành chuỗi thông điệp đã giải mã
    text_vanbangoc.delete("1.0", "end")  # Xóa nội dung cũ trong đối tượng Text
    text_vanbangoc.insert("1.0", decrypted_text)  # Hiển
def xuatfile():
    content = text_noidungdaky.get("1.0", "end-1c")  # Lấy nội dung từ ô văn bản
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    # Hiển thị hộp thoại để chọn đường dẫn và tên tệp tin lưu

    if filepath:
        with open(filepath, "w") as file:
            file.write(content)  # Ghi nội dung vào tệp tinn

def xuatfile1():
    content = text_vanbangoc.get("1.0", "end-1c")  # Lấy nội dung từ ô văn bản
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    # Hiển thị hộp thoại để chọn đường dẫn và tên tệp tin lưu

    if filepath:
        with open(filepath, "w") as file:
            file.write(content)  # Ghi nội dung vào tệp tinn

def showkey():
    if show_password_var.get():
        text_key.config(show="")
    else:
        text_key.config(show="*")
#=================setup giao dien===

#Nội dung cần ký
lable_canky = tk.Label(main_windows,bg="#D3D3D3",width=13,height=2, text="Văn bản cần ký:")
lable_canky.place(x=3, y=30)
text_noidung = tk.Text(main_windows, width=75, height=2, borderwidth=0)
text_noidung.place(x=105, y=30)

#xác thực văn bản ==============
lable_vanbangocc = tk.Label(main_windows,bg="#D3D3D3",width=13,height=2, text="Xác Thực:")
lable_vanbangocc.place(x=3, y=400)
text_vanbangocc = tk.Text(main_windows, width=75, height=2, borderwidth=0)
text_vanbangocc.place(x=105, y=400)


#Kiểm tra xác thực

lable_vanbangoc = tk.Label(main_windows,bg="#D3D3D3",width=13,height=2, text="Văn bản gốc:",)
lable_vanbangoc.place(x=3, y=470)
text_vanbangoc = tk.Text(main_windows, width=75, height=2, borderwidth=0)
text_vanbangoc.place(x=105, y=470)

#nội dung cần mã hóa
lable_canmahoa = tk.Label(main_windows,bg="#D3D3D3",width=13,height=2, text="Văn bản đã ký")
lable_canmahoa.place(x=3, y=230)
text_noidungdaky = tk.Text(main_windows, width=75, height=2, borderwidth=0)
text_noidungdaky.place(x=105, y=230)


#Sinh khóa
lable_sinhkhoa = tk.Label(main_windows,text="Khóa mã hóa",bg="#D3D3D3", width=13, height=2)
lable_sinhkhoa.place(x=3, y=100)
#Khóa bí mật
lable_key = tk.Label(main_windows, text="1. private key:",width=23, fg="red")
lable_key.place(x=120, y=103)
text_key = tk.Entry(main_windows,show="*",width=14, borderwidth=0)
text_key.place(x=120, y=127)

lable_rac = tk.Label(main_windows, height=5, bg="white")
lable_rac.place(x=300, y=103)

lable_rac1 = tk.Label(main_windows, height=5, bg="white")
lable_rac1.place(x=620, y=103)

lable_rac2 = tk.Label(main_windows, text="---------------------------------------", width=114, bg="black", fg="red")
lable_rac2.place(x=0, y=350)
#==================================
lable_key = tk.Label(main_windows, text="2. public key:",width=41, fg="red")
lable_key.place(x=320, y=103)
lable_p = tk.Label(main_windows, text="p",bg="#D3D3D3",width=5, height=1)
lable_p.place(x=320, y=127)
text_p = tk.Entry(main_windows, width=10,borderwidth=0)
text_p.place(x=365, y=127)
#=======================
lable_q = tk.Label(main_windows, text="q",bg="#D3D3D3",width=5, height=1)
lable_q.place(x=320, y=150)
text_q = tk.Entry(main_windows, width=10,borderwidth=0)
text_q.place(x=365, y=150)

lable_sinhkhoaa = tk.Label(main_windows, text="Sinh khóa",bg="#D3D3D3",width=22, height=1)
lable_sinhkhoaa.place(x=450, y=127)
text_keyy = tk.Entry(main_windows, width=14,borderwidth=0)
text_keyy.place(x=450, y=150)



#=================Giao dien chưc nang======
button_canky = tk.Button(main_windows, text= "Chọn File", bg="red", fg="white", width=11, height=1,command=layfile)
button_canky.place(x=710, y=34)
button_xuatfile = tk.Button(main_windows, text= "Xuất File", bg="red", fg="white", width=11, height=1,command=xuatfile)
button_xuatfile.place(x=710, y=234)

button_xacthuc = tk.Button(main_windows, text= "Chọn File", bg="red", fg="white", width=11, height=1,command=layfile1)
button_xacthuc.place(x=710, y=404)

button_vanbangoc = tk.Button(main_windows, text= "Xuất File", bg="red", fg="white", width=11, height=1,command=xuatfile1)
button_vanbangoc.place(x=710, y=474)

button_kyvanban = tk.Button(main_windows, text="Mã Hóa", bg="red", fg="white",width=50,height=2, command=encrypt_message)
button_kyvanban.place(x=225, y=280)

button_kyvanban = tk.Button(main_windows, text="Kiểm tra", bg="red", fg="white",width=50,height=2,command=decrypt_message)
button_kyvanban.place(x=225, y=530)


show_password_var = tk.BooleanVar(value=False)
show_password_checkbox = tk.Checkbutton(main_windows, text="Show Key",bg="red", height=1, fg="white", variable=show_password_var, command=showkey)
show_password_checkbox.place(x=208, y=127)


button_sinhkhoa = tk.Button(main_windows, text="Sinh khóa", bg="red", fg="white", width=9, height=1, command=generate_rsa_key )
button_sinhkhoa.place(x=540, y=150)

button_sinhkhoangaunhien = tk.Button(main_windows, text="Ngẫu nhiên", bg="red", fg="white", width=10, height=1, command=sinhkhoangaunhien)
button_sinhkhoangaunhien.place(x=450, y=170)

button_cosotoanhoc = tk.Button(main_windows,text="Tính toàn vẹn", bg="red", fg="white", width=14, height=3, command=kiemtra)
button_cosotoanhoc.place(x=660, y=127)


main_windows.mainloop()