# Lab Exam: Canteen Receipt Printer (Python + Git)

This is an individual lab exam. You will write small programs for a school canteen receipt. It covers Git, string variables, numbers, and conditions. You do not need functions: write plain top-to-bottom code like we do in class. You may use your notes and the Python slides. No chat apps, no AI tools, no copying from classmates.

Time: 2 hours. Your commit times are part of the grade.

## Part A: Get set up (10 minutes)

1. Click **Fork** (top right of this page) to copy this repo to your own GitHub account.
2. Clone YOUR fork. Replace `<your-username>` with your GitHub username:

   ```
   git clone https://github.com/<your-username>/canteen-receipt-lab.git
   cd canteen-receipt-lab
   ```
3. Tell Git who you are. Use your REAL full name, because your grade depends on it:

   ```
   git config user.name "Juan Dela Cruz"
   git config user.email "your-github-email@example.com"
   ```
4. Run `git status` and `git log --oneline` to see where you are.

## Part B: The five tasks (90 minutes)

Open each file, read the notes at the top, write your code under `# TODO`, and test with:

```
python -m unittest -v
```

Many tests will fail at the start. That is normal. Your job is to turn them green.

You can also run one file yourself, for example `python task3_numbers.py`, and type the answers.

| File | Topic | Points |
|---|---|---|
| `task1_bughunt.py` | Find and fix a bug in an if / elif chain | 10 |
| `task2_strings.py` | Strings: strip, title, indexing, slicing, f-strings | 15 |
| `task3_numbers.py` | Numbers: conversion, rounding, VAT, `//` and `%` | 15 |
| `task4_conditions.py` | if / elif / else for discounts and payment check | 25 |
| `task5_receipt.py` | Combine everything into one receipt program | 15 |

**One commit per task.** When a task is done, commit ONLY that file before you start the next one:

```
git add task1_bughunt.py
git commit -m "Fix tier bug: the 100 check came before the 500 check"
```

Do the same for each file, with a clear message that says what you did. For Task 1 your message must say what the bug was.

Rules:
- Do NOT edit anything in the `tests` folder.
- Do not squash, rewrite or delete your commits.
- Never put text inside `input()`. Write `input()`, not `input("Name: ")`. The tests type the answers for you and compare your printed lines exactly.
- Task 5 reuses your own code from Tasks 2 to 4, so finish those first and copy what you need.

## Part C: Hand in (20 minutes)

1. `git log --oneline` should show at least 5 commits of your own.
2. `git push origin main`
3. On GitHub, open your fork and click **Contribute > Open pull request**.
4. Title the pull request exactly: `Section - Surname, Firstname` (example: `9A - Dela Cruz, Juan`).
5. Show your instructor the pull request page before you leave.

No pull request means no grade, because the pull request is how your work reaches your instructor.

## Grading (100 points)

| What | Points |
|---|---|
| Task 1 tests pass | 10 |
| Task 2 tests pass | 15 |
| Task 3 tests pass | 15 |
| Task 4 tests pass | 25 |
| Task 5 tests pass | 15 |
| One separate commit for each task file | 10 |
| Clear commit messages (not empty, not "asdf") | 4 |
| All commits made during the exam time | 3 |
| Pull request title in the right format | 3 |
