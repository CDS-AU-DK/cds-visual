# Assignment 3 - Document classification using pretrained image embeddings

In Language Analytics so far, we've done lots of document classification based on linguistic features of documents. This week, we are working on a slightly different problem - can we predict what type of document we have based only on its *appearance* rather than its contents?

Think about how different documents look when written on a page. A poem appears differently to a newpaper article, both of which are different from a billboard advertisement. This assignment tries to leverage this knowledge to try to predict what type of document we have, based on its visual appearance.

For this assignment, we'll be working with the *```Tobacco3482```* dataset. You can learn more about this dataset in the original paper which uses it [here](https://dl.acm.org/doi/pdf/10.1145/1148170.1148307). The dataset we are working with is only a small subset of this larger corpus.

You should write code which does the following:

- Loads the *```Tobacco3482```* data and generates labels for each image
- Train a classifier to predict document type based on visual features
- Present a classification report and learning curves for the trained classifier
- Your repository should **also** include a short description of what the classification report and learning curve show.

## Data access

The data for the assignment is available in the shared drive on UCloud. For the purposes of this assignment, you can link to [this version](https://www.kaggle.com/datasets/patrickaudriaz/tobacco3482jpg?resource=download) in your README files.


## Tips
- The images are arranged into folders which have the label name for those images
- The training data comprises 3842 images across 10 different document types. Running code might be quite slow - be sure to plan accordingly.
- You should structure your project by having scripts saved in a folder called ```src```, and have a folder called ```out``` where you save the classification reports.

## Purpose

- To demonstrate that you can use ```tensorflow``` to train Convolutional Neural Networks
- To synthesize existing skills to create pipelines for transfer learning with pretrained CNNs
- To show understanding of how to interpret machine learning outputs