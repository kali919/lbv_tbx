import pyspark
from pyspark.sql import SparkSession

def sayhello():
    spark = SparkSession.builder.appName("Test").getOrCreate()
    print("Hello World")
    spark.stop()

