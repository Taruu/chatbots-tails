import datetime

from additionally import Platform
from abc import ABC, abstractmethod
from message import Message


class Chat(ABC):
    id: str = ""
    name: str = ""
    create_at = datetime.datetime.now()

    @abstractmethod
    async def send_message(self, content: str, images=None, files=None):
        pass

    @abstractmethod
    async def delete(self):
        pass

    @abstractmethod
    async def get_message(self, message_id) -> Message:
        pass

    @abstractmethod
    async def messages_history(self, limit=100, before=None, after=None,
                               oldest_first=None):
        pass
