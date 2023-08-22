"""18010011014 ÖMER FARUK KOLCU"""
"""AMİRAL BATTI OYUNU: 10X10 LUK TABLODA RASTGELE YERLEŞTİRİLMİŞ GEMİLERİN YERLERİ TAHMİN EDİLİR"""
"""GİZLİ MOD VE AÇIK MOD OLMAK ÜZERE İKİ MOD VARDIR
   VE PUAN HESAPLAMASI YAPILIR"""
#HOCAM OYUNU BİTİRMEK İSTİYORMUSUNUZ SORUSUNU EN SON SORDUM ÇÜNKÜ ÖDEV DOSYASINDA GÖRMEMİŞTİM KONTROL EDERKEN GÖRDÜM
#O YÜZDEN ÖDEVİ DÖNGÜDEN SONRASI OLACAK ŞEKİLDE KES YAPIŞTIR YAPTIM
import random
kackere=1
while kackere==1:
    liste = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        , [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
             [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    yonler = ["dikey", "yatay"]
    sdd = 0
    # bir birimlik geminin dizilimi
    satirsayisi = random.randint(0, 9)  # satırın random seçilimi
    sutunsayisi = random.randint(0, 9)  # sutunun random secilimi
    bir_birimlik_gemi = liste[satirsayisi][sutunsayisi]
    # ---------------------------------------------------------------------------------------------------------------
    sabitsutun = 0
    dsatir1 = 0
    dsatir2 = 0
    ssatir = 0
    dsutun1 = 0
    dsutun2 = 0
    # iki birimlik geminin dizilimi-----------------------------------------------------------------------------------
    yon1 = random.choice(yonler)  # rasgele yön seçimi yapımı
    sat1 = 0
    if yon1 == "dikey":  # --------------------------------------------------DİKEY----------------------------------------
        sabitsutun = random.randint(0, 9)
        dsatir1 = random.randint(0, 9)
        dsatir2 = dsatir1 - 1
        if dsatir2 not in range(0, 9):  # yukarı gidilebilirmi konturalu
            dsatir2 = dsatir1 + 1
            if dsatir1 == dsatir2:
                dsatir2 = dsatir1 + 2
        # dik konulduğu zamna aynı yere denk gelme kontrolu
        for i in range(1, 10):  # 10 defa kontrol eder ancak şart sağlanmaz ise döngüyü kırar
            if (dsatir1 == satirsayisi and sabitsutun == sutunsayisi) or (
                    dsatir2 == satirsayisi and sabitsutun == sutunsayisi):
                sabitsutun = random.randint(0, 9)
                dsatir1 = random.randint(0, 9)
                dsatir2 = dsatir1 - 1
                if dsatir2 not in range(0, 9):  # yukarı gidilebilirmi konturalu
                    dsatir2 = dsatir1 + 1
                    if dsatir1 == dsatir2:
                        dsatir2 = dsatir1 + 2
                say1 = 1
            else:
                break
    sat2 = 0
    if yon1 == "yatay":  # ------------------------------------------YATAY------------------------------------------
        ssatir = random.randint(0, 9)
        dsutun1 = random.randint(0, 9)
        dsutun2 = dsutun1 - 1
        if dsutun2 not in range(0, 10):  # sola gidilebilirmi konturalu
            dsutun2 = dsutun1 + 1
            if dsutun1 == dsutun2:
                dsutun2 = dsutun1 + 2

        for i in range(0, 10):  # yatay konulduğu zaman aynı yere gelme kontrolu
            if (dsutun1 == satirsayisi and ssatir == sutunsayisi) or (dsutun2 == satirsayisi and ssatir == sutunsayisi):
                satirsayisi = random.randint(0, 9)  # satırın random seçilimi print(satirsayisi,sutunsayisi)
                sutunsayisi = random.randint(0,
                                             9)  # sutunun random secilimi print(liste[satirsayisi][sutunsayisi]) print("bir birimlik gemi {}.satir {}.sutunda".format(satirsayisi+1,sutunsayisi+1))
                ssatir = random.randint(0, 9)
                dsutun1 = random.randint(0, 9)
                dsutun2 = dsutun1 - 1
                if dsutun2 not in range(0, 10):  # sola gidilebilirmi konturalu
                    dsutun2 = dsutun1 + 1
                    if dsutun1 == dsutun2:
                        dsutun2 = dsutun1 + 2
                sat2 = 1
            else:
                break
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # üç birimlik gemi yapımıyukarıdakiler farklı yerlerde olduğu için yeni karşılaştırmalarda sadece 3 birimliğin yeri değişir
    ussutun = 0
    udsatir1 = 0
    udsatir2 = 0
    udsatir3 = 0
    yon2 = random.choice(yonler)
    day1 = 0
    day2 = 0
    day3 = 0
    if yon2 == "dikey":  # ------------------------------------------------------------------------DİKEY-----------------
        ussutun = random.randint(0, 9)
        udsatir1 = random.randint(0, 9)
        udsatir2 = udsatir1 + 1
        udsatir3 = udsatir2 + 1
        if udsatir2 not in range(0, 10):  # yön olarak aşağıya gidebilirmi konrtrolu
            udsatir2 = udsatir1 - 1
            udsatir3 = udsatir1 - 2
        elif udsatir3 not in range(0, 10):
            udsatir3 = udsatir1 - 1
    for i in range(0, 20):
        if yon2 == "dikey":  # eğer üçlük gemi dikeyse
            if yon1 == "dikey":  # ve eğer ikilik gemide dikeyse ve aynı yere denk gelmişler ise yeni dikey üç birimlik gemi tanımla
                if ((udsatir1 == dsatir1 and ussutun == sabitsutun) or (
                        udsatir1 == dsatir2 and ussutun == sabitsutun)) or \
                        ((udsatir2 == dsatir1 and ussutun == sabitsutun) or (
                                udsatir2 == dsatir2 and ussutun == sabitsutun)) or \
                        ((udsatir3 == dsatir1 and ussutun == sabitsutun) or (
                                udsatir3 == dsatir2 and ussutun == sabitsutun)):
                    ussutun = random.randint(0, 9)
                    udsatir1 = random.randint(0, 9)
                    udsatir2 = udsatir1 + 1
                    udsatir3 = udsatir2 + 1
                    if udsatir2 not in range(0, 10):
                        udsatir2 = udsatir1 - 1
                        udsatir3 = udsatir1 - 2
                    elif udsatir3 not in range(0, 10):
                        udsatir3 = udsatir1 - 1
                    day1 = 1
            if yon1 == "yatay":  # eğer üç birimlik gemi dik ve iki birimlik gemi yataysa ve karşılaşmışlarsa yeni DİK üç birimlik gemi yapılır
                if ((udsatir1 == ssatir) and (ussutun == dsutun1)) or ((udsatir1 == ssatir) and (ussutun == dsutun2)) or \
                        ((udsatir2 == ssatir) and (ussutun == dsutun1)) or (
                        (udsatir2 == ssatir) and (ussutun == dsutun2)) or \
                        ((udsatir3 == ssatir) and (ussutun == dsutun1)) or (
                        (udsatir3 == ssatir) and (ussutun == dsutun2)):
                    ussutun = random.randint(0, 9)
                    udsatir1 = random.randint(0, 9)
                    udsatir2 = udsatir1 + 1
                    udsatir3 = udsatir2 + 1
                    if udsatir2 not in range(0, 10):
                        udsatir2 = udsatir1 - 1
                        udsatir3 = udsatir1 - 2
                    elif udsatir3 not in range(0, 10):
                        udsatir3 = udsatir1 - 1
                    day2 = 1
                    # eğer üçlük gemi dik ve birlik gemi ile karşılaşmışlar ise yeni DİK üç birimlik tanımla
            if (udsatir1 == satirsayisi and ussutun == sutunsayisi) or (
                    udsatir2 == satirsayisi and ussutun == sutunsayisi) or (
                    udsatir3 == satirsayisi and ussutun == sutunsayisi):
                ussutun = random.randint(0, 9)
                udsatir1 = random.randint(0, 9)
                udsatir2 = udsatir1 + 1
                udsatir3 = udsatir2 + 1
                if udsatir2 not in range(0, 10):
                    udsatir2 = udsatir1 - 1
                    udsatir3 = udsatir1 - 2
                elif udsatir3 not in range(0, 10):
                    udsatir3 = udsatir1 - 1
                day3 = 1
        else:
            break
    yay1 = 0
    yay2 = 0
    yay3 = 0
    if yon2 == "yatay":  # yani üç birimlik gemi yatay ise
        ussatir = random.randint(0, 9)
        udsutun1 = random.randint(0, 9)
        udsutun2 = udsutun1 + 1
        udsutun3 = udsutun2 + 1
        if yon2 == "yatay":
            if udsutun2 not in range(0, 10):
                udsutun2 = udsutun1 - 1
                udsutun3 = udsatir1 - 2
            elif udsutun3 not in range(0, 10):
                udsutun3 = udsutun1 - 1

    for i in range(0,
                   20):  # eğer üç birimlik yatay ile iki birimlik gemi aynı yere denk gelirse yeni üç birimlik YATAY yapılır
        if yon2 == "yatay":
            if yon1 == "dikey":
                if ((ussatir == dsatir1) and (udsutun1 == sabitsutun)) or (
                        (ussatir == dsatir2) and (udsutun1 == sabitsutun)) or \
                        ((ussatir == dsatir1) and (udsutun2 == sabitsutun)) or (
                        (ussatir == dsatir2) and (udsutun2 == sabitsutun)) or \
                        ((ussatir == dsatir1) and (udsutun3 == sabitsutun)) or (
                        (ussatir == dsatir2) and (udsutun3 == sabitsutun)):
                    ussatir = random.randint(0, 9)
                    udsutun1 = random.randint(0, 9)
                    udsutun2 = udsutun1 + 1
                    udsutun3 = udsutun2 + 1
                    if udsutun2 not in range(0, 10):
                        udsutun2 = udsutun1 - 1
                        udsutun3 = udsatir1 - 2
                    elif udsutun3 not in range(0, 10):
                        udsutun3 = udsutun1 - 1
                    yay1 = 1
            if yon1 == "yatay":  # eğer iki birimlik gemi de yatay üç birimlik gemide yatay ise ve aynı yere denk gelmişler ise yeni YATAY üçlük oluşturulur
                if ((ussatir == ssatir) and (udsutun1 == dsutun1)) or ((ussatir == ssatir) and (udsutun1 == dsutun2)) or \
                        ((ussatir == ssatir) and (udsutun2 == dsutun1)) or (
                        (ussatir == ssatir) and (udsutun2 == dsutun2)) or \
                        ((ussatir == ssatir) and (udsutun3 == dsutun1)) or (
                        (ussatir == ssatir) and (udsutun3 == dsutun2)):
                    ussatir = random.randint(0, 9)
                    udsutun1 = random.randint(0, 9)
                    udsutun2 = udsutun1 + 1
                    udsutun3 = udsutun2 + 1
                    if udsutun2 not in range(0, 10):
                        udsutun2 = udsutun1 - 1
                        udsutun3 = udsatir1 - 2
                    elif udsutun3 not in range(0, 10):
                        udsutun3 = udsutun1 - 1
                    yay2 = 1
                    # yatay üç birimlik ile bir birimlik aynı yere gelirse yeni üç birimlik tanımlanır
            if (ussatir == satirsayisi and udsutun1 == sutunsayisi) or (
                    ussatir == satirsayisi and udsutun2 == sutunsayisi) or (
                    ussatir == satirsayisi and udsutun3 == sutunsayisi):
                ussatir = random.randint(0, 9)
                udsutun1 = random.randint(0, 9)
                udsutun2 = udsutun1 + 1
                udsutun3 = udsutun2 + 1
                if udsutun2 not in range(0, 10):
                    udsutun2 = udsutun1 - 1
                    udsutun3 = udsatir1 - 2
                elif udsutun3 not in range(0, 10):
                    udsutun3 = udsutun1 - 1
                yay3 = 1
        else:
            break
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # DÖRT BİRİMLİK GEMİNİN YAPIM

    yon3 = random.choice(yonler)
    fssutun = 0
    fdsatir1 = 0
    fdsatir2 = 0
    fdsatir3 = 0
    fdsatir4 = 0
    if yon3 == "dikey":
        fssutun = random.randint(0, 9)
        fdsatir1 = random.randint(0, 9)
        fdsatir2 = fdsatir1 + 1
        fdsatir3 = fdsatir1 + 2
        fdsatir4 = fdsatir1 + 3
        if fdsatir2 not in range(0, 10):
            fdsatir2 = fdsatir2 - 2
            fdsatir3 = fdsatir3 - 4
            fdsatir4 = fdsatir4 - 6
        if fdsatir3 not in range(0, 10):
            fdsatir3 = fdsatir3 - 3
            fdsatir4 = fdsatir4 - 5
        if fdsatir4 not in range(0, 10):
            fdsatir4 = fdsatir4 - 4
    # DİYER GEMİLER İLE OLAN KARŞILAŞTIRMASINI YAPARKEN 4 BİRİMLİK GEMİNİN YERİ DEĞİŞTİRİLECEK ÇÜNKÜ ZATEN DİYER LERİ FARKLI YERLERDE
    say1 = 0
    say2 = 0
    say3 = 0
    say4 = 0
    say5 = 0
    for i in range(0, 20):
        if yon3 == "dikey":
            if yon2 == "dikey":  # dik üç birimlik gemi ile dik dört birimlik gemi karşılaştırması aynı ise yeni dikey dörtlük yapılır
                if ((fdsatir1 == udsatir1) and (fssutun == ussutun)) or (
                        (fdsatir1 == udsatir2) and (fssutun == ussutun)) or (
                        (fdsatir1 == udsatir3) and (fssutun == ussutun)) \
                        or ((fdsatir2 == udsatir1) and (fssutun == ussutun)) or (
                        (fdsatir2 == udsatir2) and (fssutun == ussutun)) or (
                        (fdsatir2 == udsatir3) and (fssutun == ussutun)) \
                        or ((fdsatir3 == udsatir1) and (fssutun == ussutun)) or (
                        (fdsatir3 == udsatir2) and (fssutun == ussutun)) or (
                        (fdsatir3 == udsatir3) and (fssutun == ussutun)) \
                        or ((fdsatir4 == udsatir1) and (fssutun == ussutun)) or (
                        (fdsatir4 == udsatir2) and (fssutun == ussutun)) or (
                        (fdsatir4 == udsatir3) and (fssutun == ussutun)):
                    fssutun = random.randint(0, 9)
                    fdsatir1 = random.randint(0, 9)
                    fdsatir2 = fdsatir1 + 1
                    fdsatir3 = fdsatir1 + 2
                    fdsatir4 = fdsatir1 + 3
                    if fdsatir2 not in range(0, 10):
                        fdsatir2 = fdsatir2 - 2
                        fdsatir3 = fdsatir3 - 4
                        fdsatir4 = fdsatir4 - 6
                    if fdsatir3 not in range(0, 10):
                        fdsatir3 = fdsatir3 - 3
                        fdsatir4 = fdsatir4 - 5
                    if fdsatir4 not in range(0, 10):
                        fdsatir4 = fdsatir4 - 4
                    say1 = 1
            if yon2 == "yatay":  # eğer dik dört birimlik gemi yatay üç birimlik gemi ile karşılaşırsa yeni dört birimlik yapılır
                if ((fdsatir1 == ussatir) and (udsutun1 == fssutun)) or (
                        (fdsatir1 == ussatir) and (fssutun == udsutun2)) or (
                        (fdsatir1 == ussatir) and (fssutun == udsutun3)) \
                        or ((fdsatir2 == ussatir) and (udsutun1 == fssutun)) or (
                        (fdsatir2 == ussatir) and (fssutun == udsutun2)) or (
                        (fdsatir2 == ussatir) and (fssutun == udsutun3)) \
                        or ((fdsatir3 == ussatir) and (udsutun1 == fssutun)) or (
                        (fdsatir3 == ussatir) and (fssutun == udsutun2)) or (
                        (fdsatir3 == ussatir) and (fssutun == udsutun3)) \
                        or ((fdsatir4 == ussatir) and (udsutun1 == fssutun)) or (
                        (fdsatir4 == ussatir) and (fssutun == udsutun2)) or (
                        (fdsatir4 == ussatir) and (fssutun == udsutun3)):
                    fssutun = random.randint(0, 9)
                    fdsatir1 = random.randint(0, 9)
                    fdsatir2 = fdsatir1 + 1
                    fdsatir3 = fdsatir1 + 2
                    fdsatir4 = fdsatir1 + 3
                    if fdsatir2 not in range(0, 10):
                        fdsatir2 = fdsatir2 - 2
                        fdsatir3 = fdsatir3 - 4
                        fdsatir4 = fdsatir4 - 6
                    if fdsatir3 not in range(0, 10):
                        fdsatir3 = fdsatir3 - 3
                        fdsatir4 = fdsatir4 - 5
                    if fdsatir4 not in range(0, 10):
                        fdsatir4 = fdsatir4 - 4
                    say2 = 1
            if yon1 == "dikey":  # dik dört birimlik dik iki birimlik ile aynı yere denk gelirse yeni bir dört birimlik yapılır
                if ((fdsatir1 == dsatir1) and (fssutun == sabitsutun)) or (
                        (fdsatir1 == dsatir2) and (fssutun == sabitsutun)) \
                        or ((fdsatir2 == dsatir1) and (fssutun == sabitsutun)) or (
                        (fdsatir2 == dsatir2) and (fssutun == sabitsutun)) \
                        or ((fdsatir3 == dsatir1) and (fssutun == sabitsutun)) or (
                        (fdsatir3 == dsatir2) and (fssutun == sabitsutun)) \
                        or ((fdsatir4 == dsatir1) and (fssutun == sabitsutun)) or (
                        (fdsatir4 == dsatir2) and (fssutun == sabitsutun)):
                    fssutun = random.randint(0, 9)
                    fdsatir1 = random.randint(0, 9)
                    fdsatir2 = fdsatir1 + 1
                    fdsatir3 = fdsatir1 + 2
                    fdsatir4 = fdsatir1 + 3
                    if fdsatir2 not in range(0, 10):
                        fdsatir2 = fdsatir2 - 2
                        fdsatir3 = fdsatir3 - 4
                        fdsatir4 = fdsatir4 - 6
                    if fdsatir3 not in range(0, 10):
                        fdsatir3 = fdsatir3 - 3
                        fdsatir4 = fdsatir4 - 5
                    if fdsatir4 not in range(0, 10):
                        fdsatir4 = fdsatir4 - 4
                    say3 = 1
            if yon2 == "yatay":  # yatay ikilik ile dikey dörtlük karşılaştırması aynı yere denk geliyorlarsa yeni dörtlük yapılır
                if ((fdsatir1 == ssatir) and (fssutun == dsutun1)) or ((fdsatir1 == ssatir) and (fssutun == dsutun2)) \
                        or ((fdsatir2 == ssatir) and (fssutun == dsutun1)) or (
                        (fdsatir2 == ssatir) and (fssutun == dsutun2)) \
                        or ((fdsatir3 == ssatir) and (fssutun == dsutun1)) or (
                        (fdsatir3 == ssatir) and (fssutun == dsutun2)) \
                        or ((fdsatir4 == ssatir) and (fssutun == dsutun1)) or (
                        (fdsatir4 == ssatir) and (fssutun == dsutun2)):
                    fssutun = random.randint(0, 9)
                    fdsatir1 = random.randint(0, 9)
                    fdsatir2 = fdsatir1 + 1
                    fdsatir3 = fdsatir1 + 2
                    fdsatir4 = fdsatir1 + 3
                    if fdsatir2 not in range(0, 10):
                        fdsatir2 = fdsatir2 - 2
                        fdsatir3 = fdsatir3 - 4
                        fdsatir4 = fdsatir4 - 6
                    if fdsatir3 not in range(0, 10):
                        fdsatir3 = fdsatir3 - 3
                        fdsatir4 = fdsatir4 - 5
                    if fdsatir4 not in range(0, 10):
                        fdsatir4 = fdsatir4 - 4
                    say4 = 1
                    # bir birimli gemi ile 4 birimlik gemi karşılaştırması eğer aynı yere denk geliyorlarsa yeni dört birimlik gemi yapılır
            if ((fdsatir1 == satirsayisi) and (fssutun == sutunsayisi)) \
                    or ((fdsatir2 == satirsayisi) and (fssutun == sutunsayisi)) \
                    or ((fdsatir3 == satirsayisi) and (fssutun == sutunsayisi)) \
                    or ((fdsatir4 == satirsayisi) and (fssutun == sutunsayisi)):
                fssutun = random.randint(0, 9)
                fdsatir1 = random.randint(0, 9)
                fdsatir2 = fdsatir1 + 1
                fdsatir3 = fdsatir1 + 2
                fdsatir4 = fdsatir1 + 3
                if fdsatir2 not in range(0, 10):
                    fdsatir2 = fdsatir2 - 2
                    fdsatir3 = fdsatir3 - 4
                    fdsatir4 = fdsatir4 - 6
                if fdsatir3 not in range(0, 10):
                    fdsatir3 = fdsatir3 - 3
                    fdsatir4 = fdsatir4 - 5
                if fdsatir4 not in range(0, 10):
                    fdsatir4 = fdsatir4 - 4
                say5 = 1
        else:
            break
    fssatir = 0
    fdsutun1 = 0
    fdsutun2 = 0
    fdsutun3 = 0
    fdsutun4 = 0
    if yon3 == "yatay":
        fssatir = random.randint(0, 9)
        fdsutun1 = random.randint(0, 9)
        fdsutun2 = fdsutun1 + 1
        fdsutun3 = fdsutun2 + 1
        fdsutun4 = fdsutun3 + 1
        if fdsutun2 not in range(0, 10):
            fdsutun2 = fdsutun2 - 2
            fdsutun3 = fdsutun3 - 4
            fdsutun4 = fdsutun4 - 6
        if fdsutun3 not in range(0, 10):
            fdsutun3 = fdsutun3 - 3
            fdsutun4 = fdsutun4 - 5
        if fdsutun4 not in range(0, 10):
            fdsutun4 = fdsutun4 - 4
    tay1 = 0
    tay2 = 0
    tay3 = 0
    tay4 = 0
    tay5 = 0

    for a in range(0, 20):
        if yon3 == "yatay":  # DÖRT BİRİMLİK GEMİ YATAY İSE
            if yon2 == "dikey":  # ve üç birimlik DİKEY gemi ile kesişiyorsa ve aynı ise yeni YATAY dört birimlik oluşturulur
                if ((fssatir == udsatir1) and (fdsutun1 == ussutun)) or (
                        (fssatir == udsatir2) and (fdsutun1 == ussutun)) or (
                        (fssatir == udsatir3) and (fdsutun1 == ussutun)) \
                        or ((fssatir == udsatir1) and (fdsutun2 == ussutun)) or (
                        (fssatir == udsatir2) and (fdsutun2 == ussutun)) or (
                        (fssatir == udsatir3) and (fdsutun2 == ussutun)) \
                        or ((fssatir == udsatir1) and (fdsutun3 == ussutun)) or (
                        (fssatir == udsatir2) and (fdsutun3 == ussutun)) or (
                        (fssatir == udsatir3) and (fdsutun3 == ussutun)) \
                        or ((fssatir == udsatir1) and (fdsutun4 == ussutun)) or (
                        (fssatir == udsatir2) and (fdsutun4 == ussutun)) or (
                        (fssatir == udsatir3) and (fdsutun4 == ussutun)):
                    fssatir = random.randint(0, 9)
                    fdsutun1 = random.randint(0, 9)
                    fdsutun2 = fdsutun1 + 1
                    fdsutun3 = fdsutun2 + 1
                    fdsutun4 = fdsutun3 + 1
                    if fdsutun2 not in range(0, 10):
                        fdsutun2 = fdsutun2 - 2
                        fdsutun3 = fdsutun3 - 4
                        fdsutun4 = fdsutun4 - 6
                    if fdsutun3 not in range(0, 10):
                        fdsutun3 = fdsutun3 - 3
                        fdsutun4 = fdsutun4 - 5
                    if fdsutun4 not in range(0, 10):
                        fdsutun4 = fdsutun4 - 4
                    tay1 = 1
            if yon2 == "yatay":  # yatay dörtlük ile yatay 3 lük karşılaştrıması yapılır aynı yere denk gelmişler ise yeni bir YATAY 4 lük yapılır
                if ((fssatir == ussatir) and (fdsutun1 == udsutun1)) or (
                        (fssatir == ussatir) and (fdsutun1 == udsutun2)) or (
                        (fssatir == ussatir) and (fdsutun1 == udsutun3)) \
                        or ((fssatir == ussatir) and (fdsutun2 == udsutun1)) or (
                        (fssatir == ussatir) and (fdsutun2 == udsutun2)) or (
                        (fssatir == ussatir) and (fdsutun2 == udsutun3)) \
                        or ((fssatir == ussatir) and (fdsutun3 == udsutun1)) or (
                        (fssatir == ussatir) and (fdsutun3 == udsutun2)) or (
                        (fssatir == ussatir) and (fdsutun3 == udsutun3)) \
                        or ((fssatir == ussatir) and (fdsutun4 == udsutun1)) or (
                        (fssatir == ussatir) and (fdsutun4 == udsutun2)) or (
                        (fssatir == ussatir) and (fdsutun4 == udsutun3)):
                    fssatir = random.randint(0, 9)
                    fdsutun1 = random.randint(0, 9)
                    fdsutun2 = fdsutun1 + 1
                    fdsutun3 = fdsutun2 + 1
                    fdsutun4 = fdsutun3 + 1
                    if fdsutun2 not in range(0, 10):
                        fdsutun2 = fdsutun2 - 2
                        fdsutun3 = fdsutun3 - 4
                        fdsutun4 = fdsutun4 - 6
                    if fdsutun3 not in range(0, 10):
                        fdsutun3 = fdsutun3 - 3
                        fdsutun4 = fdsutun4 - 5
                    if fdsutun4 not in range(0, 10):
                        fdsutun4 = fdsutun4 - 4
                    tay2 = 1
            if yon1 == "dikey":  # iki birimlik gemi eğer dikeyse ve aynı yere denk gelmişler ise yeni YATAY dört birimlik gemi oluşturulur
                if ((fssatir == dsatir1) and (fdsutun1 == sabitsutun)) or (
                        (fssatir == dsatir2) and (fdsutun1 == sabitsutun)) \
                        or ((fssatir == dsatir1) and (fdsutun2 == sabitsutun)) or (
                        (fssatir == dsatir2) and (fdsutun2 == sabitsutun)) \
                        or ((fssatir == dsatir1) and (fdsutun3 == sabitsutun)) or (
                        (fssatir == dsatir2) and (fdsutun3 == sabitsutun)) \
                        or ((fssatir == dsatir1) and (fdsutun4 == sabitsutun)) or (
                        (fssatir == dsatir2) and (fdsutun4 == sabitsutun)):
                    fssatir = random.randint(0, 9)
                    fdsutun1 = random.randint(0, 9)
                    fdsutun2 = fdsutun1 + 1
                    fdsutun3 = fdsutun2 + 1
                    fdsutun4 = fdsutun3 + 1
                    if fdsutun2 not in range(0, 10):
                        fdsutun2 = fdsutun2 - 2
                        fdsutun3 = fdsutun3 - 4
                        fdsutun4 = fdsutun4 - 6
                    if fdsutun3 not in range(0, 10):
                        fdsutun3 = fdsutun3 - 3
                        fdsutun4 = fdsutun4 - 5
                    if fdsutun4 not in range(0, 10):
                        fdsutun4 = fdsutun4 - 4
                    tay3 = 1
            if yon1 == "yatay":  # eğer ikilik yatay ile dörtlük yatay aynı yerde ise yeni yatay dörtlük oluşturulur
                if ((fssatir == ssatir) and (fdsutun1 == dsatir1)) or ((fssatir == ssatir) and (fdsutun1 == dsatir2)) \
                        or ((fssatir == ssatir) and (fdsutun2 == dsatir1)) or (
                        (fssatir == ssatir) and (fdsutun2 == dsatir2)) \
                        or ((fssatir == ssatir) and (fdsutun3 == dsatir1)) or (
                        (fssatir == ssatir) and (fdsutun3 == dsatir2)) \
                        or ((fssatir == ssatir) and (fdsutun4 == dsatir1)) or (
                        (fssatir == ssatir) and (fdsutun4 == dsatir2)):
                    fssatir = random.randint(0, 9)
                    fdsutun1 = random.randint(0, 9)
                    fdsutun2 = fdsutun1 + 1
                    fdsutun3 = fdsutun2 + 1
                    fdsutun4 = fdsutun3 + 1
                    if fdsutun2 not in range(0, 10):
                        fdsutun2 = fdsutun2 - 2
                        fdsutun3 = fdsutun3 - 4
                        fdsutun4 = fdsutun4 - 6
                    if fdsutun3 not in range(0, 10):
                        fdsutun3 = fdsutun3 - 3
                        fdsutun4 = fdsutun4 - 5
                    if fdsutun4 not in range(0, 10):
                        fdsutun4 = fdsutun4 - 4
                    tay4 = 1
                    # eğer 4 birimlik yatay 1 birimlik ile denk gelirse YATAY dört birimlik oluştur
            if ((fssatir == satirsayisi) and (fdsutun1 == sutunsayisi)) \
                    or ((fssatir == satirsayisi) and (fdsutun2 == sutunsayisi)) \
                    or ((fssatir == satirsayisi) and (fdsutun3 == sutunsayisi)) \
                    or ((fssatir == satirsayisi) and (fdsutun4 == sutunsayisi)):
                fssatir = random.randint(0, 10)
                fdsutun1 = random.randint(0, 10)
                fdsutun2 = fdsutun1 + 1
                fdsutun3 = fdsutun2 + 1
                fdsutun4 = fdsutun3 + 1
                if fdsutun2 not in range(0, 10):
                    fdsutun2 = fdsutun2 - 2
                    fdsutun3 = fdsutun3 - 4
                    fdsutun4 = fdsutun4 - 6
                if fdsutun3 not in range(0, 10):
                    fdsutun3 = fdsutun3 - 3
                    fdsutun4 = fdsutun4 - 5
                if fdsutun4 not in range(0, 10):
                    fdsutun4 = fdsutun4 - 4
                tay5 = 1

        else:
            break

    istek = 0
    fay1 = 0  # OYUN BİTİMİNİ DAHA RAHAT KONTROL EDEBİLMEK İÇİN BU DEĞİŞKENLERİ KULLANAĞIM
    fay2 = 0
    fay3 = 0
    fay4 = 0
    fay5 = 0
    fay6 = 0
    fay7 = 0
    ray1 = 0  # KARAVANA ATIŞINI KONTROL EDEBİLMEK İÇİN BU DEĞİŞKENLERİ KULLANAĞIM
    ray2 = 0
    ray3 = 0
    ray4 = 0
    ray5 = 0
    ray6 = 0
    sayac1 = 0  # hakkın bitip bitmediğini kontrol edebilmek için
    consaoltem = 0
    tekraryazma1 = 0  # gemiyi batırdıktan sonraki atışlarda önceki yıktığım gemiyide batırdınız yazıyordu bunu engellemek için
    tekraryazma2 = 0  # oluşturdum bu değişkenleri
    tekraryazma3 = 0
    tekraryazma4 = 0
    tekraryazma5 = 0
    tekraryazma6 = 0
    tekraryazma7 = 0
    hesaplama = 0

    tercih = int(input("GİZLİ MODA GİRMEK İÇİN 1'E BASINIZ"
                       "\nAÇIK MODA GİRMEK İÇİN  2'YE BASINIZ"))
    satah = 0  # satir athmin değişkeni
    sutah = 0  # sutun tahmin değişkeni
    if tercih == 1:
        for i in range(0, 33):
            print("10'a 10'luk tabloda")
            satah = int(input("satir tahmininizi giriniz"))
            sutah = int(input("sutun tahmininizi giriniz"))
            if (liste[satah - 1][sutah - 1] == "x") or (liste[satah - 1][sutah - 1] == "*"):
                """BURADA ÖNCEDEN VURDUĞU YERİ VURDUMU KONTROLU YAPTIM"""
                print("ÖNCEDEN BURAYA ATIŞ YAPTINIZ BAŞKA BİR YER SEÇİNİZ")
                continue
            for a in range(0, 10):
                for b in range(0, 10):
                    if (liste[a][b] != "x") and (liste[a][b] != "*"):
                        liste[a][
                            b] = "?"  # BURADA DA TABLODA GERİ KALAN KISIMLARI YANİ KARAVANA VE VURULMUŞLAR HARİÇ YERLER "?" HALİNDE GÖRÜNÜR
            if tekraryazma1 == 0:
                if ((satah - 1) == satirsayisi) and ((sutah - 1) == sutunsayisi):
                    # TAHMİN İLE BİR BİR BİRİMLİK GEMİ KARŞILAŞTIRMASI
                    print("TEBRİKLER KÜÇÜK ÇAPLI YIKIM BİRLİK GEMİYİ BATIRDINIZ")
                    liste[satirsayisi][sutunsayisi] = "x"
                    fay1 = 1
                    tekraryazma1 = 1

            if yon1 == "dikey":
                if ((dsatir1 == (satah - 1)) and ((sutah - 1) == sabitsutun)) or (
                        (dsatir2 == (satah - 1)) and ((sutah - 1) == sabitsutun)):
                    print("BOOMM ORTA ÇAPLI YIKIM"
                          " BİR GEMİYİ VURDUNUZ")  # TAHMİN İLE DİK İKİ BİRİMLİK KARŞILAŞTIRMASI
                    liste[satah - 1][satah - 1] = "x"
                    ray1 = 1
            if yon1 == "yatay":
                if (((satah - 1) == ssatir) and ((sutah - 1) == dsutun1)) or (
                        ((satah - 1) == ssatir) and ((sutah - 1) == dsutun2)):
                    print("BOOM ORTA ÇAPLI YIKIM"
                          "BİR GEMİ VURDUNUZ")  # TAHMİN İLE YATAY İKİ BİRİMLİK GEMİ KAŞILAŞTIRMASI
                    liste[satah - 1][sutah - 1] = "x"
                    ray2 = 1
            if yon2 == "dikey":
                if (((satah - 1) == udsatir1) and ((sutah - 1) == ussutun)) \
                        or (((satah - 1) == udsatir2) and ((sutah - 1) == ussutun)) \
                        or (((satah - 1) == udsatir3) and ((sutah - 1) == ussutun)):
                    print("BÜYÜK ÇAPLI YIKIM "
                          "BİR GEMİ VURDUNUZ")  # BURADA TAHMİN İLE ÜÇ BİRİMLİK DİKEY KARŞILAŞTIRMASI YAPTIM EĞER ÜÇ BİRİMLİK DİKEYSE
                    liste[satah - 1][sutah - 1] = "x"
                    ray3 = 1
            if yon2 == "yatay":
                if (((satah - 1) == ussatir) and ((sutah - 1) == udsutun1)) \
                        or (((satah - 1) == ussatir) and ((sutah - 1) == udsutun2)) \
                        or (((satah - 1) == ussatir) and ((sutah - 1) == udsutun3)):
                    print("BÜYÜK ÇAPLI YIKIM"
                          "BİR GEMİ VURDUNUZ")  # BURADA TAHMİN İLE ÜÇ BİRİMLİK YATAY KARŞILAŞTIRMASI YAPTIM EĞER ÜÇ BİRİMLİK YATAYSA
                    liste[satah - 1][sutah - 1] = "x"
                    ray4 = 1
            if yon3 == "dikey":
                if (((satah - 1) == fdsatir1) and ((sutah - 1) == fssutun)) \
                        or (((satah - 1) == fdsatir2) and ((sutah - 1) == fssutun)) \
                        or (((satah - 1) == fdsatir3) and ((sutah - 1) == fssutun)) \
                        or (((satah - 1) == fdsatir4) and ((sutah - 1) == fssutun)):
                    print("BÜYÜK VURGUN "
                          "BİR GEMİ VURDUNUZ")  # BURADA TAHMİN İLE DÖRT BİRİMLİK DİKEY KARŞILAŞTIRMASI YAPTIM EĞER DÖRT BİRİMLİK DİKEY
                    liste[satah - 1][sutah - 1] = "x"
                    ray5 = 1
            if yon3 == "yatay":
                if (((satah - 1) == fssatir) and ((sutah - 1) == fdsutun1)) \
                        or (((satah - 1) == fssatir) and ((sutah - 1) == fdsutun2)) \
                        or (((satah - 1) == fssatir) and ((sutah - 1) == fdsutun3)) \
                        or (((satah - 1) == fssatir) and ((sutah - 1) == fdsutun4)):
                    print("BÜYÜK VURGUN"
                          "BİR GEMİ VURDUNUZ")  # BURADA TAHMİN İLE DÖRT BİRİMLİK YAYAT KARŞILAŞTIRMASI YAPTIM EĞER DÖRT BİRİMLİK YATAY
                    liste[satah - 1][sutah - 1] = "x"
                    ray6 = 1

            if (liste[satah - 1][sutah - 1] == "?") and (liste[satah - 1][sutah - 1] != "x"):
                # KARAVANA ATIŞI KONTROL EDİLİYOR
                print("MALESEF BU ATIŞINIZDA HİÇBİR YERİ VURAMADINIZ")
                liste[satah - 1][sutah - 1] = "*"
            if yon1 == "dikey":
                # BURADA İSE HİÇBİR GEMİ BATTIMI KONTROLU YAPTIM
                if tekraryazma2 == 0:
                    if (liste[dsatir1][sabitsutun] == "x") and (liste[dsatir2][sabitsutun] == "x"):
                        print("TEBRİKLER DÜŞMANIN İKİ BİRİMLİK GEMİSİNİ BATIRDINIZ")
                        fay2 = 1
                        tekraryazma2 = 1

            if yon1 == "yatay":
                if tekraryazma3 == 0:
                    if (liste[ssatir][dsutun1] == "x") and (liste[ssatir][dsutun2] == "x"):
                        print("TEBRİKLER DÜŞMANIN İKİ BİRİMLİK GEMİSİNİ BATIRDINIZ")
                    fsay3 = 1
                    tekraryazma3 = 1

            if yon2 == "dikey":
                if tekraryazma4 == 0:
                    if (liste[udsatir1][ussutun] == "x") and (liste[udsatir2][ussutun] == "x") and (
                            liste[udsatir3][ussutun] == "x"):
                        print("TEBRİKLER DÜŞMANIN ÜÇ BİRİMLİK GEMİSİNİ BATIRDINIZ")
                        fay4 = 1
                        tekraryazma4 = 1

            if yon2 == "yatay":
                if tekraryazma5 == 0:
                    if (liste[ussatir][udsutun1] == "x") and (liste[ussatir][udsutun2] == "x") and (
                            liste[ussatir][udsutun3] == "x"):
                        print("TEBRİKLER DÜŞMANIN ÜÇ BİRİMLİK GEMİSİNİ BATIRDINIZ")
                        fay5 = 1
                        tekraryazma5 = 1

            if yon3 == "dikey":
                if tekraryazma6 == 0:
                    if (liste[fdsatir1][fssutun] == "x") and (liste[fdsatir2][fssutun] == "x") \
                            and (liste[fdsatir3][fssutun] == "x") and (liste[fdsatir4][fssutun] == "x"):
                        print("TEBRİKLER BÜYÜK VURGUN BAŞARILI OLDU "
                              "DÜŞMANIN EN BÜYÜK SILAHI OLAN AMİRALİ VURDUNUZ")
                        fay6 = 1
                        tekraryazma6 = 1

            if yon3 == "yatay":
                if tekraryazma7 == 0:
                    if (liste[fssatir][fdsutun1] == "x") and (liste[fssatir][fdsutun2] == "x") \
                            and (liste[fssatir][fdsutun3] == "x") and (liste[fssatir][fdsutun4] == "x"):
                        print("TEBRİKLER BÜYÜK VURGUN BAŞARILI OLDU "
                              "\nDÜŞMANIN EN BÜYÜK SILAHI OLAN AMİRALİ VURDUNUZ")
                    fay7 = 1
                    tekraryazma7 = 1

            istek = int(input("şuan tabloyu görmek isterseniz 1'e basınız"))
            if istek == 1:
                for i in range(0, 10):
                    print(liste[i])
            sayac1 = sayac1 + 1
            if sayac1 == 33:
                print("CEPHANENİZ BİTMİŞTİR SİZ DÜŞMANI YOK ETMEDEN O SİZİ YOK ETMİŞ OLABİLİR")
            if (fay1 == 1) and ((fay2 == 1) or (fay3 == 1)) and ((fay4 == 1) or (fay5 == 1)) and (
                    (fay6 == 1) or (fay7 == 1)):
                print("TEBRİKLER BÜTÜN GEMİLERİ VURDUNUZ")
                hesaplama = 33 - sayac1
                print("PUANINIZ:{}".format(hesaplama))
                break

    hay1 = 0
    hay2 = 0
    hay3 = 0
    hay4 = 0
    hay5 = 0
    hay6 = 0
    hay7 = 0

    tek = 0
    sayac = 0
    if tercih == 2:
        """BURADA ÖNCEDEN VURDUĞU YERİ VURDUMU KONTROLU YAPTIM"""
        for i in range(0, 33):
            # BURADA GEMİLERİN YERİ SİZ KONTROL EDEBİLİN DİYE AÇIK BİR ŞEKİLDE GÖRÜLÜR AMA VURDUĞUNUZ YERLER X İLE GÖRÜNDÜKTEN SONRA TEKRAR G OLMASIN DİYE TEK SEFER ATAMA YAPILIR VE YİNE SİZE 33 HAK TANINIR
            if tek == 0:
                if yon3 == "yatay":
                    if (tay1 == 0) and (tay2 == 0) and (tay3 == 0) and (tay4 == 0) and (
                            tay5 == 0):  # tay değişkeni işaretlenen geminin tek sefer işaretlenmesini sağlar  eğer diyer gemilerle  ile aynı yere gelmişse bir kez işaretleni
                        # gelmemişsede bir kez işaretlenir
                        liste[fssatir][fdsutun1] = "G"
                        liste[fssatir][fdsutun2] = "G"
                        liste[fssatir][fdsutun3] = "G"
                        liste[fssatir][fdsutun4] = "G"
                    if (tay1 == 1) and (tay2 == 0) and (tay3 == 0) and (tay4 == 0) and (tay5 == 0):
                        liste[fssatir][fdsutun1] = "G"
                        liste[fssatir][fdsutun2] = "G"
                        liste[fssatir][fdsutun3] = "G"
                        liste[fssatir][fdsutun4] = "G"
                    if (tay1 == 0) and (tay2 == 1) and (tay3 == 0) and (tay4 == 0) and (tay5 == 0):
                        liste[fssatir][fdsutun1] = "G"
                        liste[fssatir][fdsutun2] = "G"
                        liste[fssatir][fdsutun3] = "G"
                        liste[fssatir][fdsutun4] = "G"
                    if (tay1 == 0) and (tay2 == 0) and (tay3 == 1) and (tay4 == 0) and (tay5 == 0):
                        liste[fssatir][fdsutun1] = "G"
                        liste[fssatir][fdsutun2] = "G"
                        liste[fssatir][fdsutun3] = "G"
                        liste[fssatir][fdsutun4] = "G"
                    if (tay1 == 0) and (tay2 == 0) and (tay3 == 0) and (tay4 == 1) and (tay5 == 0):
                        liste[fssatir][fdsutun1] = "G"
                        liste[fssatir][fdsutun2] = "G"
                        liste[fssatir][fdsutun3] = "G"
                        liste[fssatir][fdsutun4] = "G"
                    if (tay1 == 0) and (tay2 == 0) and (tay3 == 0) and (tay4 == 0) and (tay5 == 1):
                        liste[fssatir][fdsutun1] = "G"
                        liste[fssatir][fdsutun2] = "G"
                        liste[fssatir][fdsutun3] = "G"
                        liste[fssatir][fdsutun4] = "G"

                # ----------------------------------------------------------------------------------------
                if yon3 == "dikey":
                    if (say1 == 0) and (say2 == 0) and (say3 == 0) and (say4 == 0) and (say5 == 0):
                        liste[fdsatir1][fssutun] = "G"
                        liste[fdsatir2][fssutun] = "G"
                        liste[fdsatir3][fssutun] = "G"
                        liste[fdsatir4][fssutun] = "G"
                    if (say1 == 1) and (say2 == 0) and (say3 == 0) and (say4 == 0) and (say5 == 0):
                        liste[fdsatir1][fssutun] = "G"
                        liste[fdsatir2][fssutun] = "G"
                        liste[fdsatir3][fssutun] = "G"
                        liste[fdsatir4][fssutun] = "G"
                    if (say1 == 0) and (say2 == 1) and (say3 == 0) and (say4 == 0) and (say5 == 0):
                        liste[fdsatir1][fssutun] = "G"
                        liste[fdsatir2][fssutun] = "G"
                        liste[fdsatir3][fssutun] = "G"
                        liste[fdsatir4][fssutun] = "G"
                    if (say1 == 0) and (say2 == 0) and (say3 == 1) and (say4 == 0) and (say5 == 0):
                        liste[fdsatir1][fssutun] = "G"
                        liste[fdsatir2][fssutun] = "G"
                        liste[fdsatir3][fssutun] = "G"
                        liste[fdsatir4][fssutun] = "G"
                    if (say1 == 0) and (say2 == 0) and (say3 == 0) and (say4 == 1) and (say5 == 0):
                        liste[fdsatir1][fssutun] = "G"
                        liste[fdsatir2][fssutun] = "G"
                        liste[fdsatir3][fssutun] = "G"
                        liste[fdsatir4][fssutun] = "G"
                    if (say1 == 0) and (say2 == 0) and (say3 == 0) and (say4 == 0) and (say5 == 1):
                        liste[fdsatir1][fssutun] = "G"
                        liste[fdsatir2][fssutun] = "G"
                        liste[fdsatir3][fssutun] = "G"
                        liste[fdsatir4][fssutun] = "G"

                # --------------------------------------------------------------------------------------------------
                if yon2 == "yatay":
                    if (yay1 == 0) and (yay2 == 0) and (yay3 == 0):
                        liste[ussatir][udsutun1] = "G"
                        liste[ussatir][udsutun2] = "G"
                        liste[ussatir][udsutun3] = "G"
                    if (yay1 == 1) and (yay2 == 0) and (yay3 == 0):
                        liste[ussatir][udsutun1] = "G"
                        liste[ussatir][udsutun2] = "G"
                        liste[ussatir][udsutun3] = "G"
                    if (yay1 == 0) and (yay2 == 1) and (yay3 == 0):
                        liste[ussatir][udsutun1] = "G"
                        liste[ussatir][udsutun2] = "G"
                        liste[ussatir][udsutun3] = "G"
                    if (yay1 == 0) and (yay2 == 0) and (yay3 == 1):
                        liste[ussatir][udsutun1] = "G"
                        liste[ussatir][udsutun2] = "G"
                        liste[ussatir][udsutun3] = "G"

                # --------------------------------------------------------------------------------------------------------
                if yon2 == "dikey":
                    if (day1 == 0) and (day2 == 0) and (day3 == 0):
                        liste[udsatir1][ussutun] = "G"
                        liste[udsatir2][ussutun] = "G"
                        liste[udsatir3][ussutun] = "G"
                    if (day1 == 1) and (day2 == 0) and (day3 == 0):
                        liste[udsatir1][ussutun] = "G"
                        liste[udsatir2][ussutun] = "G"
                        liste[udsatir3][ussutun] = "G"
                    if (day1 == 0) and (day2 == 1) and (day3 == 0):
                        liste[udsatir1][ussutun] = "G"
                        liste[udsatir2][ussutun] = "G"
                        liste[udsatir3][ussutun] = "G"
                    if (day1 == 0) and (day2 == 0) and (day3 == 1):
                        liste[udsatir1][ussutun] = "G"
                        liste[udsatir2][ussutun] = "G"
                        liste[udsatir3][ussutun] = "G"

                # ----------------------------------------------------------------------------------------------------
                if yon1 == "yatay":
                    if sat2 == 0:
                        liste[ssatir][dsutun1] = "G"
                        liste[ssatir][dsutun2] = "G"
                    if sat2 == 1:
                        liste[ssatir][dsutun1] = "G"
                        liste[ssatir][dsutun2] = "G"

                # ------------------------------------------------------------------------------------------------------
                if yon1 == "dikey":
                    if sat1 == 0:
                        liste[dsatir1][sabitsutun] = "G"
                        liste[dsatir2][sabitsutun] = "G"

                    if sat1 == 1:
                        liste[dsatir1][sabitsutun] = "G"
                        liste[dsatir2][sabitsutun] = "G"

                # --------------------------------------------------------------------------------------------------
                liste[satirsayisi][sutunsayisi] = "G"
                tek = 1

            for s in range(0, 10):
                for p in range(0, 10):
                    if (liste[s][p] != "G") and (liste[s][p] != "x") and (liste[s][p] != "*"):
                        liste[s][p] = "?"
            if tek == 1:
                for i in range(0, 10):
                    print(liste[i])  # TABLOYU YAZDIRDIM
            tek = 2

            print("10'a 10'luk tabloda")
            satah = int(input("satir tahmininizi giriniz"))
            sutah = int(input("sutun tahmininizi giriniz"))
            if (liste[satah - 1][sutah - 1] == "x") or (liste[satah - 1][sutah - 1] == "*"):
                print("ÖNCEDEN BURAYA ATIŞ YAPTINIZ BAŞKA BİR YER SEÇİNİZ")
                continue
            if ((satah - 1) == satirsayisi) and ((sutah - 1) == sutunsayisi):
                # TAHMİN İLE BİR BİR BİRİMLİK GEMİ KARŞILAŞTIRMASI
                print("TEBRİKLER KÜÇÜK ÇAPLI YIKIM BİRLİK GEMİYİ BATIRDINIZ")
                liste[satirsayisi][sutunsayisi] = "x"
                hay1 = 1
            if yon1 == "dikey":
                if ((dsatir1 == (satah - 1)) and ((sutah - 1) == sabitsutun)) or (
                        (dsatir2 == (satah - 1)) and ((sutah - 1) == sabitsutun)):
                    print("BOOMM ORTA ÇAPLI YIKIM"
                          " \nBİR GEMİYİ VURDUNUZ")  # TAHMİN İLE DİK İKİ BİRİMLİK KARŞILAŞTIRMASI
                    liste[satah - 1][sutah - 1] = "x"
            if yon1 == "yatay":
                if (((satah - 1) == ssatir) and ((sutah - 1) == dsutun1)) or (
                        ((satah - 1) == ssatir) and ((sutah - 1) == dsutun2)):
                    print("BOOM ORTA ÇAPLI YIKIM"
                          "BİR GEMİ VURDUNUZ")  # TAHMİN İLE YATAY İKİ BİRİMLİK GEMİ KAŞILAŞTIRMASI
                    liste[satah - 1][sutah - 1] = "x"
            if yon2 == "dikey":
                if (((satah - 1) == udsatir1) and ((sutah - 1) == ussutun)) \
                        or (((satah - 1) == udsatir2) and ((sutah - 1) == ussutun)) \
                        or (((satah - 1) == udsatir3) and ((sutah - 1) == ussutun)):
                    print("BÜYÜK ÇAPLI YIKIM "
                          "BİR GEMİ VURDUNUZ")  # BURADA TAHMİN İLE ÜÇ BİRİMLİK DİKEY KARŞILAŞTIRMASI YAPTIM EĞER ÜÇ BİRİMLİK DİKEYSE
                    liste[satah - 1][sutah - 1] = "x"
            if yon2 == "yatay":
                if (((satah - 1) == ussatir) and ((sutah - 1) == udsutun1)) \
                        or (((satah - 1) == ussatir) and ((sutah - 1) == udsutun2)) \
                        or (((satah - 1) == ussatir) and ((sutah - 1) == udsutun3)):
                    print("BÜYÜK ÇAPLI YIKIM"
                          "BİR GEMİ VURDUNUZ")  # BURADA TAHMİN İLE ÜÇ BİRİMLİK YATAY KARŞILAŞTIRMASI YAPTIM EĞER ÜÇ BİRİMLİK YATAYSA
                    liste[satah - 1][sutah - 1] = "x"
            if yon3 == "dikey":
                if (((satah - 1) == fdsatir1) and ((sutah - 1) == fssutun)) \
                        or (((satah - 1) == fdsatir2) and ((sutah - 1) == fssutun)) \
                        or (((satah - 1) == fdsatir3) and ((sutah - 1) == fssutun)) \
                        or (((satah - 1) == fdsatir4) and ((sutah - 1) == fssutun)):
                    print("BÜYÜK VURGUN "
                          "BİR GEMİ VURDUNUZ")  # BURADA TAHMİN İLE DÖRT BİRİMLİK DİKEY KARŞILAŞTIRMASI YAPTIM EĞER DÖRT BİRİMLİK DİKEY
                    liste[satah - 1][sutah - 1] = "x"
            if yon3 == "yatay":
                if (((satah - 1) == fssatir) and ((sutah - 1) == fdsutun1)) \
                        or (((satah - 1) == fssatir) and ((sutah - 1) == fdsutun2)) \
                        or (((satah - 1) == fssatir) and ((sutah - 1) == fdsutun3)) \
                        or (((satah - 1) == fssatir) and ((sutah - 1) == fdsutun4)):
                    print("BÜYÜK VURGUN"
                          "BİR GEMİ VURDUNUZ")  # BURADA TAHMİN İLE DÖRT BİRİMLİK YAYAT KARŞILAŞTIRMASI YAPTIM EĞER DÖRT BİRİMLİK YATAY
                    liste[satah - 1][sutah - 1] = "x"

            if liste[satah - 1][sutah - 1] != "x":
                print("MALESEF BU ATIŞINIZDA HİÇBİR GEMİYİ VURAMADINIZ")
                liste[satah - 1][sutah - 1] = "*"
            # BURADA İSE HİÇBİR GEMİ BATTIMI KONTROLU YAPTIM
            if yon1 == "dikey":
                if hay2 == 0:
                    if (liste[dsatir1][sabitsutun] == "x") and (liste[dsatir2][sabitsutun] == "x"):
                        print("TEBRİKLER DÜŞMANIN İKİ BİRİMLİK GEMİSİNİ BATIRDINIZ")
                        hay2 = 1

            if yon1 == "yatay":
                if hay3 == 0:
                    if (liste[ssatir][dsutun1] == "x") and (liste[ssatir][dsutun2] == "x"):
                        print("TEBRİKLER DÜŞMANIN İKİ BİRİMLİK GEMİSİNİ BATIRDINIZ")
                        hay3 = 1

            if yon2 == "dikey":
                if hay4 == 0:
                    if (liste[udsatir1][ussutun] == "x") and (liste[udsatir2][ussutun] == "x") and (
                            liste[udsatir3][ussutun] == "x"):
                        print("TEBRİKLER DÜŞMANIN ÜÇ BİRİMLİK GEMİSİNİ BATIRDINIZ")
                        hay4 = 1

            if yon2 == "yatay":
                if hay5 == 0:
                    if (liste[ussatir][udsutun1] == "x") and (liste[ussatir][udsutun2] == "x") and (
                            liste[ussatir][udsutun3] == "x"):
                        print("TEBRİKLER DÜŞMANIN ÜÇ BİRİMLİK GEMİSİNİ BATIRDINIZ")
                        hay5 = 1

            if yon3 == "dikey":
                if hay6 == 0:
                    if (liste[fdsatir1][fssutun] == "x") and (liste[fdsatir2][fssutun] == "x") \
                            and (liste[fdsatir3][fssutun] == "x") and (liste[fdsatir3][fssutun] == "x"):
                        print("TEBRİKLER BÜYÜK VURGUN BAŞARILI OLDU "
                              "DÜŞMANIN EN BÜYÜK SILAHI OLAN AMİRALİ VURDUNUZ")
                        hay6 = 1

            if yon3 == "yatay":
                if hay7 == 0:
                    if (liste[fssatir][fdsutun1] == "x") and (liste[fssatir][fdsutun2] == "x") \
                            and (liste[fssatir][fdsutun3] == "x") and (liste[fssatir][fdsutun4] == "x"):
                        print("TEBRİKLER BÜYÜK VURGUN BAŞARILI OLDU "
                              "DÜŞMANIN EN BÜYÜK SILAHI OLAN AMİRALİ VURDUNUZ")
                        hay7 = 1
            sayac = sayac + 1
            if sayac == 33:
                print("MERMİNİZ BİTMİŞTİR SİZ DÜŞMANI YOK ETMEDEN O SİZİ YOK ETMİŞ OLABİLİR")
            if (hay1 == 1) and ((hay2 == 1) or (hay3 == 1)) and ((hay4 == 1) or (hay5 == 1)) and (
                    (hay6 == 1) or (hay7 == 1)):
                print("TEBRİKLER BÜTÜN GEMİLERİ VURDUNUZ VE DÜŞMANI YOK ETTİNİZ")
                hesaplama = 33 - sayac
                print("PUANINIZ:{}".format(hesaplama))
                break

            istek = int(
                input("ŞUAN TABLOYU GÖRMEK İSTERSENİZ 1'e BASINIZ -DEVAM ETMEK İÇİN BAŞKA HERHANGİ BİR SAYIYA BASINIZ"))
            if istek == 1:
                for i in range(0, 10):
                    print(liste[i])

                # KOMSOL TEMİZLEME KALDI

            print("------------------------------------------------------------------------------------------")
    kackere=int(input("OYUNU BİTİMEK  İSTİYORSANIZ 0'A BASINIZ"))