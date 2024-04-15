from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import lit


def add_column(df: DataFrame) -> DataFrame:
    return df.withColumn("test", lit(1))


def drop_column(df: DataFrame, col: str) -> DataFrame:
    return df.drop(col)
