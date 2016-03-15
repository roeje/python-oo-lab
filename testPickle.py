import cPickle as pickle


favorite_color = { "lion": "yellow", "kitty": "red" }


pickle.dump( favorite_color, open( "save.p", "wb" ) )
print "Dump done"

favorite_color2 = pickle.load( open( "save.p", "rb" ) )

print "load done"

print favorite_color2