import numpy as np

def datapemohon(x,k,z):
    while x<len(k):
        print("Masukkan Kriteria "+str(x+1)+" :",end=" ") #Memasukkan kriteria 1 sampai n
        try: #Cek apakah user sudah menginputkan angka atau belum
            # z=input()
            print(z[x])
            k[x]=int(z[x])
            if (k[x]>=0)and(k[x])<=5: #check apakah sudah sesuai nilai atau belum
                x+=1
            else:
                print("Mohon masukkan angka 1 - 5") #error yang ditampikan saat user tidak memasukkan angka 1-5
                pass
            pass
        except ValueError:
            print("Mohon masukkan bilangan bulat.") #error yang ditampilkan saat user tidak menginputkan bilangan bulat
        pass

def masukkan_nilai_k(y,nilai_k):
    while y<=0:
        try:
            print("Masukkan nilai k :",end=" ")
            # nilai_k=input()
            print(nilai_k)
            nilai_k=int(nilai_k)
            if nilai_k<=0:
                print("Mohon masukkan angka minimal angka 1")
            else:
                y+=1
                pass
            pass
        except ValueError:
            print("Mohon masukkan bilangan bulat.")
            pass
    return nilai_k

def hitung(hasil,i,d,k):
    while i<len(d): #Ulangi sebanyak data train yang ada.
        i2=0
        while i2<5: #while untuk menghitung masing masing selisih data train dan data test dikuadrat pada kriteria.
            hasil_sq=abs(k[i2]-d[i][i2+1])**2 #rumus menghitung selisih data train dan data test dikuadrat
            hasil[i][0]+=hasil_sq #setiap hasil hitung yang ada ditambahkan
            i2=i2+1
            pass
        hasil[i][0]=np.sqrt(hasil[i][0])#total hasil hitung di akar kuadratkan
        hasil[i][1]=i+1 #menyimpan nomor data train
        hasil[i][2]=d[i][6] #menyimpan keputusan hasil hitung
        i=i+1
        pass
    hasil = list(hasil)

def urutkan(hasil, nilai_k, i3):
    kebenaran = 0
    print("Sebelum pengurutan kedekatan")
    print("No \t Kedekatan")
    for x in hasil:	#pengulangan untuk menampilkan hasil hitung sebelum diurutkan
        print(int(x[1]),end="\t")
        print(x[0])
        pass
    hasil.sort(key=lambda x:x[0]) #mengurutkan  array berdasarkan kedekatan dengan data test
    print("Sesudah pengurutan kedekatan")
    print("No \t Kedekatan")
    for x in hasil: #pengulangan untuk menampilkan hasil hitung setelah diurutkan
        print(int(x[1]),end="\t")
        print(x[0])
        pass
    while i3<nilai_k: #pengulangan untuk memilih hasil penghitungan dengan nilai k yang diurutkan berdasarkan kedekatan.
        kebenaran+=hasil[i3][2] #menghitung total nilai keputusan (0 untuk tidak memenuhi dan 1 untuk memenuhi)
        i3=i3+1
        pass
    return kebenaran