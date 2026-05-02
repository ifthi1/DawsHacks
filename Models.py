class Commuter:
    def __init__(self, commuterType, money, speed, game_id):
        self.commuterType = commuterType
        self.money = money
        self.speed = speed
        self.game_id = game_id
    def to_dict(self):
        return {
            'commuterType': self.commuterType,
            'money': self.money
        }
        
    def __str__(self):
        return f"commuterType: {self.commuterType}, money: {self.money}, speed: {self.speed}"

class Bridge:
    def __init__(self, id, capacity, toll, scenery, game_id ):
        self.id = id
        self.capacity = capacity
        self.toll = toll
        self.scenery = scenery
        self.game_id = game_id
    
    def to_dict(self):
        return {
            'id': self.id,
            'level': self.level,
            'capacity': self.capacity,
            'toll': self.toll
        }

class Game:
    def __init__(self, id, level, bridge_id, commuter_id, user_id, current_money ):
        self.id = id
        self.level = level
        self.bridge_id = bridge_id
        self.commuter_id = commuter_id
        self.user_id = user_id
        self.current_money = current_money


dictionary = {
    "level_1": {
        "bridge": "wood",
        "commuter": {
            "type": "person",
            "money":  "1"
        }
        
    },
    "level_2": {
        "bridge": "stone",
        "commuter": {
            "type": "carriage",
            "money":  "5"
        }
        
    },
    "level_3": {
        "bridge": "iron",
        "commuter": {
            "type": "bike",
            "money":  "10"
        }
        
    },
    "level_4": {
        "bridge": "steel",
        "commuter": {
            "type": "car",
            "money":  "25"
        }
        
    },
    "level_5": {
        "bridge": "illuminate bar",
        "commuter": {
            "type": "bus",
            "money":  "50"
        }
        
    }

}