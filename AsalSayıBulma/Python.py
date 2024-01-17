while True:
    sayı = int(input("Bir sayı girin : "))

    if sayı == 0:
        print("Çıkış yapılıyor.")
        break

    if sayı <= 1:
        print(f"{sayı} asal bir sayı değildir.")
    else:
        asal_mi = True
        for i in range(2, int(sayı ** 0.5) + 1):
            if sayı % i == 0:
                asal_mi = False
                break

        if asal_mi:
            print(f"{sayı} asal bir sayıdır.")
        else:
            print(f"{sayı} asal bir sayı değildir.")