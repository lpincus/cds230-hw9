# movies.py
# JM Kinser

# ########### Loading Functions #################
def LoadMovies( movieName ):
    txt = open( movieName ).read()
    txt = txt.split('\n')
    movies =  []
    for i in range( 1,len(txt)-1 ):
        a = txt[i].split('\t')
        mid = int( a[0] )
        if a[2].isnumeric():
            year = int(a[2] )
        else:
            year = 0
        if a[3].isnumeric():
            grade = int(a[3] )
        else: 
            grade = 0
        movies.append( (mid,a[1],year,grade))
    return movies

def LoadIsin( isinName ):
    txt = open( isinName ).read().split('\n')
    isin = []
    for i in range( 1, len(txt)-1 ):
        a = txt[i].split('\t')
        isin.append( (int(a[0]), int(a[1]), int(a[2] )))
    return isin

def LoadActors( actorsName ):
    txt = open( actorsName ).read().split('\n')
    actors = []
    for i in range( 1, len(txt)-1):
        a = txt[i].split('\t')
        aid = int(a[0])
        actors.append( (aid,a[1],a[2] ))
    return actors

def LoadCtryLang( filename ):
    data = open(filename).read()
    data = data.split('\n')
    answ = []
    for i in data[1:-1]:
        r = i.split('\t')
        cid = int( r[0] )
        answ.append( (cid, r[1] ) )
    return answ

def LoadInCtryLang( filename ):
    data = open(filename).read()
    data = data.split('\n')
    answ = []
    for i in data[1:-1]:
        r = i.split('\t')
        cndx, mid, cid = int( r[0] ), int( r[1] ), int( r[2] )
        answ.append( ( cndx, mid, cid) )
    return answ

# ########### Analysis Functions #################

# average:   avg = sum(inlist)/len(inlist)

def CombineLists( list1, list2 ):
    s1 = set(list1)
    s3 = s1.intersection( list2 )
    outlist = list( s3 )
    return outlist


# ########### Single input single output #################

def TitleFromMid( movies, mid ):
    tt = ''
    for i in movies:
        if mid==i[0]:
            tt = i[1]
            break
    return tt

def MovieDataFromMid( movies, mid ):
    tt = ()
    for i in movies:
        if mid==i[0]:
            tt = i
            break
    return tt

def LidFromLanguage( languages, inputlang ):
    """Returns lid
    languages: the languages table
    inputlang: a string that is the query language
    output: integer that is the lid"""
    lid = -1
    for i in languages:
        if i[1] == inputlang:
            lid = i[0]
            break
    return lid

def LangFromLndx( langs, lndx ):
    lang = ''
    for i in langs:
        if lndx == i[0]:
            lang = i[1]
            break
    return lang

def NameFromAid( actors, aid ):
    fn, ln = '',''
    for a in actors:
        if aid == a[0]:
            fn, ln = a[1], a[2]
            break
    return fn, ln

def AidFromName( actors, first, last ):
    fn, ln = '',''
    for a in actors:
        if first == a[1] and last==a[2]:
            aid = a[0]
            break
    return aid

# ########### Single Input - Multi Output #################

def TitlesFromYear( movies, year ):
    titles = []
    for m in movies:
        if year== m[2]:
            titles.append( m[1] )
    return titles

def MidsFromYear( movies, year ):
    mids = []
    for m in movies:
        if year== m[2]:
            mids.append( m[0] )
    return mids

def MidsFromGradeRange( movies, lo, hi ):
    mids = []
    for m in movies:
        if lo <= m[3] <= hi:
            mids.append( m[0] )
    return mids
    
def MidsFromLid( inlang, lid ):
    mids = []
    for l in inlang:
        if lid == l[2]:
            mids.append(l[1])
    return mids

def YearsFromGrades( movies, grade ):
    years = []
    for m in movies:
        if grade==m[3]:
            years.append( m[2] )
    years = list(set(years))
    return years


def GradesFromYear( movies, year ):
    grades = []
    for m in movies:
        if year==m[2]:
            grades.append( m[3] )
    return grades

def MoviesDataFromMids( movies, mids ):
    answ = []
    for m in mids:
        answ.append( MovieDataFromMid( movies, m ))
    return answ

def AidFromName( actors, firstname, lastname ):
    aid = -1
    for a in actors:
        if a[1] == firstname and a[2] == lastname:
            aid = a[0]
            break
    return aid
            

def AidsFromMid( isin, mid ):
    aids = []
    for i in isin:
        if mid==i[1]:
            aids.append( i[2] )
    return aids

def MidsFromAid( isin, aid ):
    mids = []
    for i in isin:
        if aid == i[2]:
            mids.append( i[0] )
    return mids

def LndxsFromMid( inlang, mid ):
    lndxs = []
    for l in inlang:
        if mid == l[1]:
            lndxs.append( l[2] )
    return lndxs

def LidsFromLanguage( languages, lid ):
    lids = []
    for i in languages:
        if lid==i[1]:
            lids.append( i[0] )
    return lids
    
# ########### Multi Input - Multi Output #################


def GradesFromYears( movies, years ):
    answ = []
    for y in years:
        answ.extend( GradesFromYear( movies, y  ) )
    return answ

def TitlesFromMids( movies, mids ):
    answ = []
    for m in mids:
        t = TitleFromMid( movies, m )
        answ.append( t )
    return answ

def LndxsFromMids( inlang, mids ):
    answ = []
    for m in mids:
        n = LndxsFromMid( inlang, m )
        answ.extend( n )
    answ = list(set(answ))
    return answ

def LangsFromLndxs( langs, lndxs ):
    answ = []
    for i in lndxs:
        answ.append( LangFromLndx(langs, i ))
    return answ

def AidsFromMids( isin, mids ):
    aids = []
    for m in mids:
        aids.extend( AidsFromMid( isin, m ))
    aids = list(set(aids))
    return aids

def NamesFromAids( actors, aids ):
    names = []
    for a in aids:
        names.append( NameFromAid(actors,a))
    return names

def CountriesFromCids( countries, cids ):
    ctrys = []
    for i in countries:
        if i[0] in cids:
            ctrys.append( i[1] )
    return ctrys

def MidsFromLids( inlang, lids ):
    mids = []
    for ld in lids:
        mids.extend( MidsFromLid(inlang,ld))
    mids = list(set(mids))
    return mids




# ########### Multi Table Functions #################

def MidsFromLid( inlang, lid ):
    mids = []
    for i in inlang:
        if i[2] == lid:
            mids.append( i[1] )            
    return mids

def MidsFromAid( isin, aid ):
    mids = []
    for i in isin:
        if i[2] == aid:
            mids.append( i[1] )            
    return mids

def CidsFromMids( incountry, mids ):
    cids = []
    for i in incountry:
        if i[1] in mids:
            cids.append( i[2] )
    cids = list( set( cids ))
    return cids



