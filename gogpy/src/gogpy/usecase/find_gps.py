

# 피타고라스 정리를 활용하여
# 주변 n km 좌표를 구함.
def execute(origin: tuple, target: tuple, r: float) -> bool:
    if r**2 > (target[0] - origin[0])**2 + (target[1] - origin[1])**2:
        return True
    else:
        return False
