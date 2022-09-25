package Classtraining;

import java.util.Scanner;

public class backtext {
	private String s;
	private String res="";
	private int count;
	public void input() {
		Scanner in=new Scanner(System.in);
		System.out.print("Enter the String: ");;
		s=in.nextLine();
	}
	
	public String arrangetext() {
		int i;
		for(i=0;i<s.length();i++) {
			res=Character.toString((char)s.charAt(i))+res;
		}
		return res;
	}
}
