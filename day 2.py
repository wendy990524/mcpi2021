from mcpi.minecraft import Minecraft
mc=Minecraft.create()


x,y,z=mc.player.getTilePos()
mc.setBlocks(x,y,z,x+10,y+10,z+10,0)
mc.setBlocks(x+1,y+1,z+1,x+9,y+9,z+9,0)


import time

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock(x,y,z,175,4)
    time.sleep(1)
    

while True:
    x,y,z=mc.player.getTilePos()
    a=mc.getBlock(x+1,y-1,z)
    b=mc.getBlock(x-1,y-1,z)
    c=mc.getBlock(x,y-1,z+1)
    d=mc.getBlock(x,y-1,z-1)
    
    if a == 8 or a == 9 or b == 8 or b == 9 or c == 8 or c == 9 or d == 8 or d == 9:
        mc.setBlocks(x-1,y-1,z-1,x+1,y-1,z+1,20)


#海綿水壩
x,y,z=mc.player.getTilePos()
a=0
while a < 5:
    mc.setBlocks(x+10,y-1,z,x-5,y-5,z,19)
    z=z+5
    a=a+1


x,y,z=mc.player.getTilePos()
a=int(input('想放什麼方塊?'))
mc.setBlock(x,y,z,a)


name=input('enter your name:')
message=input('enter your message')
mc.postToChat('<'+name+'>'+message)



 
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,0,'water','','','canyon')   


while True:
    x,y,z=mc.player.getTilePos()
    a=mc.getBlockWithData(x,y-1,z)
    if a.data == 15:
        mc.postToChat('死路')
    if a.data == 11:
        mc.postToChat('turn right')




mc.postToChat("Block ID: " + str(block))

x,y,z=mc.player.getPos()
mc.spawnEntity(x,y,z,93)