# Log-Archive-Tool

A simple CLI tool to compress and archive log files or directories on demand, helping keep your system clean and organized.

## Overview

`Log-Archive-Tool` is a command-line utility designed to help you manage and maintain log files on your system. It compresses a specified log file or all log files from a specified directory (such as `/var/log` on Unix-based systems) into a `.tar.gz` archive and stores them in a new directory. This helps free up space while keeping logs available for future reference in a compressed format.

## Features

- Accepts a log file **or** a log directory as a command-line argument
- Compresses the specified file or all files in the specified directory into a `.tar.gz` archive
- Stores the archive in a new `archives` directory
- Logs the date and time of each archive operation to `archive_log.txt`

## Usage

```sh
python log-archive.py <path>
```

- `<path>`: The path to the log file **or** directory you want to archive (e.g., `/var/log/syslog` or `/var/log`).

### Examples

Archive a single log file:

```sh
python log-archive.py /var/log/syslog
```

Archive all files in a directory:

```sh
python log-archive.py /var/log
```

This will compress the specified file or all files in the directory and store the archive in the `archives` directory, e.g., `logs_archive_20240816_100648.tar.gz`.

## Archive Naming Convention

Archives are named using the format:

```
logs_archive_YYYYMMDD_HHMMSS.tar.gz
```

## Logging

Each archive operation logs the date, time, and the archived path to `archive_log.txt` for tracking purposes.

## Requirements

- Python 3.x
- Access to the file or directory you wish to archive

## Advanced Features (Optional)

- Emailing the user updates on the archive
- Sending the archive to a remote server or cloud storage

## Learn More

- [tar command documentation](https://www.gnu.org/software/tar/manual/tar.html)

---

Feel free to contribute or suggest improvements!
