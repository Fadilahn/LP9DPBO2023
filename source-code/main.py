from tkinter import *
from PIL import ImageTk, Image
import residen

# fungsi untuk navigasi ke data residen
def open_residen_page():
    root.destroy()
    residen.main()

root = Tk()
root.title('LP9DPBO2023')

# Gambar
# Buka gambar dan atur ukurannya menjadi kecil
image = Image.open(r"D:\Fadhil\Computer Science\semester-4\dpbo\code\python\db_mysql\assets\images\img.jpg")
image = image.resize((320, 200))  # Atur ukuran gambar menjadi 200x200 piksel

# Buat objek PhotoImage dengan gambar yang sudah diubah ukurannya
img = ImageTk.PhotoImage(image)

# Tampilkan gambar di dalam label
image_label = Label(root, image=img)
image_label.pack()

# Frame
frm = LabelFrame(root, padx=10, pady=10)
frm.pack(padx=10, pady=10)

# Tombol
button = Button(frm, text='Go to Residen Page', command=open_residen_page)
button.pack()

root.mainloop()