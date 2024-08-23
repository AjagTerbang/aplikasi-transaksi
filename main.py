from toko.toko import Toko
from transaksi.transaksi import Transaksi
from produk.produk import Produk

def tampilkan_menu():
    print("\nPilih opsi:")
    print("1. Tambah Produk")
    print("2. Hapus Produk")
    print("3. Tampilkan Daftar Produk")
    print("4. Buat Transaksi")
    print("5. Tampilkan Daftar Transaksi")
    print("6. Keluar")
def main():
    toko = Toko()
    transaksi = Transaksi()
    # Menu Utama
    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            id_produk = int(input("Masukkan ID produk: "))
            nama_produk = input("Masukkan nama produk: ")
            harga_produk = float(input("Masukkan harga produk: "))
            stok_produk = int(input("Masukkan stok produk: "))
            produk = Produk(id_produk, nama_produk, harga_produk, stok_produk)
            toko.tambah_produk(produk)
            print("Produk berhasil ditambahkan.")

        elif pilihan == '2':
            id_produk = int(input("Masukkan ID produk yang ingin dihapus: "))
            toko.hapus_produk(id_produk)
            print("Produk berhasil dihapus.")

        elif pilihan == '3':
            toko.tampilkan_daftar_produk()

        elif pilihan == '4':
            id_produk = int(input("Masukkan ID produk yang ingin dibeli: "))
            jumlah = int(input("Masukkan jumlah produk yang ingin dibeli: "))
            transaksi.buat_transaksi(toko, id_produk, jumlah)

        elif pilihan == '5':
            transaksi.tampilkan_transaksi()

        elif pilihan == '6':
            print("Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
