kiri = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v', 'b']
kanan = ['y', 'u', 'i', 'o', 'p', 'h', 'j', 'k', 'l', 'n', 'm']
kondisi = True
word = input('masukkan kata: ')
for i in range(len(word)-1):
    if word[i] in kiri and word[i+1] in kiri:
        kondisi = False
    elif word[i] in kanan and word[i+1] in kanan:
        kondisi = False
    