import sys
import psycopg2


total = len(sys.argv)
conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="localhost", port="5432")
cur = conn.cursor()
print "Total number of arguments = ", total - 1

if total == 2:
    cur.execute("SELECT count from tweetwordcount where word = '%s';" % (sys.argv[1]))
    #cur.execute("SELECT count(*) from tweetwordcount where word = %s", (sys.argv[1]))
    print "Total number of occurences of %s = %s" % (sys.argv[1], cur.fetchone()[0])
else:
     cur.execute("SELECT word, count from tweetwordcount order by word;")

#cur.execute("SELECT word, count(*) from tweetwordcount group by word order by word limit 5;")
print cur.fetchall()

# for record in cur:
#     print cur.fetchone()
# conn.close()
