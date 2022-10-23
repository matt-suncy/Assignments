'''
CISC-121 2022W
  
This program organizes animals into different clusters based on the
attributes of each animal. This program contains 3 different distance
measures that are used to create clusters. 

Name: Matthew Sun
Student Number: 20273229
Email: matt.suncy@gmail.com

I confirm that this assignment solution is my own work and conforms to 
Queen's standards of Academic Integrity
'''

import numpy as np
import math
import random

# use skiprows to ignore lines at the top of the file
# use usecols to select specific columns
zoo_table = np.loadtxt("zoo_1.txt", dtype=int,
                       skiprows=1, usecols=range(1, 16))

# Making a dictionary with all the animals are their info
zoo_dict = {}
infile = open('zoo_1.txt', 'r', encoding='UTF-8')
infile = infile.readlines()[1:]
table_index = 0
for line in infile:
    line_words = line.split()
    zoo_dict[line_words[0]] = list(zoo_table[table_index])
    table_index += 1


def manhattan_metric(list1, list2):
    '''
    Function calculates the Manhattan distance distance betwen two points, as
    such the lists should contain the same number of elements.

    Parameters: list1 - a list of integers
    list2 - a list of integers

    Returns: distance - the calculated distance
    '''

    distance = 0
    for i in range(len(list1)):
        distance += abs(int(list1[i]) - int((list2[i])))

    return distance


def euclid_dist(list1, list2):
    '''
    Function calculates the Euclidean distance distance betwen two points, as
    such the lists should contain the same number of elements.

    Parameters: list1 - a list of integers
    list2 - a list of integers

    Returns: distance - the calculated distance
    '''

    distance_squared = 0
    for i in range(len(list1)):
        distance_squared += (abs(int(list1[i]) - int(list2[i]))) ** 2
    distance = math.sqrt(distance_squared)

    return distance


def canberra_dist(list1, list2):
    '''
    Function calculates the Canberra distance distance betwen two points, as
    such the lists should contain the same number of elements.

    Parameters: list1 - a list of integers
    list2 - a list of integers

    Returns: distance - the calculated distance
    '''

    distance = 0
    for i in range(len(list1)):
        try:
            distance += (abs(int(list1[i]) - int(list2[i]))) / \
                (abs(int(list1[i])) + abs(int(list2[i])))
        except:
            distance += 0

    return distance


def make_clusters_manhattan(zoo_dict):
    '''
    Function uses the Manhattan distance measure to group animals into 7
    clusters based on their attributes.

    Parameters: zoo_dict - a dictionary with animal names as keys and a list
    of integers that represent their attributes

    Returns: new_clusters - a list of clusters of animals
    '''

    animal_names = list(zoo_dict.keys())

    # Setting up the first 7 clusters set up

    old_centers = []
    # Choosing 7 unqiue animals to be the starting centers
    while len(old_centers) < 7:
        add_element = random.choice(animal_names)
        if add_element not in old_centers:
            old_centers.append(zoo_dict[add_element])

    # The index for centers and clusters should line up
    old_clusters = []
    for i in range(7):
        old_clusters.append([])

    for n in animal_names:

        list_of_dists = []
        for c in old_centers:
            list_of_dists.append(manhattan_metric(
                zoo_dict[n], c))

        index_of_min = list_of_dists.index(min(list_of_dists))
        old_clusters[index_of_min].append(n)

    # Now we repeat the process until the clusters stabilize
    new_clusters = []
    temp_clusters = [0]
    iter_counter = 0
    while iter_counter < 100 and new_clusters != temp_clusters:

        new_centers = []
        for i in range(len(old_clusters)):

            if old_clusters[i] == []:
                new_centers.append(old_centers[i])

            else:
                temp_list = []
                # There are 15 'attributes' for each animal
                for j in range(15):
                    temp_list.append(0)

                # We go through all animals of each cluster and add each column of attributes together
                for j in range(len(old_clusters[i])):
                    for k in range(len(temp_list)):
                        temp_list[k] += zoo_dict[old_clusters[i][j]][k]

                # Taking the avearge of the sum to find a new center
                for j in range(len(temp_list)):
                    temp_list[j] = temp_list[j] / len(old_clusters[i])

                new_centers.append(temp_list)

        new_clusters = []
        for i in range(7):
            new_clusters.append([])

        for n in animal_names:

            list_of_dists = []
            for c in old_centers:
                list_of_dists.append(manhattan_metric(
                    zoo_dict[n], c))

            # Finds the position of the smallest distance and adds it to the corresponding cluster
            index_of_min = list_of_dists.index(min(list_of_dists))
            new_clusters[index_of_min].append(n)

        old_centers = new_centers

        temp_clusters = old_clusters
        old_clusters = new_clusters

        iter_counter += 1

    return new_clusters


