numbers = [10, 501, 22, 37, 100, 999, 87, 351]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

mylist = [10, 501, 22, 37, 100, 999, 87, 351]
prime = []
for num in mylist:
    if num > 1:
        c = 0
        for num1 in range(1, num + 1):
            if num % num1 == 0:
                c += 1
        if c == 2:
            prime.append(num)

print(prime)

a = [10, 501, 22, 37, 100, 999, 87, 351]
b = []

def happy(a):
    for num in range(len(a)):
        sum = a[num]
        while sum != 1 and sum != 4:
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2
            sum = tempsum
        if sum == 1:
            b.append(a[num])
    return b

print(happy(a))


number = 34

number = str(number)

first_digit = int(number[0])  
last_digit = int(number[-1])   

addition = first_digit + last_digit  

print('Sum of first and last interger', addition)


def man(n, m):
    res = 1

    if m > n - m:
        m = n - m

    for num in range(m):
        res *= (n - num)
        res /= (num + 1)

    return res


def calculate(n, m):
    if n < m:
        return 0

    ways = man(m + n - 1, m - 1)
    return int(ways)

if __name__ == '__main__':
    n = 7
    m = 5

    result = calculate(n, m)
    print(result)



def intersects(arr1, arr2, arr3):
    common = list(filter(lambda x: x in arr2 and x in arr3, arr1))
    print(common)

arr1 = [1, 2, 3, 4, 5 ]
arr2 = [5, 6, 7, 8, 9, 10]
arr3 = [3, 4, 1, 2, 3, 5, 7, 8]

intersects(arr1, arr2, arr3)



def count(arr, n):
    visited = [False for num in range(n)]  
    for num in range(n):
        if visited[num]:
            continue
        count = 1
        for num1 in range(num + 1, n):
            if arr[num] == arr[num1]:
                visited[num1] = True  
                count += 1
        if count == 1:
            print(arr[num]) 
arr = [10, 30, 40, 20, 10, 20, 50, 10]
n = len(arr)
count(arr, n)




list1 = [2, 1, 6, 3, 9]

list1.sort()

print("Minimum element is:", list1[0])



from itertools import combinations
def findTriplets(lst, key):
    def valid(val):
        return sum(val) == key
    return list(filter(valid, combinations(lst, 3)))

lst = [10, 20, 30, 9]
print(findTriplets(lst, 59))



def subArray(arr, l):
    for num in range(l - 1):
        s = arr[num]
        for num1 in range(num + 1, l):
            s += arr[num1]
            if s == 0:
                return True
    return False

array = [4, 2, -3, 1, 6]

print(subArray(array, len(array)))









