#include<iostream>
#include "shape.h"
using namespace std;
using namespace shapes;
void circle::input()
	{
	cout<<"\nCircle...";
	cout<<"\nEnter shapecode: ";
	cin>>shapecode;
	cout<<"\nEnter the radius: ";
	cin>>ra;
	}
float circle::area()
	{
	return (22/7.0)*ra*ra;
	}
char *circle::Tostring()
	{
	char *s=new char[100];
	sprintf(s,"%d %c %f %f",shapecode, shapetype, ra, area());
	return s;
		
	}

