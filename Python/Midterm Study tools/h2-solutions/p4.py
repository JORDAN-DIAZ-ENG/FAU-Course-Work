# Python Programming.
# Homework 2, problem 4
# Instructor: Dr. Ionut Cardei
# Do not distribute.


import csv


def read_ranking(f):
    """
    Can be called with the file of ratings ranking or with the file of top grossing rankings.
    Both files have the same format, with the last column having different meaning.
    Score (below) will be either the ratings score (e.g. 8.9) or US box office grossing $$.
    
    Returns tuple ({(title,year):(rank,score)}, [(rank, (title,year), score)])
    First is a dictionary indexed by (title, year) and with value (rank, score).
    Second is a sorted list with tuples (rank, (title,year), score).

    For the top rating file the line format is: Rank,Title,Year,IMDB Rating.
    For the top grossing file the line format is: Rank,Title,Year,USBoxOffice$$

    May throw parsing and IO exceptions.
    The csv module helps parsing titles containing comma, such as "Monsters, Inc."

    precondition: f is an open CSV file
    """
    rdr = csv.reader(f)
    next(rdr)     # skip header. rdr is an iterator (we'll learn later about them)
    # tr_lst is a list with one tuple per movie: (year, title, year, score)
    t_lst = [(int(ls[0]), ls[1], int(ls[2]), float(ls[3])) for ls in rdr]

    # tr_dict is a dict with key (title,year) and value tuples (rank, score):
    t_dct = { (ls[1], ls[2]):(ls[0], ls[3]) for ls in t_lst }

    # in case the file does not come already sorted:
    # sorted list with tuples (rank, (title,year)):
    t_ranked_lst = sorted([(ls[0], (ls[1], ls[2]), ls[3]) for ls in t_lst ])
    # t_dct looks like: {('The Shawshank Redemption', 1994): (1, 9.2), ('The Godfather', 1972): (2, 9.2), ...}
    # t_ranked_lst looks like: [(1, ('The Shawshank Redemption', 1994), 9.2), (2, ('The Godfather', 1972), 9.2), ...]
    return (t_dct, t_ranked_lst)
    

def read_casts(f):
    """
    Returns a dictionary {(title,year):(Director,Actor1,Actor2,Actor3,Actor4,Actor5)}
    File format: Title,Year,Director,Actor1,Actor2,Actor3,Actor4,Actor5
    Parses the casts file.
    May throw parsing and IO exceptions.
    Precondition: f is an open CSV file
    """
    rdr = csv.reader(f)
    # dictionary comprehension for each list returned by reader:
    casts_dct = {(ml[0], int(ml[1])):(ml[2], ml[3],ml[4],ml[5],ml[6],ml[7])
                 for ml in rdr}
    # casts_dct looks like: {('101 Dalmatians', 1961): ('Clyde Geronimi', 'Rod Taylor', "J. Pat O'Malley", 'Betty Lou Gerson', 'Martha Wentworth', 'Ben Wright'), ...}
    return casts_dct


###########

# a) code

def top_collaborations(ranked_lst:list, cast_dct:dict):
    """ Returns the sorted list with format (#movies, director, actor) for all
        director-actor pairs in the top-ranked list.
        Parameter ranked_lst: list with top-ranked movies, with format [(rank, (title,year), score), ....]
        Parameter cast_dct: dictionary {(title,year):(Director,Actor1,Actor2,Actor3,Actor4,Actor5), ...}
        Precondition parameters properly initialized
        Postcondition: none
    """         
    # The algorithm is this:
    # create empty dictionry collab_dct, with key (director, actor) and value being the number of movies together
    # in the top list.
    # For each movie in top ranked list:
    #    for each (director, actor) combination for the current movie:
    #       increment counter in collab_dct
    # create list of tuples (movies_counter, (director, actor)) and sort it descendingly
    # return sorted list
    
    collab_dct = dict()
    for (rank, (title, year), score) in ranked_lst:
        director = cast_dct[(title, year)][0]
        for actor_nr in range(5):
            actor = cast_dct[(title, year)][1 + actor_nr]
            collab_dct[(director, actor)] = collab_dct.get((director, actor), 0) + 1  # set to 0 initially.

    # get a sortable list of tuples with the counter in the first position:
    collab_lst = [(counter, (director, actor)) for ((director, actor), counter) in collab_dct.items()]
    return sorted(collab_lst, reverse=True)    # sort  by tuple's first field, descending order
    # the returned list looks like:  [(4, ('Christopher Nolan', 'Christian Bale')), (4, ('Charles Chaplin', 'Charles Chaplin')), (3, ('Sergio Leone', 'Clint Eastwood')), ...]
    

def display_slice(msg:str, lst:list, n:int):
    """ Displays a message followed by slice lst[:n].
        Precondition: 0 <= n && n <= len(lst)
        Postcondition: message and slice printed to stdout.
    """
    print(msg)
    for x in lst[:n]: 
        print(x)



def display_top_collaborations(ranked_lst:list, cast_dct:dict):
    """ Displays a chunk of the sorted list of top director-actor pairs based on IMDB ranking.
    """
    top_collab_lst = top_collaborations(ranked_lst, cast_dct)
    display_slice("The top director-actor collaborations are (up to 2014):", top_collab_lst, 20)



#############

# b) code    
def top_grossing_directors(top_gross_lst:list, cast_dct:dict):
    """ Returns the sorted list of top directors based on their box office totals.
    """
    dir_total_dct = dict()
    for movie in top_gross_lst:      # movie is a tuple (rank, (title, year), movie$$)
        director = cast_dct[movie[1]][0]
        dir_total_dct[director] = dir_total_dct.get(director, 0) + movie[2]

    # make a sortable list:
    dir_total_lst = [(total, director) for (director, total) in dir_total_dct.items()]
    return sorted(dir_total_lst, reverse=True)     # sorted by the total, descending order


def display_top_directors(top_gross_lst:list, cast_dct:dict):
    """ Displays a chunk of the sorted list of top directors based on their box office totals.
    """
    total_dir_lst = top_grossing_directors(top_gross_lst, cast_dct)
    display_slice("The top directors (based on box office $$s):", total_dir_lst, 20)
    

# ===========================================================

# c)
def main():
    try:
        cast_f = None
        topranked_f = None
        topgrossing_f = None
        cast_f = open("imdb-top-casts.csv", "r")
        casts_dct = read_casts(cast_f)

        topranked_f = None
        topranked_f = open("imdb-top-rated.csv", "r")
        (tr_dct, tr_rank_lst) = read_ranking(topranked_f)

        topgrossing_f = open("imdb-top-grossing.csv", "r")
        (tg_dct, tg_rank_lst) = read_ranking(topgrossing_f)

        # a):
        display_top_collaborations(tr_rank_lst, casts_dct)

        # b)
        print("\n\n")
        display_top_directors(tg_rank_lst, casts_dct)

    except ValueError as err:
        print("Error:", err)
    except FileNotFoundError as err:
        print("Error:", err)
    except:
        print("Error")
        exit(1)
    finally:
        if cast_f:
            cast_f.close()
        if topranked_f:
            topranked_f.close()


if __name__ == "__main__":
    main()
