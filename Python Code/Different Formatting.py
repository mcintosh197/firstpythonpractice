'''
Formatting using +
'''

olympics = "Rio"
year = 2016
athlete = "Mo Farah"
goldMedals = 2

print ("At the " + str(year) + " " + olympics + " Olympics, " + athlete + " won " + str(goldMedals) + " gold medals")

'''
Formatting using comma
'''

olympics = "Rio"
year = 2016
athlete = "Mo Farah"
goldMedals = 2

print("At the", str(year), olympics, "Olympics,", athlete, "won", str(goldMedals), "gold medals")

'''
Formatting using %s
'''

olympics = "Rio"
year = 2016
athlete = "Mo Farah"
goldMedals = 2

print("At the %i %s Olympics, %s won %i gold medals" % (year, olympics, athlete, goldMedals))

'''
Formatting using f
'''

olympics = "Rio"
year = 2016
athlete = "Mo Farah"
goldMedals = 2

print (f"At the {year} {olympics} Olympics, {athlete} won {goldMedals} gold medals")