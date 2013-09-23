#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mt
#
# Created:     20/09/2013
# Copyright:   (c) mt 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    tt = {'1':123,'4':989}
    t2 = {'2':345,'3':999}
    tt.update(t2)
    print tt
    for key in tt:
        print key,tt[key]

if __name__ == '__main__':
    main()
