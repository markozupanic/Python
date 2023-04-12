#2. Napišite listu gradovi s barem pet gradova. Programski odredite 
#ime grada koji se nalazi na kraju liste. Tako određen grad nadodajte 
#na prvu poziciju u listi gradovi te ispišite listu. Iz liste gradovi
#izbacite sva pojavljivanja zadnjeg grada te ponovo ispišite listu.

cities=["Zagreb","Osijek","Rijeka","Split","Lipik"]
last_city=cities[-1]
print(last_city)

cities.pop(-1)
print(cities)

cities.insert(0,last_city)
print(cities)













