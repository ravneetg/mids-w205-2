### Instructions

# Following python libraries need to be setup for executing this application
1) psycopg2
2) tweepy
3) streamparse

For installation, use pip install <library name>

# For the EC2 instance, use below AMI, this include storm and postgres

AMI Name: UCB MIDS W205 EX2-FULL
AMI ID: ami-d4dd4ec3

# to enable postgres, run below commands
service postgresql init # initialize the db
service postgresql start  # start the instance

# to run the application (data sourcing piece)
cd tweetwordcount; sparse run

# to extract the data from db for serving
python finalresults.py
