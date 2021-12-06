print("Welkom bij mijn programma")

naam = input("gelieve uw naam te verschaffen")

pincode = input("gelieve uw pincode te verschaffen")

bijdrage = int(input ("gelieve uw bank saldo te verschaffen"))

donatie = bijdrage - bijdrage



if bijdrage <= 50:

    print("verdien meer geld")

else:

    print("Bedankt ", naam , "uw nieuwe saldo is" , str(donatie) , " bedankt voor uw bijdrage");