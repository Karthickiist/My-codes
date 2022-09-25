package Classtraining;

import java.util.Scanner;

public class primenumbers {
	private int n;
	public void input() {
		Scanner in=new Scanner(System.in);
		System.out.print("How many numbers: ");;
		n=in.nextInt();
	}
	
	public void primetable() {
		System.out.print("Count  Prime Number");
		System.out.print("\n-------------------\n");
		if(n==1)
			System.out.printf("%5c  %10c",'1','1');
		else {
			int count,ini=2,counts=1;
			System.out.printf("\n%5c  %10c",'1','1');
			while(counts<n) {
				count=0;
				for(int i=1;i<=ini;i++) {
					if(ini%i==0) {
						count++;
					}
				}
				if(count==2) {
					counts++;
					System.out.printf("\n%5d  %10d", counts,ini);
				}
				ini++;
			}
		}
	}

}
