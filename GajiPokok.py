import streamlit as st 

st.info("""
# Aplikasi Cek Gaji Pokok
""")
st.warning("Ini adalah aplikasi untuk mengecek Gaji Pokok Berdasarkan Masa Kerja dan Golongan")

tipe_pegawai = ["Pilih Tipe Pegawai", "Pegawai Negeri Sipil (PNS)", "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)"]
golongan_pegawai = ["Pilih Golongan",
                 "Golongan Ia",
                 "Golongan Ib"]
masa_kerja = ["Pilih Masa Kerja", 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
                 

tipe_pegawaii = st.selectbox(''':blue[Masukan Tipe Pegawai]''', tipe_pegawai)
golongan_pegawaii = st.selectbox(''':blue[Masukan Golongan]''', golongan_pegawai)
masa_kerjaa = st.selectbox(''':blue[Masukan Masa Kerja (Dalam Tahun)]''',masa_kerja)

# Golongan Ia
if tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 1.685.700")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 1.738.800")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 1.793.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 1.850.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 1.908.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 1.968.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 2.030.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 2.094.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 2.160.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 2.228.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 2.298.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 2.370.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 2.445.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ia" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.522.600")
  
# Golongan Ib  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 1.840.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 1.898.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 1.958.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.020.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.083.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.149.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.217.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.287.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.359.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 2.433.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 2.510.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 2.589.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ib" and 27 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.670.700")
  
# Golongan Ic 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 1.918.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 1.979.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.041.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.105.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.172.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.240.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.311.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.383.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.458.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 2.536.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 2.616.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 2.698.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Ic" and 27 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.783.700")
  
# Golongan Id
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 1.999.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.062.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.127.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.194.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.264.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.335.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.408.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.484.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.562.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 2.643.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 2.726.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 25 <= masa_kerjaa <=26:
  st.warning ("Gaji Pokoknya adalah 2.812.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan Id" and 27 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.901.400")
   
# Golongan IIa 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 0 <= masa_kerjaa <= 0:
  st.warning ("Gaji Pokoknya adalah 2.184.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 1 <= masa_kerjaa <= 2:
  st.warning ("Gaji Pokoknya adalah 2.218.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.288.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.360.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.434.600")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.511.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.590.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.672.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.756.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.843.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.932.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.024.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.120.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.218.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.319.800")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 3.424.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 3.532.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIa" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 3.643.400")  

# Golongan IIb  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.385.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.460.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.537.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.617.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.700.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.785.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.872.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.963.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.056.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.152.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.252.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.354.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.460.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 3.569.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 3.681.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIb" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 3.797.500")

  
# Golongan IIc 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.485.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.564.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.645.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.728.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.814.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.902.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.994.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 3.088.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.185.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.286.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.389.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.496.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.606.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 3.720.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 3.837.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIc" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 3.958.200")

# Golongan IId
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.591.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.672.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.756.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.843.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.933.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 3.025.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 3.120.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 3.219.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.320.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.425.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.533.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.644.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.759.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 3.877.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 3.999.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IId" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 4.125.600")


# Golongan IIIa
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 2.785.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 2.873.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 2.964.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.057.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.153.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.252.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.355.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 3.461.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 3.570.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 3.682.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 3.798.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 3.918.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.041.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.168.800")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 4.300.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 4.435.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIa" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.575.200")


# Golongan IIIb  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 2.903.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 2.995.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.089.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.186.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.287.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.390.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.497.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 3.607.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 3.721.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 3.838.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 3.959.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.083.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.212.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.345.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 4.482.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 4.623.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIb" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.768.800")




# Golongan IIIc 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.026.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.121.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.220.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.321.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.426.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.533.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.645.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 3.760.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 3.878.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.000.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.126.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.256.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.390.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.528.900")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 4.671.600")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 4.818.700")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIIc" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.970.500")


# Golongan IIId 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.154.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.253.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.356.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.461.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.571.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.683.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.799.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 3.919.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.042.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.169.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.301.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.436.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.576.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.720.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 4.869.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.022.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IIId" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.180.700")






  
# Golongan IVa
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.287.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.391.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.498.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.608.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.722.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.839.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.960.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.084.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.213.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.346.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.483.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.624.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.770.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.920.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.075.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.235.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVa" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.399.900")


# Golongan IVb  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.426.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.534.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.646.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.761.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.879.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.001.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.127.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.257.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.391.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.530.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.672.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.819.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.971.700")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.128.300")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.289.800")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.456.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVb" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.628.300")





