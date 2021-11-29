namaMhs = []
nimMhs = []
nTugasMhs = []
utsMhs = []
uasMhs = []
total = []

while True:
    nama = input('Nama : ')
    namaMhs.append(nama)
    nim = int(input('NIM : '))
    nimMhs.append(nim)
    nTugas = float(input('Nilai Tugas : '))
    nTugasMhs.append(nTugas)
    uts = float(input('Nilai UTS : '))
    utsMhs.append(uts)
    uas = float(input('Nilai UAS : '))
    uasMhs.append(uas)

    nAkhir = (int(nTugas) * .3) + (int(uts) * .35) + (int(uas) * .35)
    total.append(nAkhir)

    lagi = ''
    while lagi != 'y' and lagi != 't':
        lagi = input('Tambah data (y/t)? ')
    if lagi == 't':
        print('='*70)
        print('| No |\tNama\t    |  NIM   | Tugas   |  UTS    |  UAS    | Akhir   |')
        print('='*70)

        for i in range(len(nimMhs)):
            nm = '| %d. |\t%s\t' % (i+1, namaMhs[i])
            im = '    | %d' % nimMhs[i]
            tg = '   | %.2f' % nTugasMhs[i]
            ut = '   | %.2f' % utsMhs[i]
            ua = '   | %.2f' % uasMhs[i]
            ah = '   | %.2f' % total[i]
            ln = '   |'

            join = nm + im + tg + ut + ua + ah + ln
            print(join)

        break
