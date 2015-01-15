#!env python
## Jonas Lejon, Triop AB 2015
import sys
import os
import time
try:
    from kppy.database import KPDBv1
    from kppy.exceptions import KPError
except:
    print "You need to install kppy using pip install kppy or download from https://raymontag.github.io/kppy/"
    sys.exit(-1)

def main(k_db, k_passphrase):
    # open kepass db
    try:
        db = KPDBv1(k_db, k_passphrase, read_only=True)
        db.load()
    except KPError as e:
        print(e)
        sys.exit(1)

    items = ''
    for entry in db.entries:
        if entry.title != 'Meta-Info':
            print entry.title
            password = entry.password
            username = entry.username
            if username != 'SYSTEM':
                print " \_",username,password
    db.close()


########################
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print "Usage: %s <file> <password>\n" % sys.argv[0]
        sys.exit(-1)

    main(sys.argv[1], sys.argv[2])
