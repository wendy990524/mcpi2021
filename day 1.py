from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat('X:'+str(x)+'Y:'+str(y)+'Z:'+str(z))e
    
    
    
x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z,89)
mc.setBlock(x,y,z,89)
mc.setBlock(x,y+1,z,89)
mc.setBlock(x,y+2,z,89)
mc.setBlock(x,y+3,z,89)
mc.setBlock(x,y+4,z,89)
mc.setBlock(x,y+5,z,89)
mc.setBlock(x,y+6,z,89)
mc.setBlock(x,y+7,z,89)
mc.setBlock(x,y+8,z,89)

x,y,z=mc.player.getTilePos()
mc.setBlock(x+1,y,z,46)
mc.setBlock(x-1,y,z,46)
mc.setBlock(x,y,z+1,46)
mc.setBlock(x,y,z-1,46)
mc.setBlock(x+1,y,z+1,46)
mc.setBlock(x-1,y,z+1,46)
mc.setBlock(x-1,y,z-1,46)
mc.setBlock(x+1,y,z-1,46)

x,y,z=mc.player.getTilePos()
mc.setBlocks(x+20,y,z+20,x-20,y,z-20,46)

import random
import time
x,y,z=mc.player.getTilePos()
while True:
    r=random.randrange(0,16)
    mc.setBlocks(x+3,y,z+3,x-3,y,z-3,35,r)
    time.sleep(0.5)





