
def problem1n1(x1, x2):
    """Solution to polynomial

        Inputs: floats: x1 and x2
        Outputs: float: solution to 5*x1 - 2*x2 + 3
    """
    return 5*x1 - 2*x2 + 3
# y = problem1(3, 4)
# print(y)

def problem1n2(mystr):
    for l in mystr:
        print(ord(l))
# problem2("mason")

# prob 2
# help(problem1n1)

# 1. Using functions from the movies.py file, 
# compute the answer to Query 22. 
# List the titles of all of the movies that are in French. 
# lease return this list in alphabetical order.
import movies
def FrenchMovies():
    languages = movies.LoadCtryLang("langs.txt")
    lid = movies.LidFromLanguage(languages, "French")
    inlang = movies.LoadIsin("inlangs.txt")
    mids = movies.MidsFromLid(inlang, lid)
    movietxt = movies.LoadMovies("movies800.tsv")
    french = movies.TitlesFromMids(movietxt, mids)
    french.sort()
    return french
# print(FrenchMovies())

# 2. Using the functions in movies.py 
# compute the average movie grade for each decade (Query 29). 
# Your function should return a list. 
# Each item in the list is a tuple. 
# Each tuple contains the first year of the decade and the average score for that decade.
import statistics
def averageGradesByDecade():
    answr = []
    movietxt = movies.LoadMovies("movies800.tsv")
    startyr = 1920
    stopyr = 2020
    for i in range(startyr, stopyr, 10):
        grades = movies.GradesFromYears(movietxt, [i + x for x in range(0,10)])
        answr.append((i, statistics.mean(grades)))
    return answr
print(averageGradesByDecade())