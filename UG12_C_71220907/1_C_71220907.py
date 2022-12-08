def balik_kalimat(kalimat):
    x = ''
    for j in kalimat:
        x = j + x
    return x

kalimat = input('Masukkan Kata atau angka : ')
print(balik_kalimat(kalimat))