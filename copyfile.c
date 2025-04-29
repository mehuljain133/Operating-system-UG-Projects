// Write a program to copy files using system calls

#include <fcntl.h>     // open
#include <unistd.h>    // read, write, close
#include <stdio.h>     // perror
#include <stdlib.h>    // exit

#define BUFFER_SIZE 1024

int main(int argc, char *argv[]) {
    int src_fd, dest_fd, n;
    char buffer[BUFFER_SIZE];

    if (argc != 3) {
        write(2, "Usage: ./copy <source_file> <destination_file>\n", 48);
        exit(1);
    }

    // Open source file
    src_fd = open(argv[1], O_RDONLY);
    if (src_fd < 0) {
        perror("Error opening source file");
        exit(1);
    }

    // Open/create destination file
    dest_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (dest_fd < 0) {
        perror("Error opening/creating destination file");
        close(src_fd);
        exit(1);
    }

    // Read from source and write to destination
    while ((n = read(src_fd, buffer, BUFFER_SIZE)) > 0) {
        if (write(dest_fd, buffer, n) != n) {
            perror("Error writing to destination file");
            close(src_fd);
            close(dest_fd);
            exit(1);
        }
    }

    if (n < 0) {
        perror("Error reading source file");
    }

    close(src_fd);
    close(dest_fd);

    return 0;
}
