"""
Project: Images for hangman game
Start: January 24th, 2024
Last touched: January 24th, 2024 
Author: Madeleine L.
"""

if __name__ == "__main__":
# Create images for stages
    zero = '''
        
            
            
            
            
            
        
    ________________  
    '''

    one = '''
        
        |/      
        |      
        |      
        |      
        |      
        |
    ____|___________  
    '''

    two = '''
        _______
        |/      
        |      
        |      
        |       
        |      
        |
    ____|___________  
    '''

    three = '''
        _______
        |/      |
        |      
        |      
        |       
        |      
        |
    ____|___________  
    '''

    four = '''
        _______
        |/      |
        |      (_)
        |      
        |       
        |      
        |
    ____|___________  
    '''

    five = '''
        _______
        |/      |
        |      (_)
        |       |
        |       
        |      
        |
    ____|___________  
    '''

    six = '''
        _______
        |/      |
        |      (_)
        |      \|
        |       
        |      
        |
    ____|___________  
    '''

    seven = '''
        _______
        |/      |
        |      (_)
        |      \|/
        |       
        |      
        |
    ____|___________  
    '''

    eight = '''
        _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      
        |
    ____|___________  
    '''

    nine = '''
        _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / 
        |
    ____|___________  
    '''

    ten = '''
        _______
        |/      |
        |      (_)
        |      \|/
        |       |
        |      / |
        |
    ____|___________  
    '''

    image_list = [zero, one, two, three, four, five, six, seven, eight, nine, ten]

# define function to get image
def get_image(num):
    print(image_list[num])


# print("this is a test")
# get_image(0)