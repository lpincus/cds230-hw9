# def Aper(indata):
#     print('The input is', indata)

# Aper('indata')

# def Aper(indata):
#     for i in range(3):
#         print('The input is', indata)

# Aper('indata')



# def Larger(adata, bdata):
#     if adata > bdata:
#         return adata
#     else: 
#         return bdata

# val = Larger(5,9)
# print(val)


# def question5(fname='romeo-and-juliet.txt'):
#     fvar = open(fname, 'r')
#     fvar2 = fvar.read()
#     print(len(fvar2))
# question5("hw9.py")

# def BF(indata):
#     return indata.upper()
# def BA(indata2):
#     indata2 =  BF(indata2)
#     return indata2.replace(" ", "")
# print(BA("yell ow"))

# def LoadCountry(myfile="country.csv"):
#     txt = open(myfile).read().split ("\n")
#     actors = [] 
#     for i in range(1, len(txt)-1):
#         row = txt[i].split (",")
#         actors.append((int(row[0]), row[1]))
#     return actors

# def LoadInCountry(myfile="incountry.csv"):
#     txt = open(myfile).read().split ("\n")
#     actors = [] 
#     for i in range(1, len(txt)-1):
#         row = txt[i].split (",")
#         actors.append((int(row[0]), int(row[1]), int(row[2])))
#     return actors
# def CountryFromCndx(cndx):
#     countrys = LoadCountry()
#     country = ()
#     incountrys = LoadInCountry()
#     incntry = ()
#     for cntry in incountrys:
#         if cntry[0] == int(cndx):
#             incntry = cntry
#             break
#     for cntry in countrys:
#         if cntry[0] == incntry[2]:
#             return cntry[1]
# print(CountryFromCndx(21))



def LoadMovies(myfile="movies800.tsv"):
    txt = open(myfile).read().split ("\n")
    actors = [] 
    for i in range(1, len(txt)-1):
        row = txt[i].split ("\t")
        actors.append((int(row[0]), row[1], row[2], row[3]))
    return actors
# def TitleFromGrade(grade):
#     movierows = LoadMovies()
#     movies = []
#     for movie in movierows:
#         if str(movie[3]) == str(grade):
#             movies.append(movie[1])
#     return movies
# # print(TitleFromGrade(10))



# def TitlesFromGrades(grades):
#     movies = []
#     for grade in grades:
#         movies = movies + TitleFromGrade(grade)
#     return movies
# print(TitlesFromGrades([1,10]))

import statistics
def TitleList():
    movies = LoadMovies()
    titles = []
    for mov in movies:
        titles.append(mov[1])
    return titles
def AvgStdev(titles):
    titlelengths = []
    for tit in titles:
        titlelengths.append(len(tit))
    return statistics.mean(titlelengths), statistics.pstdev(titlelengths)
# print("avg, standard deviation")
# print(AvgStdev(TitleList()))

def LoadActors(myfile="actors.tsv"):
    txt = open(myfile).read().split ("\n")
    actors = [] 
    for i in range(1, len(txt)-1):
        row = txt[i].split ("\t")
        actors.append((int(row[0]), row[1], row[2]))
    return actors
def actornames(first):
    actorlist = LoadActors()
    firstnames = []
    for act in actorlist:
        if act[1] == first:
            firstnames.append(act[2])
    return firstnames
# print(actornames("Smith"))

def matchinginital(firstname, lastname):
    matches = []
    actorlist = LoadActors()
    for actor in actorlist:
        if firstname[0:1] == actor[1][0:1] and lastname[0:1] == actor[2][0:1]:
            matches.append(actor)
    return matches

def matchinginitials():
    actorlist = LoadActors()
    matches = []
    for actor in actorlist:
        match = matchinginital(actor[1], actor[2])
        if len(match) > 1:
            matches.append(match)
    return matches
# print(matchinginitials())

# 13. Starting with the script in Code 16.36, 
# write a function that sorts the (average grade, year) tuples 
# from the highest average grade to the lowest average grade.
def AverageGradeFromYear(movies, year):
    movieyear = []
    for movie in movies:
        if movie[2]:
            if str(movie[2]) == str(year):
                movieyear.append(int(movie[3]))
    return (statistics.mean(movieyear), year)
def AverageGradesByYear(movies):
    years = []
    for movie in movies:
        years.append(movie[2])
    years = set(years)
    avgyear = []
    for year in years:
        avgyear.append(AverageGradeFromYear(movies, year))
    avgyear.sort(key=lambda tup: tup[0], reverse=True)
    return avgyear
movies = LoadMovies()
avgYearGrade = AverageGradesByYear(movies)
# for tup in avgYearGrade:
    # print(tup)


# 14. Write the necessary functions 
# to return a list of movie mids 
# for movies with a specified language.
def loadInLangs(myfile="inlangs.txt"):
    txt = open(myfile).read().split ("\n")
    actors = [] 
    for i in range(1, len(txt)-1):
        row = txt[i].split ("\t")
        actors.append((int(row[0]), row[1], row[2]))
    return actors

def loadLangs(myfile="langs.txt"):
    txt = open(myfile).read().split ("\n")
    langs = [] 
    for i in range(1, len(txt)-1):
        row = txt[i].split ("\t")
        langs.append((int(row[0]), row[1]))
    return langs

def GetLidFromLang(lang):
    langs = loadLangs()
    for l in langs:
        if lang == l[1]:
            return l[0]
def GetMidsByLid(lid):
    movies = loadInLangs()
    answr = []
    for mov in movies:
        if str(mov[2]) == str(lid):
            answr.append(mov[0])
    return answr

def GetMidsByLang(lang):
    lid = GetLidFromLang(lang)
    return GetMidsByLid(lid)
# print(GetMidsByLang("Hebrew"))


# 15. Write a function that uses 
# MidsFromAid: (isin[], aid) => mids[]
# and AidFromNames : (actors[], first, last) => aid
# that counts the number of movies for every actor. 
# Sort this data from the most number of movies to the least. 
# Print the five actors with the most movies from this sorted list.
import movies
def MoviesByActors():
    isin = movies.LoadIsin("isin.txt")
    actors = movies.LoadActors("actors.tsv")
    actorcounts = []
    for actor in actors:
        fname = actor[1]
        lname = actor[2]
        aid = movies.AidFromName(actors, fname, lname)
        num = len(movies.MidsFromAid(isin, aid))
        actorcounts.append((fname, lname, num))
    actorcounts.sort(key=lambda x: x[2], reverse=True)
    return actorcounts
moviesbyactors = MoviesByActors()
for i in range(5):
    print(moviesbyactors[i])

