/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ebillon <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/25 10:26:32 by ebillon           #+#    #+#             */
/*   Updated: 2022/11/25 10:26:32 by ebillon          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

int	readbuffer(int fd, char buffer[BUFFER_SIZE + 1])
{
	int		r_out;

	r_out = read(fd, buffer, BUFFER_SIZE);
	if (r_out == 0)
		buffer[0] = '\0';
	if (r_out < 0)
		return (1);
	buffer[r_out] = '\0';
	return (0);
}

int	ft_strlen(char *s)
{
	int	i;

	i = 0;
	if (!s)
		return (0);
	while (s[i] != '\n' && s[i])
		i++;
	return (i);
}

int	count_to_nl(char *buff, int *c)
{
	int	i;
	int	j;

	i = 0;
	j = 0;
	while (buff[j] != '\n' && buff[j++])
		i++;
	*c += i;
	return (i);
}

char	*ft_realloc(char *src, char *add, int lenght)
{
	char	*res;
	char	*temp;
	int		i;
	int		j;

	temp = src;
	i = 0;
	j = 0;
	res = malloc(sizeof(char) * (ft_strlen(src) + lenght + 1));
	if (!res)
	{
		if (src)
			free(src);
		return (NULL);
	}
	if (src)
		while (src[j])
			res[i++] = src[j++];
	while (lenght--)
		res[i++] = *add++;
	res[i] = '\0';
	if (temp)
		free(temp);
	return (res);
}

char	*errors(char **res)
{
	if (*res)
		free(*res);
	return (NULL);
}
