dataput <- read.table(text="1  768
2	5
4	5
8	7
16	11
32	20
64	41
128	134
256	205
512	317
1024	434
2048	972
4096	791
8192	1205
16384	545
32768	675
65536	1447
131072	2572
262144	5169
524288	11900
1048576	23960", col.names=c('records', 'time'))

dataget <- read.table(text="1  165
2	42
4	6
8	7
16	11
32	14
64	31
128	118
256	216
512	262
1024	694
2048	882
4096	1040
8192	1001
16384	1039
32768	1974
65536	5213
131072	11984
262144	20739
524288	68610", col.names=c("records", "time"))

dataput$id <- "put"
dataget$id <- "get"

data <- rbind(dataput, dataget)

library(ggplot2)
ggplot(data=data, aes(x=records, y=time, color=id)) + 
  geom_line() + 
  geom_point(size=5) + 
  scale_x_log10() + 
  xlab("Total Number of Processed Records") +
  ylab("Execution Time (millisecond)") + 
  ggtitle("HBase List Get/Put Timing Experiment")
