### Day 01

1. **Linux Brief History Introduction**
   - Resource: [YouTube - Linux Brief History](https://www.youtube.com/watch?v=ShcR4Zfc6Dw&t=1s)
     - This video provides insights into the history and evolution of Linux, offering a foundational understanding of the operating system.

2. **Linux Basics Introduction**
   - Resources: 
     - [YouTube - Linux Basics Introduction](https://www.youtube.com/watch?v=pTFZFxd4hOI&t=1707s)
     - This tutorial covers fundamental Linux commands essential for navigating and managing files and directories in a Linux environment.

3. **Virtual Box Installation**
   - Command: 
     ```
     sudo apt install virtualbox
     ```
     - Installs VirtualBox, a powerful open-source virtualization software that allows users to create and manage virtual machines on their systems.

4. **Download Deb File from Oracle VM and Run**
   - Command:
     ```
     sudo dpkg -i virtualbox-7.0_7.0.14-161095~Ubuntu~focal_amd64.deb
     ```
     - Downloads and installs the VirtualBox .deb file. Note that dependency issues may occur during installation, requiring the use of `sudo apt -f install` to fix broken dependencies.

5. **Setup Virtual Environment (Hypervisors)**
   - Resource: [YouTube - Setting Up Virtual Environment](https://www.youtube.com/watch?v=wX75Z-4MEoM&t=3s)
     - This tutorial guides users through the process of setting up virtual environments with hypervisors, allowing for isolated experimentation and development.

6. **Basic Commands**
   1. `echo`: Prints a message to the terminal.
   2. `whoami`: Displays the current username.
   3. `echo $0`: Shows the location of the current bash program.
   4. `history`: Lists the history of commands used.
   5. `apt`: Advanced Package Tool for package management.
      - `apt list`: Lists all available packages.
      - `apt update`: Updates the package database.
      - `apt install <package>`: Installs a package.
      - `apt remove <package>`: Removes a package.
   6. `pwd`: Prints the present working directory.
   7. `ls`: Lists files and directories in the present working directory.
      - `ls -1`: Lists one entry per line.
      - `ls -l`: Provides detailed information about files and directories.
      - `ls -la`: Lists all entries, including hidden files.
   8. `cd <path>`: Changes directory.
      - `cd ..`: Moves one directory up.
      - `cd ~`: Navigates to the home directory.
   9. `mkdir <directory>`: Creates a new directory.
   10. `mv <file> <destination>`: Moves files to a specified destination.
   11. `touch <file1> <file2> <file3...>`: Creates files with specific extensions.
   12. `rm <file1>`: Removes files.
       - `rm file*`: Deletes files whose names start with "file".
       - `rm -r <directory>`: Deletes a directory.
   13. `cat <filename>`: Views the content of a file.
   14. `more <filename>`: Views the content of large files.
   15. `less <filename>`: Scrolling view for file content.
   16. `head <lines>`: Displays the first few lines of a file.
   17. `tail <lines>`: Displays the last few lines of a file.

7. **Redirection**
   - Example:
     ```
     cat file.txt > file2.txt
     ```
     - Redirects the output from the terminal screen to `file2.txt`.

This documentation aims to provide a comprehensive guide to Day 01 of the training sessions, covering Linux basics, VirtualBox installation, virtual environment setup, and essential Linux commands. It includes links to relevant resources for further exploration and understanding.
