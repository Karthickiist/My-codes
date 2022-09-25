package Classtraining;

import java.util.Scanner;

public class stringencrypt {
	private String s,res="";
	
	public void input() {
		Scanner in=new Scanner(System.in);
		System.out.print("Enter the String: ");;
		s=in.next();
	}
	
	public void encryption() {
		int i,count;
		count=s.length();
		for(i=0;i<count;i++) {
			res+=Character.toString((char)(s.charAt(i)-1));
		}
	}
	public String inputstring() {
		return s;
	}
	public String encryptedstring() {
		return res;
	}

}
