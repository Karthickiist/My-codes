package shapesmanager;

public class rectangle extends shapes{
	private double width;
	private double height;
		
		public rectangle() {
			shapetype="Rectangle";
		}

		@Override
		public void getinput() {
			getid();
			p.print("\nEnter the width of the Rectangle: ");
			width=in.nextDouble();
			p.print("\nEnter the height of the Rectangle: ");
			height=in.nextDouble();

		}

		@Override
		public double area() {
			sarea=width*height;
			return sarea;
		}

		@Override
		public String tostring() {
			String res=String.format("%10s  %5s  Area:%5.2f  width:%5.2f  Height:%5.2f", 
					shapetype, shapeid, area(), width, height);
			return res;
		}

		@Override
		public String CDstring() {
			String res=String.format("%10s,%5s,%5.2f,%5.2f,%5.2f", shapetype, shapeid, area(), width, height);
			return res;
		}
		
		public void deserialize(String text) {
			super.deserialize(text);
			String tokens[]=text.split(",");
			width=Double.parseDouble(tokens[3]);
			height=Double.parseDouble(tokens[4]);
		}

}
