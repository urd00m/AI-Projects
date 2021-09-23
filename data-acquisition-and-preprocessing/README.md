[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5720557&assignment_repo_type=AssignmentRepo)
# AIDA Bootcamp #2: Data Acquisition and Preprocessing

Thanks for joining the second AIDA bootcamp session. Today, we'll be taking the next step towards building our AI tweet prediction engine - preparsing a dataset.

Most machine learning models today work in a . Though a magical process called backpropogation and gradient descent (which we'll discuss next week),

If you attended last week (which we hope and will assume that you did), you should have your terminal, Git, and Conda set up and ready to go. If you're still facing issues with this or are not able to run any of the commands below, please do ask for help.

To get started this week, we've provided you with some code in the repo as well as a conda environment file to make installing all the packages easier.

To get started, run the following commands:

```bash
git clone <Your GitHub Repo URL>
cd <Your Git Repo>
conda env create -f environment.yml
conda activate data-preprocessing 
jupyter lab
```

If the three steps above worked, you should be inside a Jupyter notebook and good to go.

## Step 1: Load the Tweets

Our dataset consists of many tweets and their corresponding authors. We've saved them as a `.csv` file to make it easier to access. Your task is to use the `pandas` library to load the tweets as a `DataFrame`.

We don't expect you to know what these are just yet. Ask around and search the internet to see if you can figure this out.

## Step 2: Tokenization and Vectorization

Once you've. This step is a little complicated, so we did it for you. But instead of just running the code, try to read it and see if you can understand what's going on.

## Step 3: Make the Tensors Easy to Load/Use

Ok, we finally got a PyTorch `Tensor`. Cool, but notice how you had to run a bunch of code in your Jupyter notebook to get that done? Imagine doing that for every sample the dataset (which can get quite large)~

To make our lives easier in the future, we're going to "refactor" our code. This is software engineering jargon that just means tidying up and organizing the code in a way that makes it cleaner to read and easier to use.

Specifically, we're going to use a PyTorch `Dataset` object . Again, see if you can look up what that means and figure out how to implement it.

Here are some resources that you might find useful:

Some (possibly) helpful links:

- [Classes — Python 3.9.7 documentation](https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables)
- [Understanding `__getitem__` method](https://stackoverflow.com/questions/43627405/understanding-getitem-method)
- [A detailed example of data loaders with PyTorch](https://stanford.edu/~shervine/blog/pytorch-how-to-generate-data-parallel)
