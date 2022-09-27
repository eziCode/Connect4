user_moves = []
cpu_moves = []
userTurn = True
cpuTurn = False
gameOverUser = False
gameOverCpu = False
first_move = input("Who goes first P/C? ")
if first_move == 'P' or first_move == 'p' or first_move == 'Player':
    userTurn = True
    cpuTurn = False
elif first_move == 'C' or first_move == 'c' or first_move == 'CPU':
    userTurn = False
    cpuTurn = True
    
possible_moves = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6',
                  'B1', 'B2', 'B3', 'B4', 'B5', 'B6',
                  'C1', 'C2', 'C3', 'C4', 'C5', 'C6',
                  'D1', 'D2', 'D3', 'D4', 'D5', 'D6',
                  'E1', 'E2', 'E3', 'E4', 'E5', 'E6',
                  'F1', 'F2', 'F3', 'F4', 'F5', 'F6',
                  'G1', 'G2', 'G3', 'G4', 'G5', 'G6']

"""
1. If AI can win, it should win.
2. If AI can't win, it should block.
3. If AI can't win or block, it should make its move in a place to win in 2.
4. If AI has no where to play for win in 2, make its move for win in 3.
5. If AI has no where to move for win in 3, AI should play a randomly generated move.
"""

#while possible_moves != []:


#Ways to win for user
if 'A1' and 'A2' and 'A3' and 'A4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A2' and 'A3' and 'A4' and 'A5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A3' and 'A4' and 'A5' and 'A6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B1' and 'B2' and 'B3' and 'B4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False
    
if 'B2' and 'B3' and 'B4' and 'B5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B3' and 'B4' and 'B5' and 'B6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C1' and 'C2' and 'C3' and 'C4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C2' and 'C3' and 'C4' and 'C5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C3' and 'C4' and 'C5' and 'C6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D1' and 'D2' and 'D3' and 'D4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D2' and 'D3' and 'D4' and 'D5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D3' and 'D4' and 'D5' and 'D6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'E1' and 'E2' and 'E3' and 'E4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'E2' and 'E3' and 'E4' and 'E5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'E3' and 'E4' and 'E5' and 'E6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'F1' and 'F2' and 'F3' and 'F4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'F2' and 'F3' and 'F4' and 'F5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'F3' and 'F4' and 'F5' and 'F6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'G1' and 'G2' and 'G3' and 'G4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'G2' and 'G3' and 'G4' and 'G5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'G3' and 'G4' and 'G5' and 'G6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A1' and 'B1' and 'C1' and 'D1' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B1' and 'C1' and 'D1' and 'E1' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C1' and 'D1' and 'E1' and 'F1' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D1' and 'E1' and 'F1' and 'G1' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A2' and 'B2' and 'C2' and 'D2' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B2' and 'C2' and 'D2' and 'E2' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C2' and 'D2' and 'E2' and 'F2' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D2' and 'E2' and 'F2' and 'G2' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A3' and 'B3' and 'C3' and 'D3' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B3' and 'C3' and 'D3' and 'E3' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C3' and 'D3' and 'E3' and 'F3' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D3' and 'E3' and 'F3' and 'G3' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A4' and 'B4' and 'C4' and 'D4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B4' and 'C4' and 'D4' and 'E4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C4' and 'D4' and 'E4' and 'F4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D4' and 'E4' and 'F4' and 'G4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A5' and 'B5' and 'C5' and 'D5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B5' and 'C5' and 'D5' and 'E5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C5' and 'D5' and 'E5' and 'F5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D5' and 'E5' and 'F5' and 'G5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A6' and 'B6' and 'C6' and 'D6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B6' and 'C6' and 'D6' and 'E6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C6' and 'D6' and 'E6' and 'F6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D6' and 'E6' and 'F6' and 'G6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A1' and 'B2' and 'C3' and 'D4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B2' and 'C3' and 'D4' and 'E5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C3' and 'D4' and 'E5' and 'F6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B1' and 'C2' and 'D3' and 'E4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C2' and 'D3' and 'E4' and 'F5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D3' and 'E4' and 'F5' and 'G6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'C1' and 'D2' and 'E3' and 'F4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D2' and 'E3' and 'F4' and 'G5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D1' and 'E2' and 'F3' and 'G4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A2' and 'B3' and 'C4' and 'D5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'B3' and 'C4' and 'D5' and 'E6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'A3' and 'B4' and 'C5' and 'D6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False



