package Classtraining;

import java.util.Scanner;

public class interactive {
	private int n;
	public boolean prime(int n) {
		if(n==1)
			return true;
		else {
			int count=0;
			for(int i=1;i<=n;i++) {
				if(n%i==0)
					count++;
			}
			if(count==2)
				return true;
			else
				return false;
		}
	}
	
	public boolean fibo(int n) {
		if(n==1)
			return true;
		else {
			int a,b,c;
			a=1;
			b=1;
			c=a+b;
			while(c<n) {
				a=b;
				b=c;
				c=a+b;
			}
			if(c==n)
				return true;
			else
				return false;
		}
	}
	
	public void input() {
		Scanner in=new Scanner(System.in);
		System.out.print("\nEnter the number: ");
		n=in.nextInt();
	}
	
	public void display() {
		do {
			input();
			if(fibo(n)==true)
				System.out.print("The number is fibbonoaci number..");
			else
				System.out.print("The number is not fibbonoaci number..");
			if(prime(n)==true)
				System.out.print("The number is prime number..");
			else
				System.out.print("The number is not prime number..");
		}while(n!=0);
	}

}