def make_clusters_euclid(zoo_dict):
    '''
    Function uses the Euclidean distance measure to group animals into 7
    clusters based on their attributes.

    Parameters: zoo_dict - a dictionary with animal names as keys and a list
    of integers that represent their attributes

    Returns: new_clusters - a list of clusters of animals
    '''
    animal_names = list(zoo_dict.keys())

    # Setting up the first 7 clusters set up

    old_centers = []
    # Choosing 7 unqiue animals to be the starting centers
    while len(old_centers) < 7:
        add_element = random.choice(animal_names)
        if add_element not in old_centers:
            old_centers.append(zoo_dict[add_element])

    # The index for centers and clusters should line up
    old_clusters = []
    for i in range(7):
        old_clusters.append([])

    for n in animal_names:

        list_of_dists = []
        for c in old_centers:
            list_of_dists.append(euclid_dist(
                zoo_dict[n], c))

        index_of_min = list_of_dists.index(min(list_of_dists))
        old_clusters[index_of_min].append(n)

    # Now we repeat the process until the clusters stabilize
    new_clusters = []
    temp_clusters = [0]
    iter_counter = 0
    while iter_counter < 100 and new_clusters != temp_clusters:

        new_centers = []
        for i in range(len(old_clusters)):

            if old_clusters[i] == []:
                new_centers.append(old_centers[i])

            else:
                temp_list = []
                # There are 15 'attributes' for each animal
                for j in range(15):
                    temp_list.append(0)

                for j in range(len(old_clusters[i])):
                    for k in range(len(temp_list)):
                        temp_list[k] += zoo_dict[old_clusters[i][j]][k]

                for j in range(len(temp_list)):
                    temp_list[j] = temp_list[j] / len(old_clusters[i])

                new_centers.append(temp_list)

        new_clusters = []
        for i in range(7):
            new_clusters.append([])

        for n in animal_names:

            list_of_dists = []
            for c in old_centers:
                list_of_dists.append(manhattan_metric(
                    zoo_dict[n], c))

            index_of_min = list_of_dists.index(min(list_of_dists))
            new_clusters[index_of_min].append(n)

        iter_counter += 1
        old_centers = new_centers
        temp_clusters = old_clusters
        old_clusters = new_clusters

    return new_clusters


def make_clusters_canberra(zoo_dict):
    '''
    Function uses the Canberra distance measure to group animals into 7
    clusters based on their attributes.

    Parameters: zoo_dict - a dictionary with animal names as keys and a list
    of integers that represent their attributes

    Returns: new_clusters - a list of clusters of animals
    '''

    animal_names = list(zoo_dict.keys())

    # Setting up the first 7 clusters set up

    old_centers = []
    # Choosing 7 unqiue animals to be the starting centers
    while len(old_centers) < 7:
        add_element = random.choice(animal_names)
        if add_element not in old_centers:
            old_centers.append(zoo_dict[add_element])

    # The index for centers and clusters should line up
    old_clusters = []
    for i in range(7):
        old_clusters.append([])

    for n in animal_names:

        list_of_dists = []
        for c in old_centers:
            list_of_dists.append(manhattan_metric(
                zoo_dict[n], c))

        index_of_min = list_of_dists.index(min(list_of_dists))
        old_clusters[index_of_min].append(n)

    # Now we repeat the process until the clusters stabilize
    new_clusters = []
    temp_clusters = [0]
    iter_counter = 0
    while iter_counter < 100 and new_clusters != temp_clusters:

        new_centers = []
        for i in range(len(old_clusters)):

            if old_clusters[i] == []:
                new_centers.append(old_centers[i])

            else:
                temp_list = []
                # There are 15 'attributes' for each animal
                for j in range(15):
                    temp_list.append(0)

                for j in range(len(old_clusters[i])):
                    for k in range(len(temp_list)):
                        temp_list[k] += zoo_dict[old_clusters[i][j]][k]

                for j in range(len(temp_list)):
                    temp_list[j] = temp_list[j] / len(old_clusters[i])

                new_centers.append(temp_list)

        new_clusters = []
        for i in range(7):
            new_clusters.append([])

        for n in animal_names:

            list_of_dists = []
            for c in old_centers:
                list_of_dists.append(canberra_dist(
                    zoo_dict[n], c))

            index_of_min = list_of_dists.index(min(list_of_dists))
            new_clusters[index_of_min].append(n)

        old_centers = new_centers
        temp_clusters = old_clusters
        old_clusters = new_clusters
        iter_counter += 1

    return new_clusters


# Testing each of the distance measure methods

print('Clustering using Manhattan Metric:')
for i in range(10):
    print('Trial', i + 1)
    manhattan_cluster = make_clusters_manhattan(zoo_dict)
    for j in range(len(manhattan_cluster)):
        print('Group', j+1, manhattan_cluster[j], '\n')

print()

print('Cluster using Euclid Distance:')
for i in range(10):
    print('Trial', i + 1)
    euclid_cluster = make_clusters_euclid(zoo_dict)
    for j in range(len(euclid_cluster)):
        print('Group', j+1, euclid_cluster[j], '\n')

print()

print('Cluster using Canberra Distance:')
for i in range(10):
    print('Trial', i + 1)
    canberra_cluster = make_clusters_canberra(zoo_dict)
    for j in range(len(canberra_cluster)):
        print('Group', j+1, canberra_cluster[j], '\n')
