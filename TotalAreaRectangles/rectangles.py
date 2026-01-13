def calculate(rectangles):
    
    # Instantiate empty list
    area_set = []
    
    # function to add unique rectangles to list
    def count_rectangle(rect):
        for x in range(rect[0], rect[2]):
            for y in range(rect[1], rect[3]):
                if [x,y] not in area_set:
                    area_set.append([x,y])
    
    # iterate over given data (possibly can use list comprehension)
    for rectangle in rectangles:
        count_rectangle(rectangle)
    
    return len((area_set))
    
