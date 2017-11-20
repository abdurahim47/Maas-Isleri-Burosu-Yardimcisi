# -*- coding: utf-8 -*-

"""
Algoritma ve Programlama Güz Dönemi 1. Proje
PyCharm Edu 4 ile Python 3.6.3 sürümü altında geliştirilmiştir.
UTF-8 ile kodlanmıştır.
"""

toplam_brut_ucret = toplam_net_ucret = toplam_gelir_vergisi = 0.0
calisan_sayisi = ikibin_alti_calisan_sayisi = 0
onbeslik_vergi_calisan_say = yirmilik_vergi_calisan_say = 0
yirmiyedilik_vergi_calisan_say = otuzbeslik_vergi_calisan_say = 0
evli_say = bekar_say = ucten_fazla_cocuk_say = esi_de_calisan_say = 0
calismayan_es_yardimi = 0.0
engelli_say = toplam_cocuk_say = esi_calismayan_say = toplam_calisan_say = cocugu_olanlar = 0
aylik_brut_max = aylik_net_max = 0.0
max_brut_kimlik_no = 0
max_brut_aylik_net = max_brut_gelir_vergisi_kesintisi = 0.0
max_brut_ad_soyad = ''
max_net_kimlik_no = 0
max_net_aylik_brut = max_net_gelir_vergisi_kesintisi = 0.0
max_net_ad_soyad = ''
iki_yuzluk_say = yuzluk_say = ellilik_say = yirmilik_say = onluk_say = beslik_say = 0
birlik_say = ellikurus_say = yirmibes_kurus_say = onkurus_say = beskurus_say = birkurus_say = 0


print(__doc__)
print("-"*25,"Maaş İşleri Bürosu Yardımcısı","-"*25,end=('\n'*3))

