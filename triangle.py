from math import sqrt


class Triangle:
    def __init__(self, a:float, b:float, c:float):
        self.a = a
        self.b = b
        self.c = c


    def is_valid(self) -> bool:
        '''
        This method checks if the triangle is valid.
        
        Args: 
            No
        Returns:
            bool: True if the triangle is valid, False otherwise
        '''
        if self.a + self.b > self.c and self.b +self.c > self.a and self.a +self.c > self.b:
            return True
        else:
            return False

    def get_type(self) -> str:
        '''
        This method finds the type of the triangle.

        Note: typies are 'Teng yonli', 'Teng tomonli', 'Turli tomonli'
        '''
        if self.is_valid():
            if self.a == self.b ==self.c:
                return 'Teng yonli'
            if not self.a == self.b ==self.c:
                return 'Turli tomonli'
        
    def perimeter(self) -> float:
        '''
        This method finds the perimeter of the triangle.
        Args:
            No
        Returns:
            float: return perimeter of the triangle if the triangle is valid, 0 otherwise
        '''
        p = 0
        if self.is_valid():
            p = self.a + self.b + self.c
        return p
    

    def area(self) -> float:
        '''
        This method finds the area of the triangle.
        Args:
            NO
        Returns:
            float: return area of the triangle if the triangle is valid, 0 otherwise
        '''
        s = self.perimeter() / 2
        a = 0
        if self.is_valid():
            a = sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return a
    

tr = Triangle(3.00, 6.00, 7.00)
print(tr.area( ))