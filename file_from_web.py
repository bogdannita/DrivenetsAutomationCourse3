import requests

f = open("frankenstein.txt", "w", encoding='utf-8')  # w stands for open file for writing
r = requests.get("https://www.gutenberg.org/cache/epub/84/pg84.txt")
# print(r.content.decode())
f.write(r.content.decode())
f.close()

f = open("frankenstein2.txt", "wb")
r = requests.get("https://www.gutenberg.org/cache/epub/84/pg84.txt")
f.write(r.content)
f.close()

# count how many times the letter "a" shows up in the book
num_a = 0
f = open("frankenstein2.txt", encoding='utf-8')
for line in f:
    num_a += line.count("a")
print(f"The number of times a shows up in the book is {num_a}")
f.close()

f = open("frankenstein2.txt", encoding='utf-8')
num_words = 0
for line in f:
    words = line.split()
    num_words += len(words)

print(f"In frankenstein there are {num_words} words")
f.close()
