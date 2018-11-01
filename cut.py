from PIL import Image as img
#import Image as img
import os

imgTypes = ['.png','.jpg','.bmp']

horizon = 8
vertic  = 8
#crtFile[:crtFile.rindex('.')]
for root, dirs, files in os.walk('.'):
    for currentFile in files:
        crtFile = root + '\\' + currentFile
        #crtFile1 = os.path.join(root + '/1' )
        if crtFile[crtFile.rindex('.'):].lower() in imgTypes:
            crtIm = img.open(crtFile)
            crtW, crtH = crtIm.size
            hStep = crtW // horizon
            vStep = crtH // vertic
            for i in range(vertic):
                for j in range(horizon):
                    crtOutFileName = crtFile[:crtFile.rindex('.')] + \
                        '_' + str(i) + '_' + str(j)\
                        + crtFile[crtFile.rindex('.'):].lower()
                    box = (j * hStep, i * vStep, (j + 1) * hStep, (i + 1) * vStep)
                    cropped = crtIm.crop(box)
                    cropped.save(crtOutFileName)