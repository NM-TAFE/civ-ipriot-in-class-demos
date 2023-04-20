# In class demonstrations: Semester 1, 2023

Code that is developed in class will be uploaded here.


## Best way to work with this repository

1. Clone this repository locally:

```bash
git clone https://github.com/NM-TAFE/civ-ipriot-in-class-demos.git
cd civ-ipriot-in-class-demos
```
2. If you want to experiment on the code locally, create a new branch:

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
 if there are any conflicts, you'll need to resolve them and continue the rebase using git rebase --continue.

By following this workflow, you can keep your local branch up to date with the upstream repository while making your own modifications. Remember not to push your changes to the upstream repository.




