## PEMBELI PUPUK BERSUBSI (PPB)    I
import listHargaPS as lh
import kalkulatorPS as k

# input, hitung, tampilkan, dan opsi simpan(format = .txt) data 
def data():
    # tampilkan list harga
    lh.pupukSubsidi()
    
    # input
    print("BELI UREA".center(30,"="))
    while True :
        try:
            karungUrea = int(input("Berapa karung?\t\t: "))
            break
        except:
            print("\n"+"hanya menerima inputan angka!")

    while True:
        try:
            eceranUrea = int(input("Berapa kilogram?\t: "))
            break
        except:
            print("\n"+"hanya menerima inputan angka!")

    print("BELI NPK".center(30,"="))

    while True:
        try:
            karungNPK = int(input("Berapa karung?\t\t: "))
            break
        except:
            print("\n"+"hanya menerima inputan angka!")

    while True:
        try:
            eceranNPK = int(input("Berapa kilogram?\t: "))
            break
        except:
            print("\n"+"hanya menerima inputan angka!")

    # hitung
    print("="*50)
    ureaK = k.ureaK(karungUrea)
    ureaE = k.ureaE(eceranUrea)
    npkK = k.npkK(karungNPK)
    npkE = k.npkE(eceranNPK)
    totalBiaya = ureaK+ureaE+npkK+npkE

    # tampilkan
    print("Harga",karungUrea,"karung Urea\t: Rp",f"{ureaK:>10,}")
    print("Harga",eceranUrea,"kilogram Urea\t: Rp",f"{ureaE:>10,}")
    print("Harga",karungNPK,"karung NPK\t: Rp",f"{npkK:>10,}")
    print("Harga",eceranNPK,"kilogram NPK\t: Rp",f"{npkE:>10,}")
    print("Total Biaya Pembelian".center(50,"="))
    print("Total biaya\t\t: Rp",f"{totalBiaya:>10,}")
    print("-"*50)
    
    # simpan ?
        # logData / save
    save = True
    while (save != False):
        save = input("Apakah data ingin disimpan [y/n]?: ")
        if (save == "y"):
            nama = input("Nama Pembeli\t\t: ")
            poktan = input("Kelompok Tani\t\t: ")
            tanggal = input("Tanggal\t\t\t: ")
        
            # log data pembeli .txt
            file = open(f"[PS] {poktan} - {nama}.txt","w")
            file.write("\n"+"="*40)
            file.write(f"\nTanggal\t\t: {tanggal}" + "\n")
            file.write(f"Nama Pembeli\t: {nama}" + "\n")
            file.write(f"Kelompok Tani\t: {poktan}" + "\n" + "-"*40 + "\n")
            file.write(f"{karungUrea} karung Urea\t: Rp {ureaK:>10,}" + "\n")
            file.write(f"{eceranUrea} kilogram Urea\t: Rp {ureaE:>12,}" + "\n")
            file.write(f"{karungNPK} karung NPK\t: Rp {npkK:>10,}" + "\n")
            file.write(f"{eceranNPK} kilogram NPK\t: Rp {npkE:>12,}" + "\n" + "-"*40 + "\n")
            file.write(f"Total biaya\t: Rp {totalBiaya:>10,}" + "\n" + "="*40)
            file.close()
            print("="*50 + "\n" + "Data berhasil disimpan")
            break
        elif (save == "n") :
            print("oke!,data tidak disimpan")
            break
        else:
            pass    
    print("-"*50  + "\n" + "-"*50)