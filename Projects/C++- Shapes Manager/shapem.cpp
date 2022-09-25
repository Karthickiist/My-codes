#include<iostream>
#include<fstream.h>
#include "mains.h"
#include "menu.h"
#include "shape.h"
using namespace shapes;
using namespace MENU;
using namespace std;
using namespace MAIN;
void mains::start()
	{
	menu me;
	int opt;
	while(1)
		{
		system("cls");
		opt=me.mainmenu();
		switch(opt)
			{
			case 1:
				addshape();
				break;
			case 2:
				listshape();
				break;
			case 3:
				return;
			default:
				cout<<"\nInvalid imput...try again";
			}
		cin.ignore();
		cout<<"\nPress Enter key...";
		getchar();
		}
	
	}

void mains::addshape()
	{
	menu me;
	ofstream f;
	shape *s;
	int opt;
	while(1)
		{
		opt=me.shapemenu();
		switch(opt)
			{
			case 1:
				s=new circle();
				break;
			case 2:
				s=new rectangle();
				break;
			case 3:
				s=new triangle();
				break;
			case 0:
				return;
			default:
				cout<<"\nInvalid imput...try again";
				
			}
		s->input();
		f.open("./datas.txt",std::ios_base::app);
		f<<s->Tostring()<<endl;
		f.close();
		cout<<"\nShape added successfully.. Press Enter";
		cin.ignore();
		getchar();
		delete s;
		}
	}
	
void mains::listshape()
{
ifstream f;
string s;
f.open("./datas.txt");
while(!f.eof())
	{
	getline(f,s);
	cout<<endl<<s;
	}
f.close();
}

