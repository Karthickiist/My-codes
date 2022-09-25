package Classtraining;

import java.util.Scanner;

public class ASCIItable {
	private String s;
	public void input() {
		Scanner in=new Scanner(System.in);
		System.out.print("Enter the String: ");;
		s=in.next();
	}
	
	public void asciitable() {
		int i,a;
		char c;
		System.out.print("Character  ASCII");
		for(i=0;i<s.length();i++) {
			c=(char)s.charAt(i);
			a=(int)c;
			System.out.printf("\n%9c  %5d", c,a);
		}
	}

}
