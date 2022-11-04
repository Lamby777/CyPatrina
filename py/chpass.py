######################
#  Change passwords  #
######################

import pwd, os, sys

print("New password:")
NPWD = input()

if sys.argv[1] == "set":
	for user in pwd.getpwall():
		username = user[0]
		if username == sys.argv[2]: continue
		
		userid = user[2]
		if userid >= 1000 and userid != 65534:
			os.system("echo \"%s\\n%s\" | sudo passwd %s" % (NPWD, NPWD, user[0]))
