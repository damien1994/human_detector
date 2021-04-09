# Human_detector
Given the Dior - Eau de Parfum commercial, use any existing algorithms to generate a video that shows the existence of humans within the video by drawing boxes around them for each frame.

# Resources
https://thedatafrog.com/en/articles/human-detection-video/

https://github.com/vinay0410/Pedestrian_Detection/blob/master/detectmulti.py

https://www.pyimagesearch.com/2015/11/16/hog-detectmultiscale-parameters-explained/

https://medium.com/swlh/creating-your-own-custom-object-detector-using-transfer-learning-f26918697889

https://github.com/opencv/opencv/tree/master/data/haarcascades

# Results
### HOG (histogram of gradients) of open cv implementation ###
v1.0 - Hog implementation without hyperparameter tuning (winstride, padding, scale) : disappointing results

v1.1 - Hog implementation with hyperparameter tuning : a bit better but doesn't work well

v1.2 - Hog implementation with hyperparameter tuning and non maxima suppression : similar results with v1.1

### Use of haarcascade pre trained models from opencv ###
v2.0 - Use of fullbody haarcascade : bad results - similar with HOG implementation

v2.1 - Use of frontalface haarcascade : much better results but work only with faces and doesn't recognize a human body


# TO DO
1 - Package it

2 - Unit test

3 - Docstring and type inference

4 - Docker 

5 - Improve algo performance :
  - hyperparameter tuning of HOG opencv implementation (padding & scale)
  - implement non-maxima suppression
  - use pre trained open cv model haarcascade full body classifier  
  - implement a deep learning solution (use transfer learning)
  - test with only human faces detection ?

6 - Implement Github CI Actions