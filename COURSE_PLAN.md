# Gateway Course Plan: Learning Colab Through Densworld

## Vision

Students complete this course with two outcomes:
1. **Technical competence**: Comfort using Google Colab from opening their first notebook to completing moderately advanced data work
2. **World knowledge**: Understanding of Densworld's geography, key regions, characters, and what makes this fictional universe distinctive

These are learned *together*—each tutorial teaches a Colab skill *by* exploring a region or concept of Densworld.

---

## Course Title Options

- "Gateway to Densworld: Learning Colab Through Fiction"
- "First Steps in Densworld"
- "The Traveler's Guide: An Introduction to Colab and Densworld"
- "Entering Densworld"

---

## Structure: 10 Tutorials

The course progresses from absolute beginner (never opened a notebook) to confident practitioner (can handle most Colab tasks independently). Each tutorial pairs a technical skill level with world content.

---

## Tutorial Outline

### Tutorial 1: First Contact
**Colab Skills:** What is a notebook, running cells, Shift+Enter, text vs code cells
**Densworld Content:** What is Densworld? The overview—70,000 lines of fiction, synthetic data, why fiction for learning

*Activity:* Run simple print statements. Read short passages from different regions displayed as output. Students get a taste of the variety.

**Key insight:** "This world exists. It has rules. You're about to explore it."

---

### Tutorial 2: The Capital
**Colab Skills:** Variables, basic Python types (strings, integers), printing formatted output
**Densworld Content:** The Capital—center of civilization, the Archives, scholars, manuscripts

*Activity:* Store information about the Capital in variables. Create strings describing archivists. Use f-strings to generate "archival entries."

```python
region = "The Capital"
population = 50000
chief_archivist = "Mink"
print(f"The {region} (pop. {population}) is overseen by Chief Archivist {chief_archivist}.")
```

**Key insight:** The Capital is where knowledge is kept. Everything flows through the Archives.

---

### Tutorial 3: Yeller Quarry and Lists
**Colab Skills:** Lists, indexing, iteration (for loops), len()
**Densworld Content:** Yeller Quarry—creatures, trapping crews, danger, the yeller numbers (2, 3, 5, 7, 11)

*Activity:* Work with lists of creatures, danger ratings, crew members. Loop through creatures. Discover the prime number pattern.

```python
creatures = ["Leatherback Burrower", "Maw Beast", "Stalking Wharver", "Bone Crawler"]
danger_ratings = [5, 9, 7, 4]

for creature, danger in zip(creatures, danger_ratings):
    print(f"{creature}: Danger Level {danger}")
```

**Key insight:** The Quarry is dangerous. Data about creatures is life or death for trappers.

---

### Tutorial 4: The Dens and Dictionaries
**Colab Skills:** Dictionaries, key-value pairs, nested structures, accessing nested data
**Densworld Content:** The Dens—dissolution, shifting boundaries, the moat, lookout towers, how this place is *different*

*Activity:* Create dictionaries representing the strange properties of Dens—things that shift, opposites of appearance and reality.

```python
dens_properties = {
    "physical_nature": "shifting sludge",
    "appearance_vs_reality": {
        "feels_like": "drowning",
        "actually": "desiccation"
    },
    "stability_source": "lookout tower machines",
    "map_validity": "one day"
}
```

**Key insight:** The Dens is where things dissolve. It's the edge of what's knowable.

---

### Tutorial 5: Mirado and Functions
**Colab Skills:** Defining functions, parameters, return values, calling functions
**Densworld Content:** Tower of Mirado—the siege, The Colonel, Fincho, gradient descent as siege metaphor

*Activity:* Write functions that model siege progress. Calculate "ground gained" over time. Introduce the idea of iterative progress (setup for understanding gradient descent later).

```python
def siege_progress(years, determination, terrain_difficulty):
    """Calculate ground gained toward Mirado"""
    return years * determination / terrain_difficulty

ground_gained = siege_progress(20, 0.8, 5.0)
print(f"After 20 years, The Colonel has gained {ground_gained:.1f} units of ground.")
```

**Key insight:** The Colonel has been sieging Mirado for decades. Progress is slow. But it's steady.

---

### Tutorial 6: Importing Pandas and Loading Data
**Colab Skills:** import statements, reading CSV from URL, DataFrame basics (.head(), .shape, .columns)
**Densworld Content:** The Archives—how knowledge is structured, manuscripts as data, the shift from narrative to structured information

*Activity:* Load actual Densworld CSV data for the first time. See how fiction becomes data.

```python
import pandas as pd

BASE_URL = "https://raw.githubusercontent.com/buildLittleWorlds/yeller-quarry-data-science/main/data/"
creatures = pd.read_csv(BASE_URL + "creatures.csv")

print(f"The Archives contain records of {len(creatures)} creatures.")
creatures.head()
```

**Key insight:** The fiction is the ore. The structured data is the refined metal.

---

### Tutorial 7: Exploring DataFrames
**Colab Skills:** Selecting columns, filtering rows, .describe(), .value_counts(), basic aggregations
**Densworld Content:** Yeller Quarry creatures in depth—habitats, danger ratings, metal content, what patterns emerge

*Activity:* Explore the creatures dataset. Find the most dangerous creature. Count creatures by habitat. Start seeing patterns.

```python
# Most dangerous creatures
creatures.sort_values('danger_rating', ascending=False).head()

# Creatures by habitat
creatures['habitat'].value_counts()

# Average danger by habitat
creatures.groupby('habitat')['danger_rating'].mean()
```

