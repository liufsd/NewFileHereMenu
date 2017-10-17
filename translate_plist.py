import os
import plistlib
from googletrans import Translator

def main():
   translator = Translator()

   fileName=os.path.expanduser('Preferences.strings')

   if os.path.exists(fileName):

      pl=plistlib.readPlist(fileName)
      lst = []
      for key in pl:
        val = pl[key]
        print('key: %s, val: %s' % (key, val))
        translation = translator.translate(val, dest='ru')
        pl[key]=translation.text
        print('translation: %s' % (pl[key]))
        
      plistlib.writePlist(pl, 'Preferences_ru.strings')
   else:
      print( '%s does not exist, so can\'t be read' % fileName)

if __name__ == '__main__':
   main()