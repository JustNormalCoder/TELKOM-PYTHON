# meminta  pengguna memassukan angka
angka = int(input("Masukkan angka:"))
# menggunakan percabangan untuk menentukan genap atau ganjil
if angka % 2 == 0:
    print ("Bilangan Genap")

else:
    print("bilangan Ganjil")

# program pengulangan dengan while
# menghitung mundur dari 10 hingga 1
count = 10
while count > 0:
     print(count)
     count -= 1
print ("selesai menghitung mundur pak")

#program Mengunakan Break dan continue
# mencetk angka dari 1 hingga 10
for i in range(1, 11):
    if i == 5:
        continue #melewati angka 5
    print(i)

9
# Penangnan Masalah Dengan Try Dan Except
# meminta pengguna memasukkan angka dan menaganai inout

try:
    number = int(input("masukkan angka:"))
    print("angka yang dimasukkan salah", number)
except ValueError:
      print("input tidak valid, silakan masukkan angka")    


while True:
    print("/nKalkulator Sederhana")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = input("pilih operasi 1/2/3/4/5")
    if pilihan == '5':
       print ("Terimakasih telah mengunakan kalkulator kami")
       break
    num1 = float(input("masukkan lah angka pertama"))
    num2 = float(input("Masukkanlah angka kedua "))
    if pilihan ==  '1':
        print("hasil:", num1 + num2)
    elif pilihan == '2':
        print("hasil:", num1 - num2)
    elif pilihan == '3':
        print("hasil:", num1 * num2)
    elif pilihan == '4':
        if num2 != 0:
         print("hasil:", num1 / num2 )
    else:
        print("Tidak bisa dibagikan dengan 0")   

             

           
