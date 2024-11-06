hari_senin = [
    ["Upacara", "PJOK", "BAHASA INDONESIA", "PENDIDIKAN AGAM BUDI PEKERTI"],
    [" - 07:00-11:15", " - 11:13-13:30", " 13:30 - 14:40", " 14:30-15:30 "],
    ["- Pembina Upacara", " - mochammad faujan nur akbar", " - uswatun hassanah", " - Amrinah Rosyadah"]
]

hari_selasa = [
    ["REKAYASA TEKNOLOGI", "SENTRA PEMOGRAMAN PYTHON 2", "PENDIDIKAN PANCASILA", "K3LH"],
    [" - 07:00-08:30", " - 08:30-11:15", " - 11:15-13:45", " - 13:45-15:30"],
    ["Pak anggi kresna", " - Apdaniel Alamsyah", " - lindah setiyana", " - ihsan abdul akbar"]
]

hari_rabu = [ 
    ["PROJEK ILMU PENGETAHUAN (IPAS)", "P5.1", "MANAJEMEN PROYEK", "BIMBINGAN KONSELING"],
    [" - 07:00-09:15", " - 09:15-12:30", " - 12:30-13:45", " - 13:45-15:15", " - 15:15-15:30"],
    ["- nur putri ningsih", " - intan rizky", " - abdul kholki", " - desi nuraini"]
]

hari_kamis = [ 
    ["SEJARAH", "PEMOGRAMAN BERBASIS OBJEK", "SENI BUDAYA", "DASAR PEMOGRAMAN (PEMDAS)"],
    [" - 07:00-09:15", " - 09:15-11:15", " - 11:15-13:45", " - 13:45-15:30"],
    ["- afri ratnaningsih", " - alzaro rashad", " - pasaor pasaribuan", " - apdaniel alamsyah"]
]

hari_jumat = [
    ["AKTIVITAS JUMAT", "INFORMATIKA", "MATEMATIKA", "BAHASA INGGRIS"],
    [" - 07:00-07:45", " - 07:45-10:00", " - 10:30-13:45", " - 13:45-15:05"],
    ["- ihsan abdul akbar", " - Een rohenan", " - ", " - MR azzis"]
]

print('\n')
print('=== HARI KAMIS===')
# Menambahkan "piket" di baris pertama
hari_kamis[0].insert(0, "Piket")

# Menambahkan "06:00-07:00" di baris ke-2
hari_kamis[1].insert(0, "06:00-07:00")

# Menambahkan "Diala" di baris ke-3
hari_kamis[2].insert(0, "Dimas")

# Mencetak hasil
for row in hari_selasa:
    print(row)
print('=== HARI SENIN ===')
# Data yang akan ditambahkan
eskul_floorball = "Eskul Floorball"
waktu_floorball = "16:00-17:00"
nama_floorball = "Coach Fajar aulia"

# Menambahkan elemen ke dalam daftar menggunakan append
hari_senin[0].append(eskul_floorball)
hari_senin[1].append(waktu_floorball)
hari_senin[2].append(nama_floorball)

# Menampilkan daftar setelah penambahan
for row in hari_senin:
    print(row)

print('\n')
print('=== UPACARA ===')
print('- Senin')
print(hari_senin[1][0], '|', hari_senin[2][0])
print('\n')

print('=== MATEMATIKA ===')
print("- JUMAT ")
print(hari_jumat[1][2], '|', hari_jumat[2][2])
print('\n')

print('=== PENDIDIKAN PANCASILA ===')
print("- SELASA ")
print(hari_selasa[1][2], '|', hari_selasa[2][2])
print('\n')

print('=== PENDIDIKAN JASMANI ===')
print("- SENIN ")
print(hari_senin[1][3], '|', hari_senin[2][3])
print('\n')

print('=== DASAR PEMOGRAMAN ===')
print("- KAMIS ")
print(hari_kamis[1][3], '|', hari_kamis[2][3])
print('\n')

print('=== KELAS SENTRA PEMROGRAMAN PYTHON 2 ===')
print("- SELASA ")
print(hari_selasa[1][1], '|', hari_selasa[2][1])
print('\n')

print('=== SENI DAN BUDAYA ===')
print("- KAMIS ")
print(hari_kamis[1][2], '|', hari_kamis[2][2])
print('\n')

print('=== BAHASA INGGRIS ===')
print("- JUMAT ")
print(hari_jumat[1][3], '|', hari_jumat[2][3])
print('\n')

print('=== PENDIDIKAN AGAMA ===')
print("- SENIN ")
print(hari_senin[1][2], '|', hari_senin[2][2])
print('\n')

print('=== MEDIA DAN ALAT UKUR ===')
print("- KAMIS ")
print(hari_kamis[1][1], '|', hari_kamis[2][1])
print('\n')

print('=== BAHASA INDONESIA ===')
print("- RABU ")
print(hari_rabu[1][2], '|', hari_rabu[2][2])
print('\n')

print('=== BIMBINGAN KONSELING ===')
print("- RABU ")
print(hari_rabu[1][3], '|', hari_rabu[2][3])
print('\n')

print('=== PROJEK ILMU PENGETAHUAN (IPAS) ===')
print("- RABU ")
print(hari_rabu[1][0], '|', hari_rabu[2][0])
print('\n')

print('=== TEKNOLOGI JARINGAN K3LH ===')
print("- KAMIS ")
print(hari_kamis[1][0], '|', hari_kamis[2][0])
print('\n')

print('=== P5.1 ===')
print("- KAMIS ")
print(hari_kamis[1][1], '|', hari_kamis[2][1])
print('\n')

print('=== SEJARAH ===')
print("- KAMIS ")
print(hari_kamis[1][2], '|', hari_kamis[2][2])
print('\n')

print('=== PEMBIASAAN JUMAT ===')
print("- JUMAT ")
print(hari_jumat[1][0], '|', hari_jumat[2][0])
print('\n')

print('=== INFORMATIKA ===')
print("- JUMAT ")
print(hari_jumat[1][1], '|', hari_jumat[2][1])
print('\n')

print('=== IPAS ===')
print("- RABU ")
print(hari_rabu[1][0], '|', hari_rabu[2][0])
print('\n')

print('=== MANAJEMEN PROYEK ===')
print("- RABU ")
print(hari_rabu[1][2], '|', hari_rabu[2][2])
print('\n')
