# In class demonstrations: Semester 2, 2023

The code that is developed in class will be uploaded here.


## Recommended workflow
Note: not a general development workflow, just a useful way to work with this (constantly updating) repository.
1. Clone this repository locally:

```bash
git clone https://github.com/NM-TAFE/civ-ipriot-in-class-demos.git
cd civ-ipriot-in-class-demos
```
2. If you want to experiment with the code locally, create a new branch:

```bash
git checkout -b local_experiments
```

3. Periodically, fetch changes from the upstream repository:

```bash
git fetch origin
```

4. Merge the changes from the upstream's main branch into your local branch:

```bash
git checkout local_experiments
git merge origin/main
```

5. If you want to keep your local branch's history clean, you can rebase instead of merge:

```bash
git checkout local_experiments
git rebase origin/main
```
 If there are any conflicts, you'll need to resolve them and continue the rebase using git rebase --continue.

Following this workflow lets you update your local branch with the upstream repository. Remember not to push your changes to the upstream repository.




