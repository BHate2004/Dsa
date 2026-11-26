def n_quuens(n):
    chess_box=[['*' for i in range(n)] for i in range(n)]
    chess_box[0][0]='q'
    return chess_box
print(n_quuens(4))