import sqlite3

#creates the file when it runs
conn = sqlite3.connect('emaildb.sqlite')
#open then send SQL commands through the cursor (kinda like handle)
cur = conn.cursor()

#stops the file from blowing up if we start with a fresh database
#shouldn't do anything in this code
cur.execute('DROP TABLE IF EXISTS Counts')

#pretend that it's a dictionary
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # ? is a place holder to stop SQL injections
    # (email,) is a tuple we have to do this to make a tuple
    # cur is opening a record set
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    print(row)
    
    #this is us initiatng a count, we are making a count to index
    #this is going to spit us out an indexed tuple (email,1)
    #and this creates a row called counts in sql
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        #always better to update because there might be multiple apps
        #talking to the the db, it would also be 2 statements if we
        #had python do the counting
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    #commit takes time and you coud just commit every 10 times
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
