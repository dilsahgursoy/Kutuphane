def DosyaAc(adres,param):
    from os.path import exists
    if exists(adres):
        if param == 1:
            return open(adres,"r+",encoding="UTF-8")
        elif param == 2:
            return open(adres,"a+",encoding="UTF-8")
    else:
        return open(adres,"w+",encoding="UTF-8")


def Listeleme():
    
    for _id,item in enumerate(kayitListesi):
        print(_id,*item.split(";"),end="")

def Donustur(giris):
    return ";".join(giris) + "\n"


def GirisAl():
    liste = []
    for item in girisListe:
        liste.append(input(f"{item} Giriniz:"))
    return ";".join(liste) + "\n"

def Ekleme(param=0,giris=[]):
    if param:
        kayitListesi.append(Donustur(giris))
    else:
        kayitListesi.append(GirisAl())

def Guncelleme():
    Listeleme()
    kayitListesi[int(input("Güncellenecek Kayıt Numarasını Giriniz:"))] = GirisAl()

def Silme():
    Listeleme()
    del kayitListesi[int(input("Silinecek Kayıt Numarasını Giriniz:"))]

kayitListesi = []
girisListe = []

def Menu(adres=r"C:\Users\90536\Desktop\kütüphane\defter2.csv",girisListesi=["Adı","Soyadı","Telefon Numarası"]):
    global kayitListesi
    global girisListe
    dosya = DosyaAc(adres,1)
    girisListe = girisListesi
    kayitListesi = dosya.readlines()
    menu = f"""
    {adres} üzerinde çalışılıyor
    0-Ekleme
    1-Güncelleme
    2-Silme
    3-Listeleme
    4-Çıkış
    İşlem Numarasını Giriniz:
    """
    fonkList = [Ekleme,Guncelleme,Silme,Listeleme]
    anahtar = 1
    while anahtar == 1:
        islem = input(menu)
        if islem:
            if islem.isdigit():
                islem = int(islem)
                if islem in range(4):
                    fonkList[islem]()
                elif islem == 4:
                    anahtar = 0
                else:
                    print("Geçerli bir işlem numarası giriniz")
            else:
                print("İşlem Numarasını Sayısal olarak giriniz")
        else:
            print("İşlem Numarası Giriniz")
    else:
        dosya.seek(0)
        dosya.truncate()
        dosya.writelines(kayitListesi)
        dosya.close()

Menu(r"C:\Users\90536\Desktop\kütüphane\defter2.csv0",girisListesi=["KitapNo","KitapAdi","Yazar","Tür"])
