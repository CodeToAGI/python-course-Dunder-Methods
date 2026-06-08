"""
╔═══════════════════════════════════════════════════════════════╗
║  CodeToAGI — Episode 15 Challenge                             ║
║  Smart Temperature Class                                      ║
║  Complete all 7 requirements                                  ║
╚═══════════════════════════════════════════════════════════════╝
"""

# ================================================================
# YOUR TASK: Complete the Temperature class below
# ================================================================

class Temperature:
    """
    Smart Temperature Class
    
    Requirements:
    1. Store temperature internally in Celsius
    2. @property fahrenheit that converts on the fly
    3. @property kelvin that converts on the fly
    4. __str__ returns formatted string like "25°C"
    5. __eq__ compares two temperatures by Celsius value
    6. @classmethod from_fahrenheit to create from Fahrenheit
    7. @staticmethod is_freezing returns True if Celsius <= 0
    """
    
    # Step 1: Constructor - store Celsius internally
    def __init__(self, celsius):
        # TODO: Store celsius in an internal variable (e.g., self._celsius)
        pass
    
    # Step 4: __str__ method
    def __str__(self):
        # TODO: Return formatted string like "25°C"
        pass
    
    # Step 5: __eq__ method for equality comparison
    def __eq__(self, other):
        # TODO: Return True if both temperatures have same Celsius value
        # Hint: Check if other is a Temperature instance first
        pass
    
    # Step 2: @property fahrenheit
    @property
    def fahrenheit(self):
        # TODO: Convert Celsius to Fahrenheit
        # Formula: (Celsius * 9/5) + 32
        pass
    
    # Step 3: @property kelvin
    @property
    def kelvin(self):
        # TODO: Convert Celsius to Kelvin
        # Formula: Celsius + 273.15
        pass
    
    # Step 6: @classmethod from_fahrenheit
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        # TODO: Convert Fahrenheit to Celsius, then create Temperature object
        # Formula: (Fahrenheit - 32) * 5/9
        pass
    
    # Step 7: @staticmethod is_freezing
    @staticmethod
    def is_freezing(celsius):
        # TODO: Return True if celsius is 0 or below
        pass


# ================================================================
# BONUS (Optional): Add these extra features
# ================================================================

    # Bonus 1: __repr__ for developers
    def __repr__(self):
        return f"Temperature({self._celsius})"
    
    # Bonus 2: __lt__ for sorting (less than)
    def __lt__(self, other):
        return self._celsius < other._celsius
    
    # Bonus 3: @fahrenheit.setter to set temperature using Fahrenheit
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9


# ================================================================
# TEST CODE - Run this to verify your solution
# ================================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Testing Smart Temperature Class")
    print("=" * 50)
    
    # Test 1: Create temperatures
    print("\n[TEST 1] Creating temperatures")
    temp1 = Temperature(25)
    temp2 = Temperature(0)
    print(f"  temp1 = {temp1}")
    print(f"  temp2 = {temp2}")
    
    # Test 2: Property conversions
    print("\n[TEST 2] Property conversions")
    print(f"  25°C = {temp1.fahrenheit}°F = {temp1.kelvin}K")
    print(f"  0°C = {temp2.fahrenheit}°F = {temp2.kelvin}K")
    
    # Test 3: Class method from_fahrenheit
    print("\n[TEST 3] Class method from_fahrenheit")
    temp3 = Temperature.from_fahrenheit(32)
    print(f"  from_fahrenheit(32) = {temp3}")
    
    # Test 4: Equality comparison
    print("\n[TEST 4] Equality comparison __eq__")
    temp4 = Temperature(0)
    print(f"  temp2 == temp4: {temp2 == temp4}")
    print(f"  temp1 == temp2: {temp1 == temp2}")
    
    # Test 5: Static method is_freezing
    print("\n[TEST 5] Static method is_freezing")
    print(f"  is_freezing(0): {Temperature.is_freezing(0)}")
    print(f"  is_freezing(5): {Temperature.is_freezing(5)}")
    print(f"  is_freezing(-10): {Temperature.is_freezing(-10)}")
    
    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("=" * 50)


# ================================================================
# SOLUTION (Check only after you try)
# ================================================================

"""
SOLUTION:

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    def __str__(self):
        return f"{self._celsius}°C"
    
    def __eq__(self, other):
        if isinstance(other, Temperature):
            return self._celsius == other._celsius
        return False
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15
    
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
    @staticmethod
    def is_freezing(celsius):
        return celsius <= 0
"""
