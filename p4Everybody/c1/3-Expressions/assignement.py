# 2.3 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
# Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
#You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking or bad user data


# ask for hours

hrs = input("Enter Hours:")
fhours=float(hrs)

#ask for rate 

frate=float(input("Enter Rate per Hour:"))

# Do the calcul and print it
pay = frate* fhours
print( "Pay:",str(pay))
