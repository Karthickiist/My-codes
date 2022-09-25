package shapesmanager;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class smanager {
	ArrayList<shapes> shape=new ArrayList<shapes>();
	String filename="./datas.txt";
	public enum shapetypes{Triangle,Rectangle,Cube,Circle};
	Scanner in=new Scanner(System.in);
	public void addshapes(shapetypes shapetype) {
		shapes s=null;
		switch(shapetype) {
		case Triangle:
			s=new triangle();
			break;
		case Rectangle:
			s=new rectangle();
			break;
		case Circle:
			s=new circle();
			break;
		case Cube:
			s=new cube();
			break;
		default:
			System.out.print("Invalid input... Try again...");
		}
		s.getinput();
		shape.add(s);
		writetofile(s);
		s=null;
	}
	
	public void writetofile(shapes s) {
		FileWriter f=null;
		try{
			f=new FileWriter(filename,true);
			BufferedWriter bw=new BufferedWriter(f);
			bw.write(s.CDstring());
			bw.write("\n");
			bw.close();
			f.close();
			bw=null;
		}catch(Exception ex) {
			ex.printStackTrace();
		}
		finally {
			f=null;
		}
		
	}

	public void listshapes() {
		for(shapes s:shape) {
			System.out.printf(s.tostring());
			System.out.print("\n");
		}
	}
	
	public smanager() {
		boolean ffound=new File(filename).isFile();
		if(ffound) {
			FileReader f=null;
			try {
				f=new FileReader(filename);
				BufferedReader br= new BufferedReader(f);
				String text;
				shapes s=null;
				while((text=br.readLine())!=null) {
					String token[]=text.split(",");
					switch(token[0].trim()) {
					case "Rectangle":
						s=new rectangle();
						break;
					case "Triangle":
						s=new triangle();
						break;
					case "Cube":
						s=new cube();
						break;
					case "Circle":
						s=new circle();
						break;
					default:
						break;
					}
					s.deserialize(text);
					shape.add(s);
				}
				br.close();
				f.close();
				br=null;
				s=null;
			}catch(Exception ex) {
				ex.printStackTrace();
			}
			finally {
				f=null;
			}
		}
	}

	public shapes getshape(String shapeid) {
		shapes s=null;
		for(shapes a:shape) {
			if(shapeid.equals(a.shapeid)) {
				s=a;
			}
		}
		return s;
	}

	public void deleteshape() {
		String id;
		System.out.print("\nEnter shape id:  ");
		id=in.nextLine();
		shapes s=null;
		s=getshape(id);
		if(s==null) {
			System.out.print("\nShape not found...");
			return;
		}
		shape.remove(s);
		FileWriter f=null;
		try{
			f=new FileWriter(filename);
			BufferedWriter bw=new BufferedWriter(f);
			for(shapes a:shape) {
				bw.write(a.CDstring());
				bw.write("\n");
			}
			bw.close();
			f.close();
			bw=null;
		}catch(Exception ex) {
			ex.printStackTrace();
		}
		finally {
			f=null;
		}
	System.out.print("\nShape has been successfully removed from the database...");
	}
}
