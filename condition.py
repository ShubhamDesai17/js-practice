import sys

type=sys.argv[1]
if type=="t2.ec2.micro":
    print("this is charge you 2$ / day")
elif type=="t2.ec2.medium":
    print("this charge you 4$/day")
else:
    print("this charge you for 8$/day")
