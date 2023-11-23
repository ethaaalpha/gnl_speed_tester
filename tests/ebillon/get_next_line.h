/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ebillon <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/25 10:26:09 by ebillon           #+#    #+#             */
/*   Updated: 2022/11/25 10:26:12 by ebillon          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# include <stdlib.h>
# include <unistd.h>
# include <stdlib.h>
# include <fcntl.h>

char	*get_next_line(int fd);
char	*ft_realloc(char *src, char *add, int lenght);
char	*errors(char **res);

int		readbuffer(int fd, char buffer[BUFFER_SIZE + 1]);
int		ft_strlen(char *s);
int		count_to_nl(char *buff, int *c);

#endif
