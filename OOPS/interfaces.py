# Interfaces in Python
# Python doesn't have a formal interface construct like Java, but there are several approaches:

# 1. Informal Interfaces (Duck Typing)
# Just define methods that must be implemented

# No enforcement, relies on convention

class JSONSerializable:
    def to_json(self):
        pass
    
    @classmethod
    def from_json(cls, json_data):
        pass


# 2. Formal Interfaces using ABC
# More strict, enforces implementation

from abc import ABC, abstractmethod

class JSONSerializable(ABC):
    @abstractmethod
    def to_json(self):
        """Convert instance to JSON"""
        pass
    
    @classmethod
    @abstractmethod
    def from_json(cls, json_data):
        """Create instance from JSON"""
        pass

# 3. Protocol (Python 3.8+)
# Structural subtyping (typing.Protocol)

from typing import Protocol

class JSONSerializable(Protocol):
    def to_json(self) -> str: ...
    
    @classmethod
    def from_json(cls, json_data: str) -> 'JSONSerializable': ...


# When to Use Each in Python:
# Use ABC when:

# You need to enforce method implementation

# You want to provide some base implementation

# You're creating a framework that requires subclassing

# Use informal interface when:

# You're following duck typing principles

# You want maximum flexibility

# Documentation is sufficient for implementation

# Use Protocol when:

# You want structural typing

# You're using static type checking

# You don't want to force inheritance

# Python-Specific Notes:
# Python emphasizes "duck typing" over formal interfaces

# The @abstractmethod decorator can be combined with @property, @classmethod, etc.

# ABCs can provide __subclasshook__ for custom subclass checks

# Python's approach is more flexible but less strict than Java's interfaces

# Multiple inheritance makes ABCs more powerful than Java's abstract classes

# Example combining multiple concepts:


from abc import ABC, abstractmethod
from typing import Protocol

# Abstract Base Class example
class DatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def disconnect(self):
        pass
    
    @property
    @abstractmethod
    def is_connected(self) -> bool:
        pass

# Protocol example
class Loggable(Protocol):
    def log(self, message: str) -> None: ...

# Combined implementation
class PostgreSQL(DatabaseConnector, Loggable):
    def connect(self):
        print("Connecting to PostgreSQL...")
    
    def disconnect(self):
        print("Disconnecting from PostgreSQL...")
    
    @property
    def is_connected(self) -> bool:
        return True
    
    def log(self, message: str) -> None:
        print(f"[PostgreSQL LOG]: {message}")

