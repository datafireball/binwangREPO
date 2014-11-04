#!/bin/bash

# -D: map only job
# -files: the files that you want to distribute to the cluster
# -input: the big raw html file in HDFS
# -output: the output folder
# -mapper: the mapper name

hadoop jar \
/opt/cloudera/parcels/CDH-5.1.0-1.cdh5.1.0.p0.53/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.3.0-mr1-cdh5.1.0.jar \
-D mapred.reduce.tasks=0 \
-files /tmp/local/mapper.py \
-input /tmp/hdfs/output.json \
-output /tmp/rscomponents \
-mapper mapper.py
