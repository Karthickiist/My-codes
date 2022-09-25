package Classtraining;

import java.util.Scanner;

public class sinx {
	private int x,n;
	private double sin=0;
	public void input() {
		Scanner in=new Scanner(System.in);
		System.out.print("\nEnter the value of N: ");
		n=in.nextInt();
		System.out.print("\nEnter the value of X: ");
		x=in.nextInt();
	}
	
	public void sinxcal() {
		int mf=1;
		for(int i=1,k=1;i<=n;i++,k+=2) {
			int fact=1;
			for(int j=1;j<=k;j++) {
				fact=fact*j;
			}
			sin=sin+(((mf)*Math.pow(x,k))/fact);
			mf=mf*(-1);
			
		}
		System.out.print("The sin value is "+sin);
	}
}
