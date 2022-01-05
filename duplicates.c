/*
Exercício feito no whiteboard com os
recrutadores do mercado livre

Foi soilicitado para verificar números duplicados
em um array de ints

Nessa implementação feita em C
provavelmente daria um timeout
devido ao while dentro do while,
sendo necessário percorrer o array
len(array) vezes
(com percurso menor a cada vez)
*/

#include "stdio.h"
#include "stdbool.h"
#include <stdlib.h>

bool	verify_duplicates(int *array, int len)
{
	int	i;
	int	j;

	i = 0;
	while (array[i] != '\0')
	{
		j = i + 1;
		while (array[i] != array[j] && array[j])
			j++;
		if (j < len)
			return (true);
		i++;
	}
	return (false);
}

int	*do_atoi(int argc, char **argv)
{
	int	i;
	int	*array;

	array = malloc(sizeof(int) * argc);
	i = 0;
	while (i < argc - 1)
	{
		array[i] = atoi(argv[i + 1]);
		i++;
	}
	array[i] = '\0';
	return (array);
}

int	main(int argc, char **argv)
{
	int	*array;

	array = do_atoi(argc, argv);
	printf("%d\n", verify_duplicates(array, argc - 1));
	free(array);
}