while True:
    kimlik_no = engel_yuzdesi = engel_derecesi = 0
    aylik_brut = aylik_net = gelir_vergisi_kesintisi = cocuk_yardimi = 0.0
    calisanin_toplam_brutu = 0.0
    medeni_durum = es_calisiyor_mu = cocuk_var_mi = engelli_mi = ''
    kac_cocuk = altidan_buyuk = alti_ve_altidan_kucuk = 0
    ad_soyad = ''
    gecici_net_ucret = 0.0
    sayi1 = sayi2 = sayi3 = sayi4 = sayi5 = sayi6 = sayi7 = sayi8 = sayi9 = sayi10 = sayi11 = sayi12 = 0


    kimlik_no = int(input("Kimlik numaranızı giriniz: "))
    ad_soyad = input("Adınızı Soyadınızı giriniz: ")

    while True:
        aylik_brut = float(input("Aylık brüt ücretinizi girin( > 1777,5 ):"))
        if aylik_brut >= 1777.50:
            break
        else:
            continue

    calisanin_toplam_brutu = aylik_brut

    #Medeni durumun sorgulanması ve buna bağlı olarak evli-bekar/eşi işsiz-çalışan tespiti
    while True:
        medeni_durum = input("Medeni durumunuz (Evliyse e/E bekarsa b/B):")
        if medeni_durum == 'e' or medeni_durum == 'E' or medeni_durum == 'b' or medeni_durum == 'B':
            break
        else:
            continue

    if medeni_durum == 'e' or medeni_durum == 'E':
        evli_say = evli_say + 1

        while True:
            es_calisiyor_mu = input("Eşiniz çalışıyor mu(e/E-h/H):")
            if es_calisiyor_mu == 'e' or es_calisiyor_mu == 'E' or es_calisiyor_mu == 'h' or es_calisiyor_mu == 'H':
                break
            else:
                continue

        if es_calisiyor_mu == 'e' or es_calisiyor_mu == 'E':
            esi_de_calisan_say = esi_de_calisan_say + 1
            calismayan_es_yardimi = 0.0
        elif es_calisiyor_mu == 'h' or es_calisiyor_mu == 'H':
            calismayan_es_yardimi = 220.0
            calisanin_toplam_brutu = calisanin_toplam_brutu + calismayan_es_yardimi
            esi_calismayan_say = esi_calismayan_say + 1
    elif medeni_durum == 'b' or medeni_durum == 'B':
        bekar_say = bekar_say + 1

    #Çocukların sorgulanması ve üçten fazla çocuk sahibi çalışan sayısı tespiti

    while True:
            cocuk_var_mi = input("Çocuğunuz var mı?(e/E-h/H):")
            if cocuk_var_mi == 'e' or cocuk_var_mi == 'E' or cocuk_var_mi == 'h' or cocuk_var_mi == 'H':
                break
            else:
                continue

    if cocuk_var_mi == 'e' or cocuk_var_mi == 'E':
        cocugu_olanlar = cocugu_olanlar + 1

        while True:
            kac_cocuk = int(input("Kaç çocuğunuz var? :"))
            if kac_cocuk > 0:
                break
            else:
                continue

        if kac_cocuk > 3:
            ucten_fazla_cocuk_say = ucten_fazla_cocuk_say + 1

        while True:
            altidan_buyuk = int(input("Altı yaşından büyük çocuk sayısı:"))
            if altidan_buyuk > 0:
                break
            else:
                continue

        alti_ve_altidan_kucuk = kac_cocuk - altidan_buyuk
        cocuk_yardimi = alti_ve_altidan_kucuk * 25.0 + altidan_buyuk * 45.0
        calisanin_toplam_brutu = calisanin_toplam_brutu + cocuk_yardimi
        toplam_cocuk_say = toplam_cocuk_say + kac_cocuk

    #Aylık net maaş hesabı - engelli indirimi olmadan
    if aylik_brut < 2000.0:
        onbeslik_vergi_calisan_say = onbeslik_vergi_calisan_say + 1
        gelir_vergisi_kesintisi = calisanin_toplam_brutu * 0.15
        aylik_net = calisanin_toplam_brutu - gelir_vergisi_kesintisi
    elif aylik_brut < 5000.0:
        yirmilik_vergi_calisan_say = yirmilik_vergi_calisan_say + 1
        gelir_vergisi_kesintisi = calisanin_toplam_brutu * 0.20
        aylik_net = calisanin_toplam_brutu - gelir_vergisi_kesintisi
    elif aylik_brut < 10000.0:
        yirmiyedilik_vergi_calisan_say = yirmiyedilik_vergi_calisan_say + 1
        gelir_vergisi_kesintisi = calisanin_toplam_brutu * 0.27
        aylik_net = calisanin_toplam_brutu - gelir_vergisi_kesintisi
    else:
        otuzbeslik_vergi_calisan_say = otuzbeslik_vergi_calisan_say + 1
        gelir_vergisi_kesintisi = calisanin_toplam_brutu * 0.35
        aylik_net = calisanin_toplam_brutu - gelir_vergisi_kesintisi

    #Maksimum aylık brüt ücret alan çalışanın bilgileri
    if calisanin_toplam_brutu > aylik_brut_max:
        aylik_brut_max = calisanin_toplam_brutu
        max_brut_kimlik_no = kimlik_no
        max_brut_ad_soyad = ad_soyad
        max_brut_aylik_net = aylik_net
        max_brut_gelir_vergisi_kesintisi = gelir_vergisi_kesintisi


    #Çalışanlara ödenen toplam brüt ücretin hesaplanması
    toplam_brut_ucret = toplam_brut_ucret + calisanin_toplam_brutu

    while True:
            engelli_mi = input("Engellilik durumunuz var mı(e/E-h/H):")
            if engelli_mi == 'e' or engelli_mi == 'E' or engelli_mi == 'h' or engelli_mi == 'H':
                break
            else:
                continue

    if engelli_mi == 'e' or engelli_mi == 'E':
        engelli_say = engelli_say + 1

        while True:
            engel_yuzdesi = int(input("Engellinin engel yüzdesi? :"))
            if engel_yuzdesi > 0 and engel_yuzdesi < 101:
                break
            else:
                continue

        if engel_yuzdesi >= 80 and engel_yuzdesi <= 100:
            engel_derecesi = 1
            aylik_net = aylik_net + 900.00
            gelir_vergisi_kesintisi = gelir_vergisi_kesintisi - 900.00
        elif engel_yuzdesi >= 60:
            engel_derecesi = 2
            aylik_net = aylik_net + 470.00
            gelir_vergisi_kesintisi = gelir_vergisi_kesintisi - 470.00
        elif engel_yuzdesi >= 40:
            engel_derecesi = 3
            aylik_net = aylik_net + 210.00
            gelir_vergisi_kesintisi = gelir_vergisi_kesintisi - 210.00

    #Aylık 2000.0 TL net maaşın altında çalışan gariban takımı
    if aylik_net < 2000.0:
        ikibin_alti_calisan_sayisi = ikibin_alti_calisan_sayisi + 1

    #Maksimum aylık net ücret alan çalışanın bilgileri
    if aylik_net > aylik_net_max:
        aylik_net_max = aylik_net
        max_net_kimlik_no = kimlik_no
        max_net_ad_soyad = ad_soyad
        max_net_aylik_brut = aylik_brut
        max_net_gelir_vergisi_kesintisi = gelir_vergisi_kesintisi

    #Çalışanlara ödenen toplam net ücretin hesaplanması
    toplam_net_ucret = toplam_net_ucret + aylik_net

    #Devlete ödenen toplam gelir vergisinin hesaplanması
    toplam_gelir_vergisi = toplam_gelir_vergisi + gelir_vergisi_kesintisi


    print("-"*50)

    print("Çalışanın kimlik numarası: ",kimlik_no)
    print("Çalışanın adı soyadı: ",ad_soyad)
    print("Çalışanın aylık brüt ücreti: {:.2f}".format(aylik_brut))
    if medeni_durum == 'e' or medeni_durum == 'E':
        if es_calisiyor_mu == 'h' or es_calisiyor_mu == 'H':
            print("Çalışmayan eş yardımı: {:.2f}".format(calismayan_es_yardimi))

    if cocuk_var_mi == 'e' or cocuk_var_mi == 'E':
        print("Çalışana yapılan çocuk yardımı: {:.2f}".format(cocuk_yardimi))

    print("Çalışanın aylık toplam brütü: {:.2f}".format(calisanin_toplam_brutu))


    if engelli_mi == 'e' or engelli_mi == 'E':
        print("Engellilik derecesi: ",engel_derecesi)
        if engel_derecesi == 1:
            print(engel_derecesi,". derece engelliye yapılan engelli ödeneği: {:.2f}".format(900.00))
        elif engel_derecesi == 2:
            print("Engelliye iade edilen vergi kesintisi: {:.2f}".format(470.00))
        elif engel_derecesi == 3:
            print("Engelliye iade edilen vergi kesintisi: {:.2f}".format(210.00))


    print("Gelir Vergisi Kesintisi: {:.2f}".format(gelir_vergisi_kesintisi))
    print("Çalışanın aylık net ücreti: {:.2f}".format(aylik_net))

    gecici_net_ucret = aylik_net


    sayi1 = gecici_net_ucret // 200
    if sayi1 > 0:
        print("Gerekli olan 200 TL'lik banknot sayısı: {:.0f}".format(sayi1))
        iki_yuzluk_say = iki_yuzluk_say + sayi1
        gecici_net_ucret = gecici_net_ucret - sayi1 * 200

    sayi2 = gecici_net_ucret // 100
    if sayi2 > 0:
        print("Gerekli olan 100 TL'lik banknot sayısı: {:.0f}".format(sayi2))
        yuzluk_say = yuzluk_say + sayi2
        gecici_net_ucret = gecici_net_ucret - sayi2 * 100

    sayi3 = gecici_net_ucret // 50
    if sayi3 > 0:
        print("Gerekli olan 50 TL'lik banknot sayısı: {:.0f}".format(sayi3))
        ellilik_say = ellilik_say + sayi3
        gecici_net_ucret = gecici_net_ucret - sayi3 * 50


    sayi4 = gecici_net_ucret // 20
    if sayi4 > 0:
        print("Gerekli olan 20 TL'lik banknot sayısı: {:.0f}".format(sayi4))
        yirmilik_say = yirmilik_say + sayi4
        gecici_net_ucret = gecici_net_ucret - sayi4 * 20


    sayi5 = gecici_net_ucret // 10
    if sayi5 > 0:
        print("Gerekli olan 10 TL'lik banknot sayısı: {:.0f}".format(sayi5))
        onluk_say = onluk_say + sayi5
        gecici_net_ucret = gecici_net_ucret - sayi5 * 10


    sayi6 = gecici_net_ucret // 5
    if sayi6 > 0:
        print("Gerekli olan 5 TL'lik banknot sayısı: {:.0f}".format(sayi6))
        beslik_say = beslik_say + sayi6
        gecici_net_ucret = gecici_net_ucret - sayi6 * 5


    sayi7 = gecici_net_ucret // 1
    if sayi7 > 0:
        print("Gerekli olan 1 TL'lik banknot sayısı: {:.0f}".format(sayi7))
        birlik_say = birlik_say + sayi7
        gecici_net_ucret = gecici_net_ucret - sayi7 * 1


    sayi8 = gecici_net_ucret // 0.5
    if sayi8 > 0:
        print("Gerekli olan 0.50 TL'lik banknot sayısı: {:.0f}".format(sayi8))
        ellikurus_say = ellikurus_say + sayi8
        gecici_net_ucret = gecici_net_ucret - sayi8 * 0.50


    sayi9 = gecici_net_ucret // 0.25
    if sayi9 > 0:
        print("Gerekli olan 0.25 TL'lik banknot sayısı: {:.0f}".format(sayi9))
        yirmibes_kurus_say = yirmibes_kurus_say + sayi9
        gecici_net_ucret = gecici_net_ucret - sayi9 * 0.25


    sayi10 = gecici_net_ucret // 0.10
    if sayi10 > 0:
        print("Gerekli olan 0.10 TL'lik banknot sayısı: {:.0f}".format(sayi10))
        onkurus_say = onkurus_say + sayi10
        gecici_net_ucret = gecici_net_ucret - sayi10 * 0.10


    sayi11 = gecici_net_ucret // 0.05
    if sayi11 > 0:
        print("Gerekli olan 0.05 TL'lik banknot sayısı: {:.0f}".format(sayi11))
        beskurus_say = beskurus_say + sayi11
        gecici_net_ucret = gecici_net_ucret - sayi11 * 0.05


    sayi12 = gecici_net_ucret // 0.01
    if sayi12 > 0:
        print("Gerekli olan 0.01 TL'lik banknot sayısı: {:.0f}".format(sayi12))
        birkurus_say = birkurus_say + sayi12
        gecici_net_ucret = gecici_net_ucret - sayi12 * 0.01


    devam_mi = ''
    devam_mi = input("Başka çalışan var mı? (e/E(vet)-h/H(ayır))")
    if devam_mi == 'h' or devam_mi == 'H':
        break

