package inheritance;

public abstract class vehicle {
private String make,owner,colour;
private double price;

public vehicle() {
	make="";
	owner="";
	colour="";
	price=0;
}

public vehicle(String make, String owner, String colour, double price) {
	this.make=make;
	this.colour=colour;
	this.price=price;
	this.owner=owner;
}

public void display() {
	System.out.printf("\nMake: %s",this.make);
	System.out.printf("\nowner: %s",this.owner);
	System.out.printf("\ncolour: %s",this.colour);
	System.out.printf("\nprice: %f",this.price);
	
}

abstract void sample();
}
