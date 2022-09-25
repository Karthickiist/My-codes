package shapesmanager;

public class circle extends shapes{
private double radius;
	
	public circle() {
		shapetype="Circle";
	}

	@Override
	public void getinput() {
		getid();
		p.print("\nEnter the radius of the circle: ");
		radius=in.nextDouble();

	}

	@Override
	public double area() {
		sarea=(22/7.0)*radius*radius;
		return sarea;
	}

	@Override
	public String tostring() {
		String res=String.format("%10s  %5s  Area:%5.2f  Radius:%5.2f", shapetype, shapeid, area(), radius);
		return res;
	}

	@Override
	public String CDstring() {
		String res=String.format("%10s,%5s,%5.2f,%5.2f", shapetype, shapeid, area(), radius);
		return res;
	}
	
	public void deserialize(String text) {
		super.deserialize(text);
		String tokens[]=text.split(",");
		radius=Double.parseDouble(tokens[3]);
	}

}
