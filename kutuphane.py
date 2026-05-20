import abc

class Kaynak:
    def __init__(self, baslik, kayitNo):
        self._baslik = baslik
        self._kayitNo = kayitNo

    @property
    def baslik(self):
        return self._baslik

    @property
    def kayitNo(self):
        return self._kayitNo

    def __str__(self):
        return f"No: {self.kayitNo} - Baslik: {self.baslik}"


class Kitap(Kaynak):
    def __init__(self, baslik, kayitNo, yazar, sayfa_sayisi):
        super().__init__(baslik, kayitNo)
        self._yazar = yazar
        self._sayfa_sayisi = sayfa_sayisi

    @property
    def yazar(self):
        return self._yazar

    @property
    def sayfa_sayisi(self):
        return self._sayfa_sayisi

    def __str__(self):
        return f"[Kitap] No: {self.kayitNo} | {self.baslik} - {self.yazar} ({self.sayfa_sayisi} Sayfa)"


class Dergi(Kaynak):
    def __init__(self, baslik, kayitNo, yayin_donemi, sayi_no):
        super().__init__(baslik, kayitNo)
        self._yayin_donemi = yayin_donemi
        self._sayi_no = sayi_no

    @property
    def yayin_donemi(self):
        return self._yayin_donemi

    @property
    def sayi_no(self):
        return self._sayi_no

    def __str__(self):
        return f"[Dergi] No: {self.kayitNo} | {self.baslik} - Dönem: {self.yayin_donemi} (Sayı: {self.sayi_no})"


class Islem(abc.ABC):
    @abc.abstractmethod
    def ekle(self, kaynak):
        pass

    @abc.abstractmethod
    def sil(self, kayitNo):
        pass

    @abc.abstractmethod
    def guncelle(self, kayitNo, yeni_baslik):
        pass

    @abc.abstractmethod
    def listele(self):
        pass


class KutuphaneYonetimi(Islem):
    def __init__(self):
        self.liste = []

    def ekle(self, kaynak):
        for k in self.liste:
            if k.kayitNo == kaynak.kayitNo:
                print("\nHata: Bu kayit numarasi zaten var!")
                return False
        self.liste.append(kaynak)
        print(f"\n{kaynak.baslik} basariyla eklendi.")
        return True

    def sil(self, kayitNo):
        for k in self.liste:
            if k.kayitNo == kayitNo:
                self.liste.remove(k)
                print(f"\n{kayitNo} numarali kayit silindi.")
                return True
        print("\nHata: Kayit bulunamadi!")
        return False

    def guncelle(self, kayitNo, yeni_baslik):
        for k in self.liste:
            if k.kayitNo == kayitNo:
                k._baslik = yeni_baslik
                print(f"\n{kayitNo} numarali kayit güncellendi.")
                return True
        print("\nHata: Kayit bulunamadi!")
        return False

    def listele(self):
        if len(self.liste) == 0:
            print("\nKütüphane bos, görüntülenecek kayit yok.")
            return
        print("\n--- LISTE ---")
        for k in self.liste:
            print(k)


def menu():
    yonetim = KutuphaneYonetimi()
    while True:
        print("\n--- ISUBÜ KÜTÜPHANE SİSTEMİ ---")
        print("1- Kitap Ekle")
        print("2- Dergi Ekle")
        print("3- Kaynak Sil")
        print("4- Isim Guncelle")
        print("5- Listele")
        print("9- Cikis")
        secim = input("Seciminiz: ")

        if secim == "1":
            baslik = input("Kitap Adi: ")
            try:
                kayitNo = int(input("Kayit No: "))
                yazar = input("Yazar: ")
                sayfa = int(input("Sayfa Sayisi: "))
                yonetim.ekle(Kitap(baslik, kayitNo, yazar, sayfa))
            except ValueError:
                print("\nHata: Lütfen sayisal deger girin!")

        elif secim == "2":
            baslik = input("Dergi Adi: ")
            try:
                kayitNo = int(input("Kayit No: "))
                donem = input("Yayin Donemi: ")
                sayi = int(input("Sayi No: "))
                yonetim.ekle(Dergi(baslik, kayitNo, donem, sayi))
            except ValueError:
                print("\nHata: Lütfen sayisal deger girin!")

        elif secim == "3":
            try:
                no = int(input("Silinecek Kayit No: "))
                yonetim.sil(no)
            except ValueError:
                print("\nHata: Gecersiz no!")

        elif secim == "4":
            try:
                no = int(input("Guncellenecek Kayit No: "))
                yeni_isim = input("Yeni Adi: ")
                yonetim.guncelle(no, yeni_isim)
            except ValueError:
                print("\nHata: Gecersiz no!")

        elif secim == "5":
            yonetim.listele()

        elif secim == "9":
            print("\nCikis yapiliyor.")
            break
        else:
            print("\nGecersiz secim!")

if __name__ == "__main__":
    menu()