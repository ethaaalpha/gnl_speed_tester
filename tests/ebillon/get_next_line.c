/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ebillon <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/11/25 10:26:19 by ebillon           #+#    #+#             */
/*   Updated: 2022/11/25 10:26:21 by ebillon          ###   ########lyon.fr   */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*make_line(int fd, char *res)
{
	static char	buff[BUFFER_SIZE + 1] = "\0";
	static int	i = 0;

	if (buff[i] == '\n')
		return (ft_realloc(res, &buff[i++], 1));
	while (buff[i] != '\n')
	{
		if (buff[i] == '\0')
		{
			if (readbuffer(fd, buff) == 1)
				return (errors(&res));
			i = 0;
			if (buff[i] == '\0')
				break ;
		}
		res = ft_realloc(res, &buff[i], count_to_nl(&buff[i], &i));
		if (buff[i] == '\n')
		{
			res = ft_realloc(res, &buff[i++], 1);
			break ;
		}
	}
	return (res);
}

char	*get_next_line(int fd)
{
	char	*res;

	res = NULL;
	if (fd < 0 || BUFFER_SIZE < 0)
		return (NULL);
	return (make_line(fd, res));
}
