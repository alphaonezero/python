while True:
    cypher_base = "abcdefghijklmnopqrstuvwxyz0123456789 "
    key = input("Please input a number: ")
    text_in = input("Please type what you'd like to encrypt.: ").lower()
    text_out = ""
    x = 100
    y = 100
    z = 0
    
    for character in text_in:
        print("="*20)
        print("STARTING CHAR: ",character)
        
        print("KEY: ",key)
        key_step = (int(key) + x)
        print("KEY_STEP: ",key_step)
        
        position = cypher_base.find(character)
        print("POSITION: ",position)
        
        position_step = (position + y)
        print("POSITION_STEP: ",position_step)
        
        new_position = ((position_step + key_step) % 37)
        print("NEW_POSITION: ",new_position)
        
        new_character = cypher_base[new_position]
        print("NEW CHAR: ",new_character)
        
        if z % 2 == 0:
            x += 10
            y += 11
        elif z % 2 == 1:
            x += 3
            y += 6

        z += 1
        text_out += new_character
    
    print("+"*30)
    print("Encrypted Comms: ","--->",text_out,"<---")
    print("x: ",x," ","y: ",y," ","z: ",z," ")
