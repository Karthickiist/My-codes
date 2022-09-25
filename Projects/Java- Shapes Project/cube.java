package shapesmanager;

public class cube extends shapes{
	private double sides;
		
		public cube() {
			shapetype="Cube";
		}

		@Override
		public void getinput() {
			getid();
			p.print("\nEnter the sides of the Cube: ");
			sides=in.nextDouble();
		}

		@Override
		public double area() {
			sarea=6*(sides*sides);
			return sarea;
		}

		@Override
		public String tostring() {
			String res=String.format("%10s  %5s  Area:%5.2f  Sides:%5.2f", 
					shapetype, shapeid, area(), sides);
			return res;
		}

		@Override
		public String CDstring() {
			String res=String.format("%10s,%5s,%5.2f,%5.2f", shapetype, shapeid, area(), sides);
			return res;
		}
		
		public void deserialize(String text) {
			super.deserialize(text);
			String tokens[]=text.split(",");
			sides=Double.parseDouble(tokens[3]);
		}

}
