kecepatan = float(input("Masukkan kecepatan internet Anda (dalam Mbps): "))

if kecepatan >= 100:
    print("Koneksi Luar Biasa")
elif (kecepatan >= 50 and kecepatan < 100):
    print("Koneksi Baik")
elif (kecepatan >= 10 or kecepatan >= 6):
    print("Koneksi Cukup")
else:
    print("Koneksi Lambat")
