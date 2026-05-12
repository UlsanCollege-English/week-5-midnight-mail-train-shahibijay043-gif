

from __future__ import annotations
import re



class TrainCarNode:
    """A node in a doubly linked list of train cars."""

    def __init__(self, car_id: str) -> None:
        self.car_id = car_id
        self.prev: TrainCarNode | None = None
        self.next: TrainCarNode | None = None


class MidnightMailDLL:
    """A doubly linked list for train cars."""

    def __init__(self) -> None:
        self.head: TrainCarNode | None = None
        self.tail: TrainCarNode | None = None

    def append_car(self, car_id: str) -> None:
        """Add a train car to the end of the list."""

        new_node = TrainCarNode(car_id)

        # If list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # Otherwise attach to end
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def detach_last_car(self) -> str | None:
        """Remove the last train car and return its ID.

        Return None if the list is empty.
        """

      
        if self.tail is None:
            return None

        removed_id = self.tail.car_id

        
        if self.head == self.tail:
            self.head = None
            self.tail = None

      
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return removed_id

    def to_reverse_list(self) -> list[str]:
        """Return all train car IDs from tail to head."""

        result = []
        current = self.tail

        while current is not None:
            result.append(current.car_id)
            current = current.prev

        return result


def is_valid_ticket_code(code: str) -> bool:
    """Return True only if code matches MM-1234 format."""

    pattern = r"MM-\d{4}"

    return bool(re.fullmatch(pattern, code))




def count_priority_labels(labels: list[str], target: str) -> int:
    """Recursively count how many times target appears."""

   
    if not labels:
        return 0

    
    current = 1 if labels[0] == target else 0

    
    return current + count_priority_labels(labels[1:], target)




def clean_radio_message(message: str) -> str:
    """Recursively remove all spaces from message."""

   
    if message == "":
        return ""

    
    if message[0] == " ":
        return clean_radio_message(message[1:])

   
    return message[0] + clean_radio_message(message[1:])


def count_priority_labels_iterative(
    labels: list[str],
    target: str,
) -> int:
    """Iterative version of count_priority_labels."""

    count = 0

    for label in labels:
        if label == target:
            count += 1

    return count


def clean_radio_message_iterative(message: str) -> str:
    """Iterative version of clean_radio_message."""

    result = ""

    for char in message:
        if char != " ":
            result += char

    return result