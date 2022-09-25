typedef struct transaction{
int qty;
char type;
int code;
}txn;

void receivedentry();
void issueentry();
void storeitems();

int getname(int, char *);
int getqty(int);

