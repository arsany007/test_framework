from .platform_abstract import PlatformAbstract


class Platform1(PlatformAbstract):
    """
    The Platform1 class.
    """

    def read(self) -> str:
        return "Platform1"

    def write(self, data) -> None:
        raise NotImplementedError
