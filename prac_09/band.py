"""Band class for CP1404"""


class Band:
    """Band has Musicians (association)."""

    def __init__(self, name=""):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation like:
        Extreme (Nuno Bettencourt ([Guitars]), Gary Cherone ([]), ...)
        """
        musicians_text = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_text})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Tell each musician to play."""
        for musician in self.musicians:
            print(musician.play())
