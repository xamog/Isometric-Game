class Product():
    """Static constants related to the things that cities can build"""
    NOTHING = "nothing"
    
    WALL = "building:wall"
    
    ARCHER = "unit:archer"
    CAVALRY = "unit:cavalry"

    cost = {NOTHING:0, WALL:30, ARCHER:5, CAVALRY:10}

    @staticmethod
    def isUnit(product):
        return "unit" in product
    @staticmethod
    def isBuilding(product):
        return "building" in product
