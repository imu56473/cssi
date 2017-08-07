student={
"2658214":"imran",
"2957587":"rahid",
"2875879":"elvis",
"2366577":"jhonathon",
"2345678":"abigal",
"2097854":"nusrath",
"2987636":"olawale",
"2136486":"oliva",
"2380780":"rayona",
"2074389":"egide",
"2740987":"zanif",
}
def studentLookUp(student,studentname):
    found = ""
    for X in student.keys():
        if (student[X].lower() == studentname.lower()):
            found = X

    if found:
        return found
    else:
        return "Invalid student name"

## print studentLookUp(student,"elViss")

#print student.keys()
