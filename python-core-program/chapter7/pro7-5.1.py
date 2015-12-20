import time
db = {}
loginTime = {}
def newuser():
	prompt = 'login desired: '
	while True:
		name = raw_input(prompt)
		if db.has_key(name):
			prompt = 'name taken, try another: '
			continue
		else:
			break
	pwd = raw_input('passwd: ')
	db[name] = pwd
	if (loginTime[name] == 'None') or (time.ctime() - loginTime[name]):
		print 'You already logged in at:%s ' % loginTime[name]
	loginTime[name] = time.ctime()
def olduser():
	name = raw_input('login: ')
	pwd = raw_input('passwd: ')
	passwd = db.get(name)
	if passwd == pwd:
		print 'welcome back', name
		if (loginTime[name] == 'None') or (time.ctime() - loginTime[name]):
			print 'You already logged in at:%s ' % loginTime[name]
		loginTime[name] = time.ctime();
	else:
		print 'login incorrect'

def showmenu():
	prompt = """
				(N)ew User login
				(E)xisting User login
				(Q)uit
				Enter choice:
			  """

	done = False
	while not done:
		chosen = False
		while not chosen:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except (EOFError, KeyboardInterrupt):
				choice = 'q'
			print '\nYou picked: [%s]' % choice
			
			if choice not in 'neq':
				print 'invalid option, try again'
			else:
				chosen = True
		if choice == 'q': done = True
		if choice == 'n': newuser()
		if choice == 'e': olduser()

if __name__ == '__main__':
	showmenu()