p1_x1, p1_y1 = input().split()
p2_x2, p2_y2 = input().split()
p1_x1 = float(p1_x1)
p1_y1 = float(p1_y1)
p2_x2 = float(p2_x2)
p2_y2 = float(p2_y2)

distance_x = ((p2_x2*p2_x2)+(p1_x1*p1_x1)) - ((p2_x2*p1_x1)+(p1_x1*p2_x2))
distance_y = ((p2_y2*p2_y2)+(p1_y1*p1_y1)) - ((p2_y2*p1_y1)+(p1_y1*p2_y2))
distance_final = (distance_x+distance_y)**(1/2)
print('{:.4f}'.format(distance_final))
