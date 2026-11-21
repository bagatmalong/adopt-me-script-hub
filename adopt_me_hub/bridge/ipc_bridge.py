"""Lightweight IPC bridge stubs for talking to a local Roblox executor socket."""
from __future__ import annotations

import json
import socket
import threading
from dataclasses import dataclass
from typing import Callable

DEFAULT_ENDPOINT = ("127.0.0.1", 43691)


@dataclass
class BridgeMessage:
    kind: str
    body: dict


class IpcBridge:
    def __init__(self, endpoint: tuple[str, int] = DEFAULT_ENDPOINT) -> None:
        self.endpoint = endpoint
        self._sock: socket.socket | None = None
        self._listeners: list[Callable[[BridgeMessage], None]] = []
        self._lock = threading.Lock()

    def connect(self, timeout: float = 1.5) -> bool:
        try:
            sock = socket.create_connection(self.endpoint, timeout=timeout)
        except OSError:
            return False
        self._sock = sock
        return True

    def subscribe(self, cb: Callable[[BridgeMessage], None]) -> None:
        self._listeners.append(cb)

    def send(self, kind: str, body: dict) -> bool:
        if self._sock is None:
            return False
        frame = json.dumps({"kind": kind, "body": body}).encode() + b"\n"
        with self._lock:
            try:
                self._sock.sendall(frame)
                return True
            except OSError:
                self._sock = None
                return False

    def close(self) -> None:
        if self._sock:
            try:
                self._sock.close()
            finally:
                self._sock = None