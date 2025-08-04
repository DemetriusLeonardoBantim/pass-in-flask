from typing import Dict
from src.models.settings.connection import db_connection_handler
from src.models.entities.events import Events

class EventsRepository:
    def insert_event(self, eventsInfo: Dict) -> Dict:
        with db_connection_handler as database:
            event = Events(
                id=eventsInfo["uuid"]
            )