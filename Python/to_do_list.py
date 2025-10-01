# (To-Do List)

import os

# Global değişkenler görevlerin listesini tutmak ve kayıt dosyası için
gorev_listesi = []
dosya_adi = "Görevler.txt"

def dosya_okuma():
    """
    Dosyadan görevleri okur ve gorev_listesi'ne yükler
    """
    global gorev_listesi
    try:
        if os.path.exists(dosya_adi):       # dosya varsa üstüne yazacağız yoksa önce oluşturacak (pythonda bultin özelliği)
            with open(dosya_adi, 'r', encoding='utf-8') as dosya:       # türkçe karakter desteği ile dosya okumak için open fonksiyonu kullandım
                gorev_listesi = [satir.strip() for satir in dosya.readlines() if satir.strip()]   # dosyayı satır satır okur get_next_line gibi . strip ile satır başı ve sonu temizlenir ve if satir.strip() ile boş satırları filtrelerdik .
            print(f"✓ {len(gorev_listesi)} görev başarıyla yüklendi.")
        else:
            print(" Henüz kayıtlı görev bulunamadı. Yeni görevler ekleyebilirsiniz.")
    except Exception as e:      #  hata durumunda çalışır
        print(f" Dosya okuma hatası: {e}")

def gorevleri_listele():
    """
    Mevcut görevleri numaralandırarak listeler
    """
    if not gorev_listesi:   # liste boş nmu kontrol eder eğer boş ise bu fonsiyondan return ile çıkar
        print(" Görev listeniz boş. Yeni görevler ekleyebilirsiniz!")
        return

    print("\n GÖREV LİSTESİ:")
    print("*" * 38)
    for i, gorev in enumerate(gorev_listesi, 1):   #  listedeki satırları 1 den başlayarak numaralandırır enumarete fonksyonu
        print(f"{i}. {gorev}")
    print("*" * 38)


def gorevleri_kaydet():
    """
     görevleri dosyaya kaydeder
    """
    try:
        with open(dosya_adi, 'w', encoding='utf-8') as dosya:  # dosyayı sadece yazma modunda açar
            for gorev in gorev_listesi:                #  her görevde  tekrar etmesi için dngü
                dosya.write(gorev + '\n')
        print(" Görevler başarıyla kaydedildi.")
    except Exception as e:                    # try except ile herhangi bir hata varsa yakalıyoruz bu yüzden her fonksiyonda var
        print(f" Dosya kaydetme hatası: {e}")


def yeni_gorev_ekle():
    """
    Yeni görev ekler
    """
    while True:                 #  whie true ile sonsuz dögü yaptım böylee geçerli input girilene kadar bekleyecek
        yeni_gorev = input("\n Yeni görev girin (iptal için 'w'): ").strip()

        if yeni_gorev.lower() == 'w':
            print(" Görev ekleme iptal edildi.")
            return

        if not yeni_gorev:
            print(" Boş görev eklenemez! Lütfen geçerli bir görev girin.")   #  continue ile eğer kişi boş görev grerse tekrar bir görev girmesi için
            continue

        gorev_listesi.append(yeni_gorev)
        print(f" '{yeni_gorev}' görevi başarıyla eklendi!")
        gorevleri_kaydet()
        break # geçerli görev girilince appaend ile görev listesine eklendi ve break ile bu fonskiyondan çıkıyor

def gorev_duzenle():
    """
    Mevcut görevi düzenler
    """
    if not gorev_listesi:   # eğer görev listesi boş ise görev bulunmadı yazdırıp bu fonksiyonadan return boş ile çıkış yapar
        print(" Düzenlenecek görev bulunamadı!")
        return

    gorevleri_listele()

    while True:
        try:                               # try içindeki kodlarda hata çıktığında except çalışır
            secim = input(f"\n Düzenlemek istediğiniz görevin numarasını girin (1-{len(gorev_listesi)}, iptal için 'w'): ").strip() # burada 1-den lsita uzunluğu kadar sayı arasında seçim yaptırıyorum yani görevler arasında

            if secim.lower() == 'w':                #  w ile bu fonksiyondan çıkıyoruz
                print(" Görev düzenleme iptal edildi.")
                return

            gorev_no = int(secim)     #  burada aslında kişi doğru bir karakter girmiş mi kontrol eğer int türüne çevrilmezse hatalı

            if 1 <= gorev_no <= len(gorev_listesi):   #  seçim listede gerçli bir görev mi kontrol burada ediyordz
                eski_gorev = gorev_listesi[gorev_no - 1]    # burada listede indeksi işaretliyoruz 3. satır 2. indeks gibi
                print(f" Mevcut görev: {eski_gorev}")

                while True:
                    yeni_gorev = input(" Yeni görev metnini girin (iptal için 'w'): ").strip()   # eski metni değiştirip bu kısımda yeni görevi giriyoruz

                    if yeni_gorev.lower() == 'w':
                        print(" Görev düzenleme iptal edildi.")
                        return

                    if not yeni_gorev:   #  yeni görev girilmedi ise continue ile  devam eder ve döngüde oldupumu içinyeni görevi bekler
                        print(" Boş görev metni giremezsiniz!")
                        continue

                    gorev_listesi[gorev_no - 1] = yeni_gorev          # listedeki görevi yeni görevle burada değiştiriyoruz
                    print(f" Görev başarıyla güncellendi: '{yeni_gorev}'")
                    gorevleri_kaydet()     #  görev listesini dosyada da kaydettik
                    return
            else:
                print(f" Lütfen 1-{len(gorev_listesi)} arasında bir sayı girin!")   # yukarda belirtien aralık mı kontrolünü if ile yapmıştık aksi durumu bu kısımda çalışır

        except ValueError:
            print(" Lütfen geçerli bir sayı girin!")

