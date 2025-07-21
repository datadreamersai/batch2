import math

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def dist_btw_2_pts(self,other):
        return math.sqrt(((self.x-other.x)**2+(self.y-other.y)**2))
    

    def dist_from_origin(self):
        return self.dist_btw_2_pts(Point(0,0))
    

    # def dist_from_origin_reg(self,other):
    #     return math.sqrt(((self.x-other.x)**2+(self.y-other.y)**2))


    def mid_point_calc(self,other):
        val1 = (self.x+other.x)/2
        val2 = (self.y+other.y)/2
        return (val1,val2)
    



class Line():
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C

    def dist_from_pt_line(self,point):
        num = abs((self.A*point.x)+(self.B*point.y)+self.C)
        den = math.sqrt((self.A*self.A)+(self.B*self.B))
        res = num/den
        return res
    

    def exist_on_line(self,point):

        if (self.A*point.x)+(self.B*point.y)+self.C==0:
            return "point exists on line"
        else:
            return "point doesn't exist on line"
        

    def relationship_btw_2_lines(line1,line2):
        m1 = -(line1.A/line1.B)
        m2 = -(line2.A/line2.B)
        if m1==m2:
            return "both are parallel"
        elif (m1*m2)==-1:
            return "both are perpendicular"
        
        else:
            return "no relationship exists between both the lines"




p1=Point(2,3)

# p2=Point(3,5)

# o=Point(0,0)

# print(p2.dist_btw_2_pts(p1))

# print(p1.dist_from_origin())

# # print(p1.dist_from_origin_reg(o))


# print(p1.mid_point_calc(p2))




line1 = Line(2,3,6)

line2 = Line(-3,2,4)
print(line1.dist_from_pt_line(p1))


print(line1.exist_on_line(p1))

print(line1.relationship_btw_2_lines(line2))






