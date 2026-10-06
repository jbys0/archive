"""Reading and writing the Archive file.

YOU IMPLEMENT THIS FILE.

The file format is CSV with no header row. One record per line, five fields
separated by commas, in this order:

    id,title,city,year,condition
    MS001,Tarikh al-Sudan,Timbuktu,1655,fragile

Remember Session 1: a file is one long line of characters. The comma
separates fields; the newline separates records. Nothing else is doing
any work.
"""

from archive.errors import MalformedRecordError
from archive.validation import validate_record

FIELD_NAMES = ["id", "title", "city", "year", "condition"]


def parse_line(line):
    """Turn one CSV line into a dict with the five FIELD_NAMES as keys.

    Whitespace around the line (including the trailing newline) is stripped.
    Field values are stripped too.

    If the line does not split into exactly 5 fields, raise
    MalformedRecordError. Do not guess, do not pad with blanks — a line with
    four fields is not a record with an empty one, it is a broken line, and
    the difference matters when you report it to whoever typed it.

    Returns dict.
    """
    line = line.strip()
    fields = [field.strip() for field in line.split(",")]

    if len(fields) != 5:
        raise MalformedRecordError("Expected exactly 5 fields")

    return dict(zip(FIELD_NAMES, fields))

def load_archive(path):
    """Read the file at `path` and return (valid_records, rejected_lines).

    valid_records   list of dicts that passed validate_record
    rejected_lines  list of the ORIGINAL line strings that did not — either
                    because they were malformed, or because validation
                    rejected them

    A file that does not exist is not an error. It means the archive is new.
    Return ([], []) and DO NOT raise. Your program must start on a machine
    where nobody has saved anything yet.

    Blank lines are skipped silently.

    Returns (list, list).
    """
    valid_records = []
    rejected_lines = []

    try:
        with open(path, "r") as file:
            for line in file:
                if not line.strip():
                    continue

                try:
                    record = parse_line(line)
                except MalformedRecordError:
                    rejected_lines.append(line)
                    continue

                reasons = validate_record(record)

                if reasons:
                    rejected_lines.append(line)
                else:
                    valid_records.append(record)

    except FileNotFoundError:
        return [], []

    return valid_records, rejected_lines

def save_archive(path, records):
    """Write every record to `path` as CSV, one per line, no header.

    Field order is FIELD_NAMES. The file is overwritten, not appended to.

    Returns None.
    """
    with open(path, "w") as file:
        for record in records:
            values = [str(record[field]) for field in FIELD_NAMES]
            file.write(",".join(values) + "\n")
