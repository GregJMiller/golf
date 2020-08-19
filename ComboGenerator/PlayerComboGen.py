import itertools
r=7 #this is the number of groupings, in DK PGA this would be 7 for example


def algo(liste):
    result1 = [ liste ]
    for i in range(r, len(liste), 2):
        result1.extend(list(itertools.combinations(liste, i)))
    return result1
 
#This is where you would copy and paste the excel list    
result1 = algo(['Matthew Wolff',
'Carlos Ortiz',
'Wyndham Clark',
'Lucas Glover',
'Brian Harman',
'Troy Merritt',
'Sam Burns',
'Scott Piercy',
'Scott Brown',
'Roger Sloan',
'Shawn Stefani',
'Tony Finau',
'Charles Howell III',
'Denny McCarthy',
'Tom Hoge',
'Brice Garnett',
'Johnson Wagner',
'Sam Ryder',
'Beau Hossler',
'Bronson Burgoon',
'Patton Kizzire',
'Hank Lebioda',
'Robert Streb',
'Ryan Armour',
'Cameron Tringale',
'Kramer Hickok',
'Dylan Frittelli',
'Richy Werenski',
'Peter Malnati',])

#print the different combintations
print(result1)
