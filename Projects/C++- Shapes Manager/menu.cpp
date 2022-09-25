#include<iostream>
#include "menu.h"
using namespace std;
using namespace MENU;
int menu::mainmenu()
	{
	cout<<"\n***SHAPES MANAGER***"<<endl;
	cout<<"\n1.Add Shapes";
	cout<<"\n2.List Shapes";
	cout<<"\n3.Exit";
	cout<<endl<<endl<<"Enter your option: ";
	cin>>selection;
	return selection;
	}
int menu::shapemenu()
	{
	system("cls");
	cout<<"\n1.Circle";
	cout<<"\n2.Rectangle";
	cout<<"\n3.Triangle";
	cout<<"\n0.Main menu..";
	cout<<endl<<endl<<"Enter your option: ";
	cin>>selection;
	return selection;
	}

