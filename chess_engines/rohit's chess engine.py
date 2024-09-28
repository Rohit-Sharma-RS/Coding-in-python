import chess
import chess.engine


def get_user_move(board):
    while True:
        user_move = input("Enter your move : ").strip()
        if(user_move == 'exit'):
            print("exiting Ro's engine")
            exit()
        if len(user_move) == 4:
            if chess.Move.from_uci(user_move) in board.legal_moves:
                return chess.Move.from_uci(user_move)
            else:
                print("Illegal move! Try again.")
        else:
            print("Invalid move format! Please enter a move in the format 'e2e4'.")


def play_chess():
    board = chess.Board()
    ropath = 'D:\.roengine\.ros-engine-windows-x86-64-modern.exe'

    with chess.engine.SimpleEngine.popen_uci(ropath) as engine:
        while not board.is_game_over():
            print(board)

            if board.turn == chess.WHITE:
                user_move = get_user_move(board)
                board.push(user_move)
            else:
                result= engine.play(board, chess.engine.Limit(depth=1))
                print("Ro's engine suggests:", "\033[91m" + result.move.uci() + "\033[0m")
                board.push(result.move)
        print("Game Over! exiting Rohit's engine")
        print("Result: " + board.result())


if __name__ == "__main__":
    play_chess()
