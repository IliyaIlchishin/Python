


sentences = ['Fuck', 'Cars', 'Girls', 'Iphone 12', 'Mamacita']
Search = 'Fuck'
count = 0

for i in range(0, len(sentences)):
    if sentences[i] == Search:
        print(f'The element {Search} is found in the list. Index {i}. \n {sentences[i]}')
        count=+1
    

if count > 0:
    print()
else:
    print(f'We found no matchings with element {Search}')

