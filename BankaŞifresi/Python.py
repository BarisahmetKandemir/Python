hak = 5
şifre = "2015" 

while hak > 0:
  giriş = input("Lütfen şifrenizi 4 haneli olarak giriniz: ")
  if len(giriş) == 4:
    if şifre == giriş:
      print("Şifre doğru, hangi işlemi yapmak istersiniz?")
      break
    else:
      hak = hak - 1 # hak -= 1
      print(f"Şifrenizi yanlış girdiniz, lütfen tekrar deneyiniz! Kalan hak: {hak}")
  else:
    hak -= 1
    print(f"Lütfen 4 haneli giriş yapınız, şifreyi yanlış girdiniz. Kalan hak: {hak}")

if hak == 0:
  print("5 kez hatalı şifre girdiniz.Şifreniz bloke olmuştur, kartınızı almak için bankayla görüşünüz.")