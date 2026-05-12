# src/challenges.py


# -----------------------------
# Problem 1: Doubly Linked List
# -----------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class MidnightMailDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_car(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def detach_last_car(self):
        if self.tail is None:
            return None

        removed = self.tail.value

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return removed

    def to_reverse_list(self):
        result = []
        current = self.tail

        while current:
            result.append(current.value)
            current = current.prev

        return result


# -----------------------------
# Problem 2: Ticket Code
# -----------------------------

def is_valid_ticket_code(code):
    if len(code) != 7:
        return False

    if not code.startswith("MM-"):
        return False

    digits = code[3:]

    return digits.isdigit()


# -----------------------------
# Problem 3: Recursion on List
# -----------------------------

def count_priority_labels(labels, target):
    if labels == []:
        return 0

    if labels[0] == target:
        return 1 + count_priority_labels(labels[1:], target)

    return count_priority_labels(labels[1:], target)


# -----------------------------
# Problem 4: Recursion on String
# -----------------------------

def clean_radio_message(message):
    if message == "":
        return ""

    if message[0] == " ":
        return clean_radio_message(message[1:])

    return message[0] + clean_radio_message(message[1:])