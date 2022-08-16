## PUPUK BERSUBSIDI

import listHargaPNS as lh

# Hitung pembelian -sub karung
def npkPlusK(jumlah):
    biaya = (jumlah*lh.npkPlusKarung)
    return biaya
def ssK(jumlah):
    biaya = (jumlah*lh.ssKarung)
    return biaya
    
# Hitung pembelian -sub eceran
def npkPlusE(jumlah):
    biaya = (jumlah*lh.npkPlusEceran)
    return biaya
def ssE(jumlah):
    biaya = (jumlah*lh.ssEceran)
    return biaya