package arrays;

import java.util.Scanner;

public class arrays {
	private int min,max,tot,avg;
	int[][] a=new int[3][3];
	public arrays() {
		
		Scanner in=new Scanner(System.in);
		for(int i=0;i<3;i++) {
			System.out.print("\nEnter row "+i);
			for(int j=0;j<3;j++) {
				a[i][j]=in.nextInt();
			}
		}
	}
	
	public void analysis() {
		System.out.print("\nValue1 value2 value3 min max tot avg\n");
		for(int[] i:a) {
			min=i[0];
			max=i[0];
			for(int j:i) {
				System.out.printf("%6d ", j);
				if(j<min)
					min=j;
				if(j>max)
					max=j;
				tot=tot+j;
				
			}
			System.out.printf("%3d %3d %3d %3d\n"
					+ "",min,max,tot,(tot/3));
		}
	}

}
