#!/usr/bin/env python3
import argparse
import os
import tarfile
import datetime
import shutil

LOG_FILE = 'archive_log.txt'
ARCHIVE_DIR = 'archives'


def create_archive(target_path):
    # Ensure the archive directory exists
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    # Create archive filename with timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    archive_name = f'logs_archive_{timestamp}.tar.gz'
    archive_path = os.path.join(ARCHIVE_DIR, archive_name)

    # Create tar.gz archive
    with tarfile.open(archive_path, 'w:gz') as tar:
        if os.path.isfile(target_path):
            tar.add(target_path, arcname=os.path.basename(target_path))
        elif os.path.isdir(target_path):
            for filename in os.listdir(target_path):
                file_path = os.path.join(target_path, filename)
                if os.path.isfile(file_path):
                    tar.add(file_path, arcname=filename)
        else:
            raise ValueError(f"{target_path} is neither a file nor a directory.")

    return archive_path, timestamp


def log_archive_operation(archive_path, timestamp, target_path):
    with open(LOG_FILE, 'a') as f:
        f.write(f'[{timestamp}] Archived {target_path} to {archive_path}\n')


def main():
    parser = argparse.ArgumentParser(description='Compress and archive a log file or all log files from a directory.')
    parser.add_argument('path', help='Path to the log file or directory to archive')
    args = parser.parse_args()

    target_path = args.path

    if not os.path.exists(target_path):
        print(f'Error: {target_path} does not exist.')
        return

    try:
        archive_path, timestamp = create_archive(target_path)
        log_archive_operation(archive_path, timestamp, target_path)
        print(f'{target_path} archived to {archive_path}')
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main() 