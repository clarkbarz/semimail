# Main file for SemiMail application
#
# Created by: Scott Clark

import cmd
import getpass
import imaplib

class HomeScreen(cmd.Cmd):



def main():
	username = raw_input("Enter gmail username: ")
	password = getpass.getpass()
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(username, password)
	HomeScreen().cmdloop()

if __name__ == '__main__':
	main()