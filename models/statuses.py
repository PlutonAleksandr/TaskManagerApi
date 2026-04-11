
import enum

class TaskStatus(enum.Enum):
    not_issued = "not issued"
    issued = "issued"
    completed = "completed"
    failed = "failed"
