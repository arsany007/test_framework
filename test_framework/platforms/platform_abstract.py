from abc import ABC, abstractmethod

class PlatformAbstract(ABC):
    """
    The platform class declares the factory method that is supposed to return an
    object of a platform class.
    """

    @abstractmethod
    def read(self) -> str:
        """
        read platform data.
        """
        return NotImplementedError

    @abstractmethod
    def write(self, data) -> None:
        """
        write platform data.
        """
        return NotImplementedError

    def log(self,msg) -> None:
        """
        log platform data.
        """
        print(msg)