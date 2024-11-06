
# Schedule data and printing details

harisenin = (
    ("Upacara", "PJOK", "BAHASA INDONESIA", "PENDIDIKAN AGAM BUDI PEKERTI"),
    (" - 07:00-11:15", " - 11:13-13:30", " 13:30 - 14:40", " 14:30-15:30"),
    ("- Pembina Upacara", " - mochammad faujan nur akbar", " - uswatun hassanah", " - Amrinah Rosyadah"),
)
hariselasa = (
    ("REKAYASA TEKNOLOGI", "SENTRA PEMOGRAMAN PYTHON 2", "PENDIDIKAN PANCASILA", "K3LH"),
    (" - 07:00-08:30", " - 08:30-11:15", " - 11:15-13:45", " - 13:45-15:30"),
    ("Pak anggi kresna", " - Apdaniel Alamsyah", " - lindah setiyana", " - ihsan abdul akbar"),
)
harirabu = (
    ("PROJEK ILMU PENGETAHUAN (IPAS)", "P5.1", "MANAJEMEN PROYEK", "BIMBINGAN KONSELING"),
    (" - 07:00-09:15", " - 09:15-12:30", " - 12:30-13:45", " - 13:45-15:15"),
    ("- nur putri ningsih", " - intan rizky", " - abdul kholki", " - desi nuraini"),
)
harikamis = (
    ("SEJARAH", "PEMOGRAMAN BERBASIS OBJEK", "SENI BUDAYA", "DASAR PEMOGRAMAN (PEMDAS)"),
    (" - 07:00-09:15", " - 09:15-11:15", " - 11:15-13:45", " - 13:45-15:30"),
    ("- afri ratnaningsih", " - alzaro rashad", " - pasaor pasaribuan", " - apdaniel alamsyah"),
)
harijumat = (
    ("AKTIVITAS JUMAT", "INFORMATIKA", "MATEMATIKA", "BAHASA INGGRIS"),
    (" - 07:00-07:45", " - 07:45-10:00", " - 10:30-13:45", " - 13:45-15:05"),
    ("- ihsan abdul akbar", " - Een rohenan", " - ", " - MR azzis"),
)

print("\n============== JADWAL MATA PELAJARAN ==============")
print("Hari Senin")
print("-", harisenin[0][0], "pada jam", harisenin[1][0], "dengan guru", harisenin[2][0])
print("-", harisenin[0][1], "pada jam", harisenin[1][1], "dengan guru", harisenin[2][1])
print("-", harisenin[0][2], "pada jam", harisenin[1][2], "dengan guru", harisenin[2][2])
print("-", harisenin[0][3], "pada jam", harisenin[1][3], "dengan guru", harisenin[2][3])

print("\nHari Selasa")
print("-", hariselasa[0][0], "pada jam", hariselasa[1][0], "dengan guru", hariselasa[2][0])
print("-", hariselasa[0][1], "pada jam", hariselasa[1][1], "dengan guru", hariselasa[2][1])
print("-", hariselasa[0][2], "pada jam", hariselasa[1][2], "dengan guru", hariselasa[2][2])
print("-", hariselasa[0][3], "pada jam", hariselasa[1][3], "dengan guru", hariselasa[2][3])

print("\nHari Rabu")
print("-", harirabu[0][0], "pada jam", harirabu[1][0], "dengan guru", harirabu[2][0])
print("-", harirabu[0][1], "pada jam", harirabu[1][1], "dengan guru", harirabu[2][1])
print("-", harirabu[0][2], "pada jam", harirabu[1][2], "dengan guru", harirabu[2][2])
print("-", harirabu[0][3], "pada jam", harirabu[1][3], "dengan guru", harirabu[2][3])

print("\nHari Kamis")
print("-", harikamis[0][0], "pada jam", harikamis[1][0], "dengan guru", harikamis[2][0])
print("-", harikamis[0][1], "pada jam", harikamis[1][1], "dengan guru", harikamis[2][1])
print("-", harikamis[0][2], "pada jam", harikamis[1][2], "dengan guru", harikamis[2][2])
print("-", harikamis[0][3], "pada jam", harikamis[1][3], "dengan guru", harikamis[2][3])

print("\nHari Jumat")
print("-", harijumat[0][0], "pada jam", harijumat[1][0], "dengan guru", harijumat[2][0])
print("-", harijumat[0][1], "pada jam", harijumat[1][1], "dengan guru", harijumat[2][1])
print("-", harijumat[0][2], "pada jam", harijumat[1][2], "dengan guru", harijumat[2][2])
print("-", harijumat[0][3], "pada jam", harijumat[1][3], "dengan guru", harijumat[2][3])
# Tuple Slicing Terbatas
tup_harisenin = ("Upacara", "PJOK", "BAHASA INDONESIA", "PENDIDIKAN AGAM BUDI PEKERTI")
print("Tuple Slicing Terbatas - harisenin")
print(tup_harisenin[0:1])    
print(tup_harisenin[0:2])    
print(tup_harisenin[0:3])    
print(tup_harisenin[0:4])  
print(tup_harisenin[0:-0])  
print(tup_harisenin[0:-1])   
print(tup_harisenin[0:-2])   
print(tup_harisenin[0:-3])   
print(tup_harisenin[0:-4],"\n")   


# Tuple Slicing Tidak Terbatas
tup_harikamis = ("DASAR PEMOGRAMAN", "PEMOGRAMAN BERBASIS OBJEK", "SEJARAH", "SENI BUDAYA")
print("\nTuple Slicing Tidak Terbatas - harikamis")
print(tup_harikamis[0:])  
print(tup_harikamis[1:])  
print(tup_harikamis[2:])  
print(tup_harikamis[3:])
print(tup_harikamis[4:])
print(tup_harikamis[5:])
print(tup_harikamis[-0:]) 
print(tup_harikamis[-1:]) 
print(tup_harikamis[-2:]) 
print(tup_harikamis[-3:]) 
print(tup_harikamis[-4:]) 



