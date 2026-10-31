# GitHub upload steps (beginner-friendly)

## 1. Create the repository

1. Sign in to https://github.com/key6308?tab=repositories
2. Click **New**.
3. Name the repository `sticky-notes-capstone-consolidation`.
4. Choose **Public**.
5. Do not add a README, `.gitignore`, or license on GitHub because these files are already in this project.
6. Click **Create repository**.

## 2. Upload files using the website

1. Open the new repository.
2. Choose **Add file** → **Upload files**.
3. Open the extracted `Sticky_Notes_Capstone_Consolidation` folder on your computer.
4. Drag the files and folders inside that folder into the GitHub upload area. Upload the contents, not the outer ZIP file.
5. Wait for the upload to finish.
6. Add a commit message such as `Add capstone Django project`.
7. Click **Commit changes**.

## 3. Branches required by the assignment

The assignment asks for actual Git branches named `docs` and `container`, with changes committed on each branch and then merged into `main`. Uploading through the website alone does not create this branch history.

If Git is installed, open a terminal in the project folder and run these commands one at a time:

```bash
git init
git add .
git commit -m "Add original Django project"
git branch -M main
git checkout -b docs
git add notes sticky_notes docs
git commit -m "Add docstrings and Sphinx documentation"
git checkout main
git checkout -b container
git add Dockerfile docker-compose.yml requirements.txt
git commit -m "Add Docker configuration"
git checkout main
git merge docs
git merge container
git remote add origin https://github.com/key6308/sticky-notes-capstone-consolidation.git
git push -u origin main
git push -u origin docs
git push -u origin container
```

If GitHub already contains files or you already initialized Git, do not blindly repeat `git init` or `git remote add origin`; the commands may need adjusting.

## 4. Final check

- Make sure the repository is public.
- Make sure `README.md`, `requirements.txt`, `.gitignore`, `Dockerfile`, `docker-compose.yml`, `docs/`, `notes/`, `sticky_notes/`, `templates/`, `diagrams/`, and `capstone.txt` are present.
- After installing the packages, build the Sphinx HTML documentation with:
  `python -m sphinx -b html docs docs/_build/html`
- Open `capstone.txt` and confirm the repository link matches your GitHub repository.
- Submit the repository link and the required files on your course dashboard, then click **Request review**.
