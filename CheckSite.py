import time, DeleteLastSlash

def toSiteUrl (href):
#must check url before. this means, tail is not '/'
    href = DeleteLastSlash.DeleteLastSlash(href)
    strlist = href.split('/')
    if len(strlist) > 2:
        return strlist[0] + "//" + strlist[2]
    else:
        return href
#two function
#one: check could visit this site? before add url into the queue
#two: check coudl process this site now? before process this page

def checkRobot (href):
    return True

#-1 not visitable
def checkSite_Visitable (href):
    global number_visited_site
    global hash_table_site
    global lastVisittime
    global visitTimes
    href = toSiteUrl(href)
    if hash_table_site.get(href) == None:
    #visit this site the first time
    #check robots.txt
    #initial visit times
        if checkRobot(href):
            hash_table_site[href] = number_visited_site
            lastVisittime[number_visited_site] = -1
            visitTimes[number_visited_site] = 0
            number_visited_site += 1
            return 1
        else:
            return -1
    else:
        return 1

#-1 not visible
#-2 not now, later, push into queue again
def checkSite_Processible (href):
    global number_visited_site
    global hash_table_site
    global lastVisittime
    global visitTimes
    href = toSiteUrl(href)
#must been checked after checkSite_Visitable
#so must be in hash table and checekd robots.txt
    index = hash_table_site[href]
    if visitTimes[index] > max_visit_times :
        return -1
    elif time.time() - lastVisittime[index] < min_visit_delay :
        return -2
    else:
        lastVisittime[index] = time.time()
        visitTimes[index] += 1
        return 1

max_visit_times = 3
min_visit_delay = 0.1 #s
number_visited_site = 0
hash_table_site = {}
lastVisittime = {}
visitTimes = {}
#todo: black list 
