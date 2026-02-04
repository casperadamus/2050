import math

class Vector:
    """A class representing mathematical vectors with operations."""
    
    def __init__(self, *components):
        """
        Initialize a vector with any number of components.
        
        Args:
            *components: Variable number of numeric values
            
        Examples:
            Vector(1, 2, 3)
            Vector(4.5, -2.1)
        """
        if not components:
            raise ValueError("Vector must have at least one component")
        self.components = list(components)
        self.dimension = len(self.components)
    
    def __repr__(self):
        """String representation of the vector."""
        return f"Vector({', '.join(map(str, self.components))})"
    
    def __str__(self):
        """Pretty print representation."""
        return f"<{', '.join(map(str, self.components))}>"
    
    def __len__(self):
        """Return the dimension of the vector."""
        return self.dimension
    
    def __getitem__(self, index):
        """Access vector components by index."""
        return self.components[index]
    
    def __setitem__(self, index, value):
        """Set vector component by index."""
        self.components[index] = value
    
    def __eq__(self, other):
        """Check if two vectors are equal."""
        if not isinstance(other, Vector):
            return False
        return self.components == other.components
    
    def __add__(self, other):
        """Vector addition."""
        if not isinstance(other, Vector):
            raise TypeError("Can only add vectors to vectors")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])
    
    def __sub__(self, other):
        """Vector subtraction."""
        if not isinstance(other, Vector):
            raise TypeError("Can only subtract vectors from vectors")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])
    
    def __mul__(self, scalar):
        """Scalar multiplication."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only multiply vector by scalar")
        return Vector(*[scalar * component for component in self.components])
    
   
    def magnitude(self):
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(sum(c ** 2 for c in self.components))

    def dot(self, other):
        """
        Calculate dot product with another vector.
        
        Args:
            other: Another Vector instance
            
        Returns:
            Scalar value of the dot product
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only compute dot product with another vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension")
        return sum(a * b for a, b in zip(self.components, other.components))
    
    def cross(self, other):
        """
        Calculate cross product (only for 3D vectors).
        
        Args:
            other: Another Vector instance
            
        Returns:
            New Vector perpendicular to both input vectors
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only compute cross product with another vector")
        if self.dimension != 3 or other.dimension != 3:
            raise ValueError("Cross product only defined for 3D vectors")
        
        a1, a2, a3 = self.components
        b1, b2, b3 = other.components
        
        return Vector(
            a2 * b3 - a3 * b2,
            a3 * b1 - a1 * b3,
            a1 * b2 - a2 * b1
        )
    def __rmul__(self, scalar):
        """Right scalar multiplication (scalar * vector)."""
        return self.__mul__(scalar)
 
    def __truediv__(self, scalar):
        """Scalar division."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Can only divide vector by scalar")
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(*[component / scalar for component in self.components])
    
    def __neg__(self):
        """Negation of vector."""
        return Vector(*[-component for component in self.components])
    
        
    def normalize(self):
        """Return a unit vector in the same direction."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return self / mag
    
   
    def angle_between(self, other):
        """
        Calculate angle between two vectors in radians.
        
        Args:
            other: Another Vector instance
            
        Returns:
            Angle in radians
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only compute angle with another vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension")
        
        dot_product = self.dot(other)
        magnitudes = self.magnitude() * other.magnitude()
        
        if magnitudes == 0:
            raise ValueError("Cannot compute angle with zero vector")
        
        cos_angle = max(-1, min(1, dot_product / magnitudes))
        return math.acos(cos_angle)
    
    def angle_between_degrees(self, other):
        """Calculate angle between vectors in degrees."""
        return math.degrees(self.angle_between(other))
    
    def project_onto(self, other):
        """
        Project this vector onto another vector.
        
        Args:
            other: Vector to project onto
            
        Returns:
            Projection as a new Vector
        """
        if not isinstance(other, Vector):
            raise TypeError("Can only project onto another vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension")
        
        other_mag_sq = other.dot(other)
        if other_mag_sq == 0:
            raise ValueError("Cannot project onto zero vector")
        
        scalar = self.dot(other) / other_mag_sq
        return scalar * other
    
    def is_parallel(self, other, tolerance=1e-10):
        """Check if two vectors are parallel."""
        if not isinstance(other, Vector):
            return False
        if self.dimension != other.dimension:
            return False
        
        try:
            angle = self.angle_between(other)
            return abs(angle) < tolerance or abs(angle - math.pi) < tolerance
        except ValueError:
            return True  # At least one is zero vector
    
    def is_perpendicular(self, other, tolerance=1e-10):
        """Check if two vectors are perpendicular."""
        if not isinstance(other, Vector):
            return False
        if self.dimension != other.dimension:
            return False
        
        return abs(self.dot(other)) < tolerance
    
    def distance_to(self, other):
        """Calculate Euclidean distance to another vector."""
        if not isinstance(other, Vector):
            raise TypeError("Can only compute distance to another vector")
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension")
        
        return (self - other).magnitude()
    
    def to_list(self):
        """Convert vector to list."""
        return self.components.copy()
    
    def to_tuple(self):
        """Convert vector to tuple."""
        return tuple(self.components)


# Example usage
if __name__ == "__main__":
    # Create vectors
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    v3 = Vector(1, 0, 0)
    v4 = Vector(0, 1, 0)
    
    print(f"\n2D vectors:")
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"Magnitude of v1: {v1.magnitude()}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"3 * v1 = {3 * v1}")
    print(f"v1 / 2 = {v1 / 2}")
    print(f"Dot product v1 · v2 = {v1.dot(v2)}")
    print(f"Angle between v1 and v2: {v1.angle_between_degrees(v2):.2f}°")
    print(f"Distance from v1 to v2: {v1.distance_to(v2):.2f}")
    
    print(f"\n3D vectors:")
    print(f"v3 = {v3}, v4 = {v4}")
    print(f"Cross product v3 × v4 = {v3.cross(v4)}")
    print(f"Are v3 and v4 perpendicular? {v3.is_perpendicular(v4)}")
