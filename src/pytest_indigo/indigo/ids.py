class IndigoIds:
    def __init__(self, start: int = 1):
        self.start = start
        self.current = start

    def __iter__(self):  # pragma: no cover
        return self

    def __next__(self) -> int:
        id = self.current
        self.current += 1
        return id

    def reset(self):  # pragma: no cover
        """
        Reset the id generator back to the starting state.

        This will result in duplicate ids being returned.
        """
        self.current = self.start

    def set_next_id(self, id: int):  # pragma: no cover
        """
        Set the value for the next id to return.

        The id sequence will resume from the set value. Setting the value
        lower than the current value will result in duplicate ids being
        returned.

        Parameters
        ----------
        id: int
            The next value to return.

        Raises
        ------
        TypeError: When the value is not an integer.
        ValueError: When the value is negative.
        """
        if not isinstance(id, int):
            raise TypeError(f"id must be an int, got: {type(id)}")

        if id < 0:
            raise ValueError("id must not be negative")

        self.current = id

    def peek(self) -> int:
        """
        Get the next id in the sequence without incrementing.

        This is useful to determine what the next id will be.

        Returns
        -------
        id: int
            The next id in the sequence.
        """
        return self.current
