"""
Docstring for Creational.Factory.factory

Factory design pattern is a creational pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

here the creation and use of objects are separated. The client code calls a factory method instead of calling a constructor directly to create an object. The factory method is responsible for creating the object and returning it to the client code.



# Requirements Change (frequent change of requirements or code)
# Dynamic Switiching (eliminate if-else or switch-case statements)
# Separation of Concerns
# Code Reusability
"""

"""
CLient---- >  Database Factory -----> Database ---> (MySQLDatabase, PostgreSQLDatabase, SQLiteDatabase)

"""
from abc import ABC, abstractmethod
from typing import Type, Dict
from dataclasses import dataclass

# domain type

@dataclass(frozen=True)
class Connection:
    dsn: str
    engine: str

class unknownDatabaseTypeError(ValueError):
    pass


# --- Interface ----

class Database(ABC):
    @abstractmethod
    def connect(self,dsn: str) -> Connection:
        pass
# concrete implementations
class MySQLDatabase(Database):
    def connect(self,dsn: str) -> Connection:
        return Connection(dsn=dsn, engine="mysql")
class PostgreSQLDatabase(Database):
    def connect(self,dsn: str) -> Connection:
        return Connection(dsn=dsn, engine="postgresql")
class SQLiteDatabase(Database):
    def connect(self,dsn: str) -> Connection:
        return Connection(dsn=dsn, engine="sqlite")

#---- Factory

class DatabaseFactory:
    # registry based approch to avoid if-else or switch-case statements. 
    _registry : Dict[str, Type[Database]] = {
        "mysql": MySQLDatabase,
        "postgresql": PostgreSQLDatabase,
        "sqlite": SQLiteDatabase
    }

    @classmethod
    def register(cls, db_type: str, db_class: Type[Database]):
        k = db_type.strip().lower()
        if not k:
            raise ValueError("Database type cannot be empty.")
        cls._registry[k] = db_class
        
    @classmethod
    def create(cls, db_type: str) -> Database:
        db_class = cls._registry.get(db_type.lower())
        if not db_class:
            available = ", ".join(sorted(cls._registry.keys()))
            raise unknownDatabaseTypeError(f"Unknown database type '{db_type}'. Available types: {available}")
        return db_class()
    
# CLient code
def main()  -> None:
    db = DatabaseFactory.create("mysql")
    conn = db.connect(dsn="mysql://user:pass@host:3306/app")
    print(conn)
if __name__ == '__main__':
    main()



##Examples of when to use Factory Pattern
# 1. When the exact types and dependencies of the objects your code needs to work with are not known until runtime.
# 2. When you want to provide a library of products but only expose their interfaces, not their implementations.
# 3. When you want to centralize the creation logic of objects to make it easier to manage and maintain.
# 4. When you want to implement a plugin architecture where new types can be added without modifying existing code.


