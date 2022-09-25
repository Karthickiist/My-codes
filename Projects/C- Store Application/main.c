#include<stdio.h>
#include "items.h"
#include "txn.h"
void menu();
int main()
{
initialization();
menu();
}
void menu()
{
int opt;
while(1)
	{
	system("cls");
	printf("\nTIM HORTONS");
	printf("\n****Stock management****");
	printf("\n\n1.Add items");
	printf("\n2.List items");
	printf("\n3.Stock received entry");
	printf("\n4.Stock sold entry");
	printf("\n5.Stock list");
	printf("\n6.Stock transaction");
	printf("\n0.Exit");
	printf("\nEnter your option: ");
	scanf("%d",&opt);
	fflush(stdin);
	switch(opt)
		{
		case 1:
			additems();
			break;
		case 2:
			listitems();
			break;
		case 3:
			receivedentry();
			break;
		case 4:
			issueentry();
			break;
		case 5:
			stocklist();
			break;
		case 6:
			transaction();
			break;
		case 0:
			return;
			break;
		default:
			printf("\nInvalid input...Try again");
			break;	       
		}
	printf("\nPress enter...");
	getchar();
	}
}

