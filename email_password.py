"""
Blue Way Logistics Software

Copyright (C) 2023 Masscollabs Services

Copyright (C) 2023 procyberian and contributors

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
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
