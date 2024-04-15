from transformations import examples
from pyspark.sql import SparkSession
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
spark = SparkSession.builder.appName("Spark App").getOrCreate()

source = [("srikanth", 1), ("Ashoka", 2)]
df = spark.createDataFrame(source, ["name", "id"])
examples.add_column(df).show(False)
examples.drop_column(df, "id").show(False)
