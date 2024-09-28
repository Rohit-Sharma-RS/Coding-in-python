import chess
import chess.svg
import random


def get_random_move(board):
    legal_moves = [move for move in board.legal_moves]
    return random.choice(legal_moves)


def play_chess():
    board = chess.Board()

    while not board.is_game_over():
        print(board)
        user_move_uci = input("Enter your move (in UCI format, e.g., 'e2e4'): ")

        try:
            user_move = chess.Move.from_uci(user_move_uci)
            if user_move in board.legal_moves:
                board.push(user_move)
            else:
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid move format. Try again.")
            continue

        engine_move = get_random_move(board)
        board.push(engine_move)
        print(f"Engine moves: {engine_move.uci()}")

    print("Game Over")
    print("Result:", board.result())


if __name__ == "__main__":
    play_chess()
