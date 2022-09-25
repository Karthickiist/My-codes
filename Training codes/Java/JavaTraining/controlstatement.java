package JavaTraining;

import java.io.PrintStream;
import java.util.Scanner;

public class controlstatement {

	public static void main(String[] args) {
		int g;
		double ns,bs;
		Scanner in=new Scanner(System.in);
		PrintStream cout=System.out;
		cout.print("Enter the Salary: ");
		bs=in.nextDouble();
		cout.print("Enter the grade: ");
		g=in.nextInt();
		if(g==1)
			ns=bs;
		else if(g==2)
			ns=bs+(bs*0.2);
		else if(g==3)
			ns=bs+(bs*0.3);
		else
			ns=bs+(bs*0.5);
		cout.print("The net salary is: "+ns);
	}

}
