def check_pos(x_start, x_end, y_start, y_end, mouse) -> bool:
  if x_end > mouse[0] > x_start and y_end > mouse[1] > y_start:
    return True