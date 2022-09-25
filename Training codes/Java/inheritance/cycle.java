package inheritance;

public class cycle extends vehicle{
	private int wheelcount;
	public cycle() {
		super();
		wheelcount=0;
	}
	public cycle(String make, String owner, String colour, double price, int wheelcount) {
		super(make, owner, colour, price);
		this.wheelcount=wheelcount;
	}
	
	public void display() {
		super.display();
		System.out.printf("\nWheelcount: %d", this.wheelcount);
	}

}
