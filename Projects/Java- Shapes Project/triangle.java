package shapesmanager;

public class triangle extends shapes{
private double base;
private double height;
	
	public triangle() {
		shapetype="Triangle";
	}

	@Override
	public void getinput() {
		getid();
		p.print("\nEnter the base of the Triangle: ");
		base=in.nextDouble();
		p.print("\nEnter the height of the Triangle: ");
		height=in.nextDouble();

	}

	@Override
	public double area() {
		sarea=(base*height)/2.0;
		return sarea;
	}

	@Override
	public String tostring() {
		String res=String.format("%10s  %5s  Area:%5.2f  Base:%5.2f  Height:%5.2f", 
				shapetype, shapeid, area(), base, height);
		return res;
	}

	@Override
	public String CDstring() {
		String res=String.format("%10s,%5s,%5.2f,%5.2f,%5.2f", shapetype, shapeid, area(), base, height);
		return res;
	}
	
	public void deserialize(String text) {
		super.deserialize(text);
		String tokens[]=text.split(",");
		base=Double.parseDouble(tokens[3]);
		height=Double.parseDouble(tokens[4]);
	}


}
