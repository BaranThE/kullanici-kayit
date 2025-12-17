import json
import os

class KayitSistemi:
    def __init__(self, dosya_adi='database.json'):
        self.dosya_adi = dosya_adi
        self.kullanicilar = self.verileri_yukle()

    def verileri_yukle(self):
        """JSON dosyasından verileri okur."""
        if not os.path.exists(self.dosya_adi):
            return {}
        with open(self.dosya_adi, 'r', encoding='utf-8') as f:
            return json.load(f)

    def verileri_kaydet(self):
        """Verileri JSON dosyasına yazar."""
        with open(self.dosya_adi, 'w', encoding='utf-8') as f:
            json.dump(self.kullanicilar, f, indent=4, ensure_ascii=False)

    def kayit_ol(self, kullanici_adi, sifre):
        if kullanici_adi in self.kullanicilar:
            print(f"\n[!] Hata: '{kullanici_adi}' ismi zaten alınmış.")
            return False
        
        self.kullanicilar[kullanici_adi] = sifre
        self.verileri_kaydet()
        print(f"\n[+] Başarılı: '{kullanici_adi}' kaydı oluşturuldu.")
        return True

    def giris_yap(self, kullanici_adi, sifre):
        if kullanici_adi in self.kullanicilar and self.kullanicilar[kullanici_adi] == sifre:
            print(f"\n[✓] Hoş geldiniz, {kullanici_adi}!")
            return True
        else:
            print("\n[!] Hata: Kullanıcı adı veya şifre yanlış.")
            return False

def ana_menu():
    sistem = KayitSistemi()
    
    while True:
        print("\n--- KULLANICI KAYIT SİSTEMİ ---")
        print("1. Kayıt Ol")
        print("2. Giriş Yap")
        print("3. Çıkış")
        
        secim = input("Seçiminiz (1/2/3): ")

        if secim == '1':
            k_adi = input("Yeni Kullanıcı Adı: ")
            sifre = input("Şifre: ")
            sistem.kayit_ol(k_adi, sifre)
        
        elif secim == '2':
            k_adi = input("Kullanıcı Adı: ")
            sifre = input("Şifre: ")
            sistem.giris_yap(k_adi, sifre)
            
        elif secim == '3':
            print("Sistemden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    ana_menu()
