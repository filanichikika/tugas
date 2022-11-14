total_cow = int(input('jumlah sapi: '))
total = 0

for i in range(total_cow):
    cow = int(input(f'kode sapi {i + 1}: '))
    if cow == 1:
        total += 690
    elif cow == 2:
        total += 420
    elif cow == 3:
        total += 530
    elif cow == 4:
        total += 330
    
print(f'Jumlah hari yang diperlukan adalah {sum//365} tahun {(sum%365)//30} bulan {((sum%365)%30)} hari')