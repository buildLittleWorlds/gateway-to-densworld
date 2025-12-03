# Introduction to Google Colab
## Your First Steps with Jupyter Notebooks

---

*This guide is for students who have never used a Jupyter notebook before. If you've used notebooks, skip to the Densworld courses.*

---

## What Is Google Colab?

Google Colab (short for "Colaboratory") is a free tool that lets you write and run Python code in your web browser. You don't need to install anything on your computer—just click a link, and you're coding.

It's like Google Docs for code: your work saves automatically, you can share it with others, and everything runs on Google's computers instead of yours.

All Densworld courses use Google Colab. When you see a button like this:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)

...clicking it opens a notebook in your browser, ready to go.

---

## What Is a Jupyter Notebook?

A Jupyter notebook is a document that mixes text and code. It's organized into **cells**—blocks that you run one at a time.

There are two types of cells:

1. **Text cells** (like this one): Explanations, instructions, context
2. **Code cells**: Python code that you can run and modify

Notebooks are perfect for learning because you can read an explanation, run some code, see what happens, then read the next explanation. It's like a textbook that actually does things.

---

## Getting Started: Your First Notebook

### Step 1: Open a Colab Notebook

Click this link to open a blank notebook:

**[Open a Blank Colab Notebook](https://colab.research.google.com/)**

You'll see something like this:

```
┌──────────────────────────────────────────────────────┐
│  Untitled0.ipynb                                      │
├──────────────────────────────────────────────────────┤
│  [+ Code]  [+ Text]                                   │
├──────────────────────────────────────────────────────┤
│  ▶ │                                                 │
│    │  (empty code cell)                              │
└──────────────────────────────────────────────────────┘
```

### Step 2: Sign In

You need a Google account to use Colab. If you're not signed in, you'll see a prompt. Sign in with any Google/Gmail account.

### Step 3: Run Your First Code Cell

Click in the empty code cell and type:

```python
print("Hello, Densworld!")
```

Now run the cell by either:
- Clicking the **▶ Play button** on the left side of the cell
- Pressing **Shift + Enter** on your keyboard

You should see output appear below the cell:

```
Hello, Densworld!
```

Congratulations! You've run Python code in a Jupyter notebook.

---

## The Colab Interface

### Top Menu Bar

```
File  Edit  View  Insert  Runtime  Tools  Help
```

**File**: Save, download, share your notebook
**Edit**: Cut, copy, paste cells
**Runtime**: Run cells, restart the environment
**Insert**: Add new code or text cells

### The Toolbar

```
[+ Code]  [+ Text]  [▶ Run all]  ...
```

- **+ Code**: Add a new code cell
- **+ Text**: Add a new text cell (for notes)
- **Run all**: Run every cell from top to bottom

### Cells

Each cell has:
- A **play button** (▶) to run it
- A **number** showing when it was run (e.g., `[1]`, `[2]`)
- **Output** area below where results appear

---

## Running Cells: The Key Skill

The most important thing to understand about notebooks: **cells run in the order you click them, not the order they appear on the page.**

This matters because code often depends on what came before. If you run cell 5 before cell 3, you might get an error because cell 3 set up something cell 5 needed.

### The Golden Rule

**When starting a notebook, run cells from top to bottom in order.**

Use **Shift + Enter** to run a cell and move to the next one. Keep pressing until you've run through all the cells.

### What If Something Goes Wrong?

If you get errors or weird behavior:

1. Go to **Runtime → Restart runtime** (this clears everything)
2. Go to **Runtime → Run all** (this runs everything from scratch)

This is like turning a computer off and on again. It fixes most problems.

---

## Working Through a Densworld Tutorial

Here's how to work through any Densworld course notebook:

### 1. Click the Colab Badge

Every tutorial has a badge like this:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com)

Click it. The notebook opens in your browser.

### 2. Save a Copy to Your Drive

**Important!** The notebook you just opened is read-only. To make changes:

Go to **File → Save a copy in Drive**

This creates your own copy that you can edit and save.

### 3. Run the Setup Cells

The first few cells usually load libraries and data:

```python
import pandas as pd

BASE_URL = "https://raw.githubusercontent.com/buildLittleWorlds/..."
creatures = pd.read_csv(BASE_URL + "creatures.csv")
```

Run these first. They don't produce exciting output, but everything else depends on them.

### 4. Read and Run

Work through the notebook from top to bottom:
- Read the text explanations
- Run each code cell
- Look at the output
- Think about what happened

### 5. Do the Exercises

Most tutorials have exercises at the end. These ask you to write code yourself.

The pattern is:
```python
# Exercise: Find all creatures with danger rating above 7
# Your code here:

```

Type your code where it says "Your code here" and run the cell.

### 6. Save Your Work

