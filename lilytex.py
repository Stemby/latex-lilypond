#!/usr/bin/env python

import os, sys
from ConfigParser import ConfigParser

def main():
    lil = ConfigParser()
    lil.read(sys.argv[1])
    filename = lil.get('Config','filename')
    os.system('lilypond -dbackend=eps -dno-gs-load-fonts -dinclude-eps-fonts %s' % filename)

if __name__ == '__main__':
    main()
