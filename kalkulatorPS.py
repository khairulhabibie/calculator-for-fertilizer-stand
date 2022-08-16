## PUPUK BERSUBSIDI

import listHargaPS as lh

# Hitung pembelian -sub karung
def ureaK(jumlah):
    biaya = (jumlah*lh.ureaKarung)
    return biaya
def npkK(jumlah):
    biaya = (jumlah*lh.npkKarung)
    return biaya
    
# Hitung pembelian -sub eceran
def ureaE(jumlah):
    biaya = (jumlah*lh.ureaEceran)
    return biaya
def npkE(jumlah):
    biaya = (jumlah*lh.npkEceran)
    return biaya