# Dataset Reference Card: Gateway to Densworld

## Course Overview

**Gateway to Densworld** teaches Python and Google Colab through the lens of Densworld fiction. Students progress from running their first code cell to exploring DataFrames and visualizations.

**Skills Taught:** Python basics (variables, lists, dictionaries, functions), pandas fundamentals (loading CSVs, filtering, groupby, merging), matplotlib visualization

**Narrative Frame:** A journey through Densworld's regions—from the Capital Archives to Yeller Quarry to the Tower of Mirado—each teaching a programming concept.

---

## Datasets Used

### Primary Datasets (Loaded from GitHub)

| Dataset | Rows | Description | Used In |
|---------|------|-------------|---------|
| `creatures.csv` | 50 | Creature catalog: name, habitat, danger rating, size, diet, defense | Tutorials 6, 7, 9, 10 |
| `crews.csv` | 12 | Trapping crews: name, leader, size, specialty, years active | Tutorial 6 |
| `catches.csv` | 100+ | Catch records: crew, creature, date, location, outcome | Tutorial 6 |
| `traps.csv` | 20 | Trap designs: name, mechanism, target creatures | Tutorial 6 (exercise) |
| `densworld_places.csv` | 100+ | World locations: name, region, description, coordinates | Tutorial 8 |
| `densworld_journey_steps.csv` | 200+ | Journey waypoints: journey ID, step, location, notes | Tutorial 8 |

### Local Reference Datasets

| Dataset | Description | Purpose |
|---------|-------------|---------|
| `regions.csv` | 12 major regions with themes and characters | Narrative reference |
| `characters.csv` | 27 key characters with roles and appearances | Narrative reference |
| `tutoring_sessions.csv` | 50 tutoring sessions from Hilly Dale | Practice dataset |

### Event Log (Living Ledger)

| File | Size | Description |
|------|------|-------------|
| `EVENT_LOG.jsonl` | 773 events | Full Densworld event log |
| `ledger_lite.py` | Query module | Python module for event queries |

---

## Data Loading Pattern

All notebooks use the central densworld-datasets repository:

```python
import pandas as pd

BASE_URL = "https://raw.githubusercontent.com/buildLittleWorlds/densworld-datasets/main/data/"
creatures = pd.read_csv(BASE_URL + "creatures.csv")
```

---

## Canonical Events (Seeded to Living Ledger)

This course establishes 7 canonical events in Densworld history:

| Event ID | Year | Type | Description |
|----------|------|------|-------------|
| EV-0700-001 | 700 | archive_accession | Capital Archives formally established |
| EV-0820-001 | 820 | expedition_launch | Siege of Mirado begins (The Colonel) |
| EV-0835-001 | 835 | crew_formed | The Boss forms legendary trapping crew |
| EV-0855-001 | 855 | expedition_launch | Redmane Expedition launches |
| EV-0855-002 | 855 | disappearance | The Boss disappears during Redmane |
| EV-0880-001 | 880 | manuscript_written | Bagbu Olt writes "The Road's Four Feet" |
| EV-0890-001 | 890 | discovery | Yeller numbers (primes 2,3,5,7,11) discovered |

### Cascaded Events (Auto-generated)

| Event ID | Type | Parent | Description |
|----------|------|--------|-------------|
| EV-0820-002 | archive_accession | EV-0820-001 | Siege records accessioned |
| EV-0835-002 | archive_accession | EV-0835-001 | Boss's trap designs cataloged |
| EV-0855-003 | investigation_launched | EV-0855-002 | Investigation into Boss's disappearance |
| EV-0855-004 | archive_accession | EV-0855-001 | Redmane Expedition records accessioned |
| EV-0880-002 | archive_accession | EV-0880-001 | "The Road's Four Feet" accessioned |

---

## Key Entities

### Characters Introduced

| Character | Role | Region | First Appears |
|-----------|------|--------|---------------|
| Chief Archivist Mink | Archives overseer | Capital | Tutorial 2 |
| The Boss | Legendary trapper | Yeller Quarry | Tutorial 3 |
| The Colonel | Siege commander | Mirado | Tutorial 5 |
| Fincho | Colonel's lieutenant | Mirado | Tutorial 5 |
| Bagbu Olt | Wandering mapmaker | Multiple | Tutorial 10 |

### Regions Explored

| Region | Tutorial | Theme | Key Concept |
|--------|----------|-------|-------------|
| The Capital | 2 | Knowledge, civilization | Variables, f-strings |
| Yeller Quarry | 3, 6, 7 | Danger, creatures | Lists, loops, DataFrames |
| The Dens | 4 | Dissolution, instability | Dictionaries |
| Tower of Mirado | 5 | Pursuit, persistence | Functions |
| Northo | 8 | Faith, edges | Merging, missing data |
| Dead River | 8 | Absence, paradox | NaN values |

---

## Skill Progression

| Tutorial | Python/Pandas Skill | Densworld Content |
|----------|---------------------|-------------------|
| 1 | Running cells, basics | World overview |
| 2 | Variables, f-strings | The Capital |
| 3 | Lists, loops | Yeller Quarry creatures |
| 4 | Dictionaries | The Dens |
| 5 | Functions | Siege of Mirado |
| 6 | pandas, CSV loading | Fiction → data transformation |
| 7 | Filtering, groupby | Creature data analysis |
| 8 | Merging, NaN handling | Edges of the world |
| 9 | matplotlib basics | Data visualization |
| 10 | Capstone review | Cosmology, next steps |
| 11 | Event log queries | Living Ledger exploration |

---

## Living Ledger Integration

Tutorial 11 introduces the event log system:

```python
import sys
sys.path.insert(0, 'data')
import ledger_lite as ledger
import pandas as pd

# Get statistics
stats = ledger.stats()
print(f"Total events: {stats['total_events']}")

# Query events by type
expeditions = ledger.query_events(event_type='expedition_launch')
df = pd.DataFrame(expeditions)

# Query events by actor
boss_events = ledger.query_events(actor='the_boss')

# Trace causal chains
descendants = ledger.get_descendants('EV-0855-001')
```

---

## Connections to Other Courses

| After Gateway... | Recommended Course | Shared Entities |
|------------------|-------------------|-----------------|
| Want more pandas? | Yeller Quarry Data Science | creatures, crews, catches |
| Interested in text? | Capital Archives NLP | Mink, Archives |
| Want ML math? | ML Math with Densworld | Mirado siege metaphor |
| Like the world? | Spatial Series | Dens, boundary phenomena |

---

## Dataset Sources

| Dataset | Origin | Living Ledger Status |
|---------|--------|---------------------|
| creatures.csv | Hand-crafted | Static (taxonomic) |
| crews.csv | Hand-crafted | Partially event-derived |
| catches.csv | Hand-crafted | Could be event-derived |
| densworld_places.csv | Encyclopedia-derived | Static (geographic) |
| EVENT_LOG.jsonl | Living Ledger | Event-based (773 events) |

---

*Reference card created: December 2024*
*Course status: Living Ledger integrated (Tutorial 11 added)*
