from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image

# Membuat list hunians yang berisi objek Apartemen, Rumah, dan Indekos
hunians = []
hunians.append(Apartemen("Nelly Joy", 3, 3, "D:/Fadhil/Computer Science/semester-4/dpbo/code/python/latihan/assets/images/hunian1.png"))
hunians.append(Rumah("Sekar MK", 5, 2, "D:/Fadhil/Computer Science/semester-4/dpbo/code/python/latihan/assets/images/hunian2.png"))
hunians.append(Indekos("Bp. Romi", "Cahya", "D:/Fadhil/Computer Science/semester-4/dpbo/code/python/latihan/assets/images/hunian3.png"))
hunians.append(Rumah("Satria", 1, 4, "D:/Fadhil/Computer Science/semester-4/dpbo/code/python/latihan/assets/images/hunian4.png"))

# Membuat fungsi utama
def main():

    # Membuat fungsi details(index) yang akan menampilkan detail hunian ketika tombol Details di klik
    def details(index):
        top = Toplevel()
        top.title("Detail " + hunians[index].get_jenis())

        # Membuat label-frame untuk menampilkan data hunian
        d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
        d_frame.pack(padx=10, pady=10)

        # Menampilkan summary, info, dan dokumen hunian
        d_summary = Label(d_frame, text="Summary: " + hunians[index].get_summary(), anchor="w").grid(row=0, column=0, sticky="w")
        d_info = Label(d_frame, text= hunians[index].get_info(), anchor="w").grid(row=1, column=0, sticky="w")
        d_dokumen = Label(d_frame, text="Dokumen: " + hunians[index].get_dokumen(), anchor="w").grid(row=2, column=0, sticky="w")

        # Menampilkan foto hunian jika ada
        if hunians[index].get_foto():
            img = Image.open(hunians[index].get_foto())
            img = img.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)

            img_label = Label(top, image=photo)
            img_label.image = photo
            img_label.pack()

        # Menampilkan tombol Close untuk menutup jendela detail hunian
        btn = LabelFrame(top, padx=0, pady=0)
        btn.pack(padx=10, pady=10)
        b_close = Button(btn, text="Close", command=top.destroy)
        b_close.grid(row=0, column=0)

    root = Tk()
    root.title("LP9DPBO2023 - Muhammad Fadhillah Nursyawal")

    # Membuat frame untuk menampilkan data seluruh hunian
    frame = LabelFrame(root, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    opts = LabelFrame(root, padx=10, pady=10)
    opts.pack(padx=10, pady=10)

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=root.quit)
    b_exit.grid(row=0, column=1)

    # Menampilkan data hunian pada frame
    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        # Menampilkan nama pemilik atau nama penghuni tergantung jenis hunian
        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        # Menampilkan tombol Details untuk setiap hunian
        b_detail = Button(frame, text="Details ", command=lambda index=index: details(index))
        b_detail.grid(row=index, column=3)

    root.mainloop()

# Menjalankan fungsi utama jika script ini dijalankan secara langsung
if __name__ == '__main__':
    main()
