# Log-Archive-Tool

A simple CLI tool to compress and archive log files on a schedule, helping keep your system clean and organized.

## Overview

`Log-Archive-Tool` is a command-line utility designed to help you manage and maintain log files on your system. It compresses log files from a specified directory (such as `/var/log` on Unix-based systems) into a `.tar.gz` archive and stores them in a new directory. This helps free up space while keeping logs available for future reference in a compressed format.

## Features

- Accepts the log directory as a command-line argument
- Compresses all logs in the specified directory into a `.tar.gz` archive
- Stores the archive in a new directory
- Logs the date and time of each archive operation

## Usage

```sh
log-archive <log-directory>
```

- `<log-directory>`: The path to the directory containing the log files you want to archive (e.g., `/var/log`).

### Example

```sh
log-archive /var/log
```

This will compress the logs in `/var/log` and store the archive in a new directory, e.g., `logs_archive_20240816_100648.tar.gz`.

## Archive Naming Convention

Archives are named using the format:

```
logs_archive_YYYYMMDD_HHMMSS.tar.gz
```

## Logging

Each archive operation logs the date and time to a log file for tracking purposes.

## Requirements

- Python 3.x (or your chosen language)
- Access to the log directory you wish to archive

## Advanced Features (Optional)

- Emailing the user updates on the archive
- Sending the archive to a remote server or cloud storage

## Learn More

- [tar command documentation](https://www.gnu.org/software/tar/manual/tar.html)

---

Feel free to contribute or suggest improvements!
