# takes as input a positive integer n
# returns True if n is prime and False otherwise

def is_prime(n):
    if (n == 1):
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# takes as input a string in lower case and the size
# of the hash table and returns the index the string
# will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# takes as input a string in lower case and the constant
# for double hashing and returns the step size for that
# string
def step_size(s, const):
    key = hash_word(s, const)
    step_size = const - (key % const)

    return step_size


# takes as input a string and a hash table and enters
# the string in the hash table, it resolves collisions
# by double hashing
def insert_word(s,hash_table):  # call hash_word take the index, might not fit the box, so include double hashing conditionals

    len_hash = len(hash_table)  # this stuff is supposed to be in main
    while not is_prime(len_hash):  # this stuff be in main
        len_hash += 1  #

    step_size = step_size(s, 13)
    OG_hash_idx = hash_word(s, len(hash_table):
    dbl_hash_idx = OG_hash_idx
    while hash_table[dbl_hash_idx] != " ":
        double_hash_idx += step_size

    if hash_table[OG_hash_idx] == " ":  # no col
        hash_table[OG_hash_idx] = s
    else:
        hash_table[dbl_hash_idx] = s
    return hash_table

    # string --> #for each letter, is a number, we take that number and we are supposed to put it in the hash table but if a spot is taken, we will use
    # step size as our %. so it will be string %step_size to place the letter into the hash table. %

    # if hash_word # if the spot in hash word is taken, we will do insert word <--- we going to do this main <---
    # < -- we figured out the double hash spot its index now we have to take the hash table
    # put in the letter inside the hash table at the double hashing index. and if the double hashing index the spot is taken, we have to do quadratic hashing x + 1 x + 2^2


# has the index value, so its a number where the letter should go, but we don't know which letter ?


# takes as input a string and a hash table and returns True
# if the string is in the hash table and False otherwise
def find_word(s, hash_table):  # check if the word in the hashtable
    if x in list:
        return True
    else:
        return False


# recursively finds if a word is reducible, if the word is
# reducible it enters it into the hash memo and returns True
# and False otherwise
def is_reducible(s, hash_table,
                 hash_memo):  # a i and o if string has letter ai and o if len(str) == 1 and equal to a, i, and o double recurse
    if find_word(s, hash_table) == True:


hash_memo.append(s)

return True


# goes through a list of words and returns a list of words
# that have the maximum length
#def get_longest_words(string_list):


#def main():


# create an empty word_list

# open the file words.txt

# read words from words.txt and append to word_list

# close file words.txt

# find length of word_list

# determine prime number N that is greater than twice
# the length of the word_list

# create and empty hash_list

# populate the hash_list with N blank strings

# hash each word in word_list into hash_list
# for collisions use double hashing

# create an empty hash_memo

# populate the hash_memo with M blank strings

# create and empty list reducible_words

# for each word in the word_list recursively determine
# if it is reducible, if it is, add it to reducible_words

# find words of the maximum length in reducible_words

# print the words of maximum length in alphabetical order
# one word per line

# This line above main is for grading purposes. It will not
# affect how your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()