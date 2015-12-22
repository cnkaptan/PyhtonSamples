my_name = "Cihan Kaptan"
my_age = 26
my_height = 168
my_weight = 66
my_eyes = 'brown'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." %my_name
print "He's %d inches tall." %my_height
print "He's %d pounds heavy." %my_weight
print "Actually that's not too heavy"
print "He's got %s eyes and %s hair." %(my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee." %my_teeth

print "If I add %d, %d, and %d I get %d." %(my_age,my_height,my_weight,my_age+my_height+my_weight)

print '%(language)s has %(#)03d quote types.' % \{'language': "Python", "#": 2}
