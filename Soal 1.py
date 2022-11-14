total_name = int(input('jumlah nama: '))

for i in range(total_name):
    name = str(input(f'nama {i + 1}: '))
    for i in range(len(name) - 1):
        if ord(name[i]) - ord(name[i-1]) < 0:
            print(f'{name[i]} kurang dari {name[i+1]}', f'dengan selisih {(ord(name[i]) - ord(name[i-1])) * -1}')
        elif ord(name[i]) - ord(name[i-1]) > 0:
            print(f'{name[i]} lebih dari {name[i+1]}', f'dengan selisih {ord(name[i]) - ord(name[i-1])}' )
        else:
            print(f'{name[i]} sama dengan {name[i+1]} dengan selisih 0')
        