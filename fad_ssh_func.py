#functions fad_ssh_func

import json
import paramiko
import time
import re

fhostname = "192.168.47.21"
fusername = "boby"
fpassword = "Fortinet123$"

def checkfguard():
  ssh = paramiko.SSHClient()
  ssh.load_system_host_keys()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(hostname=fhostname, username=fusername, password=fpassword)
  channel = ssh.invoke_shell()
  channel.send('execute web-category-test www.wp.pl\n')
  time.sleep(2)
  output=channel.recv(2048)
  ssh.close()
  outstr=str(output)
  result=re.search('Category:\sSearch\sEngines\sand\sPortals',outstr)
  if result:
   return 1
  else:
   return 0

def changeTTL():
  ssh = paramiko.SSHClient()
  ssh.load_system_host_keys()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(hostname=fhostname, username=fusername, password=fpassword)
  channel = ssh.invoke_shell()
  channel.send('config global\n')
  time.sleep(2)
  output=channel.recv(2048)
  channel.send('config system web-filter\n')
  time.sleep(2)
  output=channel.recv(2048)
  channel.send('set cache-ttl 15\n')
  time.sleep(2)
  output=channel.recv(2048)
  channel.send('end\n')
  time.sleep(2)
  output=channel.recv(2048)
  channel.send('config global\n')
  time.sleep(2)
  output=channel.recv(2048)
  channel.send('config system web-filter\n')
  time.sleep(2)
  output=channel.recv(2048)
  channel.send('set cache-ttl 14\n')
  time.sleep(2)
  output=channel.recv(2048)
  channel.send('end\n')
  time.sleep(2)
  output=channel.recv(2048)
  ssh.close()


  
