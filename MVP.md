Hello Meta,

I'm writing to update you all on the progress of the GAN Project, "Entering the Metaverse." This is intended to be an MVP: taking my first pass through the model and adjusting as needed. This is a key step in the process, as it enables me to examine whether my current trajectory seems appropriate and effective.

Thusfar, I have 2 different images of myself as "content images" and 2 different NFT's as "style images," which are then passed through a GAN model. This model uses a pretrained VGG model, trained on imagenet.

Here is the first photo of myself that I used for this process:   
<img src="https://user-images.githubusercontent.com/73137112/143954979-be16fb1d-86ab-4710-9f6f-e20ce0bed489.jpeg" alt="Slack_Headshot" width="200"/>

Here are the 2 styling images utilized thus far:   
<img src="https://user-images.githubusercontent.com/73137112/143955012-f9275ac7-4c0b-49ee-b05d-bb0f64386a04.jpg" alt="Bored Ape" width="200"/>   
<img src="https://user-images.githubusercontent.com/73137112/143955017-620fbcc9-9e83-4cae-b4ae-e2d5061f2c48.png" alt="Mask" width="200"/>

Here is the result of combining my photo with each respective styling photo:   
<img src="https://user-images.githubusercontent.com/73137112/143955245-157d339a-1a8c-4a3a-8467-13e72643f392.png" alt="Mask" width="200"/>   
<img src="https://user-images.githubusercontent.com/73137112/143955161-801f3734-cf5e-4fb4-994c-f6eed7a64c7b.png" alt="Bored Ape" width="200"/>     

Then, I tried using a picture of myself with much less background noise:    
<img src="https://user-images.githubusercontent.com/73137112/143956070-cc4952e7-2652-4b49-8ae8-7bd9cf4939fe.jpg" alt="2nd Picture of Me" width="200"/>  

And combining it with the mask NFT, I had the following result:   
<img src="https://user-images.githubusercontent.com/73137112/143956181-6cdf0f18-69db-4efb-afce-bff8150aef44.png" alt="2nd Picture of Me" width="200"/>    

While there are signs of progress here, the goal of the project is not yet satisified: to create a hybrid of an NFT that can be used as a profile picture. These are too distorted and still don't capture the NFT itself.

Here are some ideas I will experiment with to try to accomplish my goal:   
-Vary iterations. Currently around 500 to 50,000, but maybe letting the model run for several hours could produce a better result.  
-Try feeding the model many different versions of the same NFT to see if it can generalize better that way.   
-Try to implement Cycle GAN model

I also want to take the following suggestions from Radford et al. paper and Francois Chollet's book on stabilizing GAN's (I gathered this all from https://www.pyimagesearch.com/2020/11/16/gans-with-keras-and-tensorflow/):    

**Radford**  
-Replace pooling layers with strided convolutions.  
-Batch normalization for both the generator and discriminator.  
-Use ReLU in generator except for the final layer, which will use tanh.  
-Use Leaky ReLU in the discriminator.  

**Chollet**   
-Sample random vectors from a normal distribution rather than uniform one.  
-Add dropout to discriminator.  
-Use a kernel size that is divisible by the stride in convulution layers in generator and discriminator (this will reduce checkboard pixel artifacts).   

Overall, I know I need many attempts of trial and error here, and I know that time will be a crunch, but I will attempt as many as I can before the deadline.

Best,

Michael
