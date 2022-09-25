#include<stdio.h>
#include "items.h"
#include "txn.h"
char file[]="./storeitems.bin";
int count;
items it1[50];
items it;
void additems()
{
FILE *f;
f=fopen(file,"ab");
printf("\nEnter item code: ");
scanf("%d",&it.code);
fflush(stdin);
printf("\nEnter item name: ");
gets(it.name);
fwrite(&it, sizeof(items),1,f);
fclose(f);
printf("\nItem added successfully..");
initialization();
}

void initialization()
{
FILE *f;
f=fopen(file,"rb");
count=0;
while(fread(&it, sizeof(items),1,f))
	{
	it1[count].code=it.code;
	strcpy(it1[count].name,it.name);
	count++;
	}
fclose(f);
}

void listitems()
{
int i;
system("cls");
printf("\n***Items list***");
for(i=0;i<count;i++)
	{
	printf("\n%3d  %-10s",it1[i].code,it1[i].name);
	}
}

int getname(int code, char *name)
{
int i;
int res=0;
for(i=0;i<count;i++)
	{
	if(it1[i].code==code)
		{
		res=1;
		strcpy(name,it1[i].name);
		break;
		}
	}
return res;
}

void stocklist()
{
int i;
int qty;
for(i=0;i<count;i++)
	{
	qty=getqty(it1[i].code);
	printf("\n%2d %-10s     %-5d",it1[i].code,it1[i].name,qty);
	}	 
}

