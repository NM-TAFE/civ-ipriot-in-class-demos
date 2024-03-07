# In-class Demonstrations

The code developed in class will be uploaded here. Each semester's delivery for each lecturer is in a separate branch. To find your class, look for a branch named in the format `yyyy/sn/lecturer`. For example, for Semester 2 of 2023 with lecturer Raf, the branch would be `2023/s2/raf`.

## Recommended Workflow

This workflow is specifically tailored for working with this repository, which will be constantly updated by the lecturer during the class.

### Initial Setup

1. Clone this repository locally:

    ```bash
    git clone https://github.com/NM-TAFE/civ-ipriot-in-class-demos.git
    cd civ-ipriot-in-class-demos
    ```

2. List all available branches to find your class:

    ```bash
    git branch -r
    ```

3. Switch to the appropriate branch for your class:

    ```bash
    git checkout -b local_class_branch origin/yyyy/sn/lecturer
   # alternatively
    git switch -c your_branch_name --track origin/yyyy/sn/lecturer
    ```

### Ongoing Work

1. If you want to experiment with the code locally, create a new branch:

    ```bash
    git switch -c local_experiments
    ```

2. Periodically, fetch changes from the upstream repository:

    ```bash
    git fetch origin yyyy/sn/lecturer
    ```

3. Merge the changes from the upstream's class-specific branch into your local branch:

    ```bash
    git switch local_experiments
    git merge origin/yyyy/sn/lecturer
    ```

    or, if you want to keep your local branch's history clean, you can rebase instead of merge:

    ```bash
    git switch local_experiments
    git rebase origin/yyyy/sn/lecturer
    ```

    If there are any conflicts, you'll need to resolve them and continue the rebase using `git rebase --continue`.

4. Remember not to push your changes to the upstream repository.
