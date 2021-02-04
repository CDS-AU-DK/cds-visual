# Syllabus Cultural Data Science - Visual #

## Overview ##

The purpose of the course is to enable students to conduct systematic computational analyses of visual objects such as paintings, photographs, archaeological artefacts, and digital products. Students will learn to understand the composition of collections of visual objects, and to apply statistical and machine learning methods for analysing them. The course will enable students to carry out projects within their primary subject area, and to reflect critically on others' analytical decisions. Students will also obtain the ability to present the result of their own analyses, and to visualize their results.

The course introduces basic programming and visualization skills for the systematic analysis of collections of visual materials. Students will learn how to develop research questions about visual materials, to structure research projects to address their research questions, and to apply computational tools in their projects to provide answers to their questions.

### Academic Objectives ###

In the evaluation of the student’s performance, emphasis is placed on the extent to which the student is able to:

1. Knowledge:
    * explain central theories underlying computational approaches to the analysis of visual objects
    * reflect on the creation, composition, and limitations of a data corpus of visual materials.
2. Skills:
    * develop a collection of visual materials for analysis
    * conduct large scale analyses of visual materials using computational methods
    * choose the appropriate visualization of results.
3. Competences:
    * independently reflect critically on the integration of hermeneutical-conceptual and quantitative-methodological choices for an analysis
    * apply acquired methods and procedures to topics from the student’s core field.

## Course Assessment ##
This course is graded. In order to proceed to the final exam (take-home project) at the first instance, you need to participate by submitting and peer-reviewing at least 5 out of 8 assignments to Blackboard.

### Participation ###
Answers to weekly questions or tasks will be required before the next session. You are welcome to either upload your code or link to a Github repo. You will be expected to peer review 2 submissions from your classmates.

Assignment will be graded on a 0 to 3 point scale based on a simple effort-focused rubric found on the course website. These are designed first and foremost to develop skills rather than “prove” you have learned concepts. I encourage you to communicate and work together, so long as you write and explain your code yourself and do not copy work wholesale. You can learn a lot from replicating others’ code but you will learn nothing if you copy it without knowing how it works.


## Schedule ##
Each course element (1-13) is a four hour session, consisting of a 1hr lecture, 1hr coding task explanation, and 2hrs code-along session.

1. Python exemplified with image processing
    * basic manipulation of images
    * image translation
2. Image processing with Python
    * color-channels and -space
    * histograms
3. Image processing with `OpenCV`
  * convolution kernels
4. Use cases: Face detection & handwriting recognition
5. Introduction to classical machine learning
6. Image classification with `scikit-learn`
7. Image classification with shallow neural networks
8. From shallow to deep learning
9. Image classification with convolutional neural networks
10. Out-of-the-box CNNs for classification
11. A CNN from scratch (or from `TensorFlow`)
12. Use cases: Style transfer & image embedding
13. Beyond CNNs & project proposals

## Reading ##
* You should acquire
  * M. Kirk, “Thoughtful Machine Learning with Python”

