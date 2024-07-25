def digit(n):
    result=[]*len(n)
    for i in range(len(n)):
        res=[]
        for j in str(n[i]):
            res.append(int(j))
        result.append(res)
    return result

def checking(output, target):
    max_count = 0
    result = []

    for i in output:
        temp = 0
        for j in i:
            if j == target:
                temp += 1
        
        if temp > max_count:
            max_count = temp
            result = [i]
        elif temp == max_count:
            result.append(i)

    return result

def list_to_int(n):
    result = 0
    for digit in n:
        result = result * 10 + digit
    return result

arr = [111, 112, 111]
output = digit(arr)
result = checking(output, 1)

for i in result:
    print(list_to_int(i), end=' ')









# def digit(n):
#     result=[]*len(n)
#     for i in range(len(n)):
#         res=[]
#         for j in str(n[i]):
#             res.append(int(j))
#         result.append(res)
#     return result

# def checking(output,target):
#     count = 0
#     result = []

#     for i in output:
#         temp = 0
#         for j in i:
#             if j == target:
#                 temp += 1

#         if temp > count:
#             count = temp
#             result.append(i)

#         elif temp == count:
#             result.append(i)
        
#     return result

# def list_to_int(n):
#     result = 0
#     for digit in n:
#         result = result *10 + digit
#     return result



# arr = [121, 122, 222]
# output = digit(arr)
# result = checking(output,2)

# for i in result:
#     print(list_to_int(i),end=' ')