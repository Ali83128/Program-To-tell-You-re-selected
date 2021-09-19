letter= '''Dear <|NAME|>,
You're Selected!
Date:<|DATE|>
'''
name=input("Enter Your Name ")
date=input("Enter the date ")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
