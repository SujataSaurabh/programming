'''
Pattern 1: 
* * * * 
 * * * 
  * * 
   * 
'''
def print_star_pattern_1(rows):
    for i in range(rows, 0, -1):
        # Print leading spaces
        for _ in range(rows - i):
            print(' ', end='')

        # Print '*' characters for this row
        for _ in range(i):
            print('* ', end='')

        print()  # Move to the next line

'''
Pattern 2:
        *
       * *
      * * *  
'''
def print_star_pattern_2(rows):
    for i in range(0, rows + 1):
        # Print leading spaces
        for _ in range(rows - i):
            print(' ', end='')
        # Print '*' characters for this row
        for _ in range(i):
            print('* ', end='')
        print()  # Move to the next line

 
print_star_pattern_1(4)
print('\n \n')
print_star_pattern_2(4)
 

