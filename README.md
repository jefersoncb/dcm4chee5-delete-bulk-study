# PACS dcm4chee5 Bulk Study Deletion

## What it does
This Python script automates the bulk deletion of studies in the PACS dcm4chee5 by specifying the date.

### Features
- Selects the desired PACS.
- Allows date input in the formats: `YYYYMMDD`, `YYYYMMDD-YYYYMMDD`, or `-YYYYMMDD`.
- Searches for all studies within the specified date range.
- Rejects and deletes the studies.

## Configuration
In the `PACS_LIST` section of the script, insert:
- PACS Name
- AE Title
- IP Address

## Execution
To run the script, execute the following command in the terminal:

```bash
python3 reject_remove.py
```

## Compatibility
- Python must be installed on the machine.
- Tested on **dcm4chee5 version 5.24.1**.
