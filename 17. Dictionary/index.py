Capitals = {
    'Nepal':'ktm',
    'India':'New Delhi',
    'China':'Beijing',
    'USA':'Washington DC',
    'Russia':'Moscow'
}

print(Capitals['Nepal'])

print(Capitals.get('Germany'))

print(Capitals.items())

#print(Capitals.Keys())
#print(Capitals.Values())


# Another Way to Print all keys and Values:

for Key,Value in Capitals.items():
    print(Key,Value)