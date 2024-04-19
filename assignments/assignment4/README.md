# Assignment 4 - Detecting faces in historical newspapers

If you have ever looked at old newspapers, you might notice that they are very verbose. There is a lot of text, perhaps some illustrations - but, ultimately, they are very text heavy data sources. However, this begins to change in the 19th century with the advent of new technology and with the adoption of personal cameras in the 20th century, images become increasingly dominant.

In this assignment, we're going to build on this idea to look for changing patterns in print media. Specifically, we are going to look at the presence in historical newspapers of *pictures of human faces*. This is a culturally meaningful question - how has the prevelance of images of human faces changed in print media over the last roughly 200 years? Are there any significant differences and what might this mean?

We're going to work with a corpus of historic Swiss newspapers: the *Journal de Genève* (JDG, 1826-1994); the *Gazette de Lausanne* (GDL, 1804-1991); and the Impartial (IMP, 1881-2017). You can read more about this corpus in the associated reserch article (linked to below).

You should write code which does the following:

- For each of the three newspapers
    - Go through each page and find how many faces are present
    - Group these results together by *decade* and then save the following:
        - A CSV showing the total number of faces per decade and the percentage of pages for that decade which have faces on them
        - A plot which shows the latter information - i.e. percentage of pages with faces per decade over all of the decades avaiable for that newspaper
- Repeat for the other newspapers

Finally, remember your repository should include a writtens summary and interpretation of what you think this analysis might being showing. You do not need to be an expert in the history of printed Swiss media - just describe what you see and what that might mean in this context. Make sure also to mention any possible limitations of your approach!


## Starter code

For this task, we are going to use a pretrained CNN model which has been finteuned for face detection. You can see documentation of this model and some starter code about how to get it running at [this website](https://medium.com/@danushidk507/facenet-pytorch-pretrained-pytorch-face-detection-mtcnn-and-facial-recognition-b20af8771144). In particular, you'll want to use the first code block down to the line which detects faces in images:

```python
from facenet_pytorch import MTCNN, InceptionResnetV1
import torch
from PIL import Image

# Initialize MTCNN for face detection
mtcnn = MTCNN(keep_all=True)

# Load pre-trained FaceNet model
resnet = InceptionResnetV1(pretrained='casia-webface').eval()

# Load an image containing faces
img = Image.open('path_to_image.jpg')

# Detect faces in the image
boxes, _ = mtcnn.detect(img)
```

The shape of the variable ```boxes``` can then be used to tell you how many faces are on the page.

## Data access

The data for the assignment is available in the shared drive on UCloud. For the purposes of this assignment, you can link to [this version](https://zenodo.org/records/3706863) in your README files.

## Tips

- Notice that the filenames contain the name of the newspaper, and the year-month-date of publication. This will be useful for you!

## Purpose

- To demonstrate that you can pretrained CNNs to extract meaningful information from image data
- To convey the kinds of datasets and problems encountered doing image processing for cultural analytics
- To show understanding of how to interpret machine learning outputs