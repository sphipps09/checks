import check50
import check50.c

@check50.check()
def exists():
    """redundant.c exists"""
    check50.exists("redundant.c")

@check50.check(exists)
def compiles():
    """redundant.c compiles"""
    check50.c.compile("redundant.c", lcs50=True)

@check50.check(compiles)
def one_command_line_argument():
    """takes correct number of command-line arguments"""
    check50.run("./redundant hello").stdout("Usage: ./program\n", regex=False).exit(1)

@check50.check(compiles)
def prints_name():
    """prints correct name of program"""
    check50.run("./redundant").stdout("This program is called redundant\n", regex=False).exit(0)
