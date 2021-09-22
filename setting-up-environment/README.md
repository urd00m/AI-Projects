[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-f059dc9a6f8d3a56e377f745f24479a46679e63a5d9fe6f495e02850cd0d8118.svg)](https://classroom.github.com/online_ide?assignment_repo_id=5711564&assignment_repo_type=AssignmentRepo)
# AIDA Bootcamp #1: Setting Up Your Environment

Hi, and welcome the AIDA Fall 2021 bootcamp. Over the course of the next 4 weeks, you'll learn how to set up a state-of-the-art AI engine to read and predict the author of a random tweet.

But today, we'll start with something that's (hopefully) much simpler - setting up your development environment. This is something that is typically pushed away in many other classes/workshops - it's very common to use something like Google Colab. But whether we like it or not, manging python packages, spinning up jupyter notebooks, and uploading your code to a git repository are all important tasks that you will do as a machine learning practictioner, and it's worth learning how to do them early on.

## Getting Started

At a high-level, we'll be looking at installing, setting up, and using and 3 main tools:

1. [Git + GitHub](https://git-scm.com/downloads)
2. [Conda](https://docs.anaconda.com/anaconda/install/index.html)
3. [Jupyter Notebooks](https://jupyter.org)

To start off, create an account on [Github](https://github.com/). Then, follow the specific instructions for your OS.

> **Note:** Some parts of commands have angulr brackets (`<` and `>`) around them. This means you have to fill in a something that is specific to you. If you are unsure of any command at any point in time, please ask for help.

### Linux, Mac

#### Git

1. It's likely that you already have git installed. If you don't, see https://git-scm.com/book/en/v2/Getting-Started-Installing-Git or ask Jatin.
2. Open the terminal.
3. Run: `git config --global user.name "<Your name>"`
4. Run: `git config --global user.email <Your email>`
5. Run: `cd Desktop`
6. Run: `git clone <Your GitHub repo URL>`
7. Run: `cd <Your Git repo> && touch hello.txt`
8. See if `hello.txt` exists on your Desktop. If you've never used terminal before, this shows that terminal is another interface to your computer. Until now you've probably used what is called a GUI (graphical user interface) like Chrome and Finder to do things. The terminal is a more expansive, text-based way to do things with your computer.
9. Run: `git remote set-url origin <Your GitHub repo URL>`
10. Run: `git add -u`
11. Run: `git push -u origin main`

#### Conda

13. Download conda from https://www.anaconda.com/products/individual-d
14. Run: `conda install -c pytorch pytorch`.
15. Run: `jupyter notebook`
16. Execute the code in `setup_test.ipynb` and make sure it worked
17. Push all you changes to GitHub, as you did above. 


### Windows

#### Git

1. Download git for windows from https://git-scm.com/downloads
2. Open the git bash program
3. Run: `git config --global user.name "<Your name>"`
4. Run: `git config --global user.email <Your email>`
5. Run: `cd Desktop`
6. Run: `git clone <Your GitHub repo URL>`
7. Run: `cd <Your Git repo> && touch hello.txt`
8. See if `hello.txt` exists on your Desktop. If you've never used terminal before, this shows that terminal is another interface to your computer. Until now you've probably used what is called a GUI (graphical user interface) like Chrome and File Explorer to do things. The terminal is a more expansive, text-based way to do things with your computer.
9. Run: `git remote set-url origin <Your GitHub repo URL>`
10. Run: `git add -u`
11. Run: `git push -u origin main`

#### Conda

1. Download conda from https://www.anaconda.com/products/individual-d
2. Open the anaconda prompt program
3. Run: `conda install -c pytorch pytorch`.
4. Run: `jupyter notebook`
5. Execute the code in `setup_test.ipynb` and make sure it worked
6. Push all you changes to GitHub, as you did above. 

