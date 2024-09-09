from app.trunk.node1branches import branch_011, branch_012, branch_013

def start_point(number, conv_state):
    x,y,z = [int(char) for char in conv_state]
    
    match x:
        case 0:
            match y:
                case 1:
                    match z:
                        case 1:
                            branch_011(number)
                        
                        case 2:
                            branch_012(number)
                        
                        case 3:
                            branch_013(number)