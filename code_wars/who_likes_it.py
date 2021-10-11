'''
likes([]) # must be "no one likes this"
likes(["Peter"]) # must be "Peter likes this"
likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark"]) # must be "Max, John and Mark like this"
likes(["Alex", "Jacob", "Mark", "Max"]) # must be "Alex, Jacob and 2 others like this"
'''

#names=[]
#names=['Peter']
#names=['Peter', 'Jacob']
#names=['Peter', 'Jacob', 'Alex']
names=['Peter', 'Jacob', 'Alex', 'Max', 'John', 'Mark']

#as if version

def likes(names):
    if len(names)==0:
        return "no one likes this"
    elif len(names)==1:
        return names[0]+" likes this"
    elif len(names)==2:
        return names[0]+" and "+names[1]+" like this"
    elif len(names)==3:
        return names[0]+", "+names[1]+" and "+names[2]+" like this"
    else:
        return names[0]+", "+names[1]+" and "+str(len(names)-2)+" others like this"

print(likes(names))

# as dictionary version

def likes(names):
    formats = {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }
    n = len(names)
    return formats[min(n, 4)].format(*names, others=n-2)

print(likes(names))