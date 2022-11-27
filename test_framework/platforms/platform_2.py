from .platform_abstract import PlatformAbstract

class Platform2(PlatformAbstract):
    """
    The platform class declares the factory method that is supposed to return an
    object of a platform class.
    """

    def read(self) -> str:
        return "Platform2"

    def write(self, data) -> None:
        return NotImplementedError
