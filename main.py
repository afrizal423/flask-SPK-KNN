from flask import Flask, request, render_template, url_for
import numpy as np
import pandas as pd

app = Flask(__name__)
from fungsi import datapemohon, masukkan_nilai_k, hitung, urutkan

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method=="POST":
    # print(request.form.getlist('kriteria[]'))
    data = request.form.getlist('kriteria[]')
    # print(data[2])
    hasil=np.zeros((4,3)) #definisi array 4 baris 3 kolom hasil untuk menampung nomor, hasil hitung, dan kategori keputusan
    k=np.zeros(5) #definisi array untuk nilai kriteria
    d=pd.read_csv('data_train_sample.csv',delimiter=";")
    d=np.asarray(d)
    # kebenaran=0 #inisialisasi keputusan
    datapemohon(0,k,data)
    nilai_k = masukkan_nilai_k(0,request.form['nilaik'])
    hitung(hasil,0,d,k)
    print(hasil)
    hasil = list(hasil)
    kebenaran = urutkan(hasil, nilai_k, 0)
    keputusan=kebenaran/nilai_k*100 #membagi nilai keputusan dengan nilai k untuk menentukan apakah memenuhi atau tidak.	
    print("Berdasarkan perhitungan diatas, sistem menyatakan pemohon",end=" ")
    if keputusan>50:
        print("Memenuhi",end=" ")
    else:
        print("Tidak Memenuhi",end=" ")
        pass
    print("mengajukan kredit.")
    print("Persentasi kebenaran "+str(keputusan)+"%")
    data = {
        'persentase': keputusan
    }
    return render_template("index.html",data=data)
  else:
    return render_template("index.html")

app.run(debug=True)