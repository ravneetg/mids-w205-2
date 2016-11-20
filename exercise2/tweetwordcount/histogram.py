import sys
import psycopg2


total = len(sys.argv)
conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="localhost", port="5432")
cur = conn.cursor()
print "Total number of arguments = ", total - 1

if total == 3:
    cur.execute("SELECT word, count from tweetwordcount where count >= %s and count <= %s order by count desc;" % (sys.argv[1],sys.argv[2]))
    for record in cur:
        print record
else:
     print "invalid number of arguments"

conn.close()

