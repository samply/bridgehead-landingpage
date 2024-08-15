from enum import Enum


class ServiceType(Enum):
    CENTRAL = 1
    BRIDGEHEAD = 2


class ServiceGroup(Enum):
    PSEUDONYMIZATION = 1
    SEARCH = 2
    PERSISTENCE = 3
    OPERATIONS = 4
    NEGOTIATION = 5


class Service:
    def __init__(self, group, name, url, type):
        self.group = group
        self.name = name
        self.url = url
        self.type = type
