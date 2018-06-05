"""
Author = Yusuf Arslan
Website = yatechno.blogspot.com

"""
#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#-*-coding:utf8;-*-

import androidhelper
import time
import locale
import datetime
import types
import random
import sys
try:  
  import gdata.docs.service
except ImportError:
  gdata = None

droid = androidhelper.Android()

#ACİLİS BOLUMU
acilis = ['Hoşgeldin sana nasıl yardımcı olabilirim','Tekrar Hoşgeldin']
acilissecimi = random.choice(acilis)
droid.ttsSpeak(acilissecimi)
print(acilissecimi,'\n')
insan = input("")

#ROBOTUN SÖZLÜĞÜ
merhaba = ['merhaba','MERHABA','mrb','Merhaba','mrhba']
merhabac = ['Sanada merhaba', 'Merhaba']
selam = ['selam','slm','Selam','SELAM','selm','selamin aleykum','Sealmin aleykum','selamın aleyküm','Selamın aleyküm']
selamc = ['Aleyküm Selam','Sanada Selam']
naber = ['naber','nbr','Naber','NABER','nabr']
naberc = ['İyi','Muhteşem','Harika','Süper']
nasilsin = ['nasilsin','Nasilsin','nasılsın','Nasılsın','NASİLSİN','NASILSIN','naslsn','nslsn','nasilsnn','nsilsn']
camera = ['kamerayi ac','kamera','foto cek','fotograf cek','foto çek','fotoğraf çek','Kamera','camera','resim cek','resim çek','KAMERA','CAMERA','FOTO CEK','resim']
dosyaolusturma = ['doaya yap','doaya olustir','dosya olustur','dosya yap','Dosya yap','metin olustur','dosya oluştur','DOSYA OLUSTUR','dosya oustur']
cikis= ['cikis','cikis yap','Cik','uygulamadan cik','çık','cıkis','cik']

#ANA BÖLÜM
while True:
    if insan in merhaba:
        a = random.choice(merhabac)
        droid.ttsSpeak(a)
        print(a)
        
    elif insan in selam:
        b = random.choice(selamc)
        droid.ttsSpeak(b)
        print(b)

    elif insan in naber:
        c = random.choice(naberc)
        droid.ttsSpeak(c)
        print(c)

    elif insan in nasilsin:
        d = random.choice(naberc)
        droid.ttsSpeak(d)
        print(d)
        
    elif insan in camera:
        print('Kamera açılıyor...')
        time.sleep(3)
        droid.cameraInteractiveCapturePicture('/sdcard/fotograf.jpg')

    elif insan in dosyaolusturma:
         print("dosya.txt adlı bir dosya oluşturuldu \n")
         dosya = open(r"/sdcard/dosya.txt", "a")
         dosyayazisi = input("Dosya içine yazmak\nistediklerinizi yazın. \n")
         dosya.write(dosyayazisi)
         dosya.close()
         print('Istediğiniz işlemi yaptım.\n')
         
    elif insan in cikis:
        print('Çıkış')
        break;

    else:
        print('Söylediğini anlamadım.')
        print('Daha fazla komut ve yeni\nSürümler için:\nyatechno.blogspot.com adresini\nziyaret et')
  
    insan = input("")
print("Uygulamadan Çıkış Yaptınız...")
cikis = "Uygulamadan Çıkış Yaptınız..."
droid.ttsSpeak(cikis)