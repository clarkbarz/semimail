# Main file for SemiMail application
#
# Created by: Scott Clark

import cmd
import getpass

class HomeScreen(cmd.Cmd):


def main():
	username = raw_input("Enter gmail username: ")
	password = getpass.getpass()
	print password

if __name__ = '__main__':
	main()