Your copy saves automatically to Google Drive. But you can also:
- **File → Download → Download .ipynb** to save to your computer
- **File → Download → Download .py** to get just the Python code

---

## Common Problems and Solutions

### "Name 'pd' is not defined"

**Cause**: You tried to use `pd` (pandas) without running the import cell first.

**Solution**: Go back to the top and run the cell that says `import pandas as pd`

### "Name 'creatures' is not defined"

**Cause**: You tried to use a variable (like `creatures`) that hasn't been created yet.

**Solution**: Run the earlier cells that load and create that data.

### The Cell Takes Forever to Run

**Cause**:
- You might have written an infinite loop
- The runtime might have disconnected

**Solution**:
- Click the **■ Stop button** on the cell
- If that doesn't work: **Runtime → Restart runtime**

### "Your session crashed"

**Cause**: You ran out of memory or hit some limit.

**Solution**:
- Close the tab and reopen the notebook
- Run all cells again

### Nothing Happens When I Click Run

**Cause**: The runtime isn't connected yet.

**Solution**: Wait a moment—you should see "Connecting..." in the top right. When it says "RAM | Disk" with green icons, you're connected.

---

## Keyboard Shortcuts

Once you're comfortable, these speed things up:

| Shortcut | Action |
|----------|--------|
| **Shift + Enter** | Run cell, move to next |
| **Ctrl + Enter** | Run cell, stay in place |
| **Alt + Enter** | Run cell, add new cell below |
| **Ctrl + M, A** | Add cell above |
| **Ctrl + M, B** | Add cell below |
| **Ctrl + M, D** | Delete cell |
| **Ctrl + M, Z** | Undo delete |

---

## Text Cells: Reading the Narrative

Densworld tutorials include narrative text between code cells—stories about trappers, archivists, expeditions. These are text cells formatted with **Markdown**.

You don't need to run text cells. They're already "run" (displayed).

If you want to add your own notes, click **+ Text** and type. Markdown basics:

```markdown
# Big heading
## Medium heading
### Small heading

**bold text**
*italic text*

- bullet point
- another bullet

1. numbered
2. list
```

---

## The Runtime: What's Actually Happening?

When you open a Colab notebook, Google gives you a small virtual computer in the cloud. This "runtime" has:

- Python installed
- Common libraries (pandas, numpy, matplotlib)
- About 12 GB of RAM
- About 80 GB of disk space

Your code runs on this virtual machine, not on your personal computer.

**Important limitations:**
- The runtime disconnects after ~90 minutes of inactivity
- It resets completely after ~12 hours
- When it resets, you need to run all cells again (your code is saved, but variables are lost)

This is why you should:
1. Run cells from the top when starting a session
2. Save your notebook regularly (it saves automatically, but check)

---

## Local Installation (Optional)

If you prefer working on your own computer instead of in the cloud:

### 1. Install Python

Download from [python.org](https://www.python.org/downloads/) or use Anaconda.

### 2. Install Jupyter

```bash
pip install jupyter
```

### 3. Install Libraries

```bash
pip install pandas matplotlib seaborn
```

### 4. Start Jupyter

```bash
jupyter notebook
```

This opens a browser tab with your local Jupyter environment.

### 5. Download Course Notebooks

Clone the course repository:

```bash
git clone https://github.com/buildLittleWorlds/yeller-quarry-data-science.git
cd yeller-quarry-data-science
jupyter notebook
```

---

## Practice Exercise

Before starting your first Densworld course, try this:

1. Open a blank Colab notebook
2. Create a code cell with: `2 + 2`
3. Run it and see the output: `4`
4. Create another code cell with:
   ```python
   message = "I'm ready for Densworld"
   print(message)
   ```
5. Run it
6. Create a text cell with a note to yourself
7. Save your notebook

If you can do all that, you're ready.

---

## Summary

| Concept | What It Means |
|---------|---------------|
| **Colab** | Google's free tool for running Python notebooks |
| **Notebook** | Document mixing text and code |
| **Cell** | One block of text or code |
| **Runtime** | The virtual computer running your code |
| **Run** | Execute a cell and see output |

The only way to learn is by doing. Open a notebook, run some code, break things, fix them.

The creatures of Yeller Quarry are waiting.

---

## Next Steps

Ready to begin? Here are your options:

**If you've never written Python before:**
- Start with any free "Python basics" tutorial (there are hundreds online)
- Come back when you understand variables, loops, and functions

**If you know basic Python:**
- Start with **[Yeller Quarry Data Science](../standalone/yeller-quarry-data-science/)** to learn pandas
- Or try **[Capital Archives NLP](../standalone/capital-archives-nlp/)** for natural language processing

**If you want to understand the world first:**
- Read the **[Introduction to Densworld](./DENSWORLD_INTRODUCTION.md)**

---

*"Click the badge. Sign in. Run the cells. The rest will follow."*
