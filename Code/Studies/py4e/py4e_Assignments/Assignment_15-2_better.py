import sqlite3


con = sqlite3.connect('orgdb_fast.sqlite')
curse = con.cursor()
curse.execute('DROP TABLE IF EXISTS Orgs')
curse.execute('CREATE TABLE Orgs (org TEXT, count INTERGER)')


def search_split():
    file_name = 'mbox.txt'
    commit_count = 0
    lines_count = 0
    try:
        handle = open(file_name)
    except Exception as e:
        print(e)
    for line in handle:
        if not line.startswith('From: '): continue
        slices = line.split('@')
        org = slices[1]
        curse.execute('SELECT count FROM Orgs WHERE org =? ', (org,))
        row = curse.fetchone()
        lines_count = lines_count +1
        if row is None:
            curse.execute('INSERT INTO Orgs (org, count) VALUES (?,1)', (org,))
        if row is not None:
            curse.execute('UPDATE Orgs SET count = count +1 WHERE org = ?', (org,)) 
        if lines_count % 100 == 0:
            lines_count = 0
            commit_count += 1
            con.commit()
    con.commit()
           
    print('Commit count:',commit_count)
    

search_split()
sqlstr = 'SELECT org, count FROM Orgs ORDER BY count DESC LIMIT 10'

for row in curse.execute(sqlstr):
    print(str(row[0]), row[1]) 
    