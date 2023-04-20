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
The exam consists of a portfolio containing a number of assignments. The portfolio will consist of 3-7 assignments.
The number of assignments as well as their form and length will be announced at the start of the semester. The portfolio may include products. Depending on their length, and subject to the teacher’s approval, these products can replace some of the standard pages in the portfolio.

### Participation ###
Students will be expected to complete the in-class assignments in order to progress to the examination. These assignments are designed first and foremost to develop skills rather than “prove” you have learned concepts. 

I encourage you to communicate and work together, so long as you write and explain your code yourself and do not copy work wholesale. You can learn a lot from replicating others’ code but you will learn nothing if you copy it without knowing how it works.


## Schedule ##
Each course element (1-13) is a four hour session, consisting of a two-hour lecture 1hr and a two-hour code-along session.


|Week  | Session | Lecture | Classroom  |Reading |
| :---: | :-----: | ----------| -------| ---|
|  5    |    1    | Introducing Visual Analytics         | Thinking about images with Python        | NO ASSIGNED READINGS                              |
|  6    |    2    | Basic image processing               | Exploring colour channels                | *Arnold & Tilton (2019)*                          |
|  7    |    3    | More image processing                | Comparing colour histograms              | *Manovich(2012)*                                  |
|  8    |    4    | Convolutional kernels                | Thresholds and blurring                  | *Wevers & Smits (2020)*                           |
|  9    |    5    | Image classification 1               | Logistic Regression w/ Scikit-Learn      | *Mitchell (1997), VanderPlas (2016), chapter 5*   |
|  10   |    6    | Image classification 2               | Simple neural networks                   | *Nielsen (2015), Chapter 2&3*                     |
|  11   |    7	  | From shallow to deep learning        | Introducing TensorFlow                   | *Nielsen (2015), Chapter 5                        |
|  12   |    -	  | CANCELLED DUE TO ILLNESS        | CANCELLED DUE TO ILLNESS         | -- |
|  13   |    8    |Convolutional Neural Networks        | Building ConvNets w/ Tensorflow   | *Krizhevsky et al. (2017)                                        |
|  14   |         | *NO TEACHING*                        | *NO TEACHING*                            | *NO ASSIGNED READINGS*                            |
|  15   |    9    | Pretrained CNNs and transfer learning| Search algorithm with image embeddings   | *Madhu et al (2020), Tarp & Kristensen-McLachlan (2022)* |
|  16   |   10    | More on image embeddings             |Image search                           | *Gatys et al. (2015)*                             |
|  17   |   11    | Project presentations                | Project presentations                    | *NO ASSIGNED READINGS*                            |
|  18   |   12    | Text-to-Image models                 | Prompt engineering                       | *CRFM (2019), sections                            |
|  19   |   13    | Project development                  | Project development                      | *NO ASSIGNED READINGS*                            |

## Reading ##

