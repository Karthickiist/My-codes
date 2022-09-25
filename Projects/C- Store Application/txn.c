#include<stdio.h>
#include "txn.h"
char files[]="./txn.bin";
void receivedentry()
{
FILE *f;
txn t;
int check;
char name[20];
char res;
f=fopen(files,"ab");
printf("\nEnter product code: ");
scanf("%d",&t.code);
fflush(stdin);
check=getname(t.code,name);
if(check)
	{
	printf("\nItem name: %s",name);
	printf("\nDo you want to proceed (Y/N): ");
	res=getchar();
	fflush(stdin);
	if(res=='Y')
		{
		t.type= 'r';
		printf("\nEnter the quantity: ");
		scanf("%d",&t.qty);
		fflush(stdin);
		fwrite(&t,sizeof(txn),1,f);
		printf("\nRecipt entered successfully");
		}
	}
else
	{
	printf("\nItem not fount... Check item code...");
	}
fclose(f);
}

void issueentry()
{
FILE *f;
txn t;
int check;
char name[20];
char res;
f=fopen(files,"ab");
printf("\nEnter product code: ");
scanf("%d",&t.code);
fflush(stdin);
check=getname(t.code,name);
if(check)
	{
	printf("\nItem name: %s",name);
	printf("\nDo you want to proceed (Y/N): ");
	res=getchar();
	fflush(stdin);
	if(res=='Y')
		{
		t.type= 'i';
		printf("\nEnter the quantity: ");
		scanf("%d",&t.qty);
		fflush(stdin);
		fwrite(&t,sizeof(txn),1,f);
		printf("\nIssue entered successfully");
		}
	}
else
	{
	printf("\nItem not fount... Check item code...");
	}
fclose(f);
}


void transaction()
{
FILE *f;
txn t;
int check,code1;
char name[20];
char res;
int tot1, tot2;
tot1=0,tot2=0;
f=fopen(files,"rb");
printf("\nEnter product code: ");
scanf("%d",&code1);
fflush(stdin);
check=getname(code1,name);
if(check)
	{
	printf("\nItem name: %s",name);
	printf("\nDo you want to proceed (Y/N): ");
	res=getchar();
	fflush(stdin);
	if(res=='Y')
		{
		system("cls");
		printf("\nItem name: %s",name);
		while(fread(&t,sizeof(txn),1,f))
			{
			if(t.code==code1)
				{
				if(t.type== 'r')
					{
					printf("\nRecipt  %-5d",t.qty);
					tot1=tot1+t.qty;
					}
				else
					{
					printf("\nIssue          %-5d",t.qty);
					tot2=tot2+t.qty;
					}
				}
			}
		}
	}
else
	{
	printf("\nItem not fount... Check item code...");
	}
printf("\n      --------------------");
printf("\n        %-5d  %-5d",tot1,tot2);
printf("\n      --------------------");
fclose(f);
printf("\nIn stock: %d",tot1-tot2);

}

int getqty(int code)
{
FILE *f;
txn t;
int tot1=0,tot2=0;
int total;
f=fopen(files,"rb");
while(fread(&t,sizeof(txn),1,f))
			{
			if(t.code==code)
				{
				if(t.type== 'r')
					{
					tot1=tot1+t.qty;
					}
				else
					{
					tot2=tot2+t.qty;
					}
				}
			}
total=tot1-tot2;
fclose(f);
return total;
}

