from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()


    def process(self, tup):
        word = tup.values[0]

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount
        # Table name: Tweetwordcount
        # you need to create both the database and the table in advance.

        conn = psycopg2.connect(database="tcount", user="postgres", password="postgres", host="localhost", port="5432")
        cur = conn.cursor()

        #Update
        #Assuming you are passing the tuple (uWord, uCount) as an argument
        # cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (uWord, uCount))
        # conn.commit()

        #Insert
        #cur.execute("INSERT INTO tweetwordcount (word,count) \
        #      VALUES (%s, %s), (word, self.counts[word])");
        # update_word_count(cur, word)
        # if cur.rowcount == 0:   #rowcount tells you the number of rows updated
        #    try:
        #       cur.execute("insert into tweetwordcount (word, count) values (%s, 1)", (word,))
        #    except psycopg2.IntegrityError:
        #       update_word_count(cur, word)
        # conn.commit()
        #
        # conn.close()


        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (self.counts[word],word))
        cur.execute("INSERT INTO tweetwordcount (word,count) SELECT %s, %s  WHERE NOT EXISTS (SELECT 1 FROM tweetwordcount WHERE word=%s)", (word,self.counts[word],word))

        #if self.counts[word] == 1:
                #Insert
                # cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, %s)", (word, self.counts[word]));
        # else:
                #Update
                #Assuming you are passing the tuple (uWord, uCount) as an argument
                # cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (self.counts[word],word))
                # cur.execute("WITH upsert AS ( UPDATE tweetwordcount SET count = count + 1 WHERE word = 'thisisateststringdeleteme' RETURNING *) \
        conn.commit()
        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))

