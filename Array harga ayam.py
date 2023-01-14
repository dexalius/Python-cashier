# DATA PERMINTAAN
# AYAM DIJUAL UNTUK :
# DADA = 2500
# PAHA = 2000
# SAYAP = 1500
# PAJAK PEMBELIAN 10%
# DATA YANG PERLU DIINPUT BANYAK JENIS, JENIS POTONG, BANYAK BELI
# SESUAI TAMPILAN YANG DIINGINKAN 

# HEADER DATA
print("-" * 50)
print(" " * 14, "GEROBAK FRIED CHICKEN", " " * 14)
print("-" * 50)
print("Kode     Jenis Item      Harga")
print("-" * 35)
print(" D        Dada           Rp. 2500")
print(" P        Paha           Rp. 2000")
print(" S        Sayap          Rp. 1500")

# LIST
print(" ")
banyakJenis = int(input("Jumlah Jenis Yang Ingin Dibeli : "))
kodePotong = []
banyakPotong = []
jenisPotong = []
hargaPotong = []
jumlahHarga = []

# DATA ITEM YANG DIBELI
i = 0
while i < banyakJenis:

    print("*" * 35)
    
    print("Jenis ke - ", i+1)
    kodePotong.append(str(input("Dada / Paha / Sayap [D/P/S] : ")))
    banyakPotong.append(int(input("Banyaknya : ")))

    if kodePotong[i] == "D" or kodePotong[i] == "d" or kodePotong[i] == "Dada" or kodePotong[i] == "dada":
        jenisPotong.append("Dada")
        hargaPotong.append(2500)
        jumlahHarga.append(banyakPotong[i] * int(2500))
    elif kodePotong[i] == "P" or kodePotong[i] == "p" or kodePotong[i] == "Paha" or kodePotong[i] == "paha":
        jenisPotong.append("Paha")
        hargaPotong.append(2000)
        jumlahHarga.append(banyakPotong[i] * int(2000))
    elif kodePotong[i] == "S" or kodePotong[i] == "s" or kodePotong[i] == "Sayap" or kodePotong[i] == "sayap":
        jenisPotong.append("Sayap")
        hargaPotong.append(1500)
        jumlahHarga.append(banyakPotong[i] * int(1500))
    else:
        jenisPotong.append("Tidak Tersedia")
        hargaPotong.append(0)
        jumlahHarga.append(banyakPotong * int(0))
    i += 1


# OUTPUT PROSES-1
print("")
print("." * 50)
print("Data Sedang Diproses....")
print("." * 50)
print("")


# HEADER STRUK
print("=" * 50)
print(" " * 14, "GEROBAK FRIED CHICKEN", " " * 14)
print("-" * 50)
print("No     Jenis      Harga     Banyak     Jumlah")
print("       Potong     Satuan     Beli       Harga")
print("-" * 50)
template = ' {nomor}      {jenis_potong}      {harga}        {banyak_potong}        {imbuhan}{jumlah} '

# TEMPLATE ISIAN PEMBELANJAAN STRUK
a = 0
imbuhan = "Rp. "
while a < banyakJenis:
    nomor = a + 1
    print(template.format(nomor = nomor, jenis_potong = jenisPotong[a], harga = hargaPotong[a], banyak_potong = banyakPotong[a], imbuhan = imbuhan, jumlah = jumlahHarga[a]))
    a = a + 1

# PROSES TRANSAKSI
print("-" * 50)
totalPembelian = sum(jumlahHarga)
print("Total Pembelian : Rp. ",'{:>4}'.format(int(totalPembelian)))

jumlahPajak = totalPembelian * 0.1
totalBayar = totalPembelian + jumlahPajak

print("Pajak 10%       : Rp. ", '{:>4}'.format(int(jumlahPajak)))
print("Total Bayar     : Rp. ", '{:>4}'.format(int(totalBayar)))

# PROSES PEMBAYARAN
jumlahBayar = int(input("Jumlah Bayar    : Rp.  "))
kembali  = jumlahBayar - totalBayar
print("Uang Kembali    : Rp. ",'{:4>}'.format(int(kembali)))