import re

def pwStronk(pw):
    strength = 'Stronk'
    lenRegex = re.compile(r'(\w){8,}')
    mo = lenRegex.search(pw)   
    if mo is None:    
        strength = 'Weak'
    lowerRegex = re.compile(r'([a-z])')
    mo = lowerRegex.search(pw)   
    if mo is None:    
        strength = 'Weak'
    digitRegex = re.compile(r'(\d)')
    mo = digitRegex.search(pw)   
    if mo is None:    
        strength = 'Weak'
    upperRegex = re.compile(r'([A-Z])')
    mo = upperRegex.search(pw)   
    if mo is None:    
        strength = 'Weak'
    
    print(strength)

print('Enter Password to test it\'s strenth:')
pw = input()
pwStronk(pw)