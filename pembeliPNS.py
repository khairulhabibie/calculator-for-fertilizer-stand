## PEMBELI PUPUK NON SUBSIDI (PPNB)    I

import listHargaPNS as lh
import kalkulatorPNS as k

# input, hitung, tampilkan, dan opsi simpan(format = .txt) data 
def data():
    # tampilkan list harga
    lh.pupukNonSubsidi()
    
    # input
    print("BELI NPK PLUS".center(30,"="))
    while True :
        try:
            karungNPKplus = int(input("Berapa karung?\t\t: "))
            break
        except:
            print("\n"+"hanya menerima inputan angka!")

    while True:
        try:
            eceranNPKplus = int(input("Berapa kilogram?\t: "))
            break
        except:
            print("\n"+"hanya menerima inputan angka!")

    print("BELI SS".center(30,"="))

    while True:
        try:
            karungSS = int(input("Berapa karung?\t\t: "))
            break
        except:
            print("\n"+"hanya menerima inputan angka!")

    while True:
        try:
            eceranSS = int(input("Berapa kilogram?\t: "))
            break
        except:
            print("\n"+"hanya menerima inputan angka!")

    # hitung
    print("="*50)
    npkPlusK = k.npkPlusK(karungNPKplus)
    npkPlusE = k.npkPlusE(eceranNPKplus)
    ssK = k.ssK(karungSS)
    ssE = k.ssE(eceranSS)
    totalBiaya = npkPlusK+npkPlusE+ssK+ssE

    # tampilkan
    print("Harga",karungNPKplus,"karung NPK PLUS\t\t: Rp",f"{npkPlusK:>10,}")
    print("Harga",eceranNPKplus,"kilogram NPK PLUS\t: Rp",f"{npkPlusE:>10,}")
    print("Harga",karungSS,"karung SS\t\t: Rp",f"{ssK:>10,}")
    print("Harga",eceranSS,"kilogram SS\t\t: Rp",f"{ssE:>10,}")
    print("Total Biaya Pembelian".center(50,"="))
    print("Total biaya\t\t\t: Rp",f"{totalBiaya:>10,}")
    print("-"*50)
    
    # simpan ?
        # logData / save
    save = True
    while (save != False):
        save = input("Apakah data ingin disimpan [y/n]?: ")
        if save == "y":
            nama = input("Nama Pembeli\t\t: ")
            poktan = input("Kelompok Tani\t\t: ")
            tanggal = input("Tanggal\t\t\t: ")
        
            # log data pembeli .txt
            file = open(f"[PNS] {poktan} - {nama}.txt","w")
            file.write("\n"+"="*40)
            file.write(f"\nTanggal\t\t: {tanggal}" + "\n")
            file.write(f"Nama Pembeli\t: {nama}" + "\n")
            file.write(f"Kelompok Tani\t: {poktan}" + "\n" + "-"*40 + "\n")
            file.write(f"{karungNPKplus} karung NPK PLUS\t: Rp {npkPlusK:>10,}" + "\n")
            file.write(f"{eceranNPKplus} kilogram NPK PLUS\t: Rp {npkPlusE:>11,}" + "\n")
            file.write(f"{karungSS} karung SS\t\t: Rp {ssK:>10,}" + "\n")
            file.write(f"{eceranSS} kilogram SS\t\t: Rp {ssE:>11,}" + "\n" + "-"*40 + "\n")
            file.write(f"Total biaya\t\t: Rp {totalBiaya:>10,}" + "\n" + "="*40)
            file.close()
            print("="*50 + "\n" + "Data berhasil disimpan")
            break
        elif save == "n" :
            print("oke!,data tidak disimpan")
            break
        else:
            pass
    print("-"*50  + "\n" + "-"*50)
            