# Databricks notebook source
# MAGIC %md
# MAGIC Silver Note Book Lookuptables

# COMMAND ----------

# MAGIC %md
# MAGIC Parameters

# COMMAND ----------

dbutils.widgets.text("sourcefolder","netflix_directors")
dbutils.widgets.text("targetfolder","netflix_directors")


# COMMAND ----------

# MAGIC %md
# MAGIC variables

# COMMAND ----------

var_tgt_folder = dbutils.widgets.get("targetfolder")
var_src_folder = dbutils.widgets.get("sourcefolder")


# COMMAND ----------

df=spark.read.format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load(f"abfss://bronze@p2netflixprojectdatalake.dfs.core.windows.net/{var_src_folder}")


# COMMAND ----------

df.display()

# COMMAND ----------

df.write.format("delta")\
    .mode("append")\
    .option("path",f"abfss://silver@p2netflixprojectdatalake.dfs.core.windows.net/{var_tgt_folder}")\
    .save()