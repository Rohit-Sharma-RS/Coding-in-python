import chess
import chess.engine


def is_valid_move(move_str, legal_moves):
    return move_str in legal_moves


def get_user_move(board, side):
    legal_moves = [move.uci() for move in board.legal_moves]
    while True:
        user_move = input(f"Enter your move ({side}'s turn, e.g., e2e4): ").strip()
        if(user_move == 'exit'):
            exit()
        if len(user_move) == 4 and user_move.isalnum() and is_valid_move(user_move, legal_moves):
            return chess.Move.from_uci(user_move)
        else:
            print("Invalid move! Try again.")


def checkmate_in_n_moves(board, engine, n):
    result = engine.analysis(board, chess.engine.Limit(time=1.0))
    for entry in result:
        info = entry.get("info", {}).get("score", {})
        if info.get("mate") and info["mate"] <= n:
            return True
    return False


def play_chess():
    board = chess.Board()
    ropath = 'D:\.roengine\.ros-engine-windows-x86-64-modern.exe'

    side = input("Choose your side as 'black' or 'white' ?").capitalize()

    with chess.engine.SimpleEngine.popen_uci(ropath) as engine:
        while not board.is_game_over():
            print(board)

            if board.turn == chess.WHITE:
                if side == "White":
                    user_move = get_user_move(board, side)
                    board.push(user_move)
                else:
                    result = engine.play(board, chess.engine.Limit(time=2.0))
                    suggested_move = result.move.uci()
                    print("Ro suggests:", "\033[91m" + suggested_move + "\033[0m")
                    board.push(result.move)
            else:
                if side == "Black":
                    user_move = get_user_move(board, side)
                    board.push(user_move)
                else:
                    result = engine.play(board, chess.engine.Limit(time=2.0))
                    suggested_move = result.move.uci()
                    print("Ro suggests:", "\033[91m" + suggested_move + "\033[0m")
                    board.push(result.move)

        print("Game Over")
        print("Result: " + board.result())


if __name__ == "__main__":
    play_chess()
