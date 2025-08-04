Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('    Q1) Do you like Dawn or Dusk?')
print('    1) Dawn')
print('    2) Dusk')
print('')

ans1 = int(input(' Answer? (1 or 2): '))

print ()

if ans1 == 1:
    Gryffindor += 1
    Ravenclaw += 1
    
elif ans1 == 2:
    Hufflepuff += 1
    Slytherin += 1
    
else:
    print('Wrong Input!!')
    
print('')
print(' ')
print()
    
print('    Q2) When I’m dead, I want people to remember me as:')
print('    1) The Good')
print('    2) The Great')
print('    3) The Wise')
print('    4) The Bold')
print()

ans2 = int(input('Answer? (1, 2, 3 or 4): '))
print()

if ans2 == 1:
    Hufflepuff += 2
    
elif ans2 == 2:
    Slytherin += 2
    
elif ans2 == 3:
    Ravenclaw += 2
    
elif ans2 == 4:
    Gryffindor += 2
    
else:
    print('Wrong Input!')
    
print()
print()
print()

print('    Q3) Which kind of instrument most pleases your ear?')
print('    1) The violin')
print('    2) The trumpet')
print('    3) The piano')
print('    4) The drum')

print()

ans3 = int(input('Answer? (1, 2, 3 or 4): '))

print()

if ans3 == 1:
    Slytherin += 4
    
elif ans3 == 2:
    Hufflepuff += 4
    
elif ans3 == 3:
    Ravenclaw += 4
    
elif ans3 == 4:
    Gryffindor += 4
    
else:
    print('Wrong Input!')    
    
print()
print()
print()

print('Gryffindor: ', Gryffindor)
print('Ravenclaw: ', Ravenclaw)
print('Hufflepuff: ', Hufflepuff)
print('Slytherin: ', Slytherin)

print()

if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
    print('Gryffindor Won This Game With', Gryffindor ,'Points')
    
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin and Ravenclaw >= Gryffindor:
    print('Ravenclaw Won This Game With', Ravenclaw ,'Points')
   
elif Hufflepuff >= Slytherin and Hufflepuff >= Gryffindor and Hufflepuff >= Ravenclaw:
    print('Hufflepuff Won This Game With', Hufflepuff ,'Points') 
    
elif Slytherin >= Gryffindor and Slytherin >= Ravenclaw and Slytherin >= Hufflepuff:
    print('Slytherin Won This Game With', Slytherin ,'Points')