import numpy
from PIL import Image

for dim in {16, 48, 128}:
    imarray = numpy.random.rand(dim,dim,3) * 255
    im = Image.fromarray(imarray.astype('uint8')).convert('RGBA')
    im.save(f'images/icon{dim}.png')
