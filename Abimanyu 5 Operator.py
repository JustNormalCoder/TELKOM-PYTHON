print("##### BELAJAR OPERATOR #####")

print("# SENTRA PEMOGRAMAN PYTHON #")
print("Nama : Dimas Abimanyu")
print("Kelas : X TEL 08")

print("OPERATOR ARITMATIKA")
a = 10
b = 3

print(a + b) # Penjumlahan
print(a - b) # Pengurangan
print(a * b) # Perkalian
print(a / b) # Pembagian
print(a // b) # Pembagian Bulat
print(a % b) # Modulus
print(a ** b) # Eksponensial

print("\nOPERATOR PERBANDINGAN")
a = 10
b = 20

print(a == b) # Sama dengan
print(a != b) # Tidak sama dengan
print(a > b)  # Lebih besar dari
print(a < b)  # Lebih kecil dari
print(a >= b) # Lebih besar atau sama dengan
print(a <= b) # Lebih kecil atau sama dengan

print("\nOPERATOR LOGIKA")
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

print("\nOPERATOR PENUGASAN")
x = 10
x += 5  # Sama dengan x = x + 5
print(x) # Output: 15

x -= 3  # Sama dengan x = x - 3
print(x) # Output: 12

print("\nOPERATOR BITWISE")
a = 5  # 0101
b = 3  # 0011

print(a & b)  # AND -> 0001 -> 1
print(a | b)  # OR -> 0111 -> 7
print(a ^ b)  # XOR -> 0110 -> 6
print(~a)     # NOT -> (0101 + 1) -> -6
print(a << 1) # Shift Kiri -> 1010 -> 10
print(a >> 1) # Shift kanan -> 0010 -> 2

print("\nTotal harga barang setelah diskon")
harga_asli = float(input("Masukkan harga asli barang: "))
diskon = float(input("Masukkan persentase diskon: "))

harga_setelah_diskon = harga_asli - (harga_asli * (diskon / 100))
print(f"Harga setelah diskon adalah: {harga_setelah_diskon}")
