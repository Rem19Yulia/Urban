def calculate_structure_sum(data):
    total_sum = 0
    
    for item in data:
        if isinstance(item,(int, float)):
            total_sum += item
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, (list, tuple, set)):
            total_sum += calculate_structure_sum(item)
        elif isinstance(item,dict):
            total_sum += calculate_structure_sum(item.keys())
            total_sum += calculate_structure_sum(item.values())
            return total_sum
