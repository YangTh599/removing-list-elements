# Thayer Yang
# 30 OCT 2024
# Removing Lists

from random import randint
from random import shuffle
from time import sleep as sp

# Favorite Video Games

fav_games = [' Team Fortress 2', 'Left 4 Dead 2', 'VALORANT', 'Call Of Duty: BLACK OPS', 'ROBLOX', ' Minecraft','Counter Strike 2']

print(fav_games)

# pop() method used

fav_games.pop(len(fav_games)-2)

# remove() method used

fav_games.remove("ROBLOX")

# del keyword used

del fav_games[3]

# Final updated list

print(fav_games)
sp(2)
# Part 2

#Changing Guest List
print()

guests = ['Markiplier', 'Keanu Reeves', 'Michael Reeves', 'T1 Faker', 'SEN TenZ', 'Shaquille O\'Neal', 'Spongebob Squarepants']

print(f'Guests to the dinner party: {guests}')
sp(2)

shuffle(guests)
rand_index = randint(0,len(guests)-1)

print(f'OH NO! {guests[rand_index]} can not make it to the dinner party!')
guests.remove(guests[rand_index])
sp(2)

print('Sending invitations messages now.')
for guest in guests:
    print(f'Hello {guest}! You are invited to my dinner party!')
    sp(1)

# Shrinking Guest Lists
    
shuffle(guests)
print()
while len(guests) > 2:
    print(f'Sorry {guests[len(guests)-1]}! Sadly I can no longer invite you over for the dinner party!')
    guests.pop()
    sp(2)

for guest in guests:
    print(f'Hello {guest}! You\'re still invited to my dinner party!')
    sp(2)

print()
while len(guests) > 0:
    del guests[0]
print(f'List Elements: {guests}')
