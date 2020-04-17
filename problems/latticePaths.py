def lattice_paths(m, n):
  
  def _lattice_paths(row, col):
    # m -> row, n -> col
    if row < 0 or col < 0:
      return 0
      
    if row == 0 and col == 0:
      return 1
    else:
      return _lattice_paths(row - 1, col) + _lattice_paths(row, col - 1)
    
  return _lattice_paths(m, n)

if __name__ == "__main__":
  print(lattice_paths(15,15))
