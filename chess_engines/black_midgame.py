import chess
import chess.engine
#------------------






def get_best_move(board):
    stockfish_path = "D:\.roengine\.ros-engine-windows-x86-64-modern.exe"  # Replace with the path to your Stockfish executable

    try:
        with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
            result = engine.play(board, chess.engine.Limit(time=2.0))
            best_move = result.move
            return best_move
    except Exception as e:
        print(f"Error during move calculation: {e}")
        return None

def main():
    try:
        # Prompt the user for the initial FEN position input
        fen_position = input("Enter the initial FEN position: ")

        # Validate the user input
        board = chess.Board(fen_position)

        while not board.is_game_over():
            print(f"\nCurrent Position:\n{board}")

            if board.turn == chess.WHITE:
                # White's turn (engine)
                # Make the engine move
                best_move = get_best_move(board)

                if best_move is not None:
                    board.push(best_move)
                    print(f"\nEngine's Move: {best_move}")
                else:
                    print("Error in move calculation. Exiting.")
                    break
            else:
                # Black's turn (user)
                # Prompt the user for the move
                user_move = input("Enter your move (in SAN format, e.g., 'e5'): ")

                # Validate and apply the user's move
                try:
                    move = chess.Move.from_uci(board.parse_san(user_move).uci())
                    if move in board.legal_moves:
                        board.push(move)
                        print(f"\nYour Move: {user_move}")
                    else:
                        print(f"Illegal Move: {user_move}")
                        continue
                except ValueError as e:
                    print(f"Invalid Move Format: {user_move}")
                    continue

        print("\nGame Over.")
        print("Result: " + board.result())
        print("Final Position:")
        print(board)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Error during execution: {e}")

if __name__ == "__main__":
    main()
