# LP9DPBO2023
Membuat program GUI menggunakan bahasa Python sesuai dengan spesifikasi soal [LP9](https://docs.google.com/document/d/1rc2_YO9uAd6Wbg_HMhEoSZEYHxxYvqHGu2mIgWSe4zE/edit)
---
- -
Saya Muhammad Fadhillah Nursyawal NIM 2107135 mengerjakan soal LP 9
dalam mata kuliah Desain Pemrograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

## Jawaban Soal
Latihan Praktikum tidak menggunakan Database, tapi harus mengirim bukti screenshot menjalankan contoh kode yang dikirim.  
Spesifikasi:
- Lengkapi fitur summary => udah pokonya
- Buat landing Page (button yg ngarah ke halaman daftar residen) => landing page awalnya di file `main.py` lalu dapat berpindah ke file `residen.py`
- Tampilin gambar => gambar ditampilkan dalam detail, jadi dalam kelas hunian ditambahkan atribut foto untuk nyimpen gambar, gambar ditampilkan dengan full nama path nya, kenapa gitu (karena error kalau engga)
```python
main_path = "D:/Fadhil/Computer Science/semester-4/dpbo/code/python/latihan/"

gambar1 = main_path + "assets/images/hunian1.png"
# ...
```
jadi kalau mau run programnya harus ngubah dulu path nya sesuai sama sistem
- Tambahin 1 metode yang masih relevan untuk setiap kelas => nambahin method get_info()

Record
[Video](lp9-dpbo.mkv)

## Desain Program
karena tidak buat baru jadi uml nya tidak dibuat.
Program ini menggunakan bahasa Python untuk menampilkan GUI nya, datanya ditampilkan dengan konsep OOP, berikut merupakan kelas kelasnya:
```yaml
Hunian
- jenis: string
- jml_penghuni: int
- jml_kamar: int
- foto: string
+ getter()

Rumah
- nama_pemilik: string
+ getter()

Apartemen
- nama_pemilik: string
+ getter()

Indekos
- nama_pemilik: string
- nama_penghuni: string
+ getter()

Rumah Inheritance Hunian
Apartemen Inheritance Hunian
Indekos Inheritance Hunian
```

## Penjelasan Alur
Berikut merupakan simulasi dari programnya:

1. program pertama dijalankan di file main.py, file tersebut akan menampilkan gambar dan button untuk menuju tampilan berikutnya
2. ketika di klik maka tampilan berikutnya merupakan data residen pada file residen.py. ini akan menampilkan data dari hunian dengan jenisnya masing masing, disampingnya bisa melihat detail dengan menekan tombol detail
3. detail akan ditampilkan dengan gambarnya juga

## Dokumentasi
Landing Page
![Alt text](screenshot/Screenshot%202023-05-27%20191748.png)

Data Hunian
![Alt text](screenshot/Screenshot%202023-05-27%20191755.png)

Detail
![Alt text](screenshot/Screenshot%202023-05-27%20191804.png)
