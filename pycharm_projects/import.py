name = input('Please put on your name: ')
with open('guest.txt','w') as file_objects:
    file_objects.write(name)
