package Classtraining;

import java.util.Scanner;

public class fibo {
	private int n;
	public void input() {
		Scanner in=new Scanner(System.in);
		System.out.print("How many numbers: ");;
		n=in.nextInt();
	}
	public void fibbo() {
		if(n==1)
			System.out.print("1 ");
		else {
			int a=1,b=1,c;
			int count=1;
			System.out.print("1 ");
			while(count<n) {
				c=a+b;
				System.out.print(b+" ");
				a=b;
				b=c;
				count++;
			}
		}
			
	}

}
