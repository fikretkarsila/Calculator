import sys
from re import search
import PyQt5
from PyQt5.QtWidgets import QMainWindow,QApplication
from hesap_makinesi_main import Ui_MainWindow
from PyQt5.QtGui import QIcon
from math import sqrt

try:

    class hesap_makinesi(QMainWindow):
        def __init__(Self):
            super(hesap_makinesi,Self).__init__()

            Self.ui = Ui_MainWindow()
            Self.ui.setupUi(Self)

            Self.setFixedSize(379,454)
            Self.setWindowTitle("Hesap Makinesi")
            Self.setWindowIcon(QIcon("calculator.ico"))

            Self.ui.tus_negatif.clicked.connect(Self.negatif)
            Self.ui.tus_virgul.clicked.connect(Self.yazdir)

            Self.ui.tus_arti.clicked.connect(Self.yazdir)
            Self.ui.tus_eksi.clicked.connect(Self.yazdir)
            Self.ui.tus_carpi.clicked.connect(Self.yazdir)
            Self.ui.tus_bolme.clicked.connect(Self.yazdir) 

            Self.ui.tus_kok.clicked.connect(Self.koku)
            Self.ui.tus_karesi.clicked.connect(Self.karesi)
            Self.ui.tus_1_bolu_x.clicked.connect(Self.bir_bolu_x)
            Self.ui.tus_yuzde.clicked.connect(Self.yazdir)
            Self.ui.tus_ekrani_sil.clicked.connect(Self.ekrani_sil)
            Self.ui.tus_son_islem_iptal.clicked.connect(Self.son_islem_iptal)

            Self.ui.tus_tek_tek_sil.clicked.connect(Self.tek_tek_sil)

            Self.ui.tus_0.clicked.connect(Self.yazdir)
            Self.ui.tus_1.clicked.connect(Self.yazdir)
            Self.ui.tus_2.clicked.connect(Self.yazdir)
            Self.ui.tus_3.clicked.connect(Self.yazdir)
            Self.ui.tus_4.clicked.connect(Self.yazdir)
            Self.ui.tus_5.clicked.connect(Self.yazdir)
            Self.ui.tus_6.clicked.connect(Self.yazdir)
            Self.ui.tus_7.clicked.connect(Self.yazdir)
            Self.ui.tus_8.clicked.connect(Self.yazdir)
            Self.ui.tus_9.clicked.connect(Self.yazdir)

            Self.ui.tus_hesapla.clicked.connect(Self.hesapla)

            #cikis.triggered.connect(Self.cikis_yap)

            Self.ui.tus_0.setShortcut("0")
            Self.ui.tus_1.setShortcut("1")
            Self.ui.tus_2.setShortcut("2")
            Self.ui.tus_3.setShortcut("3")
            Self.ui.tus_4.setShortcut("4")
            Self.ui.tus_5.setShortcut("5")
            Self.ui.tus_6.setShortcut("6")
            Self.ui.tus_7.setShortcut("7")
            Self.ui.tus_8.setShortcut("8")
            Self.ui.tus_9.setShortcut("9")

            Self.ui.tus_arti.setShortcut("+")
            Self.ui.tus_eksi.setShortcut("-")
            Self.ui.tus_bolme.setShortcut("/")
            Self.ui.tus_carpi.setShortcut("*")
            Self.ui.tus_yuzde.setShortcut("Shift+6")
            Self.ui.tus_tek_tek_sil.setShortcut("Backspace")
            Self.ui.tus_yuzde.setShortcut("Shift+6")
            Self.ui.tus_hesapla.setShortcut("Return")
            Self.ui.tus_virgul.setShortcut(",")

        def negatif(Self):

            ekrandaki_yazi = Self.ui.ekran.text().strip()

            if ekrandaki_yazi.endswith("-"):
                ekrandaki_yazi = f"{ekrandaki_yazi[:len(ekrandaki_yazi)-1]}"
                Self.ui.ekran.setText(ekrandaki_yazi)

            elif ekrandaki_yazi.endswith("+"):
                ekrandaki_yazi = f"{ekrandaki_yazi[:len(ekrandaki_yazi)-1]}-"
                Self.ui.ekran.setText(ekrandaki_yazi)
            else:
                ekrandaki_yazi = f"{ekrandaki_yazi[:len(ekrandaki_yazi)]}-"
                Self.ui.ekran.setText(ekrandaki_yazi)

        def son_islem_iptal(Self):

            ekrandaki_yazi = Self.ui.ekran.text().strip()
                
            control = []
            for x in ekrandaki_yazi:
                if x == "x":
                    control.append(x)
                elif x == "/":
                    control.append(x)
                elif x == "+":
                    control.append(x)
                elif x == "-":
                    control.append(x)
                elif x == "%":
                    control.append(x)
                
            if len(control) == 0:
                Self.ui.ekran.setText("0")

            elif len(control) > 0:

                index = ekrandaki_yazi.index(control[0])
                Self.ui.ekran.setText(f"{ekrandaki_yazi[:index+1]}")

        def ekrani_sil(Self):
            
            Self.ui.ekran.setText("0")

        def bir_bolu_x(Self):
            try:

                ekrandaki_yazi = Self.ui.ekran.text().strip()
                Self.ui.ekran.setText(f"{1.0 / float(ekrandaki_yazi.replace(',','.'))}".replace(".",","))

            except ZeroDivisionError:
                Self.ui.ekran.setText("Sıfıra bölünemez")

            except Exception as ex:
                print(f"Hata mesajı : {ex}")

                if search("could not convert string to float",str(ex)):
                    Self.ui.ekran.setText("Geçersiz giriş")

        def tek_tek_sil(Self):

            ekrandaki_yazi = Self.ui.ekran.text().strip()

            if len(ekrandaki_yazi) == 0:
                Self.ui.ekran.setText("0")
            else:
                Self.ui.ekran.setText(ekrandaki_yazi[:len(ekrandaki_yazi)-1])

        def yazdir(Self):

            buton_bilgi = Self.ui.horizontalLayout.sender()
            objectAdi = buton_bilgi.objectName()

            ekrandaki_yazi = Self.ui.ekran.text().strip()

            if (search("[a-z]",ekrandaki_yazi) or search("[A-Z]",ekrandaki_yazi)) and not search("x",ekrandaki_yazi):
                ekrandaki_yazi = ""

            if objectAdi == "tus_0":
                ekrandaki_yazi += "0"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_1":
                ekrandaki_yazi += "1"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_2":
                ekrandaki_yazi += "2"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_3":
                ekrandaki_yazi += "3"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_4":
                ekrandaki_yazi += "4"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_5":
                ekrandaki_yazi += "5"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_6":
                ekrandaki_yazi += "6"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_7":
                ekrandaki_yazi += "7"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_8":
                ekrandaki_yazi += "8"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_9":
                ekrandaki_yazi += "9"
                Self.ui.ekran.setText(ekrandaki_yazi)

            elif objectAdi == "tus_arti":
                ekrandaki_yazi += "+"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_eksi":
                ekrandaki_yazi += "-"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_carpi":
                ekrandaki_yazi += "x"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_bolme":
                ekrandaki_yazi += "/"
                Self.ui.ekran.setText(ekrandaki_yazi)
            elif objectAdi == "tus_yuzde":
                ekrandaki_yazi += "%"
                Self.ui.ekran.setText(ekrandaki_yazi)

            elif objectAdi == "tus_virgul":
                ekrandaki_yazi += ","
                Self.ui.ekran.setText(ekrandaki_yazi)

        def hesapla(Self):
            try:
            
                ekrandaki_yazi,gecis = Self.ui.ekran.text().strip().replace(",","."),False

                for x in ekrandaki_yazi:
                    if x == "x" or x == "/" or x == "%" or x == "+" or x == "-":
                        gecis = True

                if len(ekrandaki_yazi) == 0 or ((search("[a-z]",ekrandaki_yazi) or search("[A-Z]",ekrandaki_yazi)) and not search("x",ekrandaki_yazi)):

                    Self.ui.ekran.setText("0")

                elif not gecis:
                    pass

                else:

                    try:
                        int(ekrandaki_yazi)
                        deneme = ""
                    except:
                        deneme = "Normal"

                    if deneme == "Normal":


                        if "x" in ekrandaki_yazi:

                            liste = ekrandaki_yazi.split("x")
                            sonuc =  str(float(liste[0]) * float(liste[1])).replace(".",",")
                            Self.ui.ekran.setText(sonuc)

                        elif "/" in ekrandaki_yazi:

                            liste = ekrandaki_yazi.split("/")
                            sonuc =  str(float(liste[0]) / float(liste[1])).replace(".",",")
                            Self.ui.ekran.setText(sonuc)

                        elif "+" in ekrandaki_yazi:

                            liste = ekrandaki_yazi.split("+")
                            sonuc =  str(float(liste[0]) + float(liste[1])).replace(".",",")
                            Self.ui.ekran.setText(sonuc)

                        elif "-" in ekrandaki_yazi:

                            if ekrandaki_yazi[0] == "-":
                                deger = "-"
                                sayi = 1
                            else:
                                sayi = 0
                                deger = "+"

                            liste = ekrandaki_yazi.split("-")
                            print(liste)
                            sonuc =  str(float(f"{deger}{liste[sayi + 0]}") - float(liste[sayi + 1])).replace(".",",")
                            Self.ui.ekran.setText(sonuc)

                        elif "%" in ekrandaki_yazi:

                            liste = ekrandaki_yazi.split("%")
                            sonuc =  str(float(liste[0]) % float(liste[1])).replace(".",",")
                            Self.ui.ekran.setText(sonuc)

                    elif deneme == "":
                        Self.ui.ekran.setText(ekrandaki_yazi)

            except ZeroDivisionError:
                Self.ui.ekran.setText("Sıfıra bölünemez")
            except Exception as ex:
                print(f"Hata mesajı : {ex}")

                if search("could not convert string to float",str(ex)):
                    Self.ui.ekran.setText("Geçersiz giriş")

        def karesi(Self):

            try:

                ekrandaki_yazi = Self.ui.ekran.text().strip().replace(",",".")

                Self.ui.ekran.setText(str(float(ekrandaki_yazi) ** 2).replace(".",","))

            except Exception as ex:
                print(f"Hata mesajı : {ex}")

                if str(ex) == "(34, 'Result too large')":
                    Self.ui.ekran.setText("Taşma")

                elif search("could not convert string to float",str(ex)):
                    Self.ui.ekran.setText("Geçersiz giriş")

            except:
                pass

        def koku(Self):
            try:
                ekrandaki_yazi = Self.ui.ekran.text().strip().replace(",",".")

                if search("-",ekrandaki_yazi):
                    sayi = str(sqrt(float(ekrandaki_yazi.replace("-",""))))
                    sayi = sayi.split(".")

                    if sayi[1] == "0":
                        Self.ui.ekran.setText(f"{sqrt(float(ekrandaki_yazi.replace('-','')))}".replace(".", ","))
                    else:
                        Self.ui.ekran.setText("Geçersiz giriş")
                else:
                    Self.ui.ekran.setText(f"{sqrt(float(ekrandaki_yazi))}".replace(".", ","))

            except Exception as ex:
                print(f"Hata mesajı : {ex}")

                if search("could not convert string to float",str(ex)):
                    Self.ui.ekran.setText("Geçersiz giriş")

            except:
                pass

    def Application():
        application = QApplication(sys.argv)
        window = hesap_makinesi()
        window.show()
        sys.exit(application.exec_())
        
    Application()

except Exception as ex:
    print(ex)
except:
    pass