# Decoding_of_noisy_image
Using repetition codes to decode images having noise (error).

## Requirements

prerequisites to execute this application.  
Open windows terminal and type. . .

```bash
  pip install opencv-python
  pip install pillow
  pip install numpy
```

## Make changes to the image in the main function 

![image](https://user-images.githubusercontent.com/91364256/185785339-0568f875-a100-4cec-abab-a0bcc05460e5.png)

The resultant error-free images are located at 
[Decoding_of_noisy_image/resultant_images/]()

## Features 

It has been observed from the resultant images that as the order of repetition code
increases the channel noise is overcome with greater precision and accuracy, that is we 
can obtain an image nearly similar to the originally transmitted image with more parity 
information. Code rate can be automatically adjusted to varying channel capacity, but
the order of repetition code must be chosen keeping in mind the amount of the 
bandwidth it would cost.
The images transmitted through noisy channel are received with error. The order of 
repetition code is chosen according to the amount of error at the receivers end.

## Documentation

[Encoding_and_decoding_of_images.pdf](https://github.com/Dipp3r/Decoding_of_noisy_image/files/9388813/ITA_03.pdf)
