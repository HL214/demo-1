tp1 = ()
tp2 =("red",1,2,3)
print(tp1)
print(tp2)

print([y+str(x) for x in range(1,3) for y in 'abc'])

print([x+2 for x in range(1,11)])

lst = []
for x in range(1,11):
    lst.append(x+2)
print(lst)

def calf(a,b):
    add = a+b
    bbb = a-b
    cfe = a*b
    div = a/b
    return add,bbb,cfe,div
print(calf(3,2))

def student_lesson(grade,subject):
    z = "{}年级上{}课".format(grade,subject)