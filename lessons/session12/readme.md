# Session 12 - Beyond CNNs

## Overview

In class today we've been looking at current state-of-the-art text-to-image models. These multimodal models are taking the world by storm right now, and are where the future of research is for both language and visual analytics.

Unfortunately, using the models is prohibitively difficult for teaching purposes, much more so than working with LLM's. We are not easily able to use Stable Diffusion locally, and Dall-E 2 costs money. It is possible to use Stable Diffusion via this [HuggingFace Space](https://huggingface.co/spaces/stabilityai/stable-diffusion), and you're welcome to spend some time fiddling around and experimenting today.

However, for the code-along session today, we're goint to see a few final tips and tricks for working with ML and computer vision. Firstly, we'll see how we can perform *grid search* to search over a range of hyperparameters, in order to find the best combination to train our ML models. 

Secondly, we'll see how we can create "attention heatmaps" from pretrained CNN embeddings, so that we can get an idea of what exactly a model is **seeing* when it makes predictions. This is therefore taking first steps towards explainable and interpretable models in visual analytics.

## Tasks
- Grid Search for training ML models
- Inspecting CNNs to see what they see
- Experimenting with Stable Diffusion (as much as possible on HuggingFace)
- Time for questions and coding
