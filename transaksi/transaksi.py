from toko.toko import Toko

class Transaksi:
    def __init__(self):
        # list produk
        self.transaksi_list = []

    def buat_transaksi(self, toko, id_produk, jumlah):
        # Membuat Transaksi produk
        produk = toko.cari_produk(id_produk)
        if produk and produk.stok >= jumlah:
            produk.stok -= jumlah
            total_harga = produk.harga * jumlah
            self.transaksi_list.append({'id_produk': id_produk, 'jumlah': jumlah, 'total_harga': total_harga})
            print(f"\nTransaksi berhasil: Produk {produk.nama}, Jumlah {jumlah}, Total Harga {total_harga}")
        else:
            print("\nTransaksi gagal: Stok tidak mencukupi atau produk tidak ditemukan")

    def tampilkan_transaksi(self):
        print("\nDaftar Transaksi:")
        for transaksi in self.transaksi_list:
            print(f"ID Produk: {transaksi['id_produk']}, Jumlah: {transaksi['jumlah']}, Total Harga: {transaksi['total_harga']}")
