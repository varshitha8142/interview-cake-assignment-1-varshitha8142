""" A crack team of love scientists from OkEros (a hot new dating site) 
have devised a way to represent dating profiles as rectangles on a two-dimensional plane.

They need help writing an algorithm to find the intersection of two users' 
love rectangles. They suspect finding that intersection is the key to a matching 
algorithm so powerful it will cause an immediate acquisition by Google or Facebook 
or Obama or something.

Two rectangles overlapping a little. It must be love.

Write a function to find the rectangular intersection of two given love rectangles.

As with the example above, love rectangles are always "straight" and never "diagonal." 
More rigorously: each side is parallel with either the x-axis or the y-axis.

They are defined as dictionaries like this:

  my_rectangle = {

    # Coordinates of bottom-left corner
    'left_x'   : 1,
    'bottom_y' : 1,

    # Width and height
    'width'    : 6,
    'height'   : 3,

}

Your output rectangle should use this format as well.  """

# Start coding from here
def rectangular_intersection(rect1,rect2):
  rect1_x_indicies=[v for v in range(rect1['left_x'],rect1['left_x']+rect1['width']+1)]
  rect1_y_indicies=[v for v in range(rect1['bottom_y'],rect1['bottom_y']+rect1['height']+1)]
  rect2_x_indicies=[v for v in range(rect2['left_x'],rect2['left_x']+rect2['width']+1)]
  rect2_y_indicies=[v for v in range(rect2['bottom_y'],rect2['bottom_y']+rect2['height']+1)]
  req_rect_x_indicies=list(set(rect1_x_indicies).intersection(rect2_x_indicies))
  req_rect_y_indicies=list(set(rect1_y_indicies).intersection(rect2_y_indicies))
  req_rect={'left_x':req_rect_x_indicies[0],
            'bottom_y':req_rect_y_indicies[0],
            'width':len(req_rect_x_indicies)-1,
            'height':len(req_rect_y_indicies)-1}
  return req_rect
loverectangle1 = {

    'left_x'   : 1,
    'bottom_y' : 1,

    'width'    : 6,
    'height'   : 3,

}
loverectangle2 = {

    'left_x'   : 6,
    'bottom_y' : 2,

    'width'    : 1,
    'height'   : 3,

}
print(rectangular_intersection(loverectangle1,loverectangle2))
