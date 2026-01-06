def tip_calculator(total_bill: float, tip_percentage: float, people_to_split: int) -> float:
    return round((total_bill / people_to_split) * (1 + tip_percentage / 100), 2)