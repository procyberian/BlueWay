email_list = []

def email():
    email = input('email is:')
    if email == 'quit':
        print('wrong email')
    else:
        email_list.append(email)
        
def password():
    password = input('password is:')
    if password == 'quit':
        print('wrong email')
    else:
        email_list.append(password)        

def display_email_password(email, password):
    avatar = email + " " +password
    print("my avatar is: ", avatar)
    
display_email_password('myemail@myemail.com', 'myemail')
