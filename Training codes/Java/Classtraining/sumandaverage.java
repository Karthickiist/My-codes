package Classtraining;
import java.util.Scanner;

public class sumandaverage {
	private int n;
	private double sum, avg;
	
	public int getn() {
		return n;
	}
	
	public double getsum() {
		return sum;
	}
	public double geravg() {
		return avg;
	}
	
	public void start() {
		int i,num;
		sum=0;
		Scanner in=new Scanner(System.in);
		System.out.print("How many numbers: ");
		n=in.nextInt();
		for(i=0;i<n;i++) {
			System.out.print("Enter a number: ");
			num=in.nextInt();
			sum=sum+num;
		}
		avg=sum/n;
		System.out.printf("The sum: %f The avg: %f", sum,avg);
		System.out.print("\nThere are "+n+" numbers");
	}
}
