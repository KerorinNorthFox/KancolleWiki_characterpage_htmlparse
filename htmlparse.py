from bs4 import BeautifulSoup
import requests, time, csv

while(True):
  url = input("enter the url")
  
  response = requests.get(url)
  alz = BeautifulSoup(response.text, "htmlparser")
  
  which = input('''
1:Destroyer
2:LightCruiser
3:HeavyCruiser
4:Battleship
5:AircraftCarrier
6:Submarine
7:Escort
8:Special
''')
  
  if which == "Destroyer":
    header = alz.select("")
    classname = alz.select("")
    name = alz.select("")
    hp = alz.select("")
    armor = alz.select("")
    evasion = alz.select("")
    aircraft = alz.select("")
    speed = alz.select("")
    firerange = alz.select("")
    fuel = alz.select("")
    firepower = alz.select("")
    torpedo = alz.select("")
    aa = alz.select("")
    asw = alz.select("")
    los = alz.select("")
    luck = alz.select("")
    ammo = alz.select("")
    equip1 = alz.select("")
    equip2 = alz.select("")
    equip3 = alz.select("")
    equip4 = alz.select("")
    equip5 = alz.select("")
    
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
