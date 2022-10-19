#calculator.py
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
    modal(list)
        Not implemented yet.
    mode(list)
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

    def modal(self, list):
        return 0

    def mode(self, list):
        return 0
