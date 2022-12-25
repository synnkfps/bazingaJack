import random

def randomPattern(pattern) -> str:
    vowels: str = 'aeiou'
    consonants: str = 'bcdfghjklmnpqrstvwxyz'
    build: str = ''

    for i in pattern:
        if i == 'v': build += random.choice(list(vowels))
        elif i == 'V': build += random.choice(list(vowels)).upper()
        
        elif i == 'c': build += random.choice(list(consonants))
        elif i == 'C': build += random.choice(list(consonants)).upper()

        elif i == 'n': build += str(random.randrange(0, 10)) # numbers
        elif i == ' ': build += i
    
    return build

# Variables (pattern to choose | regex matcher | generated nicks list)
class Generate:
    
    pattern: str = 'Cvcv'
    amount: int = 0
    matcher: str = '....'
    generated = []

    def __new__(self, pattern, amount):
        self.pattern = pattern 
        self.amount = amount 

        for i in range(self.amount):
            b = randomPattern(self.pattern)

            while b in self.generated:  
                b = randomPattern(self.pattern)

            self.generated.append(b)

        return self.generated
