from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Mapping


@dataclass(slots=True)
class Command:
    """A request from a specific protocol."""

    source: str
    name: str
    payload: Mapping[str, Any]


Handler = Callable[[Mapping[str, Any]], Mapping[str, Any] | None]


class Orchestrator:
    """Dispatch commands to registered handlers."""

    def __init__(self) -> None:
        self._handlers: Dict[str, Handler] = {}

    def register(self, name: str, handler: Handler) -> None:
        if name in self._handlers:
            raise ValueError(f"handler already registered for '{name}'")
        self._handlers[name] = handler

    def handle(self, command: Command) -> Mapping[str, Any] | None:
        try:
            handler = self._handlers[command.name]
        except KeyError as exc:
            raise ValueError(f"no handler for '{command.name}'") from exc
        return handler(command.payload)
