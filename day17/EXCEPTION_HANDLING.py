'''1. names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'].
Unpack the first five countries and store them in a variable nordic_countries,
store Estonia and Russia in es, and ru respectively.'''

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
fin, sw, nor, den, ice, *others = names
es, ru = others

nordic_countries = [fin, sw, nor, den, ice]
print("Nordic Countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)

