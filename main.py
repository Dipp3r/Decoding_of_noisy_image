# import PIL
from PIL import Image
import cv2 as cv
import math as m
# import random as rand
import numpy as np

#image class having properties such as matrix,order,size 
# with member function to form matrix representation of the image 
class image():
    
    def __init__(self,filename):
        self.filename=filename
        self.image2=Image.open(filename)
        self.image2=self.image2.resize((200,200))
        self.image2.save(filename)
        self.image = cv.imread(filename,0)
        self.matrix=self.image.copy()
        self.matsize=self.image.size
        self.order=int(m.sqrt(self.matsize))
      
    def form_matrix(self):
        for i in range(self.order):
            for y in range(self.order):
                self.matrix[i][y]=int(round(self.image[i][y]/255))
        cv.imwrite("B&W_%s"%(self.filename),self.matrix*255)
        return self.matrix
    

#to display image
def show_image(filename,name):
    cv.imshow(filename,name)
    cv.waitKey(500)

#function to flip elements of the matrix 
def flip(image,probability):
    probability=probability/100
    matrix=image.form_matrix()
    flip=matrix.copy()
    n=np.random.randint(image.order,size=(int(image.order*image.order*probability),2))
    for x in n:
        i=x[0]
        j=x[1]
        if flip[i][j] == 0:
            flip[i][j]=1
        elif flip[i][j] == 1:
            flip[i][j]=0
    return(flip)

#function to add noise with probabilities 0.05,0.15,0.25 & 0.5
def add_Noise(img):
    for i in range(4):
        arr=[5,15,25,50]
        for x in range(1,max(3,5,7,9)+1):
            noisy_img=flip(img,arr[i])*255
            noisy_img=cv.resize(noisy_img,(200,200))
            cv.imwrite("noisy_images/error_%{e}/img{t}.png".format(e=arr[i],t=x),noisy_img)

def apply_repetition(img,redundancy): #redundancy is number of repetitions
    for i in range(4):
        arr=[5,15,25,50]
        resultant_noise=img.matrix.copy()*0
        for j in range(1,redundancy+1):
            noise=cv.imread("noisy_images/error_%{e}/img{t}.png".format(e=arr[i],t=j))/255
            for x in range(img.order):
                for y in range(img.order):
                    resultant_noise[x][y]+=int(round((noise[x][y][0]+noise[x][y][1]+noise[x][y][2])/3))
        for x in range(img.order):
            for y in range(img.order):
                resultant_noise[x][y]=int(round(resultant_noise[x][y]/redundancy))
        cv.imwrite("resultant_images/error_%{e}/R{i}.png".format(e=arr[i],i=redundancy),resultant_noise*255)
        


#main function 
if __name__ == "__main__":
    name="tom.png"
    img=image(name)
    img.form_matrix()
    add_Noise(img)
    for redundancy in range(3,10,2):
        apply_repetition(img,redundancy)
