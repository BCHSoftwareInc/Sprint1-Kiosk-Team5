print ("What is your name?")
name = input()
print (name)

print ("What is your organization?")
organization = input()
print (organization)

print ("What is your Email?")
Email = input()
print (Email)

print ("What is your access level?")
access = input()
print (access)

print ("Who is your issuer?")
issuer = input()
print (issuer)

print ("+--------------------------------------+")
print ("|        APEX ENTERTAINMENT PASS       |")
print ("|--------------------------------------|")
print ("|   Attendee : " + name.ljust(24) + "|")
print ("|   Org : " + organization.ljust() + "|")
print ("|   Contact : " + Email + "|")
print ("|   Access : " + access + "|")
print ("|   Issuer : " + issuer + "|")
print ("+--------------------------------------+")
