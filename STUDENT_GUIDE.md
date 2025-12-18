# Welcome to Gateway to Densworld
## Learning Colab Through Fiction

---

*The Archives of the Capital stretch for miles underground. Shelf after shelf of manuscripts, expedition reports, creature catalogs. Every piece of knowledge in Densworld eventually finds its way here.*

*But the Archives don't organize themselves.*

*"You're the new apprentice?" Chief Archivist Mink looked up from a stack of scrolls. "Good. I need someone who can work with data. Not just read it—transform it. Make it useful."*

*"I don't know anything about data," you admitted.*

*"You will," Mink said. "By the time we're done, you'll be able to load it, filter it, group it, merge it, visualize it. You'll understand what these numbers mean and where they come from."*

*"Where do I start?"*

*Mink smiled. "With the world itself. You can't understand data without understanding where it comes from. And in Densworld... the data comes from everywhere."*

---

### What Is This?

This is a Google Colab course disguised as an orientation to a fantasy world.

You'll learn **Python fundamentals and pandas basics**—the skills you need for data science—by exploring **Densworld**, a 70,000-line fictional universe. Instead of abstract examples, you'll work with creature catalogs from Yeller Quarry, archival entries from the Capital, and journey records from the edges of the known world.

By the end, you'll know how to:
- Write Python variables, lists, dictionaries, and functions
- Load CSV files into pandas DataFrames
- Filter, sort, group, and aggregate data
- Merge tables and handle missing values
- Create visualizations with matplotlib
- Navigate Google Colab with confidence

You'll also understand Densworld: its regions, characters, patterns, and mysteries.

### Why Learn This Way?

1. **Stories make things stick.** You'll remember how dictionaries work because you used them to model the Dens—a region where things dissolve and coordinates fail. Not because you memorized a definition.

2. **Invented worlds prevent cheating.** You can't Google "how to analyze Densworld creature data" because it doesn't exist anywhere else. You have to actually learn the skills.

3. **Context creates meaning.** The numbers in these datasets represent something: trappers who died, places that don't exist on the ground, patterns the archivists can't explain. Data is never neutral.

4. **Learning should be interesting.** If you're going to spend hours learning to code, the code should be doing something more compelling than adding numbers.

---

## The World

**Densworld** is a fictional universe with its own history, geography, and natural laws. It was created as the foundation for data science courses—a world rich enough to generate structured datasets that feel real but exist nowhere else.

### The Three Directions

Densworld has three meaningful directions, not four:

| Direction | Destination | Nature |
|-----------|-------------|--------|
| **North** | Northo | Negation—monasteries, silence, the closing of the mouth |
| **South** | Tower of Mirado | Pursuit—the Colonel's endless siege, persistence |
| **West** | The Dens | Dissolution—shifting boundaries, the edge of the knowable |

There is no East. Or rather, East exists only as absence—a direction that leads back to where you started.

### The Yeller Numbers

Throughout Densworld, certain numbers appear again and again: **2, 3, 5, 7, 11**. The first five primes. Creatures move in groups of these sizes. Catch quantities cluster around them. The archivists record the pattern but cannot explain it.

### Key Characters

| Character | Location | Role |
|-----------|----------|------|
| **Chief Archivist Mink** | The Capital | Your mentor, oversees the Archives |
| **The Boss** | Yeller Quarry | Legendary trapper, designed most traps |
| **The Colonel** | Tower of Mirado | Commander of a 20-year siege |
| **Fincho** | Tower of Mirado | The Colonel's loyal lieutenant |
| **Bagbu/Vagabu Olt** | Everywhere | Wandering mapmaker |

---

## The Tutorials

Each tutorial teaches **Colab/Python skills** by **exploring Densworld**. The technical and narrative learning happen together.

| # | Tutorial | What You'll Learn | Densworld Content |
|---|----------|-------------------|-------------------|
| 1 | First Contact | Running cells, Colab basics | Overview of the world |
| 2 | The Capital | Variables, strings, f-strings | The Archives, civilization |
| 3 | Yeller Quarry | Lists, loops, indexing | Creatures, danger, the yeller numbers |
| 4 | The Dens | Dictionaries, nested structures | Dissolution, shifting boundaries |
| 5 | Mirado | Functions, parameters, return | The Colonel's siege |
| 6 | Loading Data | pandas, CSV files | Fiction becomes structured data |
| 7 | Exploring DataFrames | Filtering, grouping, aggregating | The creature catalog |
| 8 | The Edges | Merging, missing values | Northo, Dead River |
| 9 | Visualization | matplotlib, charts | Cartography for data |
| 10 | Three Directions | Capstone, advanced Colab | Cosmology, course recommendations |

