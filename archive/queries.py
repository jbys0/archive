"""Questions we ask the Archive.

YOU IMPLEMENT THIS FILE.

Every function here takes `records` — a list of record dicts as produced by
load_archive — and answers one question about the collection. None of them
touch a file. None of them print anything. They return values.

Keep in mind from Week 2: the structure you are given decides which of these
is cheap and which is expensive. All of these are linear scans over a list.
Note in your README which one would be instant with a dictionary instead.
"""


def count_before(records, year):
    """How many manuscripts were written strictly BEFORE `year`?

    `year` is an int. Record years may be strings from the file — convert.

    Returns int.
    """
    return sum(int(record["year"]) < year for record in records

def find_by_city(records, city):
    """Every record whose city matches `city`, case-insensitively.

    Order is preserved: the records come back in the order they appear in
    `records`.

    Returns list of dicts (empty list if none match).
    """
city_lower = city.lower()
matches = []
for record in records:
    if record["city"].lower() == city_lower:
        matches.append(record)
return matches

def oldest(records):
    """The record with the smallest year.

    An empty list returns None — not an error, not a crash. Deciding what
    "the oldest of nothing" means is your job, and the answer is None.

    If two records tie on year, return the one that appears FIRST.

    Returns dict or None.
    """
if not records:
    return None
oldest_record = records[0]
for record in records[1:]:
    if int(record["year"]) < int(oldest_record["year"]):
        oldest_record = record
return oldest_record

def cities_summary(records):
    """How many manuscripts come from each city?

    Returns a dict mapping city name to count. A city with zero manuscripts
    does not appear as a key at all — do not pre-fill from KNOWN_CITIES.

    Use the city spelling exactly as it appears in the records.

    Returns dict.
    """
summary = {}
for record in records:
    city = record["city"]
    summary[city] = summary.get(city, 0) + 1
return summary

