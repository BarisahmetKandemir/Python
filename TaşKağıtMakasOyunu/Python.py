import random

def kullanıcı_seçimini_getir():
    while True:
        kullanıcı_seçimi = input("Taş mı?, Kağıt mı?, Makas mı?").lower()
        if kullanıcı_seçimi in ["taş", "kağıt", "makas"]:
            return kullanıcı_seçimi
        else:
            print("Geçersiz ifade girdiniz, lütfen belirlenen ifadelerden birini giriniz.")

def bilgisayar_seçimini_getir():
    return random.choice(["taş", "kağıt", "makas"])

def kazanını_belirle(kullanıcı_seçimi, bilgisayar_seçimi):
    if kullanıcı_seçimi == bilgisayar_seçimi:
        return "Berabere. \U0001F91E"
    elif (kullanıcı_seçimi == "taş" and bilgisayar_seçimi == "makas") or \
         (kullanıcı_seçimi == "kağıt" and bilgisayar_seçimi == "taş") or \
         (kullanıcı_seçimi == "makas" and bilgisayar_seçimi == "kağıt"):
        return "Kazandınız! \U0001F929"
    else:
        return "Bilgisayar Kazandı! \U0001F60F"

def oyun():
    print("Taş-Kağıt-Makas oyununa hoş geldiniz!")
    count_kul = 0
    count_bil = 0

    while True:
        kullanıcı = kullanıcı_seçimini_getir()
        bilgisayar = bilgisayar_seçimini_getir()
        print(f"Siz: {kullanıcı}, Bilgisayar: {bilgisayar}")
        sonuç = kazanını_belirle(kullanıcı, bilgisayar)
        if sonuç == "Kazandınız! \U0001F929":
            count_kul += 1
        elif sonuç == "Bilgisayar Kazandı! \U0001F60F":
            count_bil += 1

        if count_kul == 3:
            print("Oyunu siz kazandınız. \U0001F973")
            break
        elif count_bil == 3:
            print("Oyunu bilgisayar kazandı. \U0001F62D")
            break

oyun()