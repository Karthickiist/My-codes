package JavaTraining;

import java.io.PrintStream;
import java.util.Scanner;

public class looping {
	public static void main(String[] args) {
		String res;
		do{
			int a=1;
			Scanner in=new Scanner(System.in);
			while(a<=15) {
				System.out.print(a+"\n");
				a++;
			}
			System.out.print("Do you want to continue: ");
			res=in.next();
		}while(res.equalsIgnoreCase("Y"));
		
	}

}
