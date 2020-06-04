# Databricks notebook source
dbutils.fs.cp("/part-00000-e1fd1d71-35c0-450e-88f9-fbb54d794121-c000.snappy.parquet", "/jars")

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ifconfig

# COMMAND ----------

webbrowser.open_new