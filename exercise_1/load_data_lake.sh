mkdir -p /data/labs/w205-fall-16-labs-exercises/exercise_1/loading_and_modelling
mkdir -p /data/labs/w205-fall-16-labs-exercises/exercise_1/exercise_1/data
wget https://data.medicare.gov/views/bg9k-emty/files/Nqcy71p9Ss2RSBWDmP77H1DQXcyacr2khotGbDHHW_s?content_type=application%2Fzip%3B%20charset%3Dbinary&filename=Hospital_Revised_Flatfiles.zip

unzip Hospital_Revised_Flatfiles.zip

mv "Hospital General Information.csv" hospitals.csv
mv "Timely and Effective Care - Hospital.csv" effective_care.csv
mv "Readmissions and Deaths - Hospital.csv" readmissions.csv
mv "Measure Dates.csv" Measures.csv
mv hvbp_hcahps_05_28_2015.csv surveys_responses.csv

tail -n +2 surveys_responses.csv >new_surveys_responses.csv 
tail -n +2 Measures.csv >new_Measures.csv
tail -n +2 readmissions.csv >new_readmissions.csv
tail -n +2 hospitals.csv >new_hospitals.csv
tail -n +2 effective_care.csv >new_effective_care.csv
tail -n +2 new_surveys_responses.csv >new_new_surveys_responses.csv
wc -l *
#   217822 effective_care.csv
#     4825 hospitals.csv
#      101 Measures.csv
#   217821 new_effective_care.csv
#     4824 new_hospitals.csv
#      100 new_Measures.csv
#     3073 new_new_surveys_responses.csv
#    66990 new_readmissions.csv
#     3074 new_surveys_responses.csv
#    66991 readmissions.csv
#     3075 surveys_responses.csv
#   588696 total

sudo su - w205

hdfs dfs -mkdir -p /user/w205/hospital_compare/hospitals
hdfs dfs -mkdir /user/w205/hospital_compare/effective_care
hdfs dfs -mkdir /user/w205/hospital_compare/readmissions
hdfs dfs -mkdir /user/w205/hospital_compare/measures
hdfs dfs -mkdir /user/w205/hospital_compare/new_surveys_responses

hdfs dfs -put new_hospitals.csv /user/w205/hospital_compare/hospitals
hdfs dfs -put new_effective_care.csv /user/w205/hospital_compare/effective_care
hdfs dfs -put new_readmissions.csv /user/w205/hospital_compare/readmissions
hdfs dfs -put new_Measures.csv /user/w205/hospital_compare/measures
hdfs dfs -put new_surveys_responses.csv /user/w205/hospital_compare/new_surveys_responses
hdfs dfs -ls /user/w205/hospital_compare
#Found 5 items
#drwxr-xr-x   - w205 supergroup          0 2016-10-13 08:01 /user/w205/hospital_compare/effective_care
#drwxr-xr-x   - w205 supergroup          0 2016-10-13 08:01 /user/w205/hospital_compare/hospitals
#drwxr-xr-x   - w205 supergroup          0 2016-10-13 08:01 /user/w205/hospital_compare/measures
#drwxr-xr-x   - w205 supergroup          0 2016-10-13 08:02 /user/w205/hospital_compare/new_surveys_responses
#drwxr-xr-x   - w205 supergroup          0 2016-10-13 08:01 /user/w205/hospital_compare/readmissions
#

