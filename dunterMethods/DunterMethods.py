class Playlist:
    '''
    A class to represent a playlist of songs.
    '''

    def __init__(self, songs):
        '''
        The constructor for the Playlist class.

        Args:
            songs (list): A list of songs in the playlist.
        '''

        self.songs = songs

    def __len__(self):
        '''
        Returns the number of songs in the playlist.

        The __len__ method is used to define the length of an object. It returns the length of the object when the len() function is called on it.
        '''

        return len(self.songs)


class Range:
    '''
    A class to represent a range of numbers.
    '''

    def __init__(self, start, stop=None, step=1):
        '''
        The constructor for the Range class. if one number is given it takes as stop

        Args:
            start (int): The starting number of the range.
            stop (int, optional): The ending number of the range. If not specified, the range will end at the start number.
            step (int, optional): The step size of the range. If not specified, the step size will be 1.
        '''

        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop

        self.step = step
        self.current = self.start

    def __iter__(self):
        '''
        Makes this class iterable.

        This method is called when a for loop is used on an object. It returns an iterator object that can be used to iterate over the object's elements.
        '''

        return self

    def __next__(self):
        '''
        Returns the next value in the range.

        This method is called each time the iterator object is used to get the next value in the range. It increments the current value by the step size and returns it.

        Raises:
            StopIteration: If the current value is greater than or equal to the stop value.
        '''

        currentt = self.current
        self.current += self.step

        if (self.step > 0 and currentt >= self.stop) or (self.step < 0 and currentt <= self.stop):
            raise StopIteration

        return currentt


class Car:
    '''
    A class to represent a car.
    '''

    def __init__(self, make, model, year):
        '''
        The constructor for the Car class.

        Args:
            make (str): The make of the car.
            model (str): The model of the car.
            year (int): The year the car was made.
        '''

        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        '''
        Returns a string representation of the car.

        This method is called when the print() function is used on an object. It returns a string that represents the object.

        Returns:
            str: A string representation of the car.
        '''

        return f"{self.year} {self.make} {self.model}"

    def __repr__(self):
        '''
        Returns a string representation of the car that can be used to recreate the object.

        This method is similar to the __str__ method, but it returns a string that can be used to recreate the object. This is useful for debugging and testing.

        Returns:
            str: A string representation of the car that can be used to recreate the object.
        '''

        return f"Car('{self.make}', '{self.model}', {self.year})"

    def __eq__(self, other):
        '''
        Compares two cars for equality.

        This method is called when the == operator is used to compare two objects. It returns True if the objects are equal, and False otherwise.

        Args:
            other (Car): The other car to compare to.

        Returns:
            bool: True if the cars are equal, False otherwise.
        '''

        return self.make == other.make and self.model == other.model and self.year == other.year

    def __lt__(self, other):
        '''
        Compares two cars for less than.

        This method is called when the < operator is used to compare two objects. It returns True if the first object is less than the second object, and False otherwise.

        Args:
            other (Car): The other car to compare to.

        Returns:
            bool: True if the first car is less than the second car, False otherwise.
        '''

        return self.year < other.year

    def __getitem__(self, key):
        '''
        Gets the value of the specified attribute of the car.

        This method is called when the [] operator is used to access an attribute of an object. It returns the value of the specified attribute.

        Args:
            key (str): The name of the attribute to get the value of.

        Returns:
            The value of the specified attribute.

        Raises:
            KeyError: If the specified attribute does not exist.
        '''

        if key == 'make':
            return self.make
        elif key == 'model':
            return self.model
        elif key == 'year':
            return self.year
        else:
            raise KeyError(f"Invalid key: {key}")

    def __setattr__(self, attr, value):
        '''
        Sets the value of the specified attribute of the car.

        This method is called when the = operator is used to assign a value to an attribute of an object. It sets the value of the specified attribute to the specified value.

        Args:
            attr (str): The name of the attribute to set the value of.
            value: The value to set the attribute to.

        Raises:
            AttributeError: If the specified attribute is not a valid attribute of the object.
        '''

        if hasattr(self, attr):
            raise AttributeError("cannot modify existing attributes")
        else:
            super().__setattr__(attr, value)

    def __getattr__(self, name: str):
        '''
        Gets the value of the specified attribute of the car.

        This method is called when the . operator is used to access an attribute of an object. It returns the value of the specified attribute.

        Args:
            name (str): The name of the attribute to get the value of.

        Returns:
            The value of the specified attribute.

        Raises:
            AttributeError: If the specified attribute does not exist.
        '''

        if name == 'model' or name == 'year':
            raise AttributeError("Variable cannot be modified as they are private")
        return super().__getattribute__(name)

    def __call__(self):
        '''
        Returns a string representation of the car.

        This method is called when the object is called as a function. It returns a string representation of the object.

        Returns:
            str: A string representation of the car.
        '''

        return f"the car is made by {self.make} in year {self.year}"

    def __del__(self):
        '''
        Destructor for the Car class.

        This method is called when the object is deleted. It prints a message to the console.
        '''

        print(f"Deleting {self.year} {self.make} {self.model}...")

    # Thse two methods are vary important they make our class an iterable
    def __iter__(self):
        '''
        Returns an iterator for the car.

        This method is called when the for loop is used on an object. It returns an iterator object that can be used to iterate over the object's elements.
        '''

        pass

    def __next__(self):
        '''
        Returns the next value in the iterator.

        This method is called each time the iterator object is used to get the next value in the range. It increments the current value by the step size and returns it.

        Raises:
            StopIteration: If the current value is greater than or equal to the stop value.
        '''

        pass

    def __eq__(self, other):
        '''
        Compares two cars for equality.

        This method is called when the == operator is used to compare two objects. It returns True if the objects are equal, and False otherwise.

        Args:
            other (Car): The other car to compare to.

        Returns:
            bool: True if the cars are equal, False otherwise.
        '''

        return isinstance(other, Car) and (self.make, self.model, self.year) == (other.make, other.model, other.year)

    def __le__(self, other):
        '''
        Compares two cars for less than.

        This method is called when the < operator is used to compare two objects. It returns True if the first object is less than the second object, and False otherwise.

        Args:
            other (Car): The other car to compare to.

        Returns: True or False'''
        if not (isinstance(other,Car)) :
            raise Exception(" unmachbel type")
        return self.year<= other.year
    
    def __hash__(self):
        return hash((self.make, self.model, self.year))
    



if __name__=="__main__":
    print("mostly used dunter methods")
    # car = Car("toyata","camry",2022)
    # print(car)
    # print(list(Range(10)))
    # print(list(Range(10,1,-1)))