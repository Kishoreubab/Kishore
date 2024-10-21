input_string = "Guvi geeks network private limited"
input_string = input_string.lower()
count_a = count_e = count_i = count_o = count_u = 0
for char in input_string:
    if char == 'a':
        count_a += 1
    elif char == 'e':
        count_e += 1
    elif char == 'i':
        count_i += 1
    elif char == 'o':
        count_o += 1
    elif char == 'u':
        count_u += 1
total_vowels = count_a + count_e + count_i + count_o + count_u
print(f"Total count of all vowels: {total_vowels}")
print(f"Total count of 'A': {count_a}")
print(f"Total count of 'E': {count_e}")
print(f"Total count of 'I': {count_i}")
print(f"Total count of 'O': {count_o}")
print(f"Total count of 'U': {count_u}")



number = 20
for num in range(number):
    for num1 in range(number - num - 1):
        print(" ", end="")
    for num1 in range(num + 1):
        print(num1 + 1, end=" ")
    print()



input_string = "Hello World"
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
for words in input_string:
    if words in vowels:
        input_string = input_string.replace(words, '')
print(input_string)



input_string = "Hello World"
uc = 0
nuc = 0 
processed_chars = set()
for words in input_string:
    if words not in processed_chars:
        processed_chars.add(words)
        if input_string.count(words) > 1:
            print("Not unique character:", words)
            nuc += 1
        else:
            print("Unique character:", words)
            uc += 1
print("Total unique characters:", uc)



input_string = "RacecaR"
reversed_string = input_string[::-1]

if input_string == reversed_string:
    print("True")
else:
    print("False")



s1 = "my name is kb"
s2 = "my name is jack"
l1 = s1.split(" ")
l2 = s2.split(" ")
common = list(set(l1) & set(l2))
print("the largest common substring is", common)

input_string = "Hello World"
char_count = dict()
for char in input_string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
most_frequent_char = max(char_count, key=char_count.get)
max_count = char_count[most_frequent_char]

print(f"The most frequent character is: '{most_frequent_char}' with a count of {max_count}")




str1 = "heart"
str2 = "earth"
sor1 = sorted(str1)
sor2 = sorted(str2)
if sor1 == sor2:
    print("True.")
else:
    print("False")


input_string = "Hello World"
words = input_string.split()
count = len(words)
print("THE NUMBER OF WORDS:", count)


