text = str
textFile = open('C:/Users/seth/Downloads/text.txt', 'r')
text = textFile.readlines()
count1 = int(0)
count2 = int(0)
count3 = int(0)
count4 = int(0)
count = int(0)
textFile.close()
while count < len(text):
      if(text[count].islower()):
            count1 += 1
      elif(text[count].isspace()):
            count3 += 1
      elif(text[count].isupper()):
            count2 += 1
      elif(text[count].isnumeric()):
            count4 += 1
      count += 1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)
print("The number of spaces characters is:")
print(count3)
print("The number of numbers characters is:")
print(count4)
