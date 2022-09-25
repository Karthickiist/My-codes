package JavaTraining;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class filewrite {

	public static void main(String[] args) {
		String file="D:/nots.txt";
		String s;
		FileReader f=null;
		try {
			f=new FileReader(file);
			BufferedReader bw=new BufferedReader(f);
			s=bw.readLine();
			System.out.print(s);
			bw.close();
			bw=null;
			System.out.print("\nAll done...");
		}catch(Exception ex) {
			ex.printStackTrace();
		}
		finally {
			if(f!=null) {
				try {
					f.close();
				}catch(IOException ex) {
					ex.printStackTrace();
				}
			}
		}

	}

}