### The Capstone (Tutorial 10)

Tutorial 10 is different. You'll complete a full analysis workflow—load data, explore, filter, aggregate, visualize, and recommend—using everything you've learned. Then you'll learn about Densworld's cosmology and receive recommendations for which course to take next.

---

## How to Use This Course

### Option 1: Google Colab (Recommended)

Click any "Open in Colab" badge in the README. The notebook will open in your browser. You don't need to install anything.

1. **Click the Colab badge** for Tutorial 1
2. **Sign in** with a Google account (free)
3. Go to **File → Save a copy in Drive** to keep your work
4. **Run cells from top to bottom** (Shift+Enter)
5. **Complete the exercises** at the end of each tutorial
6. **Move to the next tutorial**

### Option 2: Local Installation

If you prefer working locally:

```bash
git clone https://github.com/buildLittleWorlds/gateway-to-densworld.git
cd gateway-to-densworld
pip install pandas matplotlib jupyter
jupyter notebook
```

Navigate to the `notebooks/` folder and open the tutorials in order.

---

## Prerequisites

**None.** This course is designed for absolute beginners.

You don't need to know Python, pandas, or data science. You don't need to know anything about Densworld. Everything you need is in the tutorials.

The only requirements are:
- A web browser
- A Google account (free) for Colab
- Curiosity

---

## Colab Quick Reference

| Action | How |
|--------|-----|
| Run a cell | `Shift+Enter` or click the play button |
| Run and stay | `Ctrl+Enter` |
| Insert cell below | `Ctrl+M B` |
| Insert cell above | `Ctrl+M A` |
| Delete cell | `Ctrl+M D` |
| Convert to Markdown | `Ctrl+M M` |
| Convert to Code | `Ctrl+M Y` |
| Save notebook | `Ctrl+S` |

**Important**: Always run cells from top to bottom. Later cells depend on earlier ones.

---

## The Data

This course uses data from multiple sources:

| Dataset | Source | Used In |
|---------|--------|---------|
| `creatures.csv` | Yeller Quarry Data Science | Tutorials 6, 7, 9, 10 |
| `places.csv` | Journeys and Graphs | Tutorial 8 |
| `journey_steps.csv` | Journeys and Graphs | Tutorial 8 |
| `regions.csv` | Gateway course | Tutorial 10 |
| `characters.csv` | Gateway course | Tutorial 10 |

The data is internally consistent. Patterns are real—if you look hard enough, you'll find them.

---

## Troubleshooting

**The notebook won't load**
- Check your internet connection
- Try a different browser (Chrome works best with Colab)
- Make sure you're signed into Google

**Cells won't run**
- Did you run the earlier cells first? Run from top to bottom.
- Is your runtime connected? Look for "Connected" in the top right.
- Click **Runtime → Restart and run all** to start fresh.

**I get an error about a variable not being defined**
- You probably skipped a cell. Run all cells from the beginning.

**My changes disappeared**
- Did you save a copy to your Drive? Go to **File → Save a copy in Drive**.
- Colab notebooks are temporary unless you save them.

**I don't understand something**
- Read the narrative text—it often explains the "why" behind the code
- Try running the code and looking at the output
- Experiment! Change values and see what happens

---

## After This Course

Once you complete Gateway, you're ready for any Densworld course. Here's a guide:

| If you want to... | Take this course |
|-------------------|------------------|
| Master pandas and data analysis | **Yeller Quarry Data Science** |
| Work with text and language | **Capital Archives NLP** |
| Learn ML math foundations | **ML Math with Densworld** |
| Build real applications | **Densworld API Course** |
| Explore networks and graphs | **Journeys and Graphs** |
| Study spatial philosophy | **Spatial Series** (5 courses) |
| Learn modern AI/transformers | **Hugging Face Series** (7 courses) |
| Solve puzzles and design languages | **Puzzle Series** (2 courses) |

**If you're unsure**: Start with **Yeller Quarry Data Science**. It builds directly on what you've learned here and will solidify your pandas foundations.

---

## Recommended Learning Paths

*The archivists have identified five progressions through the course ecosystem. Each path builds skills in a particular direction. Choose based on where you want to go.*

### Path 1: Data Science Fundamentals

**Gateway → Yeller Quarry → Journeys and Graphs → Dead River Lab**

*For students who want to build strong foundations in data manipulation, analysis, and eventually data generation.*

You'll develop:
- Deep pandas proficiency (filtering, grouping, merging, aggregation)
- Graph theory and network analysis skills
- Understanding of how structured data emerges from narrative
- The ability to design and build your own synthetic datasets

