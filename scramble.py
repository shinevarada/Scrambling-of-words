import random
def scramble(word):
 words_in_between = list(word[1:-1])
 random.shuffle(words_in_between)
 return word[0]+'' .join(words_in_between) +word[-1]

file_1= open("MyFile.txt","r")
file_2= open("MyFileScrambled.txt","w")
for line in file_1:
  words= line.split()
  for word in words:
   	scrambled_word=scramble(word)
   	file_2.write(scrambled_word)
   	file_2.write(" ");
print("Scrambled Successfully")
