
#############
#  IMPORTS  #
#############
import os

# build PyC4
os.system( "git submodule init" )
os.system( "git submodule update" )
os.system( "cd ./lib/PyC4/ ; python setup.py ;" )


#########
#  EOF  #
#########
