from bs4 import BeautifulSoup
import requests
import time
import csv
import sys

z = 0

before = "//"
while(True):
    url = input(">>urlを入力 : 前回:" + before + "\n")  #

    if url == "end":                                  #
        print("\n>>end the program")                  #
        time.sleep(3)                                 #
        sys.exit()                                    #

    time.sleep(3)
    try:
        response = requests.get(url)  # url[z]
        alz = BeautifulSoup(response.text, "html.parser")
    except BaseException:
        print("\n>>no url or error")
#        z += 1
        continue
    else:
        pass

    while(True):
        header = alz.select(
            "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
        print("\n>>" + header[0].contents[0])

        which = input('''
#1:航空スロット無し
#2:装備五スロ航空スロット無し
#3:航空2スロ
#4:航空3スロ
#5:航空4スロ
#6:航空5スロ\n''')
#        which = "1"
        try:
            if which == "1":
                header = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                classname = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(3)")
                name = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                hp = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(1)")
                armor = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(1)")
                evasion = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(1)")
                aircraft = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(1)")
                speed = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(1)")
                firerange = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(1)")
                fuel = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(1)")
                firepower = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(2)")
                torpedo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(2)")
                aa = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(2)")
                asw = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(2)")
                los = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(2)")
                luck = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(2)")
                ammo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(2)")
                equip1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td")
                equip2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td")
                equip3 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td")
                equip4 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td")

                print(header[0].contents[0])
                print(classname[0].contents[0])
                print(name[0].contents[0])
                print(hp[0].contents[0])
                print(armor[0].contents[0])
                print(evasion[0].contents[0])
                print(aircraft[0].contents[0])
                print(speed[0].contents[0])
                print(firerange[0].contents[0])
                print(fuel[0].contents[0])
                print(firepower[0].contents[0])
                print(torpedo[0].contents[0])
                print(aa[0].contents[0])
                print(asw[0].contents[0])
                print(los[0].contents[0])
                print(luck[0].contents[0])
                print(ammo[0].contents[0])

                equip1a = str(equip1)
                equip2a = str(equip2)
                equip3a = str(equip3)
                equip4a = str(equip4)

                if "href" in equip1a:
                    equip1 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td > a")
                    print(equip1[0].contents[0])
                else:
                    print(equip1[0].contents[0])
                if "href" in equip2a:
                    equip2 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td > a")
                    print(equip2[0].contents[0])
                else:
                    print(equip2[0].contents[0])
                if "href" in equip3a:
                    equip3 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td > a")
                    print(equip3[0].contents[0])
                else:
                    print(equip3[0].contents[0])
                if "href" in equip4a:
                    equip4 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td > a")
                    print(equip4[0].contents[0])
                else:
                    print(equip4[0].contents[0])

                data = [
                    header[0].contents[0],
                    classname[0].contents[0],
                    name[0].contents[0],
                    hp[0].contents[0],
                    armor[0].contents[0],
                    evasion[0].contents[0],
                    aircraft[0].contents[0],
                    speed[0].contents[0],
                    firerange[0].contents[0],
                    fuel[0].contents[0],
                    firepower[0].contents[0],
                    torpedo[0].contents[0],
                    aa[0].contents[0],
                    asw[0].contents[0],
                    los[0].contents[0],
                    luck[0].contents[0],
                    ammo[0].contents[0],
                    equip1[0].contents[0],
                    equip2[0].contents[0],
                    equip3[0].contents[0],
                    equip4[0].contents[0]]

            elif which == "2":
                header = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                classname = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(3)")
                name = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                hp = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(1)")
                armor = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(1)")
                evasion = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(1)")
                aircraft = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(1)")
                speed = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(1)")
                firerange = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(1)")
                fuel = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(1)")
                firepower = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(2)")
                torpedo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(2)")
                aa = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(2)")
                asw = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(2)")
                los = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(2)")
                luck = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(2)")
                ammo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(2)")
                equip1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td")
                equip2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td")
                equip3 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td")
                equip4 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td")
                equip5 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(17) > td")

                print(header[0].contents[0])
                print(classname[0].contents[0])
                print(name[0].contents[0])
                print(hp[0].contents[0])
                print(armor[0].contents[0])
                print(evasion[0].contents[0])
                print(aircraft[0].contents[0])
                print(speed[0].contents[0])
                print(firerange[0].contents[0])
                print(fuel[0].contents[0])
                print(firepower[0].contents[0])
                print(torpedo[0].contents[0])
                print(aa[0].contents[0])
                print(asw[0].contents[0])
                print(los[0].contents[0])
                print(luck[0].contents[0])
                print(ammo[0].contents[0])

                equip1a = str(equip1)
                equip2a = str(equip2)
                equip3a = str(equip3)
                equip4a = str(equip4)
                equip5a = str(equip5)

                if "href" in equip1a:
                    equip1 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td > a")
                    print(equip1[0].contents[0])
                else:
                    print(equip1[0].contents[0])
                if "href" in equip2a:
                    equip2 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td > a")
                    print(equip2[0].contents[0])
                else:
                    print(equip2[0].contents[0])
                if "href" in equip3a:
                    equip3 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td > a")
                    print(equip3[0].contents[0])
                else:
                    print(equip3[0].contents[0])
                if "href" in equip4a:
                    equip4 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td > a")
                    print(equip4[0].contents[0])
                else:
                    print(equip4[0].contents[0])
                if "href" in equip5a:
                    equip5 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(17) > td > a")
                    print(equip5[0].contents[0])
                else:
                    print(equip5[0].contents[0])

                data = [
                    header[0].contents[0],
                    classname[0].contents[0],
                    name[0].contents[0],
                    hp[0].contents[0],
                    armor[0].contents[0],
                    evasion[0].contents[0],
                    aircraft[0].contents[0],
                    speed[0].contents[0],
                    firerange[0].contents[0],
                    fuel[0].contents[0],
                    firepower[0].contents[0],
                    torpedo[0].contents[0],
                    aa[0].contents[0],
                    asw[0].contents[0],
                    los[0].contents[0],
                    luck[0].contents[0],
                    ammo[0].contents[0],
                    equip1[0].contents[0],
                    equip2[0].contents[0],
                    equip3[0].contents[0],
                    equip4[0].contents[0],
                    equip5[0].contents[0]]

            elif which == "3":
                header = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                classname = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(3)")
                name = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                hp = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(1)")
                armor = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(1)")
                evasion = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(1)")
                aircraft = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(1)")
                speed = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(1)")
                firerange = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(1)")
                fuel = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(1)")
                firepower = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(2)")
                torpedo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(2)")
                aa = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(2)")
                asw = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(2)")
                los = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(2)")
                luck = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(2)")
                ammo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(2)")
                slot1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td:nth-of-type(1)")
                slot2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td:nth-of-type(1)")
                equip1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td:nth-of-type(2)")
                equip2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td:nth-of-type(2)")
                equip3 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td")
                equip4 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td")

                print(header[0].contents[0])
                print(classname[0].contents[0])
                print(name[0].contents[0])
                print(hp[0].contents[0])
                print(armor[0].contents[0])
                print(evasion[0].contents[0])
                print(aircraft[0].contents[0])
                print(speed[0].contents[0])
                print(firerange[0].contents[0])
                print(fuel[0].contents[0])
                print(firepower[0].contents[0])
                print(torpedo[0].contents[0])
                print(aa[0].contents[0])
                print(asw[0].contents[0])
                print(los[0].contents[0])
                print(luck[0].contents[0])
                print(ammo[0].contents[0])
                print(slot1[0].contents[0])
                print(slot2[0].contents[0])

                equip1a = str(equip1)
                equip2a = str(equip2)
                equip3a = str(equip3)
                equip4a = str(equip4)

                if "href" in equip1a:
                    equip1 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td > a")
                    print(equip1[0].contents[0])
                else:
                    print(equip1[0].contents[0])
                if "href" in equip2a:
                    equip2 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td > a")
                    print(equip2[0].contents[0])
                else:
                    print(equip2[0].contents[0])
                if "href" in equip3a:
                    equip3 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td > a")
                    print(equip3[0].contents[0])
                else:
                    print(equip3[0].contents[0])
                if "href" in equip4a:
                    equip4 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td > a")
                    print(equip4[0].contents[0])
                else:
                    print(equip4[0].contents[0])

                data = [
                    header[0].contents[0],
                    classname[0].contents[0],
                    name[0].contents[0],
                    hp[0].contents[0],
                    armor[0].contents[0],
                    evasion[0].contents[0],
                    aircraft[0].contents[0],
                    speed[0].contents[0],
                    firerange[0].contents[0],
                    fuel[0].contents[0],
                    firepower[0].contents[0],
                    torpedo[0].contents[0],
                    aa[0].contents[0],
                    asw[0].contents[0],
                    los[0].contents[0],
                    luck[0].contents[0],
                    ammo[0].contents[0],
                    equip1[0].contents[0],
                    equip2[0].contents[0],
                    equip3[0].contents[0],
                    equip4[0].contents[0],
                    slot1[0].contents[0],
                    slot2[0].contents[0]]

            elif which == "4":
                header = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                classname = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(3)")
                name = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                hp = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(1)")
                armor = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(1)")
                evasion = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(1)")
                aircraft = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(1)")
                speed = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(1)")
                firerange = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(1)")
                fuel = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(1)")
                firepower = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(2)")
                torpedo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(2)")
                aa = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(2)")
                asw = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(2)")
                los = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(2)")
                luck = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(2)")
                ammo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(2)")
                slot1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td:nth-of-type(1)")
                slot2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td:nth-of-type(1)")
                slot3 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td:nth-of-type(1)")
                equip1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td:nth-of-type(2)")
                equip2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td:nth-of-type(2)")
                equip3 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td:nth-of-type(2)")
                equip4 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td")

                print(header[0].contents[0])
                print(classname[0].contents[0])
                print(name[0].contents[0])
                print(hp[0].contents[0])
                print(armor[0].contents[0])
                print(evasion[0].contents[0])
                print(aircraft[0].contents[0])
                print(speed[0].contents[0])
                print(firerange[0].contents[0])
                print(fuel[0].contents[0])
                print(firepower[0].contents[0])
                print(torpedo[0].contents[0])
                print(aa[0].contents[0])
                print(asw[0].contents[0])
                print(los[0].contents[0])
                print(luck[0].contents[0])
                print(ammo[0].contents[0])
                print(slot1[0].contents[0])
                print(slot2[0].contents[0])
                print(slot3[0].contents[0])

                equip1a = str(equip1)
                equip2a = str(equip2)
                equip3a = str(equip3)
                equip4a = str(equip4)

                if "href" in equip1a:
                    equip1 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td > a")
                    print(equip1[0].contents[0])
                else:
                    print(equip1[0].contents[0])
                if "href" in equip2a:
                    equip2 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td > a")
                    print(equip2[0].contents[0])
                else:
                    print(equip2[0].contents[0])
                if "href" in equip3a:
                    equip3 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td > a")
                    print(equip3[0].contents[0])
                else:
                    print(equip3[0].contents[0])
                if "href" in equip4a:
                    equip4 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td > a")
                    print(equip4[0].contents[0])
                else:
                    print(equip4[0].contents[0])

                data = [
                    header[0].contents[0],
                    classname[0].contents[0],
                    name[0].contents[0],
                    hp[0].contents[0],
                    armor[0].contents[0],
                    evasion[0].contents[0],
                    aircraft[0].contents[0],
                    speed[0].contents[0],
                    firerange[0].contents[0],
                    fuel[0].contents[0],
                    firepower[0].contents[0],
                    torpedo[0].contents[0],
                    aa[0].contents[0],
                    asw[0].contents[0],
                    los[0].contents[0],
                    luck[0].contents[0],
                    ammo[0].contents[0],
                    equip1[0].contents[0],
                    equip2[0].contents[0],
                    equip3[0].contents[0],
                    equip4[0].contents[0],
                    slot1[0].contents[0],
                    slot2[0].contents[0],
                    slot3[0].contents[0]]

            elif which == "5":
                header = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                classname = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(3)")
                name = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                hp = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(1)")
                armor = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(1)")
                evasion = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(1)")
                aircraft = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(1)")
                speed = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(1)")
                firerange = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(1)")
                fuel = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(1)")
                firepower = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(2)")
                torpedo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(2)")
                aa = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(2)")
                asw = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(2)")
                los = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(2)")
                luck = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(2)")
                ammo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(2)")
                slot1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td:nth-of-type(1)")
                slot2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td:nth-of-type(1)")
                slot3 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td:nth-of-type(1)")
                slot4 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td:nth-of-type(1)")
                equip1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td:nth-of-type(2)")
                equip2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td:nth-of-type(2)")
                equip3 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td:nth-of-type(2)")
                equip4 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td:nth-of-type(2)")

                print(header[0].contents[0])
                print(classname[0].contents[0])
                print(name[0].contents[0])
                print(hp[0].contents[0])
                print(armor[0].contents[0])
                print(evasion[0].contents[0])
                print(aircraft[0].contents[0])
                print(speed[0].contents[0])
                print(firerange[0].contents[0])
                print(fuel[0].contents[0])
                print(firepower[0].contents[0])
                print(torpedo[0].contents[0])
                print(aa[0].contents[0])
                print(asw[0].contents[0])
                print(los[0].contents[0])
                print(luck[0].contents[0])
                print(ammo[0].contents[0])
                print(slot1[0].contents[0])
                print(slot2[0].contents[0])
                print(slot3[0].contents[0])
                print(slot4[0].contents[0])

                equip1a = str(equip1)
                equip2a = str(equip2)
                equip3a = str(equip3)
                equip4a = str(equip4)

                if "href" in equip1a:
                    equip1 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td > a")
                    print(equip1[0].contents[0])
                else:
                    print(equip1[0].contents[0])
                if "href" in equip2a:
                    equip2 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td > a")
                    print(equip2[0].contents[0])
                else:
                    print(equip2[0].contents[0])
                if "href" in equip3a:
                    equip3 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td > a")
                    print(equip3[0].contents[0])
                else:
                    print(equip3[0].contents[0])
                if "href" in equip4a:
                    equip4 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td > a")
                    print(equip4[0].contents[0])
                else:
                    print(equip4[0].contents[0])

                data = [
                    header[0].contents[0],
                    classname[0].contents[0],
                    name[0].contents[0],
                    hp[0].contents[0],
                    armor[0].contents[0],
                    evasion[0].contents[0],
                    aircraft[0].contents[0],
                    speed[0].contents[0],
                    firerange[0].contents[0],
                    fuel[0].contents[0],
                    firepower[0].contents[0],
                    torpedo[0].contents[0],
                    aa[0].contents[0],
                    asw[0].contents[0],
                    los[0].contents[0],
                    luck[0].contents[0],
                    ammo[0].contents[0],
                    equip1[0].contents[0],
                    equip2[0].contents[0],
                    equip3[0].contents[0],
                    equip4[0].contents[0],
                    slot1[0].contents[0],
                    slot2[0].contents[0],
                    slot3[0].contents[0],
                    slot4[0].contents[0]]

            elif which == "6":
                header = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                classname = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(3)")
                name = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(2) > td:nth-of-type(2)")
                hp = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(1)")
                armor = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(1)")
                evasion = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(1)")
                aircraft = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(1)")
                speed = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(1)")
                firerange = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(1)")
                fuel = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(1)")
                firepower = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(4) > td:nth-of-type(2)")
                torpedo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(5) > td:nth-of-type(2)")
                aa = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(6) > td:nth-of-type(2)")
                asw = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(7) > td:nth-of-type(2)")
                los = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(8) > td:nth-of-type(2)")
                luck = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(9) > td:nth-of-type(2)")
                ammo = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(11) > td:nth-of-type(2)")
                slot1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td:nth-of-type(1)")
                slot2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td:nth-of-type(1)")
                slot3 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td:nth-of-type(1)")
                slot4 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td:nth-of-type(1)")
                slot5 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(17) > td:nth-of-type(1)")
                equip1 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td:nth-of-type(2)")
                equip2 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td:nth-of-type(2)")
                equip3 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td:nth-of-type(2)")
                equip4 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td:nth-of-type(2)")
                equip5 = alz.select(
                    "#content > div.h-scrollable > table > tbody > tr:nth-of-type(17) > td:nth-of-type(2)")

                print(header[0].contents[0])
                print(classname[0].contents[0])
                print(name[0].contents[0])
                print(hp[0].contents[0])
                print(armor[0].contents[0])
                print(evasion[0].contents[0])
                print(aircraft[0].contents[0])
                print(speed[0].contents[0])
                print(firerange[0].contents[0])
                print(fuel[0].contents[0])
                print(firepower[0].contents[0])
                print(torpedo[0].contents[0])
                print(aa[0].contents[0])
                print(asw[0].contents[0])
                print(los[0].contents[0])
                print(luck[0].contents[0])
                print(ammo[0].contents[0])
                print(slot1[0].contents[0])
                print(slot2[0].contents[0])
                print(slot3[0].contents[0])
                print(slot4[0].contents[0])
                print(slot5[0].contents[0])

                equip1a = str(equip1)
                equip2a = str(equip2)
                equip3a = str(equip3)
                equip4a = str(equip4)
                equip5a = str(equip5)

                if "href" in equip1a:
                    equip1 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(13) > td > a")
                    print(equip1[0].contents[0])
                else:
                    print(equip1[0].contents[0])
                if "href" in equip2a:
                    equip2 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(14) > td > a")
                    print(equip2[0].contents[0])
                else:
                    print(equip2[0].contents[0])
                if "href" in equip3a:
                    equip3 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(15) > td > a")
                    print(equip3[0].contents[0])
                else:
                    print(equip3[0].contents[0])
                if "href" in equip4a:
                    equip4 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(16) > td > a")
                    print(equip4[0].contents[0])
                else:
                    print(equip4[0].contents[0])
                if "href" in equip5a:
                    equip5 = alz.select(
                        "#content > div.h-scrollable > table > tbody > tr:nth-of-type(17) > td > a")
                    print(equip5[0].contents[0])
                else:
                    print(equip5[0].contents[0])

                data = [
                    header[0].contents[0],
                    classname[0].contents[0],
                    name[0].contents[0],
                    hp[0].contents[0],
                    armor[0].contents[0],
                    evasion[0].contents[0],
                    aircraft[0].contents[0],
                    speed[0].contents[0],
                    firerange[0].contents[0],
                    fuel[0].contents[0],
                    firepower[0].contents[0],
                    torpedo[0].contents[0],
                    aa[0].contents[0],
                    asw[0].contents[0],
                    los[0].contents[0],
                    luck[0].contents[0],
                    ammo[0].contents[0],
                    equip1[0].contents[0],
                    equip2[0].contents[0],
                    equip3[0].contents[0],
                    equip4[0].contents[0],
                    equip5[0].contents[0],
                    slot1[0].contents[0],
                    slot2[0].contents[0],
                    slot3[0].contents[0],
                    slot4[0].contents[0],
                    slot5[0].contents[0]]

            elif which == "end":
                print("\n>>end")
                break

            else:
                print("\n>>not selected")
                time.sleep(3)
                continue

        except BaseException:
            print("\n>>error")
            continue

        else:
            if header[0].contents[0] == before:
                print("\n>>same kanmusu, not saved to csv")
#                z += 1
                break
            with open('lightcruiser_data.csv', 'a', newline="", encoding="utf=8") as f:
                write = csv.writer(f)
                write.writerow(data)
            break

    before = header[0].contents[0]
    with open('logfile.csv', 'a', newline="") as l:
        log = csv.writer(l)
        log.writerow(before)
#    z += 1
    time.sleep(2)
