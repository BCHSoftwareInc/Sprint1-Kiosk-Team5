print ("What is your name?")
name = input()

print ("What is your organization?")
organization = input()

print ("What is your Email?")
Email = input()

print ("What is your access level?")
access = input()

print ("Issued by BCH Software")
issuer = "BCH software"

print ("+--------------------------------------------+")
print ("|           APEX ENTERTAINMENT PASS          |")
print ("|--------------------------------------------|")
print ("|   Attendee : " + name.ljust(30) + "|")
print ("|   Org : " + organization.ljust(35) + "|")
print ("|   Contact : " + Email.ljust(31) + "|")
print ("|   Access : " + access.ljust(32) + "|")
print ("|   Issuer : " + issuer.ljust(32) + "|")
print ("+--------------------------------------------+")
