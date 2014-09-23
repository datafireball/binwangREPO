Here is the output running on a Ubuntu box on my Virtualbox. 
Clearly, it poped up Java heap space error because it was trying to fit 2 million records into a list and then bulk insert that into HBase. 

log4j:WARN No appenders could be found for logger (org.apache.hadoop.metrics2.lib.MutableMetricsFactory).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
1	768
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
1048576	23960
Exception in thread "main" java.lang.OutOfMemoryError: Java heap space
	at java.lang.String.substring(String.java:1913)
	at java.util.Formatter.parse(Formatter.java:2525)
	at java.util.Formatter.format(Formatter.java:2469)
	at java.util.Formatter.format(Formatter.java:2423)
	at java.lang.String.format(String.java:2797)
	at test.Main.main(Main.java:27)
