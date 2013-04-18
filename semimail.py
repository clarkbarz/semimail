# Main file for SemiMail application
#
# Created by: Scott Clark

import cmd
import getpass
import imaplib

#class HomeScreen(cmd.Cmd):


# logs into gmail using the info in .login
def login():
	auth = open('.login', 'r')
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(auth.readline(), auth.readline())
	#HomeScreen().cmdloop()

# receives initial username and password and stores them for later
def setup():
	username = raw_input("Enter gmail username: ")
	password = getpass.getpass()
	auth = open('.login', 'w')
	auth.write(username, '\n', password)
	auth.close()

if __name__ == '__main__':
	login()
else:
	setup()