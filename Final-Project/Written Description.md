# Creating Human-NFT Hybrids Using Neural Style Transfer Models
Michael Kamel

## Abstract
The goal of this project was to utilize a Neural Style Transfer Model, as described by [Leon A. Gatys](https://arxiv.org/abs/1508.06576), to fuse a person's face with their profile picture NFT. Specifically, I chose to use Crypto Punks after some initial testing. By tuning a set of hyperparameters, I was able to create a promising yet unfulfilled output when combining the NFT with a picture of my face. More work will need to be done regarding the model's architecture and/or hyperparameters. However, the model worked successfully on transferring an art style, specifically Starry Night, to a person's face.

## Design
The recent NFT boom is continuing to grow -- according to [CNBC](https://www.cnbc.com/2021/10/06/nft-trading-volume-hit-10-billion-2-reasons-why-people-are-buying.html), Q3 of 2021 presented an NFT trading volume of $10.67 billion, a 704% increase from the previous quarter. While NFT’s have many use cases and will continue to expand down exciting paths, my project is targeted toward Art NFT’s, specifically profile picture Art NFT's, which I believe are the primary driver of this initial movement. These are most of the prominent NFT’s you may have heard of: Crypto Punks, Bored Apes, World of Women, etc… These are NFT’s that have, amongst other things, give users a sense of community and identity. I want to take it a step further, by enabling the users to combine themselves with that NFT they identify with. In some way, I feel that this would bridge the gap even more and enable the user to feel that they are entering the metaverse.

## Data
The Neural Style Transfer model actually only needs 2 pictures – a content picture and a style picture. Then, by a process of convolutions, pooling, fusion, and decompression of the fused pooling layer, the model can output a new, combined image, taking the content picture and applying the style of the style picture. For my style pictures, I chose to use a baseline picture of Starry Night by Van Googh that I knew would have success (given the many examples of using this). Then, after testing many various profile picture NFT’s, I choose to use Crypto Punks due to their structure and simplicity. For my content picture, I used a headshot of myself with minimal noise (hat to cover hair, no background, close up, etc…).

## Algorithms
The algorithm used for this problem was the Neural Style Transfer model. While there are many hyperparameters to investigate and tune, the primary ones to focus on were the optimizer's alpha (learning rate) and the model’s content and style weights (how transformations are applied). Other hyperparameters considered were the optimizers Beta_1 and Beta 2, its epsilon, and whether to utilize AMSgrad convergence. Future work could include investigating the type of optimizer selected for this model (using L-BFGS instead of Adam) and the architecture of the model (types of layers, amount of layers, etc…). In terms of the Starry Night style, given the fact that the model was designed for that specific task, the baseline hyperparameters worked well. In terms of the Crypto Punk style, I found the most success tuning down the content weight from 100 to 10 and the style weight from .01 to .001. However, I believe that more tuning of these weights in combination with the learning rates and model iterations could have continued to improve results.

## Tools
**Numpy** - Data Preparation Tool  
**TensorFlow** - Deep Neural Network software library   
**Keras** - Python library utilize as an interface for TensorFlow  
**Matplotlib** - Data visualization tools  

## Communication
After building and testing my model, I shared my findings with my cohort via this [presentation]().