def gorev_sil():
    """
    Seçilen görevi siler
    """
    if not gorev_listesi:
        print(" Silinecek görev bulunamadı!")
        return

    gorevleri_listele()

    while True:
        try:
            secim = input(f"\n Silmek istediğiniz görevin numarasını girin (1-{len(gorev_listesi)}, iptal için 'w'): ").strip()  # gorev_duzenle fonksiyonunda yaptığımızın aynısı aslında burada da gerçli aralık bekliyoruz

            if secim.lower() == 'w':
                print(" Görev silme işlemi iptal edildi.")
                return

            gorev_no = int(secim)

            if 1 <= gorev_no <= len(gorev_listesi):    # seçilen görev nuraması listede var mı kontrol ediyorum. en az 1 ve liste uzunluğu arası
                silinen_gorev = gorev_listesi.pop(gorev_no - 1)     #  pop belirtilen indeksteki görevi silip onun döndürür. -1 indeks sayısındak kaynaklı.
                print(f" '{silinen_gorev}' görevi başarıyla silindi!")
                gorevleri_kaydet()  # silinen görev ile birlikte listeyi dosyada güncelliyorum
                return
            else:
                print(f" Lütfen 1-{len(gorev_listesi)} arasında bir sayı girin!")

        except ValueError:
            print(" Lütfen geçerli bir sayı girin!")

def menu_goster():   # menü fonksiyonu

    print(" __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  ")
    print("|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__| ")
    print(" 1. Görevleri Listele")
    print(" __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  ")
    print("|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__| ")
    print(" 2. Yeni Görev Ekle")
    print(" __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  ")
    print("|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__| ")
    print(" 3. Görev Düzenle")
    print(" __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  ")
    print("|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__| ")
    print(" 4. Görev Sil")
    print(" __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  ")
    print("|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__| ")
    print(" 5. Çıkış")
    print(" __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  ")
    print("|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__| ")


def ana_program():  # tüm fonksiyonları birleştirip bir program yaptığım fonskiyon
    """
    buraya bir header ekledim texti ascıı ye çevirerek
    """
    print(" __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __ __  ")
    print("|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__| ")
    print("▄▄▄▄▄          ·▄▄▄▄            ▄▄▌  ▪  .▄▄ · ▄▄▄▄▄")
    print("•██  ▪         ██▪ ██ ▪         ██•  ██ ▐█ ▀. •██  ")
    print(" ▐█.▪ ▄█▀▄     ▐█· ▐█▌ ▄█▀▄     ██▪  ▐█·▄▀▀▀█▄ ▐█.▪")
    print(" ▐█▌·▐█▌.▐▌    ██. ██ ▐█▌.▐▌    ▐█▌▐▌▐█▌▐█▄▪▐█ ▐█▌·")
    print(" ▀▀▀  ▀█▄▀▪    ▀▀▀▀▀•  ▀█▄▀▪    .▀▀▀ ▀▀▀ ▀▀▀▀  ▀▀▀ ")

    # Başlangıçta dosyadan görevleri yüklemek için
    dosya_okuma()


    while True:   # sürekli menü ile kullanıcıdan komut bekleyecek
        menu_goster()

        try:
            secim = input(" Lütfen menüden bir işlem seçin (1-5): ").strip()

            if secim == '1':
                gorevleri_listele()
            elif secim == '2':
                yeni_gorev_ekle()
            elif secim == '3':
                gorev_duzenle()
            elif secim == '4':
                gorev_sil()
            elif secim == '5':
                print(" To Do List Uygulamasından çıkılıyor...")
                print(" Tüm değişiklikler kaydedildi.")
                break   #  break ile döngüden çıkıp uygulama sonlandıryorum
            else:
                print(" Geçersiz seçim! Lütfen 1-5 arasında bir sayı girin.")

        except KeyboardInterrupt:                                    #klavye interruptı gelince program sonlansın
            print("\n\n Program sonlandırıldı. Güle güle!")
            break
        except Exception as e:
            print(f" Beklenmeyen hata: {e}")

# Programı çalıştırmak için fonksiyon
if __name__ == "__main__":
    ana_program()