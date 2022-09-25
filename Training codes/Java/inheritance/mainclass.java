package inheritance;

import inheritance.car.FuelType;

public class mainclass {

	public static void main(String[] args) {
		interfce v=null;
		
		car c=new car("Bens","Karthick","Black",40000,3,FuelType.diesel);
		v=c;
		
		v.smaple2();
	}

}
