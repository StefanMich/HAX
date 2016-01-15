#!/usr/bin/env python2

from pwn import *

context(log_level = logging.DEBUG)

doing = term.output(float = True)

solutions = (
    'cat readme',
    'cat ./-',
    'cat spaces\ in\ this\ filename',
    'cat ./inhere/.hidden',
    'cat ./inhere/-file07',
    'du -ab | grep 1033 | grep -o \'\..*\' | xargs cat', # python escaping '
    'find / -user bandit7 -group bandit6 2>/dev/null | xargs cat',
    'cat data.txt | grep millionth | grep -o \'c.*\''
)

def solve(name,password,cmd):
    doing.update('Solving %s' % name)
    con = ssh(user = name, password = password, host = 'bandit.labs.overthewire.org')
    shell = con.shell(tty= False)
    shell.clean()
    shell.sendline(cmd)
    next_password = shell.recvline().strip()
    shell.close()
    con.close()
    print '%s gave us %s' % (name, next_password)
    return next_password

password = 'bandit0'
for i in range(0,len(solutions)):
    password = solve('bandit%d' % i,password,solutions[i])

print '\n'
