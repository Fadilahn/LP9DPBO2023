from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, foto=None):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, foto)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_info(self):
        return "Pemilik: " + self.nama_pemilik + f"\nJumlah Kamar: {self.jml_kamar}"