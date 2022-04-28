import os
import shutil
from pathlib import Path
from mando import command, main

@command
def text_replacer(ppath, pattern, replacement):
    rootdir = Path(ppath)
    
    pattern_list=[pattern.strip().lower(), pattern.strip().upper(), pattern.strip().capitalize()]
    replacement_list=[replacement.strip().lower(), replacement.strip().upper(), replacement.strip().capitalize()]

    for logo, logo_og in zip(replacement_list, pattern_list):
        for root, dirs, files in os.walk(ppath, topdown=False):
            for f in files:
                shutil.move(os.path.join(root, f), os.path.join(root, f.replace(logo_og, logo).strip()))
                print("file: ", f)


            for dr in dirs:
                shutil.move(os.path.join(root, dr), os.path.join(root, dr.replace(logo_og, logo).strip()))
                print("dir: ", dr)
        
        for dir, subdirs, names in os.walk( rootdir ):
            for name in names:
                path = os.path.join( dir, name )
                try:
                    text = open( path ).read()
                    if logo_og in text:
                        open( path, 'w' ).write( text.replace( logo_og, logo ) )
                except:
                    pass

                


if __name__ == '__main__':
    main()