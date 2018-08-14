def remove_dollar_sign (s):
    s = s.replace("$", "")
    return s

string_with_no_dollars = remove_dollar_sign("$Hoi sa$d 1 chu$t")
if string_with_no_dollars == "Hoi sad 1 chut":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
