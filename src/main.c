#include "get_next_line.h"
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv) {
    (void) argc;
    int fd;
    fd = open(argv[1], O_RDONLY);
    printf("%s", get_next_line(fd));
    close(fd);
}