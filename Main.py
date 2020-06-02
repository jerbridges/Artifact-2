# Authentication system for Zoo
import user
import hashlib
import csv

#  house keeping variables
user_good = False;
user = user.User('', '', '')
i = 1

print('Welcome to the SNHU Zoo')
while i <= 4:  # main loop 3 attempt to login in
    if i == 4 and not user_good:
        print('Too many attempts. Goodbye')
        break
    elif not user_good:
        print('attempt #%d:' % i)
        i += 1
        user.user_name = input('Please enter a username("exit" to exit): ')
        if user.user_name != 'exit':  # allows user to exit login screen
            user.user_password = input('Please enter password:')
            # md5 hash of password
            hashed_pass = hashlib.md5(user.user_password.encode())
            #  open cred file and check credentials
            with open('credentials.txt') as tsv:
                for cred_list in csv.reader(tsv, delimiter='\t'):
                    if user.user_name == cred_list[0] and hashed_pass.hexdigest() == cred_list[1]:
                        user_good = True  # found good user
                        user.user_role = cred_list[3]  # pull user role from credential file
                        f = open('%s.txt' % user.user_role)  # open the specified role file and print
                        message = f.read()
                        print('%s\n' % message)
                        i = 1  # reset iterator variable if user is found
                        f.close()  # close the opened role file
            user_good = False  # change boolean back to false to allow another login attempt
        else:
            print('Exiting')
            break
