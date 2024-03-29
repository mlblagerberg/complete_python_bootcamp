"""
Project: Images for hangman game
Start: January 24th, 2024
Last touched: January 24th, 2024 
Author: Madeleine L.
"""

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

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


image_list = [zero, one, two, three, four, five, six, seven, eight, nine, ten]


# define function to get image
def get_image(num):
    image_list = [zero, one, two, three, four, five, six, seven, eight, nine, ten]
    return(image_list[num])


if __name__ == "__main__":
    for i in range(0, len(image_list)):
        print(f"\nthis is a test... image {i}")
        print(get_image(i))