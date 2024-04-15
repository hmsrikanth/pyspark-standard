from pyspark.sql.functions import lit

from transformations import examples
from pyspark.testing.utils import assertDataFrameEqual

from pyspark.sql import SparkSession
import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = SparkSession.builder.appName("examples").getOrCreate()
source = [("srikanth", 1), ("Ashoka", 2)]
df = spark.createDataFrame(source, ["name", "id"])


def test_examples_add_column():
    assertDataFrameEqual(examples.add_column(df), df.withColumn("test", lit(1)))


def test_examples_drop_column():
    assertDataFrameEqual(examples.drop_column(df, "id"), df.drop("id"))
