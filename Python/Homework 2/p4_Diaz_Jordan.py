# Jordan Diaz, This program manages rankings from csv files
import csv


def read_from_top_casts(file_name, director_movies_dict, actor_one_movies_dict):
    """ Reads from the top casts file and modifies two dictionaries based on a csv file"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:

            reader = csv.reader(file)
            lst_of_directors_and_actor1 = []

            # Go line by line creating a dictionary of the movie[director] and movie[actor]
            for line in reader:
                title = line[0]
                director = line[2]
                actor_one = line[3]

                # Check if sets exist
                if not (director in director_movies_dict):
                    director_movies_dict[director] = set()
                if not (actor_one in actor_one_movies_dict):
                    actor_one_movies_dict[actor_one] = set()

                # Add to set and list
                director_movies_dict[director].add(title)
                actor_one_movies_dict[actor_one].add(title)
                lst_of_directors_and_actor1.append((director, actor_one))

            lst_of_tuples = []

            # Build the list of tuples and returns it
            for items in lst_of_directors_and_actor1:
                the_director = items[0]
                the_actor = items[1]

                # uses set theory to find the intersection of the two sets
                shared_movies_count = len(director_movies_dict[the_director] & actor_one_movies_dict[the_actor])
                lst_of_tuples.append((the_director, the_actor, shared_movies_count))

            return lst_of_tuples

    except FileNotFoundError as er:
        print("The file: ", file_name, " does not exist.")
        print("Exception type: {} : the error message was {} ".format(type(er), er))
    except PermissionError as er:
        print("You do not have access to read the file: ", file_name)
        print("Exception type: {} : the error message was {} ".format(type(er), er))

    finally:
        file.close()


def read_from_top_rated(file_name):
    """Reads from the top rated file and returns a list of all the movies"""
    try:
        with open(file_name, "r", encoding="utf-8") as file:

            reader = csv.reader(file)
            lst_of_top_rated = []

            for line in reader:
                title = line[1]
                lst_of_top_rated.append(title)

            lst_of_top_rated.pop(0)
            return lst_of_top_rated


    except FileNotFoundError as er:
        print("The file: ", file_name, " does not exist.")
        print("Exception type: {} : the error message was {} ".format(type(er), er))
    except PermissionError as er:
        print("You do not have access to read the file: ", file_name)
        print("Exception type: {} : the error message was {} ".format(type(er), er))

    finally:
        file.close()


def read_from_top_grossing(file_name, box_office_dict):
    """ Reads from top grossing and alters a dictionary to match the contents of the title and box office of each
    rank """
    try:
        with open(file_name, "r", encoding="utf-8") as file:

            reader = csv.reader(file)
            for line in reader:
                title = line[1]
                box_office = line[3]

                if title != "Title":
                    if not (title in box_office_dict):
                        box_office_dict[title] = set()
                    box_office_dict[title].add(box_office)

            return box_office_dict

    except FileNotFoundError as er:
        print("The file: ", file_name, " does not exist.")
        print("Exception type: {} : the error message was {} ".format(type(er), er))
    except PermissionError as er:
        print("You do not have access to read the file: ", file_name)
        print("Exception type: {} : the error message was {} ".format(type(er), er))

    finally:
        file.close()


def display_top_collaborations(display=None):
    """ Displays ranking of a tuple based on if specific elements of the tuple are in another file"""
    movie_directors = dict()
    movie_actors1 = dict()

    # Get the data from the functions
    lst_of_tuples = read_from_top_casts("imdb-top-casts.csv", movie_directors, movie_actors1)
    lst_of_movies_in_top_rated = read_from_top_rated("imdb-top-rated.csv")
    final_set_of_tuples = set()

    # Filter what is in the top rated list and top cast
    for i in range(0, len(lst_of_tuples)):
        for d_movies in movie_directors[lst_of_tuples[i][0]]:
            if d_movies in lst_of_movies_in_top_rated:
                final_set_of_tuples.add(lst_of_tuples[i])
        for a_movies in movie_actors1[lst_of_tuples[i][1]]:
            if a_movies in lst_of_movies_in_top_rated:
                final_set_of_tuples.add(lst_of_tuples[i])

    # Sort and Display
    count = 1
    final_lst = list(final_set_of_tuples)
    final_lst.sort(key=lambda x: x[2], reverse=True)
    if display is None:
        for element in final_lst:
            print("#{}. ".format(count), element)
            count += 1
    elif 1 < display < len(final_lst):
        for index in range(0, display):
            print("#{}. ".format(count), final_lst[index])
            count += 1


def display_top_directors(display=None):
    """ displays the ranking of movie directors from the top grossing list ordered by the total box office money they
    produced """

    # prepare dictionaries and get data from functions
    dict_of_director = dict()
    dict_of_actor = dict()
    dict_of_top_grossing = dict()
    dict_of_top_grossing = read_from_top_grossing("imdb-top-grossing.csv", dict_of_top_grossing)
    read_from_top_casts("imdb-top-casts.csv", dict_of_director, dict_of_actor)

    # Filter out what can and cannot be use
    final_lst = []
    for items in dict_of_director:
        director = items
        movies_lst = dict_of_director[director]
        for movie in movies_lst:
            if movie in dict_of_top_grossing:
                final_lst.append((director, dict_of_top_grossing[movie].pop(), movie))

    # Sort and Display
    count = 1
    final_lst.sort(key=lambda x: x[1], reverse=True)
    if display is None:
        for element in final_lst:
            print("#{}. ".format(count), element)
            count += 1
    elif 1 < display < len(final_lst):
        for index in range(0, display):
            print("#{}. ".format(count), final_lst[index])
            count += 1


def main():
    """ This is the main function used for testing"""
    display_top_collaborations(display=5)
    print()
    display_top_directors(display=5)


if __name__ == "__main__":
    main()
