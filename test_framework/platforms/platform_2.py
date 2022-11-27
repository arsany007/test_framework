from .platform_abstract import PlatformAbstract


class Platform2(PlatformAbstract):
    """
    The platform2 class.
    """

    def read(self) -> str:
        return "Platform2"

    def write(self, data) -> None:
        pass
