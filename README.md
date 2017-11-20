# Maaş İşleri Bürosu Yardımcısı
Ege Üniversitesi Bilgisayar Mühendisliği Güz Dönemi 1. Proje (Python Tabanlı - İşlenen konular ileri düzey olmadığından bu projenin daha üst versiyonları da olabilir/yapabilirsiniz. Bu proje sadece kaleciyi çalıştıran şutlardır. Kolay gelsin herkese.)

                                                 
                                                  ## GENEL BİLGİLER

Aylık Brüt Asgari Ücret: Çalışanlara ödenecek aylık brüt asgari ücret, 1777,50 TL’dir.

Eş İçin Aile Yardımı Ödeneği: Evli bir çalışana, eşi çalışmıyorsa her ay 220 TL brüt ek ücret
ödenmektedir.

Çocuk İçin Aile Yardımı Ödeneği: Çalışana, bakmakla yükümlü olduğu her bir çocuk için
her ay aşağıdaki miktarda brüt ek ücret ödenmektedir.


Bakmakla yükümlü olunan çocuğun yaşı        Ek ödenek (TL)
6 ve daha küçük                             25
6’dan büyük                                 45


Aylık Toplam Brüt Ücret: Çalışanlara ödenen aylık brüt ücret ile ek ödeneklerin toplamıdır.

Gelir Vergisi: Çalışanların aylık toplam brüt ücretlerinden, aşağıdaki tabloda belirtilen
oranlarda gelir vergisi kesintisi yapılarak devlete aktarılmaktadır.


Aylık toplam brüt ücret                                 Gelir vergisi oranı (%)
2000 TL’den az                                          15
2000 TL veya 2000 TL’den çok, 5000 TL’den az            20
5000 TL veya 5000 TL’den çok, 10000 TL’den az           27
10000 TL veya 10000 TL’den çok                          35


Engelli Vergi İndirimi: Engelli çalışanların aylık toplam brüt ücretlerinin aşağıdaki tabloda
belirtildiği kadarki miktarı, gelir vergisinden muaf tutulmaktadır:


Engellilik oranı                                                  Aylık toplam brüt ücretin, gelir vergisinden muaf tutulan miktarı (TL)
%80 veya daha yüksek (1. derece engelli)                          900        
%60 veya %60’dan yüksek, %80’den düşük (2. derece engelli)        470
%40 veya %40’dan yüksek, %60’dan düşük (3. derece engelli)        210


Aylık Net Ücret: Çalışanların aylık toplam brüt ücretinden gelir vergisi kesintisi yapıldıktan
sonra kalan miktardır.

Tedavüldeki Banknot Türleri: 200 TL, 100 TL, 50 TL, 20 TL, 10 TL, 5 TL

Tedavüldeki Madeni Para Türleri: 1 TL, 50 kuruş, 25 kuruş, 10 kuruş, 5 kuruş, 1 kuruş

                                                  
                                                  ## PROBLEM TANIMI

Bir işyerindeki Maaş İşleri Bürosu’nda kullanılmak üzere, çalışanların aylık toplam brüt
ücretlerini, gelir vergisi kesintilerini ve aylık net ücretlerini hesaplamak, en az sayıda banknot
ve madeni para kullanarak maaş ödemelerini yapmak ve çalışanlar hakkında bazı istatistiksel
bilgiler elde etmek için bir program geliştirilmesi istenmektedir. Bunun için işyerindeki her
çalışan için aşağıdaki veriler programa girilecektir:

*TC kimlik numarası

*Ad soyad

*Aylık brüt ücreti (TL): reel sayı (aylık brüt asgari ücret ya da daha büyük)

*Medeni durumu: evli/bekar (e/E/b/B karakterleri)

  **Evliyse eşinin çalışıp çalışmadığı: evet/hayır (e/E/h/H karakterleri)

*Bakmakla yükümlü olduğu çocuk sayısı: tamsayı (0 ya da daha büyük)

  **Bakmakla yükümlü olduğu çocuğu varsa, yaşı 6’dan büyük olanların sayısı: tamsayı (0 ya da daha büyük)

*Engelli olup olmadığı: evet/hayır (e/E/h/H karakterleri)

  **Engelliyse, engellilik oranı: tamsayı (1 ya da daha büyük ve 100 ya da daha küçük)

Her çalışanın verileri girildikten sonra, o çalışan için aşağıdaki bilgiler ekrana yazdırılmalıdır:

-TC kimlik numarası ve adı soyadı

-Aylık brüt ücreti (TL)

-Eş için aile yardımı ödeneği (TL)

-Çocuk için aile yardımı ödeneği (TL)

-Aylık toplam brüt ücreti (TL)

-Gelir vergisi kesintisi (TL)

-Engelli vergi indiriminden yararlanıyorsa, engel derecesi (1./2./3.)

-Aylık net ücreti (TL)

-Aylık net ücretin en az sayıda banknot ve madeni para kullanılarak ödenebilmesi için 
tedavüldeki her para türünden kaçar adet gerektiği (sadece gerekli olan para türleri)

-Daha sonra başka çalışan olup olmadığı sorularak (e/E/h/H karakterleri); varsa sonraki çalışana
ilişkin işlemler yapılmalı, yoksa aşağıdaki istatistiksel bilgiler ekrana yazdırılmalıdır:

--Tüm çalışanlara bir ayda ödenen aylık toplam net ücret tutarı ve devlete aktarılan aylık
toplam gelir vergisi tutarı (TL)

--Tüm çalışanların aylık toplam brüt ücretlerinin ve net ücretlerinin ortalaması (TL)

--Çalışanlara aylık net ücretlerinin en az sayıda banknot ve madeni para kullanılarak
ödenebilmesi için bir ayda tedavüldeki her para türünden toplam kaçar adet gerektiği

--2000 TL’nin altında aylık net ücret alan çalışanların sayısı

--Her gelir vergisi oranı için ayrı ayrı çalışan sayı ve yüzdeleri

--Aylık toplam brüt ücreti en yüksek olan çalışanın TC kimlik numarası, adı soyadı, aylık
toplam brüt ücreti, gelir vergisi kesintisi ve aylık net ücreti (TL)

--Aylık net ücreti en yüksek olan çalışanın TC kimlik numarası, adı soyadı, aylık toplam
brüt ücreti, gelir vergisi kesintisi ve aylık net ücreti (TL)

--Tüm çalışanlar içindeki evli ve bekar olanların yüzdeleri

--Evli olan çalışanların içinde, eşleri de çalışanların yüzdesi

--Sadece bakmakla yükümlü çocuğu olanlar dikkate alınarak, çalışanların bakmakla
yükümlü oldukları çocuk sayısının ortalaması

--Bakmakla yükümlü olduğu çocuk sayısı 3’ten fazla olan çalışanların sayısı

--Engelli çalışanların sayısı ve tüm çalışanlar içindeki yüzdesi
                                                  
                                                  
                                                  ### Notlar
1. Veri girişleri sırasında, kullanıcının parantez içinde belirtilen kısıtlara uygun olarak giriş
yapıncaya kadar beklenilmesi sağlanmalıdır.
2. Çıktı sırasında, reel sayılar virgülden sonra 2 basamağa kadar duyarlı olarak
yazdırılmalıdır.
3. Sıfıra bölme hatası oluşmaması için yeterli miktarda veri girişi yapılacağını varsayınız.
4. En büyük değer bulma istekleri için, bu değere sahip yalnız 1 varlık olabileceğini
varsayınız.
