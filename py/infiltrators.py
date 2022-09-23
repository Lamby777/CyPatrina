##############################################################
# List all actual users, make it easy to delete infiltrators #
#                  Coded by DexieTheSheep                    #
##############################################################

import pwd, grp, sys, subprocess

def getgroups(user):
	out = subprocess.getoutput("groups " + str(user))
	return out[len(user)+2:]

if len(sys.argv) == 1:
	raise AssertionError("No arguments given!")

if sys.argv[1] == "list":
	for user in pwd.getpwall():
		userid = user[2]
		if userid >= 1000 and userid != 65534:
			groups = getgroups(user[0])
			print("User %s with ID %s in groups %s" % (user[0], userid, groups))
elif sys.argv[1] == "listsudo":
	for user in pwd.getpwall():
		userid = user[2]
		if userid >= 1000 and userid != 65534:
			groups = getgroups(user[0])
			if "sudo" in groups:
				print("User %s (%s) has admin rights!" % (user[0], userid))
else:
	raise AssertionError("Invalid arguments given!")