* Texts without download links [Download](https://drive.google.com/drive/folders/1MTRDFUPIA16zgNHoW1B1PaWxBzFHY2al?usp=sharing)

* Some readings are marked with `math` indicating that students with knowledge of basic calculus, probability theory, and linear algebra can benefit from this paper instead of the `introduction` paper. In those cases, both papers are therefore _not required_ reading.

#### Lesson 1 ####

#### Lesson 2 ####
- T. Arnold & L. Tilton (2019) "Distant viewing: analyzing large visual corpora," Digital Scholarship in the Humanities. pp 1-14.
- L. Manovich, 2012, How to compare one million Images? In Berry, D. M., Understanding Digital Humanities, pp. 249-78.

#### Lesson 3 ####
- V. Dumoulin and F. Visin, 2018, "A guide to convolution arithmetic for deep learning," arXiv:1603.07285 [cs, stat], Chp 1, [Download](http://arxiv.org/abs/1603.07285).
- T. Carvalho, 2020, "Basics of Kernels and Convolutions with OpenCV", [towards data science](https://towardsdatascience.com/basics-of-kernels-and-convolutions-with-opencv-c15311ab8f55)

#### Lesson 4 ####
@Students make sure you have read previous Readings for Lessons, otherwise you should catch up now before we start ML & DL.

- A. Ranjan, V. N. J. Behera, and M. Reza, (2020) "OCR using Computer Vision and Machine Learning," p. 24.
OR
- P. Fyfe and Q. Ge, 2018, "Image Analytics and the Nineteenth-Century Illustrated Newspaper," p. 25.
- M. Wevers and T. Smits, "Detecting Faces, Visual Medium Types, and Gender in Historical Advertisements, 1950–1995," in Computer Vision – ECCV 2020 Workshops, Cham, 2020, pp. 77–91.

#### Lesson 5 ####
- T. M. Mitchell, “Does Machine Learning Really Work?,”. [Download](https://www.aaai.org/ojs/index.php/aimagazine/article/view/1303).
- M. Kirk, “Thoughtful Machine Learning with Python,” chp 2

#### Lesson 6 ####
- M. Kirk, "Thoughtful Machine Learning with Python," chp 3
- `math` Hastie et al. The Elements of Statistical Learning - 2nd edition, chp 2. [Download](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)

#### Lesson 7 ####
- M. Kirk, "Thoughtful Machine Learning with Python,"", chp 8.

#### Lesson 8 ####
- M.A. Nielsen, 2015, Neural Networks and Deep Learning, Determination Press, chp 1 [Online](http://neuralnetworksanddeeplearning.com/chap1.html).
-  P. Madhu, R. Kosti, L. Mührenberg, P. Bell, A. Maier, and V. Christlein, “Recognizing Characters in Art History Using Deep Learning,” arXiv:2003.14171 [cs], Apr. 2020, [Download](https://arxiv.org/abs/2003.14171)

#### Lesson 9 ####
- Y. Lecun, L. Bottou, Y. Bengio, and P. Haffner, 1998, “Gradient-based learning applied to document recognition,” Proceedings of the IEEE, vol. 86, no. 11, pp. 2278–2324, [Download](http://yann.lecun.com/exdb/publis/pdf/lecun-98.pdf)
- `math` V. Dumoulin and F. Visin, 2018, "A guide to convolution arithmetic for deep learning," arXiv:1603.07285 [cs, stat], [Download](http://arxiv.org/abs/1603.07285).

#### Lesson 10 ####
- A. Krizhevsky, I. Sutskever, and G. E. Hinton, “ImageNet classification with deep convolutional neural networks,” Commun. ACM, vol. 60, no. 6, pp. 84–90, [Download](https://dl.acm.org/doi/10.1145/3065386)
- Z. Sabetsarvestani, B. Sober, C. Higgitt, I. Daubechies, and M. R. D. Rodrigues, 2019 “Artificial intelligence for art investigation: Meeting the challenge of separating x-ray images of the Ghent Altarpiece,” Sci. Adv., vol. 5, no. 8, p. eaaw7416, [Download](https://advances.sciencemag.org/content/5/8/eaaw7416)

#### Lesson 11 ####
- M.A. Nielsen, 2015, Neural Networks and Deep Learning, Determination Press, chp 6 [Online](http://neuralnetworksanddeeplearning.com/chap6.html).

#### Lesson 12 ####
- L. A. Gatys, A. S. Ecker, and M. Bethge, 2015, “A Neural Algorithm of Artistic Style,” arXiv:1508.06576 [cs, q-bio], [Download](http://arxiv.org/abs/1508.06576).
- K. Simonyan and A. Zisserman, "Very Deep Convolutional Networks for Large-Scale Image Recognition," arXiv:1409.1556 [cs], [Download]](http://arxiv.org/abs/1409.1556).

#### Lesson 13 ####
[NA]

### Additional Resources ###
- `basic programming` A. Sweigart, Automate the boring stuff with Python: practical programming for total beginners. San Francisco: No Starch Press, 2015, `python`, `basic programming`.
- `neural nets for dummies` M. Taylor, Make Your Own Neural Network: An In-depth Visual Introduction For Beginners. Independently published, 2017
- `math` D. Forsyth and J. Ponce, Computer Vision: A Modern Approach (International Edition), 2nd edition. Boston: Pearson Education, 2012.
- [Cultural Analytics Lab](http://lab.culturalanalytics.info/), `Cultural Analytics`, `visualization`.

## Slack Channel ##
We will use the "c-visual-analytics" channel for class-related communication. Please ask (and answer) questions in this Slack channel. If you are not in the CD Slack, sign up here [bit.ly/SlackForCDS](bit.ly/SlackForCDS). There is no such thing as a stupid or trivial question. If a colleague asks a question you know an answer to, try and answer. Slack is not only for instructor-student interaction, it is for all students to share knowledge and resources, and to get answers as fast as possible. Slack is best-suited for short technical questions and individual threads or channels for extended conversations on a given topic. 

### Rules of Slack: ###
1. use your github username or post.au.dk address to register and use the channel.
2. post on the general, spatial-analytics, or other relevant channel instead of direct messaging instructors.
3. use proper formatting: When asking questions involving code, please make sure to use inline code formatting for short bits of code or code snippets for longer, multi-line chunks
    - Formatting messages: https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages
    - Code snippets: https://get.slack.help/hc/en-us/articles/204145658-Creating-a-Snippet
4. For specific coding advise, please use minimal reproducible examples, e.g. https://stackoverflow.com/questions/5963269/how-to-make-a-great-r-reproducible-example


## Asking questions (on Slack, in class, and elsewhere) ##
1. Google It First! Google the error Python gives you. English language errors will have more solutions online.
2. Search existing online resources (Google, Stackexchange, etc.) and class discussion on Slack for answers. If the question has already been answered, you're done!
3. If it has already been asked but you're not satisfied with the answer, refine your question to get the answer you need, and add to the thread.
    - Document the questions you ask and the responses.
    - Give your question context from course concepts not course assignments
        - Good context: "I have a question on image transformation"
        - Bad context: "I have a question on HW 1 question 4"
    - Be precise in your description:
        - Good description: "I am getting the following error and I'm not sure how to resolve it - ```ImportError: No module named cv2```"
        - Bad description: "Python is giving me errors."
    - You can edit a question in Slack after posting it.

## Disability Resources ##
Your experience in this class is important to me. If you have already established accommodations with Special Educational Support (SES), please communicate your approved accommodations to me at your earliest convenience so we can discuss your needs in this course. If you have not yet established services through SES, but have a temporary health condition or permanent disability that requires accommodations (conditions include but not limited to; mental health, attention-related, learning, vision, hearing, physical or health impacts), you are welcome to contact 8716 2720 (Monday & Thursday 9-12, Tuesday 13-15) or email sps@au.dk .  SES offers resources and coordinates reasonable accommodations for students with disabilities and/or temporary health conditions. Reasonable accommodations are established through an interactive process between you, your instructor(s) and SES. It is the policy and practice of the Aarhus University to create inclusive and accessible learning environment and ensure that all students have the opportunity to educate themselves on equal terms even if they have a disability
