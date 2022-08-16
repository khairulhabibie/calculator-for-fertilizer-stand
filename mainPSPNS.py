# FUNGSI UTAMA
import pembeliPS as ps
import pembeliPNS as pns
import logIn

# menu
def menu():
    print("MENU UTAMA".center(50,"="))
    print("1. Pembeli Pupuk Subsidi (PS)")
    print("2. Pembeli Pupuk Non Subsidi (PNS)")
    print("3. Pembeli PS dan PNS")
    print("4. Selesai")
    pilih = input("Pilihan anda?: ")   
    return pilih

# loop
print("KIOS HIDAYAH".center(50,"="))
password = logIn.user()
if (password == 'hidayah'):
    pilih = password
    while (pilih != "4"):
        
        pilih = menu()
       
        if(pilih == "1"):
            ps.data()
        elif(pilih == "2"):
            pns.data()
        elif(pilih == "3"):
            ps.data()
            pns.data()
        elif(pilih == "4"):
            print("oke, terima kasih")
        else:
            pass
else:
    pass

print("AKHIR PROGRAM".center(50,"="))