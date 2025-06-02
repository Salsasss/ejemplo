class Class:
    def __init__(self, name: str, description: str = None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Class(name={self.name}, description={self.description})"

    def __str__(self):
        return f"{self.name}: {self.description if self.description else 'No description provided'}"


    def __eq__(self, other):    
        if not isinstance(other, Class):
            return NotImplemented
        return self.name == other.name and self.description == other.description