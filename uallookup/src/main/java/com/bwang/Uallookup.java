package com.bwang;

import java.util.Map;
import java.util.HashMap;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.api.java.function.Function2;
import org.apache.spark.api.java.function.PairFunction;
import org.apache.spark.streaming.Duration;
import org.apache.spark.streaming.api.java.JavaDStream;
import org.apache.spark.streaming.api.java.JavaPairDStream;
import org.apache.spark.streaming.api.java.JavaStreamingContext;
import org.apache.spark.streaming.kafka.KafkaUtils;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import scala.Tuple2;

public class Uallookup {

	public static final String missingIP = "0.0.0.0";
	
	private Uallookup() {
	}

	public static void main(String[] args) {
		if (args.length < 5) {
			System.err
					.println("Usage: KafkaWordCount <master> <zkQuorum> <group> <topics> <numThreads>");
			System.exit(1);
		}

		// The last parameter, Jar file containing job code, to ship to cluster,
		// could be on local or hdfs, FTP URL...
		JavaStreamingContext jssc = new JavaStreamingContext(args[0],
				"KafkaWordCount", new Duration(5000),
				System.getenv("SPARK_HOME"),
				//"/root/kafka-1.0-SNAPSHOT-jar-with-dependencies.jar");
				JavaStreamingContext.jarOfClass(Uallookup.class));

		int numThreads = Integer.parseInt(args[4]);
		Map<String, Integer> topicMap = new HashMap<String, Integer>();
		String[] topics = args[3].split(",");
		for (String topic : topics) {
			topicMap.put(topic, numThreads);
		}

		JavaPairDStream<String, String> messages = KafkaUtils.createStream(
				jssc, args[1], args[2], topicMap);

		JavaDStream<String> ips = messages
				.map(new Function<Tuple2<String, String>, String>() {
					@Override
					public String call(Tuple2<String, String> tuple2) {
						String value = tuple2._2();
					    JSONObject json;
						try {
							json = (JSONObject)new JSONParser().parse(value);
						} catch (ParseException e) {
							// TODO Auto-generated catch block
							e.printStackTrace();
							return missingIP;
						}
					    Object client_ip_obj = json.get("client_ip");
					    String client_ip_str = client_ip_obj.toString();
						return client_ip_str;
					}
				});
		
	    JavaPairDStream<String, Integer> ipCounts = ips.map(
	    	      new PairFunction<String, String, Integer>() {
	    	        @Override
	    	        public Tuple2<String, Integer> call(String s) {
	    	          return new Tuple2<String, Integer>(s, 1);
	    	        }
	    	      }).reduceByKey(new Function2<Integer, Integer, Integer>() {
	    	        @Override
	    	        public Integer call(Integer i1, Integer i2) {
	    	          return i1 + i2;
	    	        }
	    	      });
		
	    ipCounts.print();
	    jssc.start();
	    jssc.awaitTermination();
		
	}
}
