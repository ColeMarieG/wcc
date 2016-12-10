print('\nWelcome to the Mad Lib Generator!\n')

# Ask user for 10 unique words
adj1 = raw_input('Type an adjective: ')
adj2 = raw_input('Type another adjective: ')
adj3 = raw_input('And another adjective: ')
adj4 = raw_input('And one more adjective: ')
animals = raw_input('Plural animal (e.g. puppies): ')
verb = raw_input('Now a verb (present tense): ')
nouns = raw_input('Now a plural noun: ')
musician_name = raw_input('The first name of a female musician: ')
beverage = raw_input('A beverage: ')
body_parts = raw_input('And finally, a plural body part: ')

# The story
print('\nExcellent choices! Here\'s your story...\n\n--------------------')
print('There once was a ' + adj1 + ' programmer named ' + musician_name + '\nwho wanted to build a ' + adj2 + ' mobile app to \nhelp ' + adj3 + ' ' + animals + ' find new homes. \n')
print(musician_name + ' stayed up all night, drinking lots \nof caffeinated ' + beverage + ' as she worked and worked \ntrying to complete her ' + adj4 + ' program. \n')
print('Whenever ' + musician_name + ' hit a dead end, she would \nexclaim \'' + nouns + '\'!\n')
print('But she was not discouraged, and after a quick break \nto ' + verb + ' and clear her head, she got back to work.\n')
print('By morning, when the sun started to rise, she let out \na big yawn and stretched her ' + body_parts + '.\nFinally, she was done.\n--------------------\n')
