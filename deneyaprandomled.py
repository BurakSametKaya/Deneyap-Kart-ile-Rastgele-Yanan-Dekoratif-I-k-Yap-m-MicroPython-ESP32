#DOSYA İSMİNİ DEĞİŞTİREBİLİRSİNİZ
import deneyap # Bu kısımda deneyap kart kütüphanemizi dahil ediyoruz. Bu bize tüm pinleri kullanabilmemizi sağlayacak.
import time  #Time modülünü ekleyerek birazdan kullanacağımız dinlenme metotunu tanıtmış olduk.

from machine import Pin # Bu kısımda machine kütüphanesinden Pin modülünü eklemiş olduk.

from random import randint # Bu kısım projemizdeki rastgelelik kavramının en önemli yeri.Random modülünü ekleyerek randint metodunu çağırdık.

#Şimdi ledlerimizi tanımlayalım. Pin.OUT kısmı pinlerimizin çıkış pini oldu anlamına geliyor. 
led1 = Pin(deneyap.D0, Pin.OUT)
led2 = Pin(deneyap.D1, Pin.OUT)
led3 = Pin(deneyap.D2, Pin.OUT)
led4 = Pin(deneyap.D3, Pin.OUT)
led5 = Pin(deneyap.D4, Pin.OUT)
led6 = Pin(deneyap.D5, Pin.OUT)
led7 = Pin(deneyap.D6, Pin.OUT)

#şimdi de bu ledleri bir liste haline getirelim.

led_list = [led1,led2,led3,led4,led5,led6,led7]

while True:   #Bu kısım ledlerimizin aralıksız çalışması için gerekli olan döngü bölümü.
    time.sleep(1) #makinemize dinlenmek ve ledlerin çok hızlı yanıp sönmemesi için süre veriyoruz
    for i in led_list: #for dögüsü ile led sayımız kadar işlem yapıyoruz.
    i.value(randint(0,1)) #i led1 den başlayarak led7 ye kadar hızlıca ledlere ranint metotu ile 0 ya da 1 değerleri atıyor yani yak sön işlemi yapıyor.
