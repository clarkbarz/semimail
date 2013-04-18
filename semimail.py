# Main file for SemiMail application
#
# Created by: Scott Clark

import cmd
import imaplib

class HomeScreen(cmd.Cmd):


# logs into gmail using the info in .login
def login():
	auth = open('.login', 'r')
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	username = auth.readline().strip()
	password = auth.readline()
	mail.login(username, password)
	HomeScreen().cmdloop()

if __name__ == '__main__':
	login()