if 'G1' and 'F2' and 'E3' and 'D4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'F2' and 'E3' and 'D4' and 'C5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'E3' and 'D4' and 'C5' and 'B6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'F1' and 'E2' and 'D3' and 'C4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'E2' and 'D3' and 'C4' and 'B5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D3' and 'C4' and 'B5' and 'A6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'E1' and 'D2' and 'C3' and 'B4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D2' and 'C3' and 'B4' and 'A5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'D1' and 'C2' and 'B3' and 'A4' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'G2' and 'F3' and 'E4' and 'D5' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'F3' and 'E4' and 'D5' and 'C6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False

if 'G3' and 'F4' and 'E5' and 'D6' in user_moves:
    gameOverUser = True
    userTurn = False
    cpuTurn = False


#Ways to win for CPU
if 'A1' and 'A2' and 'A3' and 'A4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A2' and 'A3' and 'A4' and 'A5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A3' and 'A4' and 'A5' and 'A6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B1' and 'B2' and 'B3' and 'B4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False
    
if 'B2' and 'B3' and 'B4' and 'B5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B3' and 'B4' and 'B5' and 'B6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C1' and 'C2' and 'C3' and 'C4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C2' and 'C3' and 'C4' and 'C5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C3' and 'C4' and 'C5' and 'C6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D1' and 'D2' and 'D3' and 'D4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D2' and 'D3' and 'D4' and 'D5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D3' and 'D4' and 'D5' and 'D6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'E1' and 'E2' and 'E3' and 'E4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'E2' and 'E3' and 'E4' and 'E5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'E3' and 'E4' and 'E5' and 'E6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'F1' and 'F2' and 'F3' and 'F4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'F2' and 'F3' and 'F4' and 'F5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'F3' and 'F4' and 'F5' and 'F6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'G1' and 'G2' and 'G3' and 'G4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'G2' and 'G3' and 'G4' and 'G5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'G3' and 'G4' and 'G5' and 'G6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A1' and 'B1' and 'C1' and 'D1' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B1' and 'C1' and 'D1' and 'E1' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C1' and 'D1' and 'E1' and 'F1' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D1' and 'E1' and 'F1' and 'G1' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A2' and 'B2' and 'C2' and 'D2' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B2' and 'C2' and 'D2' and 'E2' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C2' and 'D2' and 'E2' and 'F2' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D2' and 'E2' and 'F2' and 'G2' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A3' and 'B3' and 'C3' and 'D3' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B3' and 'C3' and 'D3' and 'E3' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C3' and 'D3' and 'E3' and 'F3' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D3' and 'E3' and 'F3' and 'G3' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A4' and 'B4' and 'C4' and 'D4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B4' and 'C4' and 'D4' and 'E4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C4' and 'D4' and 'E4' and 'F4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D4' and 'E4' and 'F4' and 'G4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A5' and 'B5' and 'C5' and 'D5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B5' and 'C5' and 'D5' and 'E5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C5' and 'D5' and 'E5' and 'F5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D5' and 'E5' and 'F5' and 'G5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A6' and 'B6' and 'C6' and 'D6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B6' and 'C6' and 'D6' and 'E6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C6' and 'D6' and 'E6' and 'F6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D6' and 'E6' and 'F6' and 'G6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A1' and 'B2' and 'C3' and 'D4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B2' and 'C3' and 'D4' and 'E5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C3' and 'D4' and 'E5' and 'F6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B1' and 'C2' and 'D3' and 'E4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C2' and 'D3' and 'E4' and 'F5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D3' and 'E4' and 'F5' and 'G6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'C1' and 'D2' and 'E3' and 'F4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D2' and 'E3' and 'F4' and 'G5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D1' and 'E2' and 'F3' and 'G4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A2' and 'B3' and 'C4' and 'D5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'B3' and 'C4' and 'D5' and 'E6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'A3' and 'B4' and 'C5' and 'D6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'G1' and 'F2' and 'E3' and 'D4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'F2' and 'E3' and 'D4' and 'C5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'E3' and 'D4' and 'C5' and 'B6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'F1' and 'E2' and 'D3' and 'C4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'E2' and 'D3' and 'C4' and 'B5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D3' and 'C4' and 'B5' and 'A6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'E1' and 'D2' and 'C3' and 'B4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D2' and 'C3' and 'B4' and 'A5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'D1' and 'C2' and 'B3' and 'A4' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'G2' and 'F3' and 'E4' and 'D5' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'F3' and 'E4' and 'D5' and 'C6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False

if 'G3' and 'F4' and 'E5' and 'D6' in cpu_moves:
    gameOverCpu = True
    userTurn = False
    cpuTurn = False


