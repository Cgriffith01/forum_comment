# Week 6 Homework: Forum Comments

A three step progression of a simple command line forum comment program. Each step builds on the last: Step 1 keeps comments in memory only, Step 2 loads a starting set of comments from a file, and Step 3 both loads from and saves back to a file so comments persist between runs.

Each comment is just a name and a one line comment, there's no date/timestamp tracked.

## Files

- **Week_6_Assignment_Step1_Christine_Griffith.py** - in-memory version. Comments exist only for the current run and disappear when the program exits.
- **Week_6_Assignment_Step2_Christine_Griffith.py** - loads a starting set of comments from `step2_data.txt` when the program launches. New comments added during the session are kept in memory but not saved back to the file.
- **Week_6_Assignment_Step3_Christine.py** - loads existing comments from `step3_data.txt` on launch (creating the file with a header row if it doesn't exist yet), and appends every new comment straight to that file, so comments persist across runs.
- **step2_data.txt** - tab-separated sample data (name, comment) used by Step 2.

All three share the same menu:

```
0: Exit
1: Display Comments
2: Add Comment
```

## Requirements

- Python 3

## Usage

Run whichever step you want from the command line:

```
python3 Week_6_Assignment_Step1_Christine_Griffith.py
python3 Week_6_Assignment_Step2_Christine_Griffith.py
python3 Week_6_Assignment_Step3_Christine.py
```

Step 2 needs `step2_data.txt` in the same folder. Step 3 will create `step3_data.txt` itself the first time it runs if it isn't already there.

## What was wrong with the originals and what I fixed

### Step 1
- `all_comments` was a dict where each key was a `(date, name, comment)` tuple and the value was the dict itself, a self-referential assignment that didn't actually store the comment data anywhere useful. Changed `all_comments` to a plain list, and each new comment is now appended as its own `{'date':, 'name':, 'comment':}` entry.
- Displaying comments (`option 1`) just printed the dict's keys as raw tuples. Fixed to loop through the list and print each comment's date, name, and text on their own lines.
- Added an `else` branch so an invalid menu choice tells the user to pick 0, 1, or 2 instead of silently doing nothing.

### Step 2
- The file was opened twice: once directly and once through a `with` block that was never actually used, the real loop read from the first (already partially consumed) file object. Simplified to a single file handle that's read once and closed.
- After reading the file, a hardcoded, malformed literal (a tuple containing a dict, a comma, then another dict) overwrote `all_comments` entirely, throwing away everything just read from the file. Removed that block completely, the real data from `step2_data.txt` now populates `all_comments` directly as a list of dicts.
- Because of the loop bug above, `date`, `name`, and `comment` only ever held the *last* row read from the file, so `option 1` printed the same single comment over and over for every entry in the dict. Fixed by storing each row as its own dict in the list and looping over the list correctly when displaying.
- `option 2` collected a new name and comment but never added them anywhere, so new comments vanished immediately. Fixed to append the new comment to `all_comments`.

### Step 3
- `filename` was set to a plain string (`'step3_data.txt'`), then the code tried to `for line in filename` and `filename.close()`, treating a string like an open file. That would iterate over individual characters and crash on `.close()`. Fixed to actually open the file (or create it with a header row if it doesn't exist yet) and read from a real file object.
- The file was opened in `'w'` mode (write, which erases the file) before trying to read from it, so any existing data would be wiped before it could be loaded. Fixed to open for reading first, and only create a new file if one doesn't already exist.
- Same malformed hardcoded dict/tuple literal as Step 2 was overwriting the loaded data, removed for the same reason.
- New comments were never written back to disk, so nothing actually persisted between runs despite that being the point of Step 3. Fixed so every new comment is both added to the in-memory list and appended to `step3_data.txt` right away.

## Notes

- All three now use a consistent list-of-dicts structure for `all_comments`, which makes the display logic identical across steps and easier to extend later (sorting, filtering, editing, etc.).
- Step 3's file writes use append mode (`'a'`) for each new comment rather than rewriting the whole file, so existing comments are never at risk of being lost by a later write.
- The date/timestamp field has been dropped entirely, each comment now stores just a `name` and `comment`, both in memory and in the saved data files.
