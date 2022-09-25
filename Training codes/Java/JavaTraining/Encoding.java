package JavaTraining;

import java.util.Scanner;

public class Encoding {

	public static void main(String[] args) {
		String a;
		String re="";
		Scanner in=new Scanner(System.in);
		System.out.print("Enter the string: ");
		a=in.nextLine();
		re+=Character.toString((char)a.charAt(0)-1);
		re+=Character.toString((char)a.charAt(1)-1);
		re+=Character.toString((char)a.charAt(2)-1);
		re+=Character.toString((char)a.charAt(3)-1);
		re+=Character.toString((char)a.charAt(4)-1);
		System.out.print("The encoded string is : "+re);
	}

}
