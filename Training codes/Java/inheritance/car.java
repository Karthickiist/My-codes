package inheritance;

public class car extends vehicle implements interfce{
	enum FuelType{petrol, diesel};
	private FuelType fueltype;
	private int gears;
	public car() {
		super();
		gears=0;
	}
	
	public car(String make, String owner, String colour, double price, int gears, FuelType fueltype) {
		super(make, owner, colour, price);
		this.fueltype=fueltype;
		this.gears=gears;
	}
	
	public void display() {
		super.display();
		System.out.printf("\ngears: %d", this.gears);
		System.out.printf("\nFuel: %s", this.fueltype);
	}

	@Override
	void sample() {
		System.out.print("\nHello world...");
		
	}

	@Override
	public void smaple2() {
		// TODO Auto-generated method stub
		System.out.print("\nHello world 2...");
	}
}
