from __future__ import annotations

from pathlib import Path
from typing import Any, Mapping
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from forge.orchestrator import Command, Orchestrator


def test_register_and_handle() -> None:
    orch = Orchestrator()

    def echo(payload: Mapping[str, Any]) -> Mapping[str, Any]:
        return {"echo": dict(payload)}

    orch.register("echo", echo)
    result = orch.handle(Command(source="cli", name="echo", payload={"a": 1}))
    assert result == {"echo": {"a": 1}}


def test_unknown_command() -> None:
    orch = Orchestrator()
    try:
        orch.handle(Command(source="cli", name="missing", payload={}))
    except ValueError as e:
        assert "no handler" in str(e)
    else:
        raise AssertionError("expected ValueError")


def test_duplicate_registration() -> None:
    orch = Orchestrator()

    def handler(_: Mapping[str, Any]) -> None:
        return None

    orch.register("dup", handler)
    try:
        orch.register("dup", handler)
    except ValueError as e:
        assert "already" in str(e)
    else:
        raise AssertionError("expected ValueError")
