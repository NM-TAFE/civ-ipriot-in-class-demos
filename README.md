# In-class Demonstrations

The code developed in class will be uploaded here. Each semester's delivery for each lecturer is in a separate branch. To find your class, look for a branch named in the format `yyyy/sn/lecturer`. For example, for Semester 2 of 2023 with lecturer Raf, the branch would be `2023/s2/raf`.

## Recommended Workflow

This workflow is specifically tailored for working with this repository, which the lecturer will constantly update during the class.

### Initial Setup (Basic)

The easiest way to work with this repository during in-class demonstrations is to clone it and then switch to the appropriate branch, pulling during the class to get the latest changes. Your own work should be in a separate folder that isn't part of this repository (e.g. `my-work`):

1. Clone this repository:

    ```bash
    git clone https://github.com/NM-TAFE/civ-ipriot-in-class-demos.git
    cd civ-ipriot-in-class-demos
    ```

2. Switch to the appropriate branch. For example:

    ```bash
    git switch 2024/s2/raf
    ```

3. Create an **untracked** folder for your own work:

    ```bash
    mkdir ../my-work
    ```

    This folder will be used to store your own work and will not be tracked by git.

4. During the class, pull the latest changes:

    ```bash
    git pull
    ```
5. If needed, copy to your own work folder:

    ```bash
    cp -r * ../my-work
    ```

#### Opening in PyCharm

To use in PyCharm, you are going to need a `venv`. Let's create one from the command line:

In the repository root, 

```bash
python -m venv venv
# optionally, activate (Git Bash)

source venv/Scripts/activate

```
Now in PyCharm, go to File > Open and select the root folder.


### Initial Setup (Advanced)

> These instructions are more streamlined but present more advanced git concepts to implement successfully. The most significant advantage is that it allows you to track your own work concurrently with the lecturer's work and practice git while practising coding.

The objective of this initial setup is to make it easy for you to pull work-in-progress from your lecturer while concurrently working on your version of the same work. This is **not** a standard git workflow: usually, you try to avoid having two people work on the same thing at exactly the same time. Consequently, it is a more complex setup that isn't generally applicable. But it will make for an excellent git workout and ultimately optimise git for this workflow. Note that an alternative (intermediate) approach is to set up multiple working trees, which is a bit more complex than the basic setup but also has (IMO) fewer advantages.

1. Fork this repository, ensure you *deselect* the option to copy the **main** branch only. 
⚠️ You **will** need other branches.
2. Clone your fork locally:

    ```bash
    git clone https://github.com/<YOUR_USER_NAME>/civ-ipriot-in-class-demos.git
    cd civ-ipriot-in-class-demos
    ```

3. Set this NMTAFE repository as the **upstream**

    ```bash
    git remote add upstream https://github.com/NM-TAFE/civ-ipriot-in-class-demos.git
    ```

4. Switch to the current semester's branch/lecturer. For example:

    ```bash
    git switch 2024/s2/raf
    ```

    This branch is set to track your *origin* (your fork) but we want something else.

6. Change this branch to track the *upstream* branch, not your origin:

   ```bash
   git fetch upstream 2024/s2/raf
   git branch --set-upstream-to=upstream/2024/s2/raf
   ```

7. Create your own branch to perform your work:
   
    ```bash
    git switch -c in-class-work
    ```

8. If you want to track your work on your fork, push your branch to your fork:

    ```bash
    git push -u origin in-class-work
    ```

9. During the class, if you want to pull the latest changes:

    ```bash
    git switch -
    git pull
    git switch -
    ```

    If you have work in progress, you may need to stash or commit your changes before pulling.

#### Cool awesome tips for this workflow

If you want to select what changes from `2024/s2/raf` to merge into your branch, you can use `git cherry-pick` to select individual commits. Or you can use `git checkout -p` to select individual changes from a commit or `git checkout <branch> -- <file>` to select individual files from a commit.

Here are some examples:
    
```bash
git cherry-pick 2024/s2/raf # Will pick just the latest commit - e.g. if there is a new set of exercises
git cherry-pick 2024/s2/raf^ # Will pick the commit before the latest commit
git checkout -p 2024/s2/raf # Will allow you to select individual changes from the latest committed state
git checkout 2024/s2/raf -- <file> # Will allow you to select individual files from the latest committed state
```

> ⚠️ Remember not to push your changes to the upstream repository. Also, GitHub may suggest a pull request to the upstream repository, but this is not the intention of this workflow. You should only push your changes to your fork.

