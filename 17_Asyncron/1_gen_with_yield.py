def ip_gen():
    for i_1 in range(256):
        for i_2 in range(256):
            for i_3 in range(256):
                for i_4 in range(256):
                    yield f'{i_1}.{i_2}.{i_3}.{i_4}'

ip = ip_gen()
print(ip)
 
print(ip.__next__())
print(ip.__next__())
print(ip.__next__())
print(ip.__next__())
print(ip.__next__())

# print(next(ip))
# print(next(ip))
# print(next(ip))
# print(next(ip))
# print(next(ip))
