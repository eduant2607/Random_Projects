#I had to downlad the imageio libraries through pip so I could
#import the modules
import imageio.v3 as iio

#In here we add the names of our image files
filenames = ['Snorlax1.3.png', 'Snorlax3.png']
images = [ ]

#The for loop will walk through the files listed in filenames list
#later thanks to the imread, the images will be processed, and thanks
#to the .append we can add it into our images list
for filename in filenames:
    images.append(iio.imread(filename))

#this is useful to creat the new file! the duration is in milisecons

iio.imwrite('MoveSnorlax.gif', images, duration = 500, loop = 0)