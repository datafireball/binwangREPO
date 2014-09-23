package test;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.util.Bytes;

public class Main {

//	private static final int RECORDNUMBER = 1000000;
	public static void main(String[] args) throws IOException {
		Configuration conf = HBaseConfiguration.create();
		HTable table = new HTable(conf, "testtable");
		int myrecordnumber = 1;
		
		for (int i = 0; i < 22; i++) {
			long startTime = System.currentTimeMillis();
			List<Put> puts = new ArrayList<Put>();
			for (int j = 0; j < myrecordnumber; j++) {
				Put myput = new Put(Bytes.toBytes(j));
				myput.add(Bytes.toBytes("colfam1"),
						Bytes.toBytes(String.format("qual_%d", j)),
						Bytes.toBytes(i));
				puts.add(myput);
			}
			table.put(puts);
			long endTime = System.currentTimeMillis();
			System.out.print(myrecordnumber);
			System.out.print("\t");
			System.out.println(endTime - startTime);
			
			myrecordnumber = myrecordnumber * 2;
		}
		table.close();


	}
}

