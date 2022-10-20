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
        Multiplies two numbers together.
    divide(a, b)
        Divides one number by another.
    sum(list)
        Finds total of a list of numbers added together.
    mean(list)
        Finds the mean average of a list of numbers.
    median(list)
        Finds the median average of a list of numbers.
    mode(list)
        Finds the mode average of a list of numbers.
    """

    def add(self, a, b):
        """Adds two numbers together.

        Parameters
        ----------
        a : int
             The first addend.
        b : int
             The second addend.

        Returns
        -------
        int
            The sum of a and b (a + b).
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
            The diference between a and b (a - b).
        """

        return a - b

    def multiply(self, a, b):
        """Multiplies two numbers together.

        Parameters
        ----------
        a : int
             The first factor.
        b : int
             The second factor.

        Returns
        -------
        int
            The product of a and b (a * b).
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
            The fraction of a over b (a / b).
        """

        return a / b

    def sum(self, list):
        """Adds all numbers in a list together.

        Parameters
        ----------
        list : list
             List of numbers.

        Returns
        -------
        int
            The sum of all the numbers in the list.
        """

        return sum(list)

    def mean(self, list):
        """Calculates the mean of a list of numbers

        Adds them all together then divides by the count of numbers.

        Parameters
        ----------
        list : list of int
             List of numbers.

        Returns
        -------
        float
            The mean of all the numbers in the list.
        """

        return sum(list) / len(list)

    def median(self, list):
        """Finds the median value of a list of numbers

        Sorts the list by magnitude and finds the middle number.  If there is
        an even number of numbers in the list the median will be the average
        of the middle two numbers.

        Parameters
        ----------
        list : list of int
             List of numbers.

        Returns
        -------
        float
            The median value of the list.
        """

        sorted_list = sorted(list)

        # If even number of numbers in list...
        if len(sorted_list) % 2 == 0:
            # Add the two middle numbers togther and return average
            middle_index2 = int(len(sorted_list) / 2)
            middle_index1 = middle_index2 - 1
            return (sorted_list[middle_index1] + sorted_list[middle_index2]) / 2
        else:
            # If odd number, return single middle number
            middle_index = int(((len(sorted_list) + 1) / 2) - 1)
            return sorted_list[middle_index]

    def mode(self, list):
        """Finds the mode numbers of a list of numbers

        Searches for the numbers that occur most frequently.  If every number
        occurs only once there is no mode.

        Parameters
        ----------
        list : list of int
             List of numbers.

        Returns
        -------
        list of int
            A list of the zero or more numbers that occur most frequently.
        """

        # Make dictionary with keys as each unique number from list
        # and values as how many times that number occurs in list.
        dict = {}
        for item in list:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1

        results = []

        # Numbers with only one occurrence can ever be the mode.
        max_occurrences = 2

        for item in dict.items():
            # If number has a higher number of occurrences then current max.
            if item[1] > max_occurrences:
                # There is one mode so far
                # add key as only number in results and update max_occurrences.
                results = [item[0]]
                max_occurrences = item[1]
            # If number has same number of occurrences as current max.
            elif item[1] == max_occurrences:
                # There are more than one mode so far
                # add key to other numbers in results.
                results.append(item[0])

        return results
