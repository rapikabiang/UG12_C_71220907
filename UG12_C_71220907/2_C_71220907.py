inputAngka = input('Masukkan angka : ')
dicari = input('Masukkan angka yang dihitung : ')
sum = 0
for j in inputAngka:
    if j == dicari:
        sum += 1
    else:
        continue
print('Angka',dicari,'muncul sebanyak',sum,'kali')