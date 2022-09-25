package JavaTraining;

import java.util.Scanner;

public class compoundinterest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner in=new Scanner(System.in);
		float p,r,n;
		double f,i;
		System.out.print("Enter the principal amount: ");
		p=in.nextFloat();
		System.out.print("Enter Rate of Interest:");
		r=in.nextFloat();
		System.out.print("Enter no of years: ");
		n=in.nextFloat();
		i=r/100.0;
		f=p*Math.pow((1+i),n);
		System.out.printf("The compound interest is %.2f", f);
		
	}

}
