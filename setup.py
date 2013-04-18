# Setup file for Semimail
#
# Created by: Scott Clark

import getpass

# receives initial username and password and stores them for later
def setup():
	username = raw_input("Enter gmail username: ")
	password = getpass.getpass()
	auth = open('.login', 'w')
	auth.write(username + '\n' + password)
	auth.close()

if __name__ == '__main__':
	setup()