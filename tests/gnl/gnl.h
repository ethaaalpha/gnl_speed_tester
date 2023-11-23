#ifndef GNL_H
# define GNL_H

# include <stdlib.h>
# include <stddef.h>
# include <stdio.h>
# include <unistd.h>

char	*get_next_line(int fd);
char	*read_the_line(char *buffer, int *end_file, int fd);
char	*next_line(char *buffer, int *end_file, int *i, int fd);
void	clean_buf(char *buffer, int *end_file);
char	*first_read(char *buffer, int *i);
unsigned int	next_line_len(char *buffer);
void	*ft_memmove(void *dst, const void *src, size_t len);
char	*ft_strjoin(char *s1, char *s2);
size_t	ft_strlen(const char *str);

#endif
