package JavaTraining;

import java.io.PrintStream;
import java.util.Scanner;

public class areaofcircle {

	public static void main(String[] args) {
		double a;
		float r;
		Scanner in=new Scanner(System.in);
		PrintStream cout=System.out;
		cout.print("Enter the radius of the circle: ");
		r=in.nextFloat();
		a=(22/7.0)*r*r;
		cout.print("The area of the circle is "+a);
		
	}

}
