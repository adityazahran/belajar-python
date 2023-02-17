# Kondisi if adalah kondisi yang akan dieksekusi oleh program jika bernilai benar atau TRUE

nilai = 9

# jika kondisi benar/TRUE maka program akan mengeksekusi perintah dibawahnya
if (nilai > 7):
    print("Anda lulus!")  # Kondisi Benar, Dieksekusi
else:
    print("Maaf Anda Tidak Lulus")

# Contoh penggunaan kondisi elif

hari_ini = "Minggu"

if (hari_ini == "Senin"):
    print("Saya akan kuliah")
elif (hari_ini == "Selasa"):
    print("Saya akan kuliah")
elif (hari_ini == "Rabu"):
    print("Saya akan kuliah")
elif (hari_ini == "Kamis"):
    print("Saya akan kuliah")
elif (hari_ini == "Jumat"):
    print("Saya akan kuliah")
elif (hari_ini == "Sabtu"):
    print("Saya akan kuliah")
elif (hari_ini == "Minggu"):
    print("Saya akan libur")
