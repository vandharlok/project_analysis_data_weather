
class Wrong_input(Exception):
    def __init__(self,message,value):
        self.message=message
        self.value=value
    
def test_value_user(select_user):
    if select_user > 4 or select_user < 1 :
        raise Wrong_input('Invalid Selection, you selected',int(select_user))
   
def value_selected_user(selected_user):
    if selected_user > 6 or selected_user < 1:
        raise Wrong_input('Invalid Selection, you selected',int(selected_user))
    
def valid_length_day(list,days):
    if int(days) > len(list):
        raise Wrong_input('Invalid Selection, please enter a valid number of days, you enter',days )