#!/usr/bin/env python3
"""
Living Ledger Lite - Query-only module for course notebooks.

This is a simplified version of ledger.py designed to be copied into
course repositories. It only reads events (no logging/modification).

Usage in a notebook:
    import ledger_lite as ledger

    # Query events
    deaths = ledger.query_events(event_type='death')
    grigsu = ledger.query_events(actor='grigsu_haldo')
    events_1847 = ledger.query_events(year=1847)

    # Get as DataFrame
    import pandas as pd
    df = pd.DataFrame(deaths)
"""

import json
from pathlib import Path
from typing import Iterator, Optional


# Find EVENT_LOG.jsonl relative to this file
# Works whether placed in course root or data/ folder
def _find_event_log():
    """Locate EVENT_LOG.jsonl in current directory or data/ subdirectory."""
    candidates = [
        Path.cwd() / "EVENT_LOG.jsonl",
        Path.cwd() / "data" / "EVENT_LOG.jsonl",
        Path(__file__).parent / "EVENT_LOG.jsonl",
        Path(__file__).parent / "data" / "EVENT_LOG.jsonl",
        Path(__file__).parent.parent / "EVENT_LOG.jsonl",
    ]
    for p in candidates:
        if p.exists():
            return p
    raise FileNotFoundError(
        "EVENT_LOG.jsonl not found. Expected in current directory or data/ folder."
    )


def read_events() -> Iterator[dict]:
    """Read all events from the event log."""
    event_log = _find_event_log()
    with open(event_log, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def query_events(
    event_type: str = None,
    year: int = None,
    date_start: str = None,
    date_end: str = None,
    location: str = None,
    actor: str = None,
    parent: str = None,
    source_type: str = None,
) -> list[dict]:
    """
    Query events with optional filters.

    Args:
        event_type: Filter by event type (e.g., 'death', 'expedition_launch')
        year: Filter by year (e.g., 1847)
        date_start: Filter events on or after this date (YYYY-MM-DD)
        date_end: Filter events on or before this date (YYYY-MM-DD)
        location: Filter by location (partial match)
        actor: Filter by actor (must be in actors list)
        parent: Filter by parent event ID
        source_type: Filter by source type ('course', 'cascade', etc.)

    Returns:
        List of matching events as dictionaries
    """
    results = []

    for event in read_events():
        # Type filter
        if event_type and event.get("type") != event_type:
            continue

        # Year filter
        if year:
            event_date = event.get("date", "")
            if not event_date.startswith(str(year)):
                # Handle 4-digit years with leading zeros (e.g., "0891")
                event_year = event_date.split("-")[0] if "-" in event_date else ""
                if int(event_year) != year if event_year.isdigit() else True:
                    continue

        # Date range filters
        event_date = event.get("date", "")
        if date_start and event_date < date_start:
            continue
        if date_end and event_date > date_end:
            continue

        # Location filter (partial match)
        if location:
            event_location = event.get("location", "")
            if location.lower() not in event_location.lower():
                continue

        # Actor filter
        if actor:
            actors = event.get("actors", [])
            if actor not in actors:
                continue

        # Parent filter
        if parent and event.get("parent") != parent:
            continue

        # Source type filter
        if source_type:
            source = event.get("source", {})
            if source.get("type") != source_type:
                continue

        results.append(event)

    return results


def get_event(event_id: str) -> Optional[dict]:
    """Get a single event by ID."""
    for event in read_events():
        if event.get("event_id") == event_id:
            return event
    return None


def get_descendants(event_id: str) -> list[dict]:
    """Get all events that descend from a given event (children, grandchildren, etc.)."""
    all_events = list(read_events())

    def _find_children(parent_id):
        children = []
        for e in all_events:
            if e.get("parent") == parent_id:
                children.append(e)
                children.extend(_find_children(e["event_id"]))
        return children

    return _find_children(event_id)


def get_ancestors(event_id: str) -> list[dict]:
    """Get all ancestor events (parent, grandparent, etc.)."""
    all_events = {e["event_id"]: e for e in read_events()}
    ancestors = []

    current = all_events.get(event_id)
    while current and current.get("parent"):
        parent = all_events.get(current["parent"])
        if parent:
            ancestors.append(parent)
            current = parent
        else:
            break

    return ancestors


def stats() -> dict:
    """Get summary statistics about the event log."""
    events = list(read_events())

    by_type = {}
    by_year = {}
    actors = set()
    locations = set()

    for e in events:
        # Count by type
        t = e.get("type", "unknown")
        by_type[t] = by_type.get(t, 0) + 1

        # Count by year
        date = e.get("date", "")
        year = date.split("-")[0] if "-" in date else "unknown"
        by_year[year] = by_year.get(year, 0) + 1

        # Collect actors and locations
        actors.update(e.get("actors", []))
        if e.get("location"):
            locations.add(e["location"])

    return {
        "total_events": len(events),
        "by_type": by_type,
        "by_year": by_year,
        "unique_actors": len(actors),
        "unique_locations": len(locations),
    }


# Convenience function for notebooks
def to_dataframe(events: list[dict]):
    """Convert events to a pandas DataFrame. Requires pandas."""
    try:
        import pandas as pd
        return pd.DataFrame(events)
    except ImportError:
        raise ImportError("pandas is required for to_dataframe(). Run: pip install pandas")
