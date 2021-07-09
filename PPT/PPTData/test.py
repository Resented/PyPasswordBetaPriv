f = open('C:/Users/denzl/OneDrive/Dokumente/YT_scripts/projects/passwordckecker/PyPassword/test.txt','r')
text = ''
ttr = 0
for column in (f.readlines()):
    text += column
    print(column)
print(text)