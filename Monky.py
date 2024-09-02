from kanren import Relation, fact, conde, run, var

ItIs = Relation()
ItHas = Relation()
LiveIn = Relation() 

fact(ItIs,"Floki","bigger")
fact(ItIs,"Jason","small")
fact(ItIs,"vlady","bigger")
fact(ItIs,"macmir","big")
fact(ItIs,"Mikey","small")
fact(ItIs,"Floki","big")
fact(ItIs,"cesar","bigger")

fact(ItHas,"Floki","black")
fact(ItHas,"Jason","dark brown")
fact(ItHas,"vlady","brown")
fact(ItHas,"cesar","black")
fact(ItHas,"macmir","dark brown")
fact(ItHas,"Mikey","brown")

def gorilla(name):
    return conde((ItIs(name,"bigger"),ItHas(name,"brown")))


def baboon(name):
    return conde([ItHas(name,"dark brown")],[ItHas(name,"black")])

def chimpanzee(name):
    return conde((ItIs(name,"big"),ItHas(name,"black")))

def nasnas(name):
    return conde([ItIs(name,"small")],[ItHas(name," dark brown")])

def mandrill(name):
    return conde((ItIs(name,"bigger"),ItHas(name,"brown")))

x = var()
print("gorilla monky is {}".format((run(2,x,gorilla(x)))))

print("baboon monky is {}".format((run(3,x,baboon(x)))))

print("chimpanzee monky is {}".format((run(2,x,chimpanzee(x)))))

print("nasnas monky is {}".format((run(2,x,nasnas(x)))))

print("mandrill monky is {}".format((run(2,x,mandrill(x)))))

1