* Arnold, A. & Tilton, L. (2019). "Distant viewing: analyzing large visual corpora", *Digital Scholarship in the Humanities*, 34(1), 1-14. DOI:[https://doi.org/10.1093/llc/fqz013](https://doi.org/10.1093/llc/fqz013)
* Center for Research on Foundation Models (CRFM) (2019). "On the Opportunities and Risks of Foundation Models", [arXiv:2108.07258](https://arxiv.org/abs/2108.07258) [cs.LG]
* Krizhevsky, A., Sutskever, I., & Hinton, G.E. (2017). "ImageNet classification with deep convolutional neural networks",* Commun. ACM*, 60(6), 84–90. https://doi.org/10.1145/3065386
* Gatys, L.A., Ecker, A.S., & Bethge, M. (2015), “A Neural Algorithm of Artistic Style,” [arXiv:1508.06576](http://arxiv.org/abs/1508.06576).
* Manovich, L. (2012). How to Compare One Million Images?. In: Berry, D.M. (eds) Understanding Digital Humanities. Palgrave Macmillan, London. DOI:[https://doi.org/10.1057/9780230371934_14](https://doi.org/10.1057/9780230371934_14)
*  Madhu, P., Kosti, R., Mührenberg, L., Bell, P., Maier, A. & Christlein, V. (2020) “Recognizing Characters in Art History Using Deep Learning,” [arXiv:2003.14171](https://arxiv.org/abs/2003.14171)
* Mitchell, T.M. (1997) "Does Machine Learning Really Work?,” [Available online](https://www.aaai.org/ojs/index.php/aimagazine/article/view/1303)
* Nielsen, M.A. (2015). Neural Networks and Deep Learning*, Determination Press. [Online](http://neuralnetworksanddeeplearning.com/chap1.html)
* Tarp, L. & Kristensen-McLachlan, R.D. (2021). "The reduced artefact: A case study in data visualisation and digital art history", *Perspectives*, Nov. 21. [Online](https://perspective.smk.dk/en/reduced-artefact-case-study-data-visualisation-and-digital-art-history)
  * [Also available in Danish](https://perspective.smk.dk/det-reducerede-vaerk-datavisualisering-af-tusindvis-af-vaerkfotografier)
* VanderPlas, J. (2016). _Python Data Science Handbook_. [Online](https://jakevdp.github.io/PythonDataScienceHandbook/)
* Wevers, M., & Smits, T. (2020). "Detecting Faces, Visual Medium Types, and Gender in Historical Advertisements, 1950–1995", In: Bartoli, A., Fusiello, A. (eds), *Computer Vision – ECCV 2020 Workshops. ECCV 2020. Lecture Notes in Computer Science()*, vol 12536. Springer, Cham. DOI:[https://doi.org/10.1007/978-3-030-66096-3_7](https://doi.org/10.1007/978-3-030-66096-3_7)


## Additional Resources
The following resources are *not* compulsory assigned readings. Instead, these are a mixture of textbooks and other resources which can be used as reference texts. Specifically, these will be useful for people who want to improve their understanding of linear algebra and neural networks. I strongly recommend all of the textbooks by Gilbert Strang - he's a fantastically clear writer, which is a rare skill among mathematicians. 

We'll be using VanderPlas (2016) in session 4, but it'ss a useful reference text for basic data science using Python (pandas, matplotlib, scikit-learn). It's a little below the level we'll be working at but it's good to have nevertheless.

* Bittinger, M.L., Ellenbogen, D.J., & Surgent, S.A. (2012). _Calculus and its Applications, 10th Edition_. Boston, MA: Addison-Wesley.
* Strang, G. (2009). _Introduction to Linear Algebra (4th Edition)_.  Wellesley, MA: Wellesley-Cambridge Press.
  * (2016). _Linear Algebra and its Applications, (5th Edition)_. Wellesley, MA: Wellesley-Cambridge Press.
  * (2019). _Linear Algebra and Learning from Data_. Wellesley, MA: Wellesley-Cambridge Press.
  * (2020). _Linear Algebra for Everyone_. Wellesley, MA: Wellesley-Cambridge Press.
* VanderPlas, J. (2016). _Python Data Science Handbook_. [Access](https://jakevdp.github.io/PythonDataScienceHandbook/)


## Slack Channel ##
There is no such thing as a stupid or trivial question. If a fellow student asks a question you know an answer to, try and answer!

 Slack is not only for instructor-student interaction, it is for all students to share knowledge and resources, and to get answers as fast as possible. Slack is best-suited for short technical questions and individual threads or channels for extended conversations on a given topic. 


## Disability Resources ##
Your experience in this class is important to me. If you have already established accommodations with Special Educational Support (SES), please communicate your approved accommodations to me at your earliest convenience so we can discuss your needs in this course. If you have not yet established services through SES, but have a temporary health condition or permanent disability that requires accommodations (conditions include but not limited to; mental health, attention-related, learning, vision, hearing, physical or health impacts), you are welcome to contact 8716 2720 (Monday & Thursday 9-12, Tuesday 13-15) or email sps@au.dk .  SES offers resources and coordinates reasonable accommodations for students with disabilities and/or temporary health conditions. Reasonable accommodations are established through an interactive process between you, your instructor(s) and SES. It is the policy and practice of the Aarhus University to create inclusive and accessible learning environment and ensure that all students have the opportunity to educate themselves on equal terms even if they have a disability
