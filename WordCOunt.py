# Create SparkSession and sparkcontext
from pyspark.sql import SparkSession
spark = SparkSession.builder\
                    .master("local")\
                    .appName('Firstprogram')\
                    .getOrCreate()
sc=spark.sparkContext

# Read the input file and Calculating words count
text_file_rdd = sc.textFile("firstprogram.txt")
result_test = text_file_rdd.filter(lambda line : 'sparksession' in line)
print(result_test.collect())
print(result_test.count())


'''print(text_file.flatMap(lambda line: line.split(" ")).collect())
print(text_file.flatMap(lambda line: line.split(" ")).map(lambda word : (word,1)).collect())'''
#print(text_file.flatMap(lambda line: line.split(" ")).map(lambda word : (word,1)).reduceByKey(lambda x,y :x+y).collect())

'''counts = text_file.flatMap(lambda line: line.split(" ")) .map(lambda word: (word, 1)).reduceByKey(lambda x, y: x + y)
                           '''

'''
# Printing each word with its respective count
output = counts.collect()
for (word, count) in output:
    print("%s: %i" % (word, count))
'''