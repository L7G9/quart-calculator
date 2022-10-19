class Calculator:
    """A class to represent a simple Calculator.

    ...

    Methods
    -------
    add(a, b)
        Adds two numbers together.
    subtract(a, b)
        Subtracts one number from another.
    multiply(a, b)
        Multiplies two numbers togther.
    divide(a, b)
        Divides one number by another.
    sum(list)
        Finds total of a list of numbers added together.
    mean(list)
        Finds the mean average of a list of numbers.
    median(list)
        Not implemented yet.
    mode(list)
        Not implemented yet.
    range(list)
        Not implemented yet.
    """

    def add(self, a, b):
        """Adds two numbers togther.

        Parameters
        ----------
        a : int
             The first addend.
        b : int
             The second addend.

        Returns
        -------
        int
            The sum of a and b.
        """

        return a + b

    def subtract(self, a, b):
        """Adds one number from another.

        Parameters
        ----------
        a : int
             The minuend.
        b : int
             The subtrahend.

        Returns
        -------
        int
            The diference between a and b.
        """

        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers togther.

        Parameters
        ----------
        a : int
             The first factor.
        b : int
             The second factor.

        Returns
        -------
        int
            The product of a and b.
        """

        return a * b

    def divide(self, a, b):
        """Divides one number by another.

        Parameters
        ----------
        a : int
             The dividend.
        b : int
             The divisor.

        Returns
        -------
        int
            The fraction of a over b.
        """

        return a / b

    def sum(self, list):
        """Adds  two numbers togther.

        Parameters
        ----------
        list : list
             Numbers to be added together.

        Returns
        -------
        int
            The sum of all the numbers in the list.
        """

        return sum(list)

    def mean(self, list):
        return sum(list) / len(list)

    def median(self, list):
        sorted_list = sorted(list)
        if len(sorted_list) % 2 == 0:
            middle_index2 = int(len(sorted_list) / 2)
            middle_index1 = middle_index2 - 1
            return (sorted_list[middle_index1] + sorted_list[middle_index2]) / 2
        else:
            middle_index = int(((len(sorted_list) + 1) / 2) - 1)
            return sorted_list[middle_index]

    def mode(self, list):
        # Make dictionary with keys as each unique number from list
        # and values as how many times that number occurs in list.
        dict = {}
        for item in list:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1

        results = []

        # Numbers with only one occurance can ever be the mode.
        max_occurances = 2

        for item in dict.items():
            # If number has a higher number of occurances then current max.
            if item[1] > max_occurances:
                # There is one mode so far, add key as only number in results and update max_occurances.
                results = [item[0]]
                max_occurances = item[1]
            # If number has same number of occurances as current max.
            elif item[1] == max_occurances:
                # There are more than one mode so far, add key to other numbers in results.
                results.append(item[0])

        return results
