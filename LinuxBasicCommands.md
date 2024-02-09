## System Commands

### Displaying System Information
~~~
$ hostname

Prints the hostname or domain name of the current system.
~~~
~~~
$ uname

Prints the kernel name, version, and architecture of the current system.
~~~
~~~
$ uname -r

Prints the version of the Linux kernel running on the system.
~~~
~~~
$ history

Lists the commands executed in the past in the current terminal session.
~~~
~~~
$ exit

Closes the current terminal session.
~~~

### Displaying Disk Information
~~~
$ df

Displays information about the file systems mounted on the system, including the amount of free and used space.
~~~
~~~
$ du

Estimates the amount of disk space used by files and directories.
~~~
~~~
$ du -h /

Displays the size of the root directory in a human-readable format.
~~~

### Displaying Memory Information
~~~
$ top

Displays information about running processes, including their memory usage.
~~~
~~~
$ free -m

Displays information about the amount of free and used memory on the system, in megabytes.
~~~
~~~
$ du -sh filename

Displays the size of the specified file in a human-readable format.
~~~
~~~
$ which ls

Displays the location of the `ls` command on the system.
~~~
~~~
$ which python

Displays the location of the Python interpreter on the system.
~~~
~~~
$ ps -aux

Lists all running processes on the system, along with detailed information about each process.
~~~
~~~
$ sudo kill -9 processid

Terminates the process with the specified process ID (PID). This command requires root privileges.
~~~
~~~
$ sudo fdisk

Displays information about disk partitions and allows you to manage them. This command requires root privileges.
~~~

## Directory and File Management
~~~
$ pwd

Prints the current working directory.
~~~
~~~
$ cd <directory_name, absolute or relative path>

Changes to the specified directory.
~~~
~~~
$ cd ..

Moves up one directory in the directory tree.
~~~
~~~
$ cd ~

Changes to the home directory.
~~~

## Echo Command
~~~
$ echo "hello world"

Prints "hello world" on the terminal.
~~~
~~~
$ echo $SHELL

Prints the path to the current shell.
~~~

## Creating a Directory
~~~
$ mkdir <directory name>

Creates a new directory with the specified name.
~~~
~~~
$ ls

Lists the contents of the current directory.
~~~
~~~
$ mkdir -p dir1/dir2/dir3

Creates a nested directory structure, if necessary.
~~~

## Removing a Directory
~~~
$ rmdir dirname

Removes the specified directory, if it is empty.
~~~
~~~
$ rmdir -rf dirname

Recursively removes the specified directory, including all its contents.
~~~

## Deleting a File
~~~
$ rm -rf today1.txt

Deletes the specified file or directory.
~~~

## Clearing the Terminal
~~~
$ clear

Clears the terminal screen.
~~~

## ls Command
~~~
$ ls -l

Lists the contents of the current directory in long format, showing file permissions, owner, size, and modification date.
~~~
~~~
$ ls -la

Lists all files in the current directory, including hidden files.
~~~
~~~
$ ls lrt

Lists the contents of the current directory in reverse order.
~~~

## Creating a File
~~~
$ touch <filename>

Creates an empty file with the specified name.
~~~
~~~
$ touch file1, file2, file3

Creates multiple files simultaneously.
~~~
~~~
$ rm -rf file1, file2, file3

Deletes multiple files simultaneously.
~~~

## cat Command
~~~
$ cat filename

Displays the contents of the specified file.
~~~
~~~
$ cat > filename.txt

Creates a new file and enters insert mode. Press Ctrl+D to save and exit.
~~~
~~~
$ cat >> filename.txt

Appends the contents of standard input to the specified file.
~~~
~~~
$ cat > filename.txt

Truncates the specified file and enters insert mode. Press Ctrl+D to save and exit.
~~~
---
## Copy and Paste Commands:

- `cp <sourcefile> <destinationfile>`: Copies the file from the source to the destination.

- `cp -r <source> <destination>`: Copies the directory recursively to the destination.

- `mv <source> <destination>`: Moves the file from the source to the destination. If the destination is a folder, the file is renamed instead of being moved.

- `mv -r <source> <destination>`: Moves the directory recursively to the destination.

- `mv <existingfilename> <newfilename>`: Renames the file or folder to the new filename.


## Getting Help:

- `man commandName`: Displays the documentation for the specified command.

- `ls --help`: Provides help for the `ls` command, including a list of available options.


## File Manipulation Commands:

- `head filename`: Displays the first 10 lines of a file.

- `tail filename`: Displays the last 10 lines of a file.

- `head -n filename 20`: Displays the first 20 lines of a file.

- `tail -n filename 25`: Displays the last 25 lines of a file.

- `less filename`: Views the contents of a file. Press `q` to exit.


## Searching for Patterns in a File:

- `grep pattern filename`: Finds all occurrences of the specified pattern in a file.

- `grep -n pattern filename`: Also prints the line numbers of the matching lines.

- `grep -wn apple filename`: Matches only whole words, not partial matches.

- `grep -i pattern filename`: Performs a case-insensitive search.

- `grep -v pattern filename`: Excludes lines containing the specified pattern.

- `grep -A3 pattern filename`: Displays the specified pattern and the three lines after it.

- `grep -B3 pattern filename`: Displays the specified pattern and the three lines before it.

- `grep -A3 -B3 filename`: Displays the specified pattern, along with the three lines before and after it.

- `grep -r pattern .`: Searches for the specified pattern in all files in the current directory.

- `grep -nr pattern .`: Also prints the line numbers of the matching lines.


## Comparing Files:

- `diff filename1 filename2`: Compares the contents of two files and displays the differences.

- `cmp file1 file2`: Compares two files and reports only the first difference.


## Counting File Contents:

- `wc -w filename`: Counts the number of words in a file.

- `wc -L filename`: Counts the length of the longest line in a file.

- `wc -l filename`: Counts the number of lines in a file.

- `wc -c filename`: Counts the number of characters in a file.

- `wc -m filename`: Counts the number of bytes in a file.


## Networking Commands:

- `ping codeeditors.com`: Sends data packets to the specified host and displays the response time.

- `zip zipped_file.zip file1 file2 file3 file4`: Zips the specified files into a single ZIP archive.

- `unzip zipped_file.zip`: Unzips the specified ZIP archive, extracting its contents.


## Downloading Files from the Internet:

- `wget <download link>`: Downloads the specified file from the internet.

- `wget -O output.tar.gz <link downloadable>`: Saves the downloaded file to the specified output filename.

- `wget -P <locationtoSave> <link downloadable>`: Downloads the file to the specified location.

- `curl -o <outputfilename> <link downloadable>`: Downloads the specified file from the internet using the `curl` command.


## Changing File Permissions:

- `chmod <permissions> <filename>`: Changes the permissions of the specified file or directory.