# Golongan IVc 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.571.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.684.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.800.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.920.100")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.043.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.170.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.302.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.437.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.577.500")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.721.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.870.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.023.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.182.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.345.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.513.600")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.687.200")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVc" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.866.400")


# Golongan IVd 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.723.000")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.840.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.961.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 4.085.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.214.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.347.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.484.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.625.500")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.771.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.921.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 5.076.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.236.300")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.401.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.571.400")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.746.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.927.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVd" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 6.114.500")


# Golongan IVe 
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.880.400")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 4.002.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 4.128.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 4.258.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.392.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.531.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.673.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.821.100")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.973.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 5.129.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 5.291.200")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.457.800")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.629.700")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.807.000")

elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.989.900")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 6.178.600")
  
elif tipe_pegawaii == "Pegawai Negeri Sipil (PNS)" and golongan_pegawaii == "Golongan IVe" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 6.373.200")

#PPPK

#GOLONGAN I
elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 1.938.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 1.999.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 2.062.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 2.127.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 2.194.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 2.263.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 2.334.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 2.408.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 2.484.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 2.562.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 2.643.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 2.726.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 2.812.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan I" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 2.900.900")


#GOLONGAN II

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.116.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.183.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.252.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.323.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.396.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.472.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.549.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.630.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.713.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 2.798.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 2.886.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 2.977.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan II" and 27 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 3.071.200")

#GOLONGAN III

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.206.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.276.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.347.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.421.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.497.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.576.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.657.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.741.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.827.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 2.916.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.008.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.103.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan III" and 27 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 3.201.200")


#GOLONGAN IV

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.299.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.372.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.447.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.524.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.603.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 2.685.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 2.770.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 2.857.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 2.947.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.040.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.135.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.234.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IV" and 27 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 3.336.600")


#GOLONGAN V

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 0 <= masa_kerjaa <= 0:
  st.warning ("Gaji Pokoknya adalah 2.511.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 1 <= masa_kerjaa <= 2:
  st.warning ("Gaji Pokoknya adalah 2.551.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.631.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.714.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.799.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 2.888.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 2.978.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 3.072.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 3.169.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 3.269.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.372.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.478.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.588.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.701.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.817.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 3.937.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.061.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan V" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 4.189.900")

#GOLONGAN VI

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.742.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.829.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 2.918.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 3.010.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 3.105.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 3.202.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 3.303.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 3.407.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.515.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.625.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.739.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 3.857.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 3.979.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 4.104.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.233.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VI" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 4.367.100")

#GOLONGAN VII

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.858.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 2.948.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 3.041.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 3.137.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 3.236.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 3.338.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 3.443.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 3.551.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.663.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.779.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 3.898.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 4.020.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 4.147.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 4.278.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.412.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VII" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 4.551.800")

