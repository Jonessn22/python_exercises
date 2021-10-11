#!/usr/bin/env python
# coding: utf-8

# # 1.
# ### Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[164]:


def is_two(x):
    #when the parameter variable x is passed to function is_two
    #we use a conditional to see if x is in the list with the specified results 
    # of the int value 2 or the string value 'two'
    if x in ['two', 2]:
        #if the conditional is met we return the bool value True, if it is not met we return False
        return True
    else:
        return False


# # 2.
# ### Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[168]:


def is_vowel(string):
    #using the .lower() method to lowercase all characters that will be passed through the parameter string 
    #create a conditional to test if the specified vowel values are in the parameter string
        if string.lower() in 'aeiou':
            return True
        else:
            return False


# # 3.
# ### Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[174]:


def is_consonant(string):
    #using the .lower() method to lowercase all characters that will be passed through the parameter string 
    #create a conditional to test if the specified consonant values are in the parameter string
    string = string.lower()
    return not is_vowel(string)

                


# # 4.
# ### Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[153]:


def capitalize(string):
    #takes the variable parameter string and lowercases all its letters using the .lower() method
    #uses conditional statement to check to see if consonant is at index 0 of the parameter string
    if string[0].lower() in 'bcdfghjklmnpqrstvwxyz':
        return string.capitalize()
    else: 
        return string



# # 5.
# ### Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[45]:


def tip_amt(tip_p, bill):
    #uses a conditional statement to test whether the function parameter tip_p (tip%) is between 0 and 1
    #if it is returns the product of the function parameters, tip_p and bill (amount of the bill)
    if 0 <= tip_p <= 1:
        return tip_p * bill
    else:
        return 'tip_p must be between 0 and 1 - Try again!'

tip_amt(.2, 10)


# # 6.
# ### Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[49]:


def discount(price, percent):
    #takes the function parameter price and subtracts the product of the percent and tip parameters
    #returns the discount price
    return price - (price * percent)

discount(10, .1)


# # 7.
# ### Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[155]:


def handle_commas(string):
    #takes the function parameter string and uses the .replace() method to remove all commas in an integer
    #the .replace parameters looks for commas (first parameter) and replaces them with an empty string
    return int(string.replace(',', ''))



# # 8.
# ### Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[157]:


def get_letter_grade(num_grade):
    #takes the num_grade parameter and uses conditional statements to evaluate what letter grade to return
    #when the num_grade argument is entered below it will run the function
    if num_grade > 89:
        return 'A'
    elif num_grade > 79:
        return 'B'
    elif num_grade > 69:
        return 'C'
    elif num_grade > 59:
        return 'D'
    else:
        return 'F'
    
    


# # 9. 
# ### Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[159]:


def remove_vowels(string):
    #takes the string paramter and lowercases it using the .lower() method
    string = string.lower()
    
    #creates a for loop and looks for vowels in a string to place with an empty space, returning the string
    for char in "aeiou":
        string = string.replace(char,'')
    return string


# # 10.
# ### Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# 
# ### For example:
# - Name will become name
# - First Name will become first_name
# - % Completed will become completed

# In[162]:


def normalize_name(string):
    #takes the string parameter and uses the .lower() method to lowercase all characters in the string
    string = string.lower()
    
    #takes the lowercased string and strips the empty spaces from the beg and end using the .strip() method
    string = string.strip()
    
    #takes the lowercased, stripped string and replaces the spaces with '_' character
    string = string.replace(' ', '_')
    
    #uses the not operator to test whether the string at index 0 is an alphabet character using the .isalpha() method
    #the loop will run and update the string to reflect the string, the character at the next index to the end of the string
    #the loop will stop running at the first alphabet character
    while not string[0].isalpha():
        string = string[1:] 
    
    #returns the lowercased and stripped version of the argument passed through the function
    #with the empty spaces inside the string replaced by _ character, removing the non-alphabet characters at the beg of the string
    return string

normalize_name('     @*&       here is same   ')
        


# # 11.
# ### Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# - cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# - cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[145]:


#define the function with the parameter variable = no_list
def cumulative_sum(list):
    #initalizing an empty list
    sum_list = []
    
    #setting a counting variable = to the first index number of 0
    i = 0
    
    #creating a for loop and using the range() function, starting at 0 and stopping at the length of the list 
    #(using the len() function) to update
    for count in range(0, len(list)):
        i = i + list[count]
        sum_list.append(i)
    return sum_list

cumulative_sum([1, 1, 1])


# In[ ]:





# In[ ]:




