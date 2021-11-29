bahasa = ['Python', 'Java', 'Javascript', 'Dart', 'Kotlin']

# akses list
print('='*70)
print('AKSES LIST')
print('='*70)
print('Elemen ke 3 adalah ', bahasa[3])
print('Nilai elemen ke 2 sampai ke 4 adalah ', bahasa[2:5])
print('Elemen terakhir adalah ', bahasa[-1])

# ubah element list
print('='*70)
print('UBAH ELEMEN LIST')
print('='*70)
print(bahasa)
bahasa[3] = 'c++'
print('Elemen ke 4 adalah ', bahasa[3])
print(bahasa)
bahasa[3:] = 'c#', 'PHP'
print(bahasa)

# tambah elemen list
print('='*70)
print('TAMBAH ELEMEN LIST')
print('='*70)
A = bahasa[0:2]
B = bahasa[2:]
print(A)
print(B)
B.append('Web')
print(B)
B.extend([1, 2, 3])
print(B)
B.extend(A)
print(B)
