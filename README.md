### End to End ML Project Implementation

Learning to implement an end to end ML project.

### Softwares and Tools required:

1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [VS Code IDE](https://code.visualstudio.com)
4. [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


### Configurations and git related steps
1. Create a new environment - whenever we create a new project

```
conda create -p venv python==3.7 -y
```

2. Activate the new environment

```
conda activate venv/
```

Or go to the file you want to work on and change the kernel to the environment we just created.

3. Create a requirements.txt file where you list all the libraries you need for your project. 
Then we can install them as follows:

```
pip install -r requirements.txt
```

4. Configure your git CLI to connect it to your Github account

```
git config --global user.name "your user name"
git config --global user.email "email id used for your git account"
```
5. Basic git commands

```
git add file name (or . for all files)
git status
git commit -m "your message"
git push <remote> <branch>
```

### Building a web application

I create a python file app.py that contains the code to build the web application.  