#!/usr/bin/rlwrap /usr/bin/python3 

from db_manager import DBManager
from shell import Shell

def main():
    sh = Shell()
    sh.run()

if __name__ == "__main__":
    main()