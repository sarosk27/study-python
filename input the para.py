'''
paragraph = input("Enter a paragraph: ")

lines = paragraph.split("\n")

print("Paragraph (with each line on a new line):")
for line in lines:
    print(line)

'''
para=[]
print('enter the paragraph ')
while True:
    line = input()
    if line:
        para.append(line)
    else:
        break
print(para)
new_line = '\n'.join(para)
print (new_line)