**Best for**: Students who want to become fluent in data wrangling before moving to ML. Also ideal for those interested in data engineering or analytics roles.

---

### Path 2: NLP and Language

**Gateway → Capital Archives → Puzzle Series (02) → HF Series (01-02)**

*For students fascinated by text, language, and meaning.*

You'll develop:
- Natural language processing fundamentals (tokenization, TF-IDF, sentiment)
- Understanding of formal grammars and constructed languages
- Transformer-based NLP (Hugging Face pipelines, embeddings)
- Semantic search and text analysis at scale

**Best for**: Students interested in computational linguistics, NLP engineering, or anyone who finds the Archive's manuscripts more compelling than its numbers.

---

### Path 3: Philosophy of Measurement

**Gateway → Spatial Series (01-05) → Philosophy of Pattern Series**

*For students drawn to the deep questions: What can be measured? What does measurement change? How do we know what we know?*

You'll develop:
- Time series analysis and hypothesis testing
- Understanding of coordinate systems and observer effects
- Classification theory and the ethics of taxonomy
- Advanced ML concepts through philosophical frameworks (latent spaces, multi-agent systems, anomaly detection)

**Best for**: Students who think deeply about methodology, epistemology, or the philosophy of science. Also for those who want to understand *why* ML techniques work, not just *how*.

---

### Path 4: AI/ML Practitioner

**Gateway → Yeller Quarry → HF Series (complete) → Access Architectures**

*For students who want to build production AI systems.*

You'll develop:
- Solid data foundations (pandas, data cleaning, EDA)
- Modern ML stack (transformers, embeddings, fine-tuning, RAG)
- Model deployment and API design
- Understanding of access design, governance, and platform architecture

**Best for**: Students aiming for ML engineering roles, or anyone who wants to build end-to-end AI applications that real users can interact with.

---

### Path 5: World Builder

**Gateway → Access Architectures (complete) → Dead River Lab → Living World Capstone**

*For students who want to create fictional worlds and the systems that make them explorable.*

You'll develop:
- Access architecture design (conversational AI, APIs, generators)
- Synthetic data generation from narrative
- Platform integration and deployment
- Teaching methodology for worldbuilding (10-week syllabus)

**Best for**: Game designers, fiction writers building explorable worlds, educators designing creative curricula, or anyone who wants to build something like Densworld for their own universe.

---

### Choosing Your Path

| Path | First Milestone | Final Skill |
|------|-----------------|-------------|
| Data Science Fundamentals | Investigate missing children (Yeller Quarry capstone) | Design your own synthetic dataset |
| NLP and Language | Detect manuscript forgeries (Capital capstone) | Build semantic search systems |
| Philosophy of Measurement | Test Keth's boundary predictions (Spatial capstone) | Map ML to philosophical frameworks |
| AI/ML Practitioner | Fine-tune a language model (HF Course 4) | Deploy an integrated AI platform |
| World Builder | Design an Oracle system (Access Course 1) | Teach worldbuilding to others |

*You don't have to commit to a single path. Many students complete Path 1, then branch into either Path 3 or Path 4. The courses are designed to interconnect—characters, datasets, and patterns recur across the ecosystem.*

---

## The Course Series

Gateway to Densworld is part of a larger ecosystem:

| Category | Courses | Focus |
|----------|---------|-------|
| **Gateway** | 1 | Colab basics + world orientation |
| **Standalone** | 7 | Independent courses (pandas, NLP, API, etc.) |
| **Hugging Face Series** | 7 | Modern AI/ML with Hugging Face |
| **Puzzle Series** | 2 | Pattern recognition, formal languages |
| **Spatial Series** | 5 | Philosophy of space, coordinates |

All courses share the same fictional universe. Characters appear across courses. Patterns recur. The deeper you go, the more connections you'll find.

---

## A Note on the Fiction

Densworld contains darkness. Trappers die in the Quarry. Children go missing. The Dens dissolves what enters it. Dead River is "a place on maps that doesn't exist on the ground."

This is intentional. Data is never neutral. Every row in a dataset was someone's experience. The fiction helps you remember that—before you encounter real data where the stakes are real.

Handle it carefully.

---

*"Every true journey begins in Yeller Quarry."*

*That's what the archivists say. They mean: every journey begins in danger, in the encounter with what can kill you. The trappers know the creatures. They know the numbers. They know the patterns. From that knowledge, they can go anywhere.*

*You've started your journey. You know notebooks. You know Python. You know Densworld.*

*Now choose your direction.*

---

**Ready?**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/buildLittleWorlds/gateway-to-densworld/blob/main/notebooks/tutorial_01_first_contact.ipynb) **Start Tutorial 1: First Contact**
