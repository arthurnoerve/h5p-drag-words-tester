
import imageio


images = []
for filename in range(1,6):
    
    images.append( imageio.imread(str(filename)+".png") )

imageio.mimsave('run.gif', images, duration=0.5)