toplam_calisan_say = evli_say + bekar_say


print("Çalışanlara aylık ödenen toplam net ücret: {:.2f}".format(toplam_net_ucret))
print("Devlete ödenen gelir vergisi tutarı: {:.2f}".format(toplam_gelir_vergisi))
print("Toplam brüt ücretin çalışan sayısına oranı: {:.2f}".format((toplam_brut_ucret/toplam_calisan_say)))
print("Toplam net ücretin çalışan sayısına oranı: {:.2f}".format((toplam_net_ucret/(evli_say + bekar_say))))

if iki_yuzluk_say > 0:
    print("Gerekli olan 200 TL'lik banknot sayısı: ",iki_yuzluk_say)
if yuzluk_say > 0:
    print("Gerekli olan 100 TL'lik banknot sayısı: ",yuzluk_say)
if ellilik_say > 0:
    print("Gerekli olan 50 TL'lik banknot sayısı: ",ellilik_say)
if yirmilik_say > 0:
    print("Gerekli olan 20 TL'lik banknot sayısı: ",yirmilik_say)
if onluk_say > 0:
    print("Gerekli olan 10 TL'lik banknot sayısı: ",onluk_say)
if beslik_say > 0:
    print("Gerekli olan 5 TL'lik banknot sayısı: ",beslik_say)
