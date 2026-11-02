TEETH_TRESHOLD=16
monsters = [["mike,340","blue"],["james", 14,"green"],["randall",24,"purple"]]

scary_monster = [monster for monster in monsters if monster[1]>TEETH_TRESHOLD]

print(scary_monster)