from string_processor import StringProcessor

string_processor = StringProcessor()
assert(hasattr(string_processor, "stack"))
assert(hasattr(string_processor, "reverse"))
assert(hasattr(string_processor, "process_sequence"))
assert(hasattr(string_processor, "binary_string"))
assert(hasattr(string_processor, "is_balanced"))

s = string_processor.reverse("abc123")
assert(s == "321cba")

s = string_processor.reverse("xyzert")
assert(s == "trezyx")

s = string_processor.process_sequence("AB**")
assert(s == "BA")

s = string_processor.process_sequence("AB*C**")
assert(s == "BCA")

s = string_processor.process_sequence("AB*C*DE*F***")
assert(s == "BCEFDA")

# Test if the stack if clean after/before process sequence
s = string_processor.process_sequence("AB*C*DE*F**")
assert(s == "BCEFD")

s = string_processor.process_sequence("AB**")
assert(s == "BA")

assert(string_processor.binary_string(0) == "0")
assert(string_processor.binary_string(1) == "1")
assert(string_processor.binary_string(2) == "10")
assert(string_processor.binary_string(3) == "11")
assert(string_processor.binary_string(4) == "100")
assert(string_processor.binary_string(5) == "101")
assert(string_processor.binary_string(6) == "110")
assert(string_processor.binary_string(173) == "10101101")

assert(not string_processor.is_balanced("{"))
assert(string_processor.is_balanced("{}"))
assert(string_processor.is_balanced("{0}"))
assert(not string_processor.is_balanced("{(}"))
assert(string_processor.is_balanced("{()}"))
assert(not string_processor.is_balanced("{()}["))
assert(string_processor.is_balanced("{()}[]"))
assert(string_processor.is_balanced("{(111)}[2]"))