if birlik_say > 0:
    print("Gerekli olan 1 TL'lik madeni para sayısı: ",birlik_say)
if ellikurus_say > 0:
    print("Gerekli olan 0.50 TL'lik madeni para sayısı: ",ellikurus_say)
if yirmibes_kurus_say > 0:
    print("Gerekli olan 0.25 TL'lik madeni para sayısı: ",yirmibes_kurus_say)
if onkurus_say > 0:
    print("Gerekli olan 0.10 TL'lik madeni para sayısı: ",onkurus_say)
if beskurus_say > 0:
    print("Gerekli olan 0.05 TL'lik madeni para sayısı: ",beskurus_say)
if birkurus_say > 0:
    print("Gerekli olan 0.01 TL'lik madeni para sayısı: ",birkurus_say)

if ikibin_alti_calisan_sayisi > 0:
    print("2000 TL altı net maaş alanların sayısı: ",ikibin_alti_calisan_sayisi)

if onbeslik_vergi_calisan_say > 0:
    print("Yüzde 15lik vergi dilimine girenlerin sayısı: {:d}".format(onbeslik_vergi_calisan_say))
    print("Bunların bütüne oranı: {:.2f}".format((onbeslik_vergi_calisan_say/toplam_calisan_say)*100))

if yirmilik_vergi_calisan_say > 0:
    print("Yüzde 20lik vergi dilimine girenler: {:d}".format(yirmilik_vergi_calisan_say))
    print("Bunların bütüne oranı: {:.2f}".format((yirmilik_vergi_calisan_say/toplam_calisan_say)*100))

