#Hákon Dagur Oddgeirsson
#25.01.2017
#git_verkefni

print("Sláðu inn 2 tölur")
tala1=int(input("Sláðu inn fyrstu töluna:"))
tala2=int(input("Sláðu inn seinni töluna:"))
plus=tala1 + tala2
sinnum=tala1 * tala2
print("Ef þú plúsaðar tölurnar saman færðu útkommuna", plus)
print("Ef þú margfaldar tölurnar saman færðu útkommuna", sinnum)

#dæmi2

print("Sláðu inn nafnið þitt")
fornafn=input("Sláðu inn fornafn þitt hér:")
eftirnafn=input("Sláðu inn eftirnafn þitt hér:")
print("Halló" , fornafn , eftirnafn)

#Dæmi 3

print()
lagstaf = 0
hastaf = 0
eftirha = 0
minus = -1
text = input("Sláðu inn texta: ")
leng = int(len(text))
listi = list(text)

for x in listi:
    if x.isupper():
        hastaf += 1
    elif x.islower():
        lagstaf += 1

for x in range(leng):
    if listi[x].islower() and listi[minus].isupper():
        minus += 1
        eftirha += 1
    else:
        minus += 1

print("Í þessum texta eru",hastaf,"hástafir,",lagstaf,"lágstafir og",eftirha,
      "lágstafir strax á eftir hástaf")