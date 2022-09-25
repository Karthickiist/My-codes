#include<iostream>
#include "shape.h"
using namespace std;
using namespace shapes;
void triangle::input()
	{
	cout<<"\ntriangle...";
	cout<<"\nEnter shapecode: ";
	cin>>shapecode;
	cout<<"\nEnter the Height: ";
	cin>>he;
	cout<<"\nEnter the base: ";
	cin>>ba;
	}
float triangle::area()
	{
	return ba*he;
	}
char *triangle::Tostring()
	{
	char *s=new char[100];
	sprintf(s,"%d %c %f %f",shapecode, shapetype, ba, he, area());
	return s;
		
	}

