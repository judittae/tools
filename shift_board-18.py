# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: ShiftBoard
class Tag:
    def __init__(self, name: str):
        self.name = name.strip() or f"tag_{uuid.uuid4().hex[:8]}"

    def __repr__(self):
        return f"Tag({self.name!r})"

    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.name == other.name
        return NotImplemented


class Shift:
    def add_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        for t in self.tags:
            if t == tag:
                return False
        self.tags.append(tag)
        return True

    def remove_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        before = len(self.tags)
        self.tags = [t for t in self.tags if t != tag]
        return len(self.tags) < before


class Employee:
    def add_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        for t in self.tags:
            if t == tag:
                return False
        self.tags.append(tag)
        return True

    def remove_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        before = len(self.tags)
        self.tags = [t for t in self.tags if t != tag]
        return len(self.tags) < before


class Role:
    def add_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        for t in self.tags:
            if t == tag:
                return False
        self.tags.append(tag)
        return True

    def remove_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        before = len(self.tags)
        self.tags = [t for t in self.tags if t != tag]
        return len(self.tags) < before


class Note:
    def add_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        for t in self.tags:
            if t == tag:
                return False
        self.tags.append(tag)
        return True

    def remove_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        before = len(self.tags)
        self.tags = [t for t in self.tags if t != tag]
        return len(self.tags) < before


class Time:
    def add_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        for t in self.tags:
            if t == tag:
                return False
        self.tags.append(tag)
        return True

    def remove_tag(self, tag_name_or_tag):
        tag = tag_name_or_tag if isinstance(tag_name_or_tag, Tag) else Tag(tag_name_or_tag)
        before = len(self.tags)
        self.tags = [t for t in self.tags if t != tag]
        return len(self.tags) < before


class ShiftBoard:
    def add_tag(self, target, tag_name_or_tag):
        """target: 'employee'|'role'|'note'|'time', tag_name_or_tag: str or Tag"""
        entity = {
            "employee": self.employees,
            "role": self.roles,
            "note": self.notes,
            "time": self.times,
        }.get(target)
        if not entity:
            raise ValueError(f"Unknown target: {target}")
        return entity.add_tag(tag_name_or_tag)

    def remove_tag(self, target, tag_name_or_tag):
        """target: 'employee'|'role'|'note'|'time', tag_name_or_tag: str or Tag"""
        entity = {
            "employee": self.employees,
            "role": self.roles,
            "note": self.notes,
            "time": self.times,
        }.get(target)
        if not entity:
            raise ValueError(f"Unknown target: {target}")
        return entity.remove_tag(tag_name_or_tag)
