def count_courses(courses,amount=10.5):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def help_change(amount, part):
        if amount == 0:
            return 1
        if amount == part:
            return 1
        elif amount < part:
            return 0
        else:
            return help_change(amount-part.lst[1].units,part)+help_change(amount,part*2)
    return help_change(amount,courses.lst)
    possible_courses = course_load
    
    possible_courses.print()

    
