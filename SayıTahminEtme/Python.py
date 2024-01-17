hedefsayı = random.randint(0,100)
tahmin = 0
denemesayısı = 0

while tahmin != hedefsayı :
  tahmin = int(input("Lütfen 1 ile 100 arasında bir sayı giriniz"))
  denemesayısı += 1
  if denemesayısı < 10 :
    if tahmin < hedefsayı :
      print("Sayınız küçük girdiniz sayıyı büyütünüz")
    elif tahmin > hedefsayı:
      print("Sayınız büyük sayınızı küçültünüz")
    else :
      print(f"Saynız doğrudur {denemesayısı} denemede sayıyı doğru buldunuz😉😎")
      break
  else :
    print(f"Deneme sayısını geçtiniz doğru sayı {hedefsayı}")
    break