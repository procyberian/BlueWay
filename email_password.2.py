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
password_list = []

def email():
    while True:
        email = input('email is:').strip()
        if not email:
            break
        else:
            email_list.append(email)
    return email_list
        
def password():
    while True:
        password = input('password is:').strip()
        if not password:
            break
        else:
            password_list.append(password)
    return password_list

my_email = email() 
my_password = password()
print('my emails and my passwords are:', my_email, my_password)

