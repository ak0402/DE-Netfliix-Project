# Databricks notebook source
# MAGIC %md
# MAGIC Array

# COMMAND ----------


files=[{"sourcefolder":"netflix_cast","targetfolder":"netflix_cast"},
 {"sourcefolder":"netflix_directors","targetfolder":"netflix_directors"},
 {"sourcefolder":"netflix_category","targetfolder":"netflix_category"},
 {"sourcefolder":"netflix_countries","targetfolder":"netflix_countries"}]




# COMMAND ----------

# MAGIC %md
# MAGIC Job utility to return the array 
# MAGIC

# COMMAND ----------

dbutils.jobs.taskValues.set(key="my_arr", value=files)