# f = open('/Users/iliyailchishin/Desktop/GB/Q2/Python/testfile.py', 'r')
# data = f.read() + ' '
# f.close()

# numbers = []
# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))     
#     data = data[space_pos+1:]
# print (numbers)

# out = []
# for e in numbers:
#      if not e % 2:
#          out.append((e,e **2))
# print(out)


# def f(x):
#     return x**2

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if x%2==0]

# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))

# print(data)


# data = list(map(int,input('Please enter numbers using comma ').split(',')))
# print(data)
# data=list(filter(lambda e: e>55,data))
# print(data)
lst =[2,65,87,34,44,44,23,34,23,65,22]
test = set(lst)
test = sorted(test)
print(test)
test = (set(map(int,filter(lambda e: not e%2 and e>30, test))))
print(test)


# data = '1 2 3 5 8 15 17 20'.split()
# data = list(map(int, data))
# data = list(filter(lambda e: not e % 2, data))
# data = list(map(lambda e: (e, e**2), data))
# print(data)


# lst = list(map(str, input().split()))
# print(lst)
# names = list(enumerate(lst))
# print(names)



# nums = [lambda i:i**2 for i in range (1,21) if i%2 == 0]
# print(list(nums))

# # lst = [(i,f(i)) for i in range (1,21) if i%2 == 0]
# # print(lst)
# # data = list(map(lambda e: (e, e**2), data))