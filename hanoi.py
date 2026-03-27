def tower_of_hanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    
    # Move n-1 disks from source to auxiliary rod
    tower_of_hanoi(n - 1, from_rod, aux_rod, to_rod)
    
    # Move the nth disk
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    
    # Move n-1 disks from auxiliary to destination rod
    tower_of_hanoi(n - 1, aux_rod, to_rod, from_rod)


# Driver code
if __name__ == "__main__":
    N = 3
    
    # A, B and C are names of rods
    tower_of_hanoi(N, 'A', 'C', 'B')

