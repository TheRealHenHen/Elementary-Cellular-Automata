def print_canvas(canvas): 
    for x in range(len(canvas)):
        for y in range(len(canvas[x])):
            print(canvas[x][y], end = "")
        print("")

def rule(canvas, row_number, cell_number, top_left_cell_character, top_middle_cell_character, top_right_cell_character):
    
    first_case = False
    second_case = False
    third_case = False

    top_left_cell = canvas[row_number - 1][cell_number - 1]

    top_middle_cell = canvas[row_number - 1][cell_number]

    if (cell_number + 1 == canvas_width):
        top_right_cell = canvas[row_number - 1][0]
    else:
        top_right_cell = canvas[row_number - 1][cell_number + 1]

        
    if (top_left_cell == top_left_cell_character):
        first_case = True
        
    if (top_middle_cell == top_middle_cell_character):
        second_case = True

    if (top_right_cell == top_right_cell_character):
        third_case = True

    if first_case and second_case and third_case:
        return True
    else:
        return False
    
def all_rules(canvas, row_number, cell_number):

    # Rule 1
    if (rule(canvas, row_number, cell_number, filled_character, filled_character, filled_character)):
        return False
    
    # Rule 2
    if (rule(canvas, row_number, cell_number, filled_character, filled_character, blank_character)):
        return True
    
    # Rule 3
    if (rule(canvas, row_number, cell_number, filled_character, blank_character, filled_character)):
        return False
    
    # Rule 4
    if (rule(canvas, row_number, cell_number, filled_character, blank_character, blank_character)):
        return True
    
    # Rule 5
    if (rule(canvas, row_number, cell_number, blank_character, filled_character, filled_character)):
        return True

    # Rule 6
    if (rule(canvas, row_number, cell_number, blank_character, filled_character, blank_character)):
        return False
    
    # Rule 7
    if (rule(canvas, row_number, cell_number, blank_character, blank_character, filled_character)):
        return False
    
    # Rule 8
    if (rule(canvas, row_number, cell_number, blank_character, blank_character, blank_character)):
        return True
    

canvas_width = 111
canvas_height = 111
blank_character = " "
filled_character = "#"
starting_cell = int(canvas_width / 2)
canvas = []

for row_number in range(canvas_height):
    
    row = []

    for cell_number in range(canvas_width):

        if (row_number == 0):
            if (cell_number == starting_cell):
                row.append(filled_character)
            else:
                row.append(blank_character)
        else:
            if (all_rules(canvas, row_number, cell_number)):
                row.append(filled_character)
            else:
                row.append(blank_character) 

    canvas.append(row)  

print_canvas(canvas)   