def recommended(title: str, description: str) -> str:
    """
    :param title - movie title:
    :param description - movie description:
    :return: watch_next - title of movie the system recommends

    This function takes the name and description of a movie and uses
    a spacy NLP model to provide a recommendation of what the user
    should watch next. The function uses the en_core_web_md model.
    """

    # import modules
    import spacy

    # Initialise dictionary
    dict = {}

    file_name = "movies.txt"

    # Try opening file
    try:
        # Open file and split data into list
        with open(file_name, "r") as func_file:
            func_tasks = func_file.read().splitlines()

            # Loop through list from file. First line of code skipped to skip .txt headers
            for func_pos, func_line in enumerate(func_tasks):
                # Split data using comma delimiter
                func_data = func_line.split(':')
                # Add data to dictionary
                dict[func_data[1]] = func_data[0]

    # Except block if file not found, print message
    except FileNotFoundError:
        print(f"{file_name} does not exist")

    # load npl model
    nlp = spacy.load('en_core_web_lg')
    model_desc = nlp(master_desc)

    # initialise variable
    max_similarity = 0
    watch_next = ""

    # for each movie description, compare the model description against each movie description
    for movies in dict.keys():
        similarity = nlp(movies).similarity(model_desc)

        # if similarity index is higher than the previous max, make the new max the recommended movie
        if similarity > max_similarity:
            max_similarity = similarity
            # get movie title from description
            watch_next = dict.get(movies)

    # return recommendation
    return watch_next


# Define title and description of movie
master_title = "Planet Hulk"
master_desc = "Will he save their world or destroy it? " \
              "When the Hulk becomes too dangerous for the Earth, " \
              "the Illuminati trick Hulk into a shuttle and launch him " \
              "into space to a planet where the Hulk can live in peace. " \
              "Unfortunately, Hulk land on the planet Sakaar where he " \
              "is sold into slavery and trained as a gladiator."

# Call recommended function
next_watch = recommended(master_title, master_desc)
print(f"Seems you enjoyed {master_title}, we recommend watching {next_watch}")
