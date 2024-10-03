# Intro to PRs

![Illustrative image of people working together](colab.png)

You can use the following guide to learn how and why to create a pull request.

## What is a pull request?

A pull request is a way to suggest changes to a repository. When you create a pull request, you propose your changes and request that someone review and pull in your contribution and merge them into their branch. Pull requests show differences between the content from both branches and the changes are visible in the repository.


## Set up your environment

### Create a local copy of the repository

Copy the following file to a new Git repo.

```bash
cd ~/source/repos
git init my-first-pr
cd my-first-pr
cp ~/Downloads/README.md .
```

**IMPORTANT:** Please ensure you continue working on the file copy and not the original.

### Create an empty repository on GitHub

1. Go to [GitHub](https://github.com) and sign in.
2. In the upper-right corner of any page, select `➕`, and then select `New repository`.
3. Name your repository `my-first-pr`.
   **IMPORTANT:** Do not initialize the repository with a `README`, `.gitignore`, or license.
4. Note the name of your repository `URL` here: **<URL>**
   You'll need this information later.

### Add the remote repository

1. In the terminal, add the URL of the repository you created on GitHub as the remote repository.

```bash
git remote add origin <URL>
```

2. Check that the remote repository was added.

```bash
git remote -v
```

3. Consider why it does not provide a URL for pull, only `push` and `fetch`?

---

4. Push the local repository to the remote repository.

   ```bash
   git push -u origin main
   ```

5. Refresh the GitHub page for your repository. You should see this `README.md` file.

### Why are pull requests called "Pull Requests"? (wrong answer)

Pull requests are so named basically because you are asking to _pull_ changes from a remote to your local repository. And that's because you have to ask permission to copy changes out of the repository, even if you have read access to that repository.

<!--TODO: This answer is SO wrong, I think we need to fix it! -->

### Create a local branch

You read the definition above, and you can't believe they got it this wrong. The name `Pull Request` can be misleading, but come on!

You decide to fix the definition above, but BEFORE you do that, you need to create a new branch to work on.

1. Create a new branch and switch to it.

```bash
# Older style:
git checkout -b fix/pr-definition
# Or, newer style:
git switch -c fix/pr-definition
```

2. Edit this file and address the two TODO items in two separate commits.

```bash
git commit -am "Add forks to the PR definition"
git commit -am "Give correct reason to why PRs are named that"
```

3. Check on GitHub whether the branch exists there or not. Does it? Why or why not?
4. You may think it is because you haven't pushed to the branch yet, so go ahead and try to push the branch to the remote repository.

```bash
git push
```

You probably got a similar error to this:

```text
fatal: The current branch fix/pr-definition has no upstream branch
```

5. What does this error mean? Why did it happen? Git explains how to fix it by running a command that will:
   
   1. Create a new branch on the remote repository with the same name as the local branch (if the remote branch doesn't already exist).
   2. Set the local branch to track the remote branch.
   3. Push the local branch to the remote repository.
   
7. Run the command that Git suggests to fix the error. There is also a shorthand for this command:

```bash
git push -u origin fix/pr-definition
```

7. Refresh the GitHub page for your repository. You should see the new branch there. GitHub will also suggest that you create a pull request. Do you see that?

### Create a pull request

1. Select `Compare & pull request`.
2. Note that the base repository and compare branch are correct.
3. Add a title and description for your pull request. Here is an example of a high-quality pull request description:

   ```markdown
   Title: Fix PR definition
   Description: This pull request fixes the definition of a pull request. It adds information about forks and corrects why pull requests are called "pull requests".
   ```

4. Select `Create pull request`.

### Review and merge a pull request

1. Go to the `Pull requests` tab on the repository page.
2. Select the pull request you created.
3. Review the changes in the pull request. You can see the commits that were added to the branch. You can also view the changes in the `Files changed` tab.
4. Add a comment to the pull request. Please feel free to ask for more information, suggest changes, or approve the pull request.
5. Select `Merge pull request` to merge the changes into the `main` branch.

Notice that GitHub suggests that you delete the branch after merging. This is a good practice because it keeps your repository clean and easy to navigate. It is part of a Git workflow called `GitHub flow`.

### Optional: Fork someone else's repository and create a pull request

If you are doing this in class, you can fork the repository of the person sitting next to you. If you are doing this on your own, you can fork a friend's or colleague's repository.

When you fork their repo, examine their definition and try to improve on it, then create a pull request to suggest your changes on **their** repository.
