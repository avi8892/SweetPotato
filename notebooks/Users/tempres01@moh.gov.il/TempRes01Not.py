# Databricks notebook source
dbutils.fs.cp("/part-00000-e1fd1d71-35c0-450e-88f9-fbb54d794121-c000.snappy.parquet", "/jars")


eth0      Link encap:Ethernet  HWaddr 00:16:3e:7d:0c:fa  
          inet addr:FakeIP  Bcast:FakeIP.  Mask:255.255.255.0
          inet6 addr: fe80::216:3eff:fe7d:cfa/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:45166 errors:0 dropped:0 overruns:0 frame:0
          TX packets:43856 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:30492563 (30.4 MB)  TX bytes:8281925 (8.2 MB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:805170 errors:0 dropped:0 overruns:0 frame:0
          TX packets:805170 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:174749348 (174.7 MB)  TX bytes:174749348 (174.7 MB)
              
              

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ifconfig

# COMMAND ----------

webbrowser.open_new