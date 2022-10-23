'''
CISC-121 2022W
  
This program proccesses a csv file containing information bout movies
and then plots scatter plot graphs for certain genres. 

Name: Matthew Sun
Student Number: 20273229
Email: matt.suncy@gmail.com

I confirm that this assignment solution is my own work and conforms to 
Queen's standards of Academic Integrity
'''

from matplotlib import pyplot as plt


def file_to_list(movie_data):
    '''
    This function takes a csv file and reads each line and turns the information
    into a list where each element is a list of information about the movie.

    Parameters: movie_data - a csv file of information for movies

    Returns: movies_info - a list of lists containing the information about each
    movie
    '''

    infile = open(movie_data, 'r', encoding='UTF-8')
    movies_info = []
    for line in infile:
        info = line.split(',')

        # Turn things to floats if possible starting from the second column
        # In the case the category is a string we just move on this way we compensate for those empty strings
        for i in range(1, len(info)):
            try:
                info[i] = float(info[i])
            except:
                pass

        # Splitting up the genre words so we have a list of genre words
        info[4] = info[4].split('|')

        movies_info.append(info)

    return movies_info


def list_to_dict(movies_list):
    '''
    This function takes a list of lists of information about movies and organizes
    the list into a dictionary where the keys are the genres and the values are
    the information about each movie.

    Parameters: movies_list - a list of list of information of movies

    Returns: genre_dict - a dictionary organized by genre
    '''

    genre_dict = {}
    for list in movies_list:
        for genre in list[4]:
            if genre in genre_dict:
                genre_dict[genre].append(list)
            else:
                # If the genre isn't already there we add it as a new key
                genre_dict[genre] = [list]

    return genre_dict


csv_file = '/Users/matt.suncy/Documents/CISC 121/A6/IMDB_movie_metadata_for_assignment_6.csv'
movie_info_list = file_to_list(csv_file)
genre_dict = list_to_dict(movie_info_list)

# Plotting Sci-Fi moves
x_vals = []
y_vals = []
for info in genre_dict['Sci-Fi']:
    # If either one of these is empty we'll just skip it
    if info[-4] != '' and info[-2] != '':
        x_vals.append(float(info[-4]))  # budget
        y_vals.append(float(info[-2]))  # IMDB rating
    else:
        pass


fig = plt.figure(figsize=(19, 7))
fig.suptitle('Sci-Fi movies: budget and IMDB rating')
plt.scatter(x_vals, y_vals, color="blue",
            label="Sci-Fi movies")  # color is optional
plt.xlabel("Budget($)")
plt.ylabel("IMDB rating")
plt.legend()
plt.show()

# Plotting Western movies
x_vals = []
y_vals = []
for info in genre_dict['Western']:
    # If either one of these is empty we'll just skip it
    if info[-3] != '' and info[2] != '':
        x_vals.append(float(info[-3]))  # year
        y_vals.append(float(info[2]))  # duration
    else:
        pass


fig = plt.figure(figsize=(19, 7))
fig.suptitle('Western movies: year and duration')
plt.scatter(x_vals, y_vals, color="blue",
            label="Western movies")  # color is optional
plt.xlabel("Year")
plt.ylabel("Duration(min)")
plt.legend()
plt.show()

# Plotting Family movies
x_vals = []
y_vals = []
for info in genre_dict['Family']:
    # If either one of these is empty we'll just skip it
    if info[-4] != '' and info[3] != '':
        x_vals.append(float(info[-4]))  # budget
        y_vals.append(float(info[3]))  # gross
    else:
        pass


fig = plt.figure(figsize=(19, 7))
fig.suptitle('Family movies: budget and gross')
plt.scatter(x_vals, y_vals, color="blue",
            label="Family movies")  # color is optional
plt.xlabel("Budget($)")
plt.ylabel("Gross($)")
plt.legend()
plt.show()


# Plotting Action movies
x_vals = []
y_vals = []
for info in genre_dict['Action']:
    # If either one of these is empty we'll just skip it
    if info[-2] != '' and info[3] != '':
        x_vals.append(float(info[-2]))  # IMDB rating
        y_vals.append(float(info[3]))  # gross
    else:
        pass


fig = plt.figure(figsize=(19, 7))
fig.suptitle('Action movies: IMDB Rating and Gross')
plt.scatter(x_vals, y_vals, color="blue",
            label="Action movies")  # color is optional
plt.xlabel("IMDB rating")
plt.ylabel("Gross")
plt.legend()
plt.show()


# Plotting Fantasy movies
x_vals = []
y_vals = []
for info in genre_dict['Fantasy']:
    # If either one of these is empty we'll just skip it
    if info[-2] != '' and info[3] != '':
        x_vals.append(float(info[-2]))  # IMDB rating
        y_vals.append(float(info[3]))  # gross
    else:
        pass


fig = plt.figure(figsize=(19, 7))
fig.suptitle('Fantasy movies: IMDB Rating and Gross')
plt.scatter(x_vals, y_vals, color="blue",
            label="Fantasy movies")  # color is optional
plt.xlabel("IMDB rating")
plt.ylabel("Gross")
plt.legend()
plt.show()


# Plotting horror movies
x_vals = []
y_vals = []
for info in genre_dict['Horror']:
    # If either one of these is empty we'll just skip it
    if info[-2] != '' and info[3] != '':
        x_vals.append(float(info[-2]))  # IMDB rating
        y_vals.append(float(info[3]))  # gross
    else:
        pass


fig = plt.figure(figsize=(19, 7))
fig.suptitle('Horror movies: IMDB Rating and Gross')
plt.scatter(x_vals, y_vals, color="blue",
            label="Horror movies")  # color is optional
plt.xlabel("IMDB rating")
plt.ylabel("Gross")
plt.legend()
plt.show()
