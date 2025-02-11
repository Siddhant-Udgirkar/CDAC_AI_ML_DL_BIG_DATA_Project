from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split

# Create a SparkSession
spark = SparkSession.builder.appName("StructuredStreamingExample").getOrCreate()

# Define the input source
lines = spark.readStream.format("socket").option("host", "localhost").option("port", 9999).load()

# Split the lines into words
words = lines.select(explode(split(lines.value, " ")).alias("word"))

# Count the occurrences of each word
wordCounts = words.groupBy("word").count()

# Define the output sink
query = wordCounts.writeStream.outputMode("complete").format("console").start()

# Wait for the computation to terminate
query.awaitTermination()
