

sentences = ['Fuck', 'Cars', 'Girls','honey','filth','Cars', 'Love' ,'Fuck','Girls','Iphone 12','Mamacita', 'Cars']
Search = 'Cars'
count = 0

for i in range(0, len(sentences)):
    if sentences[i] == Search:
        count+=1
        if count >=2:
            print(f'The element {Search} is found in the list {count} times. It is located at index {i}. \n {sentences[i]}')

if count > 0:
    print(f'We found {count}')
else:
    print(f'We found no matchings with element {Search}')

