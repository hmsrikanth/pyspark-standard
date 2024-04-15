# pyspark-standard


Using `black` for code formatting

https://black.readthedocs.io/en/stable/

using poetry `poetry run black .` 

format whole repo

-------------

### Run tests

`poetry run pytest -rA`

--------------------

``` poetry run pylint .\transformations\


************* Module transformations.examples
transformations\examples.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transformations\examples.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
transformations\examples.py:5:0: C0103: Function name "Addcolumn" doesn't conform to snake_case naming style (invalid-name)
transformations\examples.py:9:0: C0116: Missing function or method docstring (missing-function-docstring)
transformations\examples.py:9:0: C0103: Function name "Dropcolumn" doesn't conform to snake_case naming style (invalid-name)
transformations\examples.py:1:0: W0611: Unused SparkSession imported from pyspark.sql (unused-import)
************* Module transformations.main
transformations\main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
transformations\main.py:12:0: E1101: Module 'transformations.examples' has no 'add_column' member (no-member)
transformations\main.py:13:0: E1101: Module 'transformations.examples' has no 'drop_column' member (no-member)
transformations\main.py:2:0: C0411: third party import "pyspark.sql.SparkSession" should be placed before first party import "transformations.examples"  (wrong-import-order)
transformations\main.py:3:0: C0411: standard import "os" should be placed before third party import "pyspark.sql.SparkSession" and first party import "transformations.examples"  (wrong-import-order)
transformations\main.py:4:0: C0411: standard import "sys" should be placed before third party import "pyspark.sql.SparkSession" and first party import "transformations.examples"  (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 0.00/10 (previous run: 0.00/10, +0.00)```
