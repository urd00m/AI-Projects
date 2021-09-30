[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5814481&assignment_repo_type=AssignmentRepo)
# AIDA Bootcamp #3: Training a Model

Today, we'll finally be training a model!

So far, we've looked at setting up a reliable environment to work in (week 1) and loaded a dataset of Tweets pandas and a tokenizer. We passed the tokenizer text.

If you missed the previous sessions and/or don't fully understand what that means, that's ok. All you need to know for today is that we have a PyTorch dataset, which can fetch pairs of `(x, y)` datapoints, where `x` and `y` are `torch.Tensor` objects ([here](https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html)'s some info on what exactly a `torch.Tensor` is). This is all you need to train a model.

The setup is mostly the same as last week - clone your Git repo, create a conda environment, activate it, and launch a Jupyter notebook. This is common workflow for machine learning practitioners, so it's worthwile effort to get familiar with it and make sure it works on your computer.

```bash
git clone <Your GitHub Repo URL>
cd <Your Git Repo>
conda env create -f environment.yml
conda activate model-training 
jupyter lab
```

## Step 1: Train a Simple Multi-Layer Perceptron (TODO)

To classify our Tweets, we'll be using a Multi-Layer Perceptron, or MLP for short. Despite the fancy-sounding name, it's one of the oldest and simplest kinds of neural networks used in machine learning. Due to their versatility, they are often used in some form in many neural But despite this, the MLP is used in some way as a component fo many machine learning models today, and is still alive and well in [modern research](https://arxiv.org/abs/2105.01601) today.

We'll train our MLP to map the 768-dimensional vectors (which, again, are stored as `torch.Tensor` objects) into a vector of length 20, which represents the probability of each  

To get you started, we've provided the correct code from last week along with some extra helper code for this week in `train_mlp.ipynb`. Your goal is to edit the code in this notebook where required to train the model which we've defined for you.

> **Remember**, we don't expect you to know how to train an MLP already. Search engines and the people sitting next to you are your friends. This is not a class - we strongly encourage you to discuss, "cheat" by looking up the answers online and use every tool at your disposal to figure out how to effectively train your MLP in the simplest way possible.

## Step 2: Train a Better Model (in Google Colab)

If you were able to sucessfully complete the training code in `train_mlp.ipynb`, you might have noticed that the accuracy isn't actually that great.

This is because we're using a very simple model with very simple training techniques. The model *trains*, but it does not train very well. In practice, machine learning practioners use a variety of techniques to make their models perform well on real datasets. This is a little beyond the scope of the bootcamp, but we've provided the code for you to run in `train_transformer.ipynb`. This trains a fancier type of model called a transformer to predict the exact same thing we did with MLPs, but more accurately.

> **Note:** You probably need an Nvidia GPU to train this model. We reccomend using Google Colab this time, instead of your own environment. All you need to do is visit `https://colab.research.google.com/github/AIDA-UIUC/your-github-repo/blob/main/train_transformer.ipynb` (note that you have to use your own GitHub repo instead of `your-github-repo` in the URL).

If you're interested in these sorts of training techniques and other topics on the bleeding edge of deep learning, definetly consider attending the SIGAIDA research meetings (see the `#research` channel on Discord for more info).
