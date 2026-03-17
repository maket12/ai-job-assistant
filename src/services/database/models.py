from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

@dataclass
class User:
    id: int
    username: Optional[str]
    first_name: Optional[str]
    language: str
    cv_file_id: Optional[str]
    cv_path: Optional[str]
    created_at: datetime
    updated_at: datetime

@dataclass
class UserSettings:
    id: int
    user_id: int

