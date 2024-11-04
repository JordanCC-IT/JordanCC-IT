#Operator	Name of Operation	Example	Description
#+	Addition	x + y	x plus y
#-	Subtraction	x - y	x minus y
#*	Multiplication	x * y	x multiplied by y
#**	Exponentiation	x ** y	x raised to the power of y
#/	Division	x / y	x divided by y
#//	Floor Division	x // y	x divided by y, returning integer
#%	Modulo	x % y	The remainder of x divided by y

#Operator	Example	Description
#=	x = 4	Assign 4 to x
#+=	x += 4	Add 4 to existing value of x
#-=	x -= 4	Subtract 4 from existing value of x
#*=	x *= 4	Multiply existing value by 4
#/=	x /= 4	Divide existing value by 4
#%=	x %= 4	Modulo existing value by 4

#Operator	Description	Example
#==	Equal to	x == y
#!=	Not equal to	x != y
#>	Greater than	x > y
#<	Less than	x < y
#>=	Greater than or equal to	x >= y
#<=	Less than or equal to	x <= y

x = 5
y = 2

print('arithmetic operator (x + y): ', x + y)
print('comparison operator (x >= y): ', x >= y)
print('logical operator (x == y and x > y): ', x == y and x > y)