**Key insight:** Data reveals what narrative can only hint at. Patterns emerge from structure.

---

### Tutorial 8: Northo and Dead River—The Edges
**Colab Skills:** Multiple DataFrames, merging data, working with missing values
**Densworld Content:** Northo (religion, faith, the far reaches) and Dead River (structure without substance, maps pointing to nothing)

*Activity:* Load multiple datasets. Merge them. Handle the gaps and missing values that represent places that may not exist.

```python
# Some places exist on maps but not in reality
places = pd.read_csv(BASE_URL + "places.csv")
journeys = pd.read_csv(BASE_URL + "journeys.csv")

# Merge to see which places have actually been visited
visited = journeys.merge(places, on='place_id', how='left')

# Dead River has map coordinates but no journey records
dead_river = places[places['name'] == 'Dead River']
```

**Key insight:** Not everything that's named exists. Not everything that exists has a name.

---

### Tutorial 9: Visualization
**Colab Skills:** matplotlib basics, creating plots, customizing charts, saving figures
**Densworld Content:** Mapping the world—visualizing creatures by danger and habitat, showing the geography of data

*Activity:* Create visualizations of Densworld data. Bar charts of creatures. Scatter plots of danger vs. depth.

```python
import matplotlib.pyplot as plt

# Danger ratings by creature
plt.figure(figsize=(10, 6))
creatures.sort_values('danger_rating').plot(kind='barh', x='name', y='danger_rating')
plt.title('Yeller Quarry Creature Danger Ratings')
plt.xlabel('Danger Rating')
plt.tight_layout()
plt.show()
```

**Key insight:** Visualization is cartography for data. It maps what exists.

---

### Tutorial 10: The Three Directions and Your Journey Forward
**Colab Skills:** Capstone review, installing packages, Colab features (GPU, saving, sharing), what to learn next
**Densworld Content:** The cosmology—North (negation), South (pursuit), West (dissolution), no East. How the world fits together. What courses come next.

*Activity:* A mini-capstone that uses all skills learned. Load data, filter, aggregate, visualize. Plus: learn advanced Colab features (GPU toggle, installing packages, saving to Drive).

Final section: Which course should you take next? A guide to the full curriculum based on interests.

```python
# Your journey begins here
# North = Religious analysis → Northo courses (future)
# South = The siege → ML Math with Densworld
# West = Dissolution → Spatial series
# The Quarry = Beginning → Yeller Quarry Data Science

print("Every true journey begins in Yeller Quarry.")
```

**Key insight:** You now know how to use notebooks. You now know what Densworld is. The real exploration begins.

---

## Colab Skills Progression Summary

| Tutorial | Technical Skills | Complexity |
|----------|-----------------|------------|
| 1 | Running cells, text vs code | Absolute beginner |
| 2 | Variables, types, print/f-strings | Beginner |
| 3 | Lists, loops, indexing | Beginner+ |
| 4 | Dictionaries, nested data | Intermediate beginner |
| 5 | Functions, parameters, returns | Intermediate |
| 6 | Imports, pandas intro, CSV loading | Intermediate |
| 7 | DataFrame exploration, filtering, aggregation | Intermediate+ |
| 8 | Multiple DataFrames, merging, missing data | Advanced beginner |
| 9 | Visualization with matplotlib | Intermediate |
| 10 | Capstone, advanced Colab features | Ready for courses |

---

## Densworld Content Progression

| Tutorial | Region/Concept | Key Theme |
|----------|---------------|-----------|
| 1 | Overview | The world exists, fiction as learning |
| 2 | The Capital | Civilization, knowledge, archives |
| 3 | Yeller Quarry | Danger, creatures, patterns (prime numbers) |
| 4 | The Dens | Dissolution, instability, appearance vs reality |
| 5 | Tower of Mirado | The siege, persistence, iterative progress |
| 6 | Archives (concept) | Fiction → data transformation |
| 7 | Yeller Quarry (data) | Patterns in structure |
| 8 | Northo + Dead River | Edges, faith, absence |
| 9 | Cartography (concept) | Visualization as mapping |
| 10 | Cosmology | Three directions, full world view |

---

## Data Needs

The course will use existing Densworld CSVs where possible:
- `creatures.csv` from Yeller Quarry
- `places.csv` from Journeys and Graphs
- `journeys.csv` from Journeys and Graphs

May need small supplementary datasets:
- `regions.csv` — basic info about each region
- `characters.csv` — key characters for reference

---

## Estimated Length

- 10 tutorials
- Each tutorial: 20-40 minutes
- Total: 4-6 hours of content

This positions it as a "weekend course" that gets students ready for the main curriculum.

---

## Connections to Other Courses

After completing Gateway, students are prepared for:

| Interest | Recommended Course |
|----------|-------------------|
| "I want to learn pandas" | Yeller Quarry Data Science |
| "I'm interested in text/NLP" | Capital Archives NLP |
| "I want to understand ML math" | ML Math with Densworld |
| "I want to build things" | Densworld API Course |
| "I like the weird space stuff" | Spatial Series |
| "I want to learn Hugging Face" | HF Series (start with Archivist) |

---

## Next Steps

1. Review this plan
2. Decide on final course title
3. Create `data/` folder with supplementary CSVs if needed
4. Update existing Tutorial 1 to match new structure
5. Write Tutorials 2-10
6. Create STUDENT_GUIDE.md
7. Update README.md with full tutorial table and Colab badges
8. Publish to GitHub
