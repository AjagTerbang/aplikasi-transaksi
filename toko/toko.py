from produk.produk import Produk

class Toko:
    def __init__(self):
        # Menyimpan daftar produk
        self.daftar_produk = []

    def tambah_produk(self, produk):
         # Menambahkan produk baru ke daftar
        self.daftar_produk.append(produk)

    def hapus_produk(self, id):
        # Menghapus produk berdasarkan ID
        self.daftar_produk = [produk for produk in self.daftar_produk if produk.id != id]

    def tampilkan_daftar_produk(self):
        print("\nDaftar Produk:")
        for produk in self.daftar_produk:
            print(f"ID: {produk.id}, Nama: {produk.nama}, Harga: {produk.harga}, Stok: {produk.stok}")

    def cari_produk(self, id):
        # Mencari produk berdasarkan ID
        for produk in self.daftar_produk:
            if produk.id == id:
                return produk
        return None
