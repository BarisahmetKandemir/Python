kelime = random.choice(["kedi", "köpek", "kaplumbağa", "zürafa", "fil", "kaplan","tırtıl", "atmaca", "kartal", "jaguar", "balina", "yunus"])
geçerliharfler = "abcdefgğhıijklmnoöpqrstuüvwyz"
hak = 8
yapılan_tahmin = ""

while len(kelime) > 0:
  gerçek_kelime = ""

  for harf in kelime:                                     # bu for döngüsü ilk aşamada bilgisayar tarafından seçilen
    if harf in yapılan_tahmin:                            # kelimenin kaç karakter içerdiğini göstermek için.
      gerçek_kelime = gerçek_kelime + harf
    else:
      gerçek_kelime = gerçek_kelime + "_ "

  if gerçek_kelime == kelime:
    print(gerçek_kelime)
    print("Tebrikler Kazandınız! \U0001F973")
    break

  print(f"Kelimeyi tahmin edebilmeniz için toplam hakkınız: {hak}")
  print(f"Kelimeyi tahmin edin: {gerçek_kelime}")

  tahmin = input("Lütfen bir harf giriniz: ")

  if tahmin in geçerliharfler:
    yapılan_tahmin += tahmin
  else:
    print("Lütfen geçerli bir harf giriniz!")

  if tahmin not in kelime:
    hak -= 1
    if hak == 8:
      print("  --------  ")
      print("            ")
      print("     |      ")
    if hak == 7:
      print("  --------  ")
      print("     O      ")
      print("     |      ")
    if hak == 6:
      print("  --------  ")
      print("     O      ")
      print("     |      ")
      print("    /       ")
    if hak == 5:
      print("  --------  ")
      print("     O      ")
      print("     |      ")
      print("    / \     ")
    if hak == 4:
      print("  --------  ")
      print("   \ O      ")
      print("     |      ")
      print("    / \     ")
    if hak == 3:
      print("  --------  ")
      print("   \ O /    ")
      print("     |      ")
      print("    / \     ")
    if hak == 2:
      print("  --------  ")
      print("   \ O |/   ")
      print("     |      ")
      print("    / \     ")
    if hak == 1:
      print("  --------  ")
      print("   \ O_|/   ")
      print("     |      ")
      print("    / \     ")
    if hak == 0:
      print("Öldürdünüz beni!!! \U0001F635")
      print("  --------  ")
      print("     O_|    ")
      print("    /|\     ")
      print("    / \     ")
      break