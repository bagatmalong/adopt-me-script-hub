from __future__ import annotations

import time
from dataclasses import dataclass


@dataclass
class RateLimiter:
    min_interval: float = 0.25
    _last: float = 0.0

    def ready(self) -> bool:
        now = time.monotonic()
        if now - self._last >= self.min_interval:
            self._last = now
            return True
        return False