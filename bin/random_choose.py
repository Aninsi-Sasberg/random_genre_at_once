import random, os.path

def random_choose():
    genre_list_path = os.path.expandvars(os.path.join(".", "lists", "genre_list.txt"))
    genre_list_changed_path = os.path.expandvars(os.path.join(".",  "lists", "genre_list_changed.txt"))
    genre_list_randchosen_path = os.path.expandvars(os.path.join(".",  "lists", "genre_list_randchosen.txt"))

    if not os.path.exists(os.path.dirname(genre_list_path)):
            os.makedirs(os.path.dirname(genre_list_path))

    # if changes list doesn't exist yet
    if not os.path.exists(genre_list_changed_path):
        try:
            with open(genre_list_path, "r", encoding="utf-8") as genre_list:
                genres = genre_list.readlines()

        except:
            print(f"File couldn't be read. Execute get_genres.py to write a '{genre_list_path}' file.")

        try:
            with open(genre_list_changed_path, "x+", encoding="utf-8") as genre_list_changed:
                genre_list_changed.writelines(genres)

        except:
            print(f"File '{genre_list_changed_path}' couldn't be written.")

    # read changed file
    try:
        with open(genre_list_changed_path, "r", encoding="utf-8") as genre_list_changed:
            genres = genre_list_changed.readlines()

    except:
        print(f"File couldn't be read. Execute get_genres.py to write a '{genre_list__changed_path}' file.")

    # get random genre
    random_genre_i = random.randrange(0, len(genres))
    random_genre = genres.pop(random_genre_i)

    print(f"Your randomly chosen genre is: {random_genre}")

    # if random genre list doesn't exist yet
    if not os.path.exists(genre_list_randchosen_path):
        # write randomgenre
        try:
            with open(genre_list_randchosen_path, "x+", encoding="utf-8") as genre_list_randchosen:
                genre_list_randchosen.writelines(random_genre)

        except:
            print(f"File '{genre_list_randchosen_path}' couldn't be written.")
    else:
        # write randomgenre
        try:
            with open(genre_list_randchosen_path, "a+", encoding="utf-8") as genre_list_randchosen:
                genre_list_randchosen.writelines(random_genre)

        except:
            print(f"File '{genre_list_randchosen_path}' couldn't be written.")

    # write changes
    try:
        with open(genre_list_changed_path, "w", encoding="utf-8") as genre_list_changed:
            genre_list_changed.writelines(genres)

    except:
        print(f"File '{genre_list_changed_path}' couldn't be written.")
