# praktikum-09
## Tugas di pertemuan ke-09 (Bahasa Pemrograman)

### Program Menampilkan List Nilai (Tugas, UTS, UAS, Nilai Akhir)
* FLOWCHART :
* ![img](https://github.com/raissaputra/praktikum-09/blob/main/assets/flowchart.png)
* OUTPUT PROGRAM `test-nilai.py`:
* ![img](https://github.com/raissaputra/praktikum-09/blob/main/assets/output.png)
* __PENJELASAN__ :
  *  Inisialisasi variabel untuk menampung nilai inputan dari user:
  * ```
    namaMhs = []
    nimMhs = []
    nTugasMhs = []
    utsMhs = []
    uasMhs = []
    total = []
    ```
  * Menggunakan perulangan `While` :
    - selama bernilai true program akan looping terus
    - inputan dari user akan di `append()` langsung, berikut kode nya :
    - 
      ```
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
      ```
    - Buat perhitungan untuk nilai yang di input dengan kode berikut :
    - 
      ```
      nAkhir = (int(nTugas) * .3) + (int(uts) * .35) + (int(uas) * .35)
      total.append(nAkhir)
      ```
    - Jika ingin menambah data maka ketik 'y' dan jika 't' maka akan menampilkan hasil nilai yang sudah diinput :
    - berikut kode tambah data nya :
      ```
      lagi = ''
      while lagi != 'y' and lagi != 't':
        lagi = input('Tambah data (y/t)? ')
      ```
    - Jika Ketik 't' akan menampilkan hasil nilai nya, berikut kode nya:
    - 
      ```
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
      ```

### Program untuk akses, ubah, tambah elemen List
* OUTPUT PROGRAM `list.py`:
* ![img](https://github.com/raissaputra/praktikum-09/blob/main/assets/list.png)
* __PENJELASAN__:
* Nilai Awal : 
* `bahasa = ['Python', 'Java', 'Javascript', 'Dart', 'Kotlin']`
* | Elemen      | Index | negative index |
  | ----------- | ----- | -------------- |
  | Pyhton      | 0     | -5             |
  | Java        | 1     | -4             |
  | Javascript  | 2     | -3             |
  | Dart        | 3     | -2             |
  | Kotlin      | 4     | -1             |
  
* Untuk menampilkan elemen ke 3 :
  - `print('Elemen ke 3 adalah ', bahasa[3])`
* ambil nilai elemen ke 2 sampai elemen ke 4 :
  - `print('Nilai elemen ke 2 sampai ke 4 adalah ', bahasa[2:5])`
* ambil elemen terakhir :
  - `print('Elemen terakhir adalah ', bahasa[-1])`
* ubah elemen ke 4 dengan nilai lainnya :
  - `bahasa[3] = 'c++'
     print('Elemen ke 4 adalah ', bahasa[3])`
* ubah elemen ke 4 sampai dengan elemen terakhir :
  - `bahasa[3:] = 'c#', 'PHP'
     print(bahasa)`
* ambil 2 bagian dari list pertama (A) dan jadikan list ke 2 (B) :
  - ```
    A = bahasa[0:2]
    B = bahasa[2:]
    print(A)
    print(B)
    ```
• tambah list B dengan nilai string :
  - ```
    B.append('Web')
    print(B)
    ```
• tambah list B dengan 3 nilai :
  - ```
    B.extend([1, 2, 3])
    print(B)
    ```
• gabungkan list B dengan list A:
  - ```
    B.extend(A)
    print(B)
    ```




