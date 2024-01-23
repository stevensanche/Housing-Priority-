'''
CIS 122 Spring 2022 Project 5-2
Author(s): Steven Sanchez-Jimenez, Variel Joe Pascoal, Wyatt Humphries, 
Credit: Luis and Annika 
Description: Housing Decisions, implementing an algorithim that uses a
point system to determine the priority order for students to select their
housing
'''

def housing_priority(year, age, off_campus, acad_prob, disc_prob):
    '''
    determines number of points based on year, age, etc.
    
    >>> housing_priority(2, 22, True, True, True)
    -1
    '''
    pts = year
    if age >= 23: 
        pts = pts +1

    if off_campus == True:
        pts = pts + 1

    if acad_prob == True:
        pts = pts - 1

    if disc_prob == True:
        pts = pts - 3

    return pts 
       

def is_eligible():
    '''
    determines if senior is eligible or not

    >>> is_eligible()
    True
    '''
    x = input("Are you graduating this year? (Yes/No)")
    if x == "Yes":
        print('You are not eligible for student housing')
        return False
    elif x == "No": 
        return True
        

    
def process_application(stu_year):
    '''
    prompts questions to student
    >>> process_application(3)
    How old are you?
    '''
    age = int(input('How old are you?[input number]: '))

    off_campus = input('Are you living off campus or teaching?[Yes or No]: ')
    if off_campus == 'Yes':
        off_campus = True
    else:
        False
        
    acad_prob = input('Are you on academic probation?{Yes or No}: ')
    if acad_prob == 'Yes':
        acad_prob = True
        
    disc_prob = input('Are you on disciplinary probation?{Yes or No}: ')
    if disc_prob == 'Yes':
        disc_prob = True

    priority = housing_priority(stu_year, age, off_campus, acad_prob, disc_prob)
    return priority

def report_priority_score(score):
    '''
    says how many points you have

    >>> report_priority_score(5)
    You have 5 points
    '''
    print('You have ', score, 'points')

    return

def housing_main():
    '''
    driver for housing priority program
    '''
    # set up
    print('Welcome to the U Housing Information Center.')
    print('Please respond to the following questions: ')
    print()
    # determine eligibility for housing
    year = int(input('What year are you (1 for 1st year, 2 for 2d, etc.): '))
    if year >= 4:
        housing = is_eligible()
    else:
        housing = True
    if housing:
        priority = process_application(year)
        report_priority_score(priority)
    else:
        print('You are no longer eligible for student housing.')
        
    return
housing_main()




