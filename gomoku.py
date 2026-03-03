#!/usr/bin/env python3
"""
简单的五子棋游戏 - 控制台版本
黑棋 (●) 先手，白棋 (○) 后手
"""

# 棋盘大小
BOARD_SIZE = 15

# 棋子符号
EMPTY = "┼"
BLACK = "●"
WHITE = "○"


def create_board():
    """创建空棋盘"""
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def display_board(board):
    """显示棋盘"""
    # 打印列号
    print("   ", end="")
    for i in range(BOARD_SIZE):
        print(f"{i:2}", end=" ")
    print()
    
    # 打印棋盘
    for row in range(BOARD_SIZE):
        print(f"{row:2} ", end="")
        for col in range(BOARD_SIZE):
            print(f" {board[row][col]}", end=" ")
        print()


def is_valid_move(board, row, col):
    """检查落子是否有效"""
    if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
        return False
    return board[row][col] == EMPTY


def check_win(board, row, col, player):
    """
    检查当前落子是否获胜
    检查四个方向：横、竖、左斜、右斜
    """
    directions = [
        (0, 1),   # 横向
        (1, 0),   # 竖向
        (1, 1),   # 右斜
        (1, -1)   # 左斜
    ]
    
    for dr, dc in directions:
        count = 1  # 当前棋子
        
        # 正方向计数
        r, c = row + dr, col + dc
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            count += 1
            r += dr
            c += dc
        
        # 反方向计数
        r, c = row - dr, col - dc
        while 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE and board[r][c] == player:
            count += 1
            r -= dr
            c -= dc
        
        if count >= 5:
            return True
    
    return False


def get_player_move(board, player):
    """获取玩家落子位置"""
    player_name = "黑棋" if player == BLACK else "白棋"
    
    while True:
        try:
            move = input(f"{player_name} ({player}) 请输入落子位置 (行 列): ")
            parts = move.split()
            if len(parts) != 2:
                print("输入格式错误！请使用：行 列 (例如：7 7)")
                continue
            
            row, col = int(parts[0]), int(parts[1])
            
            if not is_valid_move(board, row, col):
                if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
                    print(f"位置超出范围！请输入 0-{BOARD_SIZE-1} 之间的数字")
                else:
                    print("该位置已有棋子！")
                continue
            
            return row, col
        
        except ValueError:
            print("输入无效！请输入两个整数")


def main():
    """主游戏循环"""
    print("=" * 50)
    print("欢迎来到五子棋游戏！")
    print("黑棋 (●) 先手，白棋 (○) 后手")
    print("输入格式：行 列 (例如：7 7 表示第 7 行第 7 列)")
    print("=" * 50)
    
    board = create_board()
    current_player = BLACK
    move_count = 0
    
    while True:
        display_board(board)
        
        # 获取落子
        row, col = get_player_move(board, current_player)
        board[row][col] = current_player
        move_count += 1
        
        # 检查是否获胜
        if check_win(board, row, col, current_player):
            display_board(board)
            winner = "黑棋" if current_player == BLACK else "白棋"
            print("=" * 50)
            print(f"🎉 恭喜 {winner} ({current_player}) 获胜！")
            print(f"总共下了 {move_count} 步")
            print("=" * 50)
            break
        
        # 检查是否平局
        if move_count >= BOARD_SIZE * BOARD_SIZE:
            display_board(board)
            print("=" * 50)
            print("🤝 平局！棋盘已满")
            print("=" * 50)
            break
        
        # 切换玩家
        current_player = WHITE if current_player == BLACK else BLACK


if __name__ == "__main__":
    main()
