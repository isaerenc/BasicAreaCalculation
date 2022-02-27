__author__ = "isaerenc"

while True:
    istek = input("Alanını Hesaplamak istediğiniz şekli seçiniz.:\n 1.Kare\n 2.Dikdörtgen\n 3.Üçgen\n 4.Daire\n 5.Paralel Kenar.:\n")
    if istek=="1":
        # Karenin Alanı Hesaplama
        kkenar = float(input("Karenin bir kenarını giriniz:"))
        print("Karenin Alanı....:", kkenar*kkenar)
    elif istek=="2":
         # Dikdörtgen Alanı Hesaplama
        dkisakenar = float(input("Dikdörtgenin kısa kenar uzunluğunu giriniz:"))
        duzunkenar = float(input("Dikdörtgenin uzun kenar uzunluğunu giriniz:"))
        print("Dikdörtgenin Alanı....:", dkisakenar * duzunkenar)
    elif istek=="3":
        # Üçgenin Alanı Hesaplama
        taban = float(input("Üçgenin taban uzunluğunu giriniz:"))
        yukseklik = float(input("Üçgenin yükseklik uzunluğunu giriniz:"))
        print("Üçgenin Alanı....:", float(taban * yukseklik / 2))
    elif istek=="4":
        # Dairenin Alanı Hesaplama
        dyaricap = float(input("Dairenin yarıçap uzunluğunu giriniz:"))
        pi = float(input("Belirtilen pi (π) sayısını giriniz:"))
        print("Dairenin Alanı....:", dyaricap * 2 * pi)
    elif istek=="5":
        # Paralel kenarın Alanı Hesaplama
        pkenartaban = float(input("Paralel Kenarın taban uzunluğunu giriniz:"))
        pkenaryukseklik = float(input("Paralel Kenarın yükseklik uzunluğunu giriniz:"))
        print("Paralel Kenarın Alanı....:", pkenaryukseklik*pkenartaban)
    else:
        print("Yanlış Giriş Yaptınız lütfen yukarıda verilen 1-2-3-4-5 sayılarından birini giriniz.")
