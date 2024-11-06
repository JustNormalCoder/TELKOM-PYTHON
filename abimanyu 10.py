print(" =======1. mendeklarasikan variabel dan mengecek tipe data======")
#deklarasi variabel dengan tipe data yang berbeda beda
nama = "dimas"
umur = 15
tinggi = 168.5
is_student = True
#penampilan nilai variabel
print("Nama:", nama)
print("Umur:" , umur)

print("Tinggi badan:", tinggi)
print("maha siswa:" , is_student)

#mengecek tipe data dari variabel yang di deklarasikan
print(type(nama)) # tipe data str (string)
print(type(umur)) # tipe data int(integer)
print(type(tinggi)) # tipe data float 
print(type(is_student)) # tipe data bool (boolean)

print( "===== 2. operasi aritmatika pada variabel =====" )
#deklrasi dua variabel numarik
bilangan1 = 15
bilangan2 = 4

#melakukan operasi aritmatika
penjumlahan = bilangan1 + bilangan2
pengurangan = bilangan1 - bilangan2
perkalian = bilangan1 * bilangan2
membagi =  bilangan1 / bilangan2
pembagian_bulat = bilangan1 // bilangan2
modulus = bilangan1 % bilangan2

#menampilkan hasil operasi
print("penjumlahan:", penjumlahan)
print("pengurangan:", pengurangan)
print("perkalian :", perkalian)
print("pembagian", membagi)
print("pembagian bulat:", pembagian_bulat)
print("modulus :", modulus)


print( "============= 3.mengonversi Tipe Data    ============")
#variabel bertipa string yang berisi angka
angka_str = "100"

#konversqi dari string ke integer dan float
angka_int = int(angka_str) #konversi ke integer
angka_float = float(angka_str) #konversi ke float

 #menampilkan hasil konversi
print("setelah konversi ke int:", angka_int)
print("setelah konversi ke float")

  #operasi setelah konversi
hasil_tambah = angka_int + 50
hasil_kali = angka_float * 1.5

print("hasil setelah hasil tambah:", hasil_tambah)
print("setelah hasil kali:", hasil_kali)


print ("===============4. Mengecekan kondisi dengan boolean   =============")
#variabel boolean
cuaca_hujan = True

#mengunakan if-else untuk pengecekan kondisi
if cuaca_hujan:
 print("bawa payung!")
else:
   print("tidak usah bawa payung")


print("==============5. mengunakan dictionary ===========")
#deklarasi dictionary dengan informasi personal

data_diri = {
    "nama": "dimas abimanyu",
    "umur": 25,
    "kota": "jakarta",


#mengakses nilai menggunakan kunci
print("nama:", data_diri["nama"])
print("umur:", data_diri["umur"])

#menambahkan elem baru ke dalam dictionary
data_diri["pekerjaan"] = "programmer"
print("setelah menambahkan pekerjaan:", data_diri)

#mengubah nilai pada kunci tertentu
data_diri["kota"] = "Medan"
print("setelah menganti kota:", data_diri)    
}
      

  
print("==============5. menggunakan dictionary ===========")
# deklarasi dictionary dengan informasi personal

data_diri = {
    "nama": "dimas abimanyu",
    "umur": 25,
    "kota": "jakarta"
}

# mengakses nilai menggunakan kunci
print("nama:", data_diri["nama"])
print("umur:", data_diri["umur"])

# menambahkan elemen baru ke dalam dictionary
data_diri["pekerjaan"] = "programmer"
print("setelah menambahkan pekerjaan:", data_diri)

# mengubah nilai pada kunci tertentu
data_diri["kota"] = "Medan"
print("setelah mengganti kota:", data_diri)
