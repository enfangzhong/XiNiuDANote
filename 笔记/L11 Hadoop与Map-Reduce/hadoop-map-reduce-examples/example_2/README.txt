#这个例子是统计人造草坪和天然草坪的数量

#删除已有文件夹
hadoop fs -rmr /sxydata/input/example_2
hadoop fs -rmr /sxydata/output/example_2

#创建输入文件夹
hadoop fs -mkdir /sxydata/input/example_2

#放入输入文件
hadoop fs -put stadiums.csv /sxydata/input/example_2

#查看文件是否放好
hadoop fs -ls /sxydata/input/example_2

#本地测试一下map和reduce
head -20 stadiums.csv | python mapper.py | sort | python reducer.py

#集群上跑任务
hadoop jar /usr/lib/hadoop-current/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
-file mapper.py \
-mapper mapper.py  \
-file reducer.py \
-reducer reducer.py \
-input /sxydata/input/example_2 \
-output /sxydata/output/example_2