#GOLONGAN VIII

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 3 <= masa_kerjaa <= 4:
  st.warning ("Gaji Pokoknya adalah 2.979.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 5 <= masa_kerjaa <= 6:
  st.warning ("Gaji Pokoknya adalah 3.073.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 7 <= masa_kerjaa <= 8:
  st.warning ("Gaji Pokoknya adalah 3.170.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 9 <= masa_kerjaa <= 10:
  st.warning ("Gaji Pokoknya adalah 3.270.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 11 <= masa_kerjaa <= 12:
  st.warning ("Gaji Pokoknya adalah 3.373.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 13 <= masa_kerjaa <= 14:
  st.warning ("Gaji Pokoknya adalah 3.479.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 15 <= masa_kerjaa <= 16:
  st.warning ("Gaji Pokoknya adalah 3.589.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 17 <= masa_kerjaa <= 18:
  st.warning ("Gaji Pokoknya adalah 3.702.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 19 <= masa_kerjaa <= 20:
  st.warning ("Gaji Pokoknya adalah 3.818.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 21 <= masa_kerjaa <= 22:
  st.warning ("Gaji Pokoknya adalah 3.938.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 23 <= masa_kerjaa <= 24:
  st.warning ("Gaji Pokoknya adalah 4.063.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 25 <= masa_kerjaa <= 26:
  st.warning ("Gaji Pokoknya adalah 4.190.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 27 <= masa_kerjaa <= 28:
  st.warning ("Gaji Pokoknya adalah 4.322.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 29 <= masa_kerjaa <= 30:
  st.warning ("Gaji Pokoknya adalah 4.459.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 31 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 4.599.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan VIII" and 33 <= masa_kerjaa <= 33:
  st.warning ("Gaji Pokoknya adalah 4.744.400")



#GolonganIX

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.203.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.304.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.408.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.515.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.626.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.740.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 3.858.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 3.980.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.105.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.234.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.368.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.505.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.647.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.794.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 4.945.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.100.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan IX" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.261.500")


#Golongan X

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.339.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.444.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.552.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.664.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.780.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 3.899.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.021.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.148.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.279.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.414.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.553.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.696.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 4.844.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 4.996.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.154.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.316.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan X" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.484.000")


#GOLONGAN XI

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.480.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.589.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.703.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.819.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 3.939.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.064.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.192.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.324.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.460.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.600.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.745.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 4.895.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.049.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.208.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.372.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.541.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XI" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.716.000")

#GolonganXII

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.627.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.741.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 3.859.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 3.981.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.106.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.235.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.369.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.506.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.648.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.795.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 4.946.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.102.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.262.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.428.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.599.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 5.775.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XII" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 5.957.800")


#GOLONGAN XIII

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.781.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 3.900.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 4.022.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 4.149.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.280.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.415.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.554.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.697.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 4.845.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 4.998.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 5.155.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.317.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.485.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.658.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 5.836.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 6.020.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIII" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 6.209.800")


#GOLONGAN XIV

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 3.940.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 4.065.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 4.193.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 4.325.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.461.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.601.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.746.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 4.896.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 5.050.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 5.209.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 5.373.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.542.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.717.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 5.897.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 6.083.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 6.274.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XIV" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 6.472.500")

#GolonganXV

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 4.107.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 4.237.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 4.370.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 4.508.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.650.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.796.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 4.947.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 5.103.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 5.264.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 5.429.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 5.600.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 5.777.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 5.959.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 6.147.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 6.340.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 6.540.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XV" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 6.746.200")

#GolonganXVI

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 4.281.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 4.416.200")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 4.555.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 4.698.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 4.846.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 4.999.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 5.156.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 5.319.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 5.486.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 5.659.600")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 5.837.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 6.021.700")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 6.211.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 6.407.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 6.608.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 6.816.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVI" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 7.031.600")





#GolonganXVII

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 0 <= masa_kerjaa <= 1:
  st.warning ("Gaji Pokoknya adalah 4.462.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 2 <= masa_kerjaa <= 3:
  st.warning ("Gaji Pokoknya adalah 4.603.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 4 <= masa_kerjaa <= 5:
  st.warning ("Gaji Pokoknya adalah 4.748.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 6 <= masa_kerjaa <= 7:
  st.warning ("Gaji Pokoknya adalah 4.897.500")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 8 <= masa_kerjaa <= 9:
  st.warning ("Gaji Pokoknya adalah 5.051.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 10 <= masa_kerjaa <= 11:
  st.warning ("Gaji Pokoknya adalah 5.210.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 12 <= masa_kerjaa <= 13:
  st.warning ("Gaji Pokoknya adalah 5.375.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 14 <= masa_kerjaa <= 15:
  st.warning ("Gaji Pokoknya adalah 5.544.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 16 <= masa_kerjaa <= 17:
  st.warning ("Gaji Pokoknya adalah 5.718.900")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 18 <= masa_kerjaa <= 19:
  st.warning ("Gaji Pokoknya adalah 5.899.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 20 <= masa_kerjaa <= 21:
  st.warning ("Gaji Pokoknya adalah 6.084.800")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 22 <= masa_kerjaa <= 23:
  st.warning ("Gaji Pokoknya adalah 6.276.400")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 24 <= masa_kerjaa <= 25:
  st.warning ("Gaji Pokoknya adalah 6.474.100")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 26 <= masa_kerjaa <= 27:
  st.warning ("Gaji Pokoknya adalah 6.678.000")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 28 <= masa_kerjaa <= 29:
  st.warning ("Gaji Pokoknya adalah 6.888.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 30 <= masa_kerjaa <= 31:
  st.warning ("Gaji Pokoknya adalah 7.105.300")

elif tipe_pegawaii == "Pegawai Pemerintah dengan Perjanjian Kerja (PPPK)" and golongan_pegawaii == "Golongan XVII" and 32 <= masa_kerjaa <= 32:
  st.warning ("Gaji Pokoknya adalah 7.329.000")


