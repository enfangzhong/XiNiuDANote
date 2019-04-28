#删除已有文件夹
hadoop fs -rmr /sxydata/input/example_1
hadoop fs -rmr /sxydata/output/example_1

#创建输入文件夹
hadoop fs -mkdir /sxydata/input/example_1

#放入输入文件
hadoop fs -put text* /sxydata/input/example_1

#查看文件是否放好
hadoop fs -ls /sxydata/input/example_1

#本地测试一下map和reduce
head -20 text1.txt | python count_mapper.py | sort | python count_reducer.py

#集群上跑任务
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-file count_mapper.py \
-mapper count_mapper.py  \
-file count_reducer.py \
-reducer count_reducer.py \
-input /sxydata/input/example_1 \
-output /sxydata/output/example_1