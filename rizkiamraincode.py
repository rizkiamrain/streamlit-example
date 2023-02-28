import streamlit as st

st.title('MENGHITUNG GAJI KARYAWAN')
namakr = st.text_input("Masukan Nama Karyawan",)
gol = st.selectbox("Masukan Golongan", [' ','A','B','C'] )
jamkerja = st.number_input("Masukan Total Jam Kerja",)
hitung = st.button("Hitung Gaji")

if hitung:
    if (gol =='A'):
        gapok = 500000
        if (jamkerja>6):
            tunjangan = 0.1*gapok
        else:
            tunjangan = 0
    elif(gol == 'B'):
        gapok = 700000
        if (jamkerja>7):
            tunjangan = 0.15*gapok
        else:
            tunjangan = 0
    elif(gol=='C'):
        gapok = 900000
        if (jamkerja>8):
            tunjangan = 0.2*gapok
        else:
            tunjangan=0
    totalgaji = gapok+tunjangan

    st.write(" P E R H I T U N G A N  G A J I ")
    st.write('Nama Karyawan   = ',namakr)
    st.write('Golongan        = ',gol)
    st.write('Total Jam kerja = ',jamkerja)
    st.write('Tunjangan       = Rp.',tunjangan)
    st.write('Total Gaji      = Rp.',totalgaji)

