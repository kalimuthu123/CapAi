class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    
def without_color():
    Color.PURPLE = ''
    Color.CYAN = ''
    Color.DARKCYAN = ''
    Color.BLUE = ''
    Color.GREEN = ''
    Color.YELLOW = ''
    Color.RED = ''
    Color.BOLD = ''
    Color.ITALIC= ''
    Color.UNDERLINE = ''
    Color.END = ''
