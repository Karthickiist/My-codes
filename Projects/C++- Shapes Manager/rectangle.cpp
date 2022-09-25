#include<iostream>
#include "shape.h"
using namespace std;
using namespace shapes;
void rectangle::input()
	{
	cout<<"\nRectangle...";
	cout<<"\nEnter shapecode: ";
	cin>>shapecode;
	cout<<"\nEnter the Height: ";
	cin>>he;
	cout<<"\nEnter the width: ";
	cin>>wi;
	}
float rectangle::area()
	{
	return wi*he;
	}
char *rectangle::Tostring()
	{
	char *s=new char[100];
	sprintf(s,"%d %c %f %f",shapecode, shapetype, wi, he, area());
	return s;
		
	}

