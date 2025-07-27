# LibraryProject - Role-Based Access Control

## Overview

This project demonstrates how to implement role-based access control in Django using:
- Custom permissions
- Groups (Editors, Viewers, Admins)
- `@permission_required` decorators in views

---

## Permissions Setup

We defined custom permissions in `bookshelf/models.py` using the `Meta` class:

```python
permissions = [
    ("can_view", "Can view book list"),
    ("can_create", "Can add a new book"),
    ("can_edit", "Can edit existing books"),
    ("can_delete", "Can delete books"),
]
