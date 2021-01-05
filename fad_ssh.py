#if not ok re-change TTL
from fad_ssh_func import *

if __name__ == '__main__': 
  f=checkfguard()
  if f:
    print('OK')
  else:
    print('changing')
    changeTTL()
    print('changed')

  react = input('Press a key')

  
