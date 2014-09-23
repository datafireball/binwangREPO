package test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.Get;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.util.Bytes;

public class Main {

	private static final int PUTRECORDNUMBER = 1000000;
	private static final int GETRECORDNUMBER = 10000;

	public static void main(String[] args) throws IOException {
		Configuration conf = HBaseConfiguration.create();
		HTable table = new HTable(conf, "testtable");
		int myrecordnumber = 1;
		
		/* List Put */
		long startTime = System.currentTimeMillis();
		List<Put> puts = new ArrayList<Put>();
		for (int j = 0; j < PUTRECORDNUMBER; j++) {
			Put myput = new Put(Bytes.toBytes(j));
			myput.add(Bytes.toBytes("colfam1"),
					Bytes.toBytes("col1"),
					Bytes.toBytes(j));
			puts.add(myput);
		}
		table.put(puts);
		long endTime = System.currentTimeMillis();
		System.out.print(myrecordnumber);
		System.out.print("\t");
		System.out.println(endTime - startTime);
		System.out.println("Put Successfully!");
		
		
		int mygetrecordnumber = 1;
		for (int j = 0; j < 20; j++) {
			/* List Get */
			startTime = System.currentTimeMillis();
			List<Get> gets = new ArrayList<Get>();
			for (int i = 0; i < mygetrecordnumber; i++) {
				Get myget = new Get(Bytes.toBytes(i));
				myget.addColumn(Bytes.toBytes("colfam1"), Bytes.toBytes("col1"));
				gets.add(myget);
			}
			
			Result[] results = table.get(gets);
//			for (Result result : results) {
//				String row = Bytes.toString(result.getRow());
//				byte[] val = result.getValue(Bytes.toBytes("colfam1"), Bytes.toBytes("col1"));
//				System.out.println(Bytes.toString(val));
//			}
			endTime = System.currentTimeMillis();
			System.out.print(mygetrecordnumber);
			System.out.print('\t');
			System.out.println(endTime - startTime);
			mygetrecordnumber = mygetrecordnumber * 2;
		}
		table.close();
	}
}