if yirmiyedilik_vergi_calisan_say > 0:
    print("Yüzde 27lik vergi dilimine girenler: {:d}".format(yirmiyedilik_vergi_calisan_say))
    print("Bunların bütüne oranı: {:.2f}".format((yirmiyedilik_vergi_calisan_say/toplam_calisan_say)*100))

if otuzbeslik_vergi_calisan_say > 0:
    print("Yüzde 35lik vergi dilimine girenler: {:d}".format(otuzbeslik_vergi_calisan_say))
    print("Bunların bütüne oranı: {:.2f}".format((otuzbeslik_vergi_calisan_say/toplam_calisan_say)*100))

print("Aylık Toplam Brüt Ücreti En Yüksek Olan Çalışan:")
print("-"*50)
print("TC Kimlik Numarası: ",max_brut_kimlik_no)
print("Adı Soyadı: ",max_brut_ad_soyad)
print("Aylık Toplam Brüt Ücreti: {:.2f}".format(aylik_brut_max))
print("Gelir Vergisi Kesintisi: {:.2f}".format(max_brut_gelir_vergisi_kesintisi))
print("Aylık Net Geliri: {:.2f}".format(max_brut_aylik_net))
print("\n"*3)

print("Aylık Toplam Net Ücreti En Yüksek Olan Çalışan:")
print("-"*50)
print("TC Kimlik Numarası: ",max_net_kimlik_no)
print("Adı Soyadı: ",max_net_ad_soyad)
print("Aylık Toplam Brüt Ücreti: {:.2f}".format(max_net_aylik_brut))
print("Gelir Vergisi Kesintisi: {:.2f}".format(max_net_gelir_vergisi_kesintisi))
print("Aylık Net Geliri: {:.2f}".format(aylik_net_max))

if evli_say > 0:
    print("Evlilerin Bütüne Oranı: {:.2f}".format((evli_say/toplam_calisan_say) * 100))
if bekar_say > 0:
    print("Bekarların Bütüne Oranı: {:.2f}".format((bekar_say/toplam_calisan_say) * 100))

if esi_de_calisan_say > 0:
    print("Evlilerin içindeki çalışan eş oranı: {:.2f}".format((esi_de_calisan_say/toplam_calisan_say) * 100))

if cocugu_olanlar > 0:
    print("Bakmakla yükümlü olduğu çocuğu bulunanların ortalama çocuk sayıları: ",end='')
    print("{:.2f}".format(toplam_cocuk_say/cocugu_olanlar))

if ucten_fazla_cocuk_say > 0:
    print("Üçten fazla çocuğu olanların sayısı: ",ucten_fazla_cocuk_say)

if engelli_say > 0:
    print("Toplamdaki engelli sayısı: ",engelli_say)
    print("Engellilerin bütüne oranı: {:.2f}".format((engelli_say/toplam_calisan_say) * 100))
