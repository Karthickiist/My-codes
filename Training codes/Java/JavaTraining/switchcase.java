package JavaTraining;

import java.io.PrintStream;
import java.util.Scanner;

public class switchcase {

	public static void main(String[] args) {
		int g;
		double ns,bs;
		Scanner in=new Scanner(System.in);
		PrintStream cout=System.out;
		cout.print("Enter the Salary: ");
		bs=in.nextDouble();
		cout.print("Enter the grade: ");
		g=in.nextInt();
		switch(g) {
		case 1:
			ns=bs;
			break;
		case 2:
			ns=bs+(bs*0.2);
			break;
		case 3:
			ns=bs+(bs*0.3);
			break;
		default:
			ns=bs+(bs*0.5);
			break;
		}
		System.out.print("The net salary is : "+ns);

	}

}
