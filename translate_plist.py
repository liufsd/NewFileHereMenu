import os
import plistlib

def main():

   fileName=os.path.expanduser('Preferences.strings')

   if os.path.exists(fileName):

      pl=plistlib.readPlist(fileName)
      lst = []
      for key in pl:
        val = pl[key]
        print('key: %s, val: %s' % (key, val))
    

   else:
      print( '%s does not exist, so can\'t be read' % fileName)

if __name__ == '__main__':
   main()