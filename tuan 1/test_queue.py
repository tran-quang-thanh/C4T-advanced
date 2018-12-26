from queue import Queue

q = Queue()
assert(q.is_empty())
assert(hasattr(q, "items"))
assert(hasattr(q, "insert"))
assert(hasattr(q, "remove"))
assert(hasattr(q, "is_empty"))

q.insert(5)
assert(not q.is_empty())
assert(q.__str__() == "5")

q.insert(7)
assert(not q.is_empty())
assert(q.__str__() == "7 5")

q.insert(-1)
assert(not q.is_empty())
assert(q.__str__() == "-1 7 5")

x = q.remove()
assert(not q.is_empty())
assert(q.__str__() == "-1 7")
assert(x == 5)

x = q.remove()
assert(not q.is_empty())
assert(q.__str__() == "-1")
assert(x == 7)

q.insert(11)
assert(not q.is_empty())
assert(q.__str__() == "11 -1")

x = q.remove()
assert(not q.is_empty())
assert(q.__str__() == "11")
assert(x == -1)

x = q.remove()
assert(q.is_empty())
assert(q.__str__() == "")
assert(x == 11)