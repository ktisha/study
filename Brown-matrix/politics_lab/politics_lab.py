voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    dictList = {}
    for i in range(len(voting_data)):
        splitted = voting_data[i].split()
        lastName = splitted[0]
        voting_record = [int(i) for i in splitted[3:]]
        dictList[lastName] = voting_record
    return dictList
    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    sen_a_vote_record = voting_dict[sen_a]
    sen_b_vote_record = voting_dict[sen_b]
    dot = 0
    assert len(sen_a_vote_record) == len(sen_b_vote_record)
    for i in range(len(sen_a_vote_record)):
        dot += sen_a_vote_record[i] * sen_b_vote_record[i]
    return dot


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """

    sen_vote_record = voting_dict[sen]
    max_similarity = -len(sen_vote_record)
    most_similar_sen = None
    for other in voting_dict:
        if other != sen:
            similarity = policy_compare(sen, other, voting_dict)
            if similarity > max_similarity:
                most_similar_sen = other
                max_similarity = similarity
    return most_similar_sen
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    sen_vote_record = voting_dict[sen]
    min_similarity = len(sen_vote_record)
    least_similar_sen = None
    for other in voting_dict:
        if other != sen:
            similarity = policy_compare(sen, other, voting_dict)
            if similarity < min_similarity:
                least_similar_sen = other
                min_similarity = similarity
    return least_similar_sen

    
    

## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold'



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    dotSum = 0
    for other in sen_set:
        dotSum += policy_compare(sen, other, voting_dict)
    return dotSum / len(sen_set)

most_average_Democrat = 'Biden' # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    average_vector = None
    for e in sen_set:
        average_vector = [0] * len(voting_dict[e])

    for x in sen_set:
        average_vector = [a + b for a, b in zip(average_vector, voting_dict[x])]

    for i in range(len(average_vector)):
        average_vector[i] /= len(sen_set)

    return average_vector

d_sen = [ ( x.split()[0] if (x.split()[1] == "D") else "" ) for x in voting_data ]
d_sen = [ x for x in d_sen if x ]
voting_dict = create_voting_dict()
average_Democrat_record = find_average_record(d_sen, voting_dict) # (give the vector)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    least_similarity = None
    for e in voting_dict:
        least_similarity = len(voting_dict[e])

    sen_pair_a = None
    sen_pair_b = None

    for sen_a in voting_dict:
        for sen_b in voting_dict:
            if sen_a == sen_b:
                pass
            else:
                similarity = policy_compare(sen_a, sen_b, voting_dict)
                if similarity < least_similarity:
                    sen_pair_a = sen_a
                    sen_pair_b = sen_b
                    least_similarity = similarity

    return sen_pair_a, sen_pair_b

