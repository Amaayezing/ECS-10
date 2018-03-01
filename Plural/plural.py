#Maayez Imam 10/13/17
#Plural program

singular = str(input('Please enter a word: '))

def vowels(a, e, i, o, u):
    a = 'a'
    e = 'e'
    i = 'i'
    o = 'o'
    u = 'u'
    if singular.endswith(a):
        plural = singular + 's'
        print("The plural form of %s is %s." % (singular, plural))
    if singular.endswith(i):
        plural = singular + 's'
        print("The plural form of %s is %s." % (singular, plural))
    if singular.endswith(o):
        plural = singular + 's'
        print("The plural form of %s is %s." % (singular, plural))
    if singular.endswith(u):
        plural = singular + 's'
        print("The plural form of %s is %s." % (singular, plural))


if singular.endswith('ch'):
    plural = singular + 'es'
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('sh'):
    plural = singular + 'es'
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('s'):
    plural = singular + 'es'
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('x'):
    plural = singular + 'es'
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('z'):
    plural = singular + 'es'
    print("The plural form of %s is %s." % (singular, plural))

vowels('a', 'e', 'i', 'o', 'u')
#  if singular.endswith('a'):
    #  plural = singular + 's'
    #  print("The plural form of %s is %s." % (singular, plural))

#  if singular.endswith('e'):
    #  plural = singular + 's'
    #  print("The plural form of %s is %s." % (singular, plural))

#  if singular.endswith('i'):
    #  plural = singular + 's'
    #  print("The plural form of %s is %s." % (singular, plural))

#  if singular.endswith('o'):
    #  plural = singular + 's'
    #  print("The plural form of %s is %s." % (singular, plural))

#  if singular.endswith('u'):
    #  plural = singular + 's'
    #  print("The plural form of %s is %s." % (singular, plural))

# if singular.endswith('y'):
 #   plural = singular + 's'
  #  print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('f'):
    plural = singular.replace('f', 'ves')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('fe'):
    singular2 = singular[:-2]
    plural = singular2 + 'ves'
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('by'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('cy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('dy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('fy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('gy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('hy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('jy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('ky'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

#  if singular.endswith('ly'):
   # plural = singular.replace('y', 'ies')
    #  print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('my'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('ny'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('py'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('qy') :
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('ry'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('sy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('ty'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('vy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('wy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('xy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('zy'):
    plural = singular.replace('y', 'ies')
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('g'):
    plural = singular + 's'
    print("The plural form of %s is %s." % (singular, plural))

if singular.endswith('v'):
    plural = singular + 's'
    print("The plural form of %s is %s." % (singular, plural))

if singular == 'fly':
    plural = 'flies'
    print("The plural form of %s is %s." % (singular, plural))

if singular == 'toy':
    plural = 'toys'
    print("The plural form of %s is %s." % (singular, plural))

