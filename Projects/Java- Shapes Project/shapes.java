package shapesmanager;

import java.io.PrintStream;
import java.util.Scanner;

public abstract class shapes {
	protected PrintStream p=System.out;
	protected Scanner in=new Scanner(System.in);
	
	protected String shapetype;
	protected String shapeid;
	protected double sarea;
	
	abstract public void getinput();
	abstract public double area();
	abstract public String tostring();
	abstract public String CDstring();
	
	public void getid() {
		p.print("\nEnter shape id: ");
		shapeid=in.nextLine();
	}
	
	public void deserialize(String text) {
		String tokens[]=text.split(",");
		shapetype=tokens[0].trim();
		shapeid=tokens[1].trim();
		sarea=Double.parseDouble(tokens[2]);
		tokens=null;
	}

}
