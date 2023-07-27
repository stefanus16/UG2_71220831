def volumekubus(sisi):
    volume=sisi**3
    return volume
def volumetabung(diameter,tinggi):
    jari2=diameter/2
    volume=3.14 * jari2**2 *tinggi
    return volume
def volumebalok(panjang,lebar,tinggi):
    volume=panjang*lebar*tinggi
    return volume


print("==================== KALKULATOR CERDAS ====================")
print("Pilihlah bangun yang ingin anda hitung(inputan angka saja) :")
print("1. Tabung")
print("2. Kubus")
print("3. Balok")
    
pilihan=int(input(">>"))

if pilihan == 1:
    diameter=float(input("Masukan diameter(cm) : "))
    tinggi=float(input("Masukan tinggi(cm) : "))
    hasil = volumetabung(diameter,tinggi)
    print("Volume tabung adalah ",hasil," cm")
elif pilihan == 2:
    sisi=float(input("Masukan sisi(cm) : "))
    hasil=volumekubus(sisi)
    print("Volume kubus adalah ",hasil," cm")
elif pilihan == 3:
    panjang=float(input("Masukan panjang(cm) : "))
    lebar=float(input("Masukan lebar(cm) : "))
    tinggi=float(input("Masukan tinggi(cm) : "))
    hasil = volumebalok(panjang,lebar,tinggi)
    print("Volume balok adalah ",hasil," cm")
else:
    print("Inputan yang anda masukkan salah !!")
    

