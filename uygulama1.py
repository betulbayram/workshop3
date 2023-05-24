"""
kullanıcıdan öğrenci için no ad soyad vize_notu final_notu verileri alalım

öğrenci bilgilerini "ogrenci.txt" dosyasına kaydedelim.

öğrenci numaralarına göre silme işlemi

öğrenci numaralarına göre güncelleme işlemi

"""



class Ogrenci():
    def __init__(self):
        self.numara = input("Öğrenci numarası giriniz: ")
        self.ad_soyad = input("Öğrenci adını ve soyadını giriniz: ")
        self.vize_notu = int(input("Vize notunu giriniz: "))
        self.final_notu = int(input("Final notunu giriniz: "))


def ogrenci_ekle():
    dosya =  open("ogrenci.txt", "a")
    ogrenci = Ogrenci()
    dosya.write(f"{ogrenci.numara},{ogrenci.ad_soyad},{ogrenci.vize_notu},{ogrenci.final_notu}" + "\n")
    dosya.close()
    
# ogrenci_ekle()    
    


def ogrenci_sil():
    dosya = open("ogrenci.txt", "r")
    numara = input("Hangi numaralı öğrenciyi silmek istiyorsunuz ?")
    ogrenciler = dosya.readlines()
    dosya.close()
    dosya = open("ogrenci.txt", "w")
    for i in ogrenciler:
        j = i.split(",")
        if j[0] == numara:
            pass
        else:
            dosya.write(i)

ogrenci_sil()