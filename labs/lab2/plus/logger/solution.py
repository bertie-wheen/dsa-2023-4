from collections.abc import Iterator
from enum import Enum

from lib.base import Base
from lib.time import get_time

from lab2.core.singly_linked_list import SinglyLinkedList


class Level(Base, Enum):
    """
    The level/severity/type of log item.

    Descriptions borrowed from:
    https://docs.python.org/3/library/logging.html#levels
    """

    INFO = 0
    """
    Confirmation that things are working as expected.
    """

    WARNING = 1
    """
    An indication that something unexpected happened, or indicative of some problem in the near future
    (e.g. ‘disk space low’). The software is still working as expected.
    """

    ERROR = 2
    """
    Due to a more serious problem, the software has not been able to perform some function.
    """


class LogItem(Base):
    """
    A single log item.
    """

    _time: float
    _level: Level
    _message: str

    def __init__(self, level: Level, message: str) -> None:
        """
        Initialize the log item.

        :parameter level: the severity level
        :parameter message: the log message
        """
        self._time = get_time()
        self._level = level
        self._message = message

    def get_time(self) -> float:
        """
        Get the time at which this item was logged.

        :returns: the time of the log item
        """
        return self._time

    def get_level(self) -> Level:
        """
        Get the severity level of this log item.

        :returns: the level of the log item
        """
        return self._level

    def get_message(self) -> str:
        """
        Get the message describing what this item was logging.

        :returns: the message of the log item
        """
        return self._message


class Log(Base):
    """
    An append-only program log.
    """

    _log: SinglyLinkedList[LogItem]

    def __init__(self) -> None:
        """
        Initialize the log.
        """
        self._log = SinglyLinkedList()

    def log(self, level: Level, message: str) -> None:
        """
        Log an item.

        :parameter level: the severity level
        :parameter message: the log message
        """
        item = LogItem(level, message)
        self._log.insert_last(item)

    def info(self, message: str) -> None:
        """
        Log a piece information.

        :parameter message: the log message
        """
        self.log(Level.INFO, message)

    def warning(self, message: str) -> None:
        """
        Log a warning.

        :parameter message: the log message describing the warning
        """
        self.log(Level.WARNING, message)

    def error(self, message: str) -> None:
        """
        Log an error.

        :parameter message: the log message describing the error
        """
        self.log(Level.ERROR, message)

    def iterator(self) -> Iterator[LogItem]:
        """
        Get a forward iterator over the items in this log.

        :returns: an iterator over the log's items, in chronological order
        """
        return self._log.iterator()
