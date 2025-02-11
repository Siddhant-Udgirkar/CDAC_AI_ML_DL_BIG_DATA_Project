from pyspark.sql import SparkSession

spark= SparkSession.builder\
    .appName("demo1")\
    .getOrCreate()


file_path= "/home/sunbeam/(PG-DBDA Sunbeam)/BigData/data/emp.csv"

df= spark.read\
    .option("inferSchema", "True")\
    .csv(file_path)

df.printSchema()

df.show()