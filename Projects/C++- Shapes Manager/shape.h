namespace shapes
{
class shape{	
protected:
	int shapecode;
	char shapetype;
public:
	shape()
	{}
	virtual void input()=0;
	virtual float area()=0;
	virtual char *Tostring()=0;
};

class circle:public shape{
private:
	float ra,ar;
public:
	circle():shape()
		{
		shapetype='C';
		}
	void input();
	float area();
	char *Tostring();
};

class rectangle:public shape{
private:
	float wi,he,ar;
public:
	rectangle():shape()
		{
		shapetype='R';
		}
	void input();
	float area();
	char *Tostring();
};

class triangle:public shape{
private:
	float he,ba,ar;
public:
	triangle():shape()
		{
		shapetype='T';
		}
	void input();
	float area();
	char *Tostring();
};
}

