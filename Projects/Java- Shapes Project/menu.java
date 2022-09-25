package shapesmanager;

import java.util.Scanner;

import shapesmanager.smanager.shapetypes;

public class menu {
	smanager sm=new smanager();
	public void mainmenu() {
		while(true) {
			int opt;
			Scanner in=new Scanner(System.in);
			System.out.print("\nSHAPES MANAGER\n");
			System.out.print("\n1.Add shapes");
			System.out.print("\n2.List shapes");
			System.out.print("\n3.Delete shapes");
			System.out.print("\n0.Exit\n");
			System.out.print("\nEnter your choice: ");
			opt=in.nextInt();
			switch(opt) {
			case 1:
				shapesmenu();
				break;
			case 2:
				sm.listshapes();
				break;
			case 3:
				sm.deleteshape();
				break;
			case 0:
				return;
			default:
				System.out.print("\nInvalid input... Try again...");
				
			}
			in.nextLine();
			in.nextLine();
		}
	
	}
	
	public void shapesmenu() {
		while(true) {
			int opt;
			Scanner in=new Scanner(System.in);
			System.out.print("\nADD SHAPES\n");
			System.out.print("\n1.Circle");
			System.out.print("\n2.Rectangle");
			System.out.print("\n3.Triangle");
			System.out.print("\n4.Cube");
			System.out.print("\n0.Main Menu\n");
			System.out.print("\nEnter your choice: ");
			opt=in.nextInt();
			switch(opt) {
			case 1:
				sm.addshapes(shapetypes.Circle);
				break;
			case 2:
				sm.addshapes(shapetypes.Rectangle);
				break;
			case 3:
				sm.addshapes(shapetypes.Triangle);
				break;
			case 4:
				sm.addshapes(shapetypes.Cube);
				break;
			case 0:
				System.out.print("\nPress Enter...");
				return;
			default:
				System.out.print("\nInvalid input... Try again...");
				
			}
			System.out.print("\nShape has been added successfully");
			in.nextLine();
			in.nextLine();
		}
	}
}
