"""
Starter Unit Tests using the built-in Python unittest library.
See https://docs.python.org/3/library/unittest.html

You can expand these to cover more cases!

To run the unit tests, use the following command in your terminal,
in the folder where this file exists:

python tests.py -v
"""
import unittest,time

import RouteFinder
import moveLogic,Board,paranoid


class moveLogicTestCases(unittest.TestCase):

    def test_avoid_left_wall(self):
        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'st', 'sb', 'sh', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['sh', 'sb', 'st', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 0, 'y': 5}, {'x': 1, 'y': 5}, {'x': 2, 'y': 5}], 'head': {'x': 0, 'y': 5}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_walls(my_snake["head"],len(board),len(board),possible_moves)
        # Assert
        self.assertEqual(["up","down","right"], result_moves)

    def test_avoid_right_wall(self):
        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'st', 'sb', 'sh', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'st', 'sb', 'sh'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 10, 'y': 5}, {'x': 9, 'y': 5}, {'x': 8, 'y': 5}], 'head': {'x': 10, 'y': 5}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_walls(my_snake["head"],len(board),len(board),possible_moves)
        # Assert
        self.assertEqual(["up","down","left"], result_moves)

    def test_avoid_bottom_wall(self):
        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'st', 'sb', 'sh', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'st', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}], 'head': {'x': 1, 'y': 0}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_walls(my_snake["head"],len(board),len(board),possible_moves)
        # Assert
        self.assertEqual(["up","left","right"], result_moves)

    def test_avoid_top_and_right_wall(self):
        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
        ['x', 'x', 'x', 'x', 'st', 'sb', 'sh', 'x', 'x', 'x', 'st'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 10, 'y': 10}, {'x': 9, 'y': 9}, {'x': 8, 'y': 8}], 'head': {'x': 10, 'y': 10}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_walls(my_snake["head"],len(board),len(board),possible_moves)
        # Assert
        self.assertEqual(["down","left"], result_moves)

    def test_head_collision_right(self):

        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'sh'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 10, 'y': 8}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6}], 'head': {'x': 10, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)
        # Assert
        self.assertEqual(["up","down","left"], result_moves)

    def test_head_collision_left(self):

        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'st', 'sb', 'sh', 'x', 'sh', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 8}], 'head': {'x':6, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)
        # Assert
        self.assertEqual(["up","down","right"], result_moves)

    def test_head_collision_down_and_left(self):
        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'st', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x': 8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 7, 'y': 7}, {'x': 7, 'y': 6}, {'x': 7, 'y': 5}], 'head': {'x': 7, 'y': 7}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)

        # Assert
        self.assertEqual(["up","right"], result_moves)

    def test_head_collision_up_and_right(self):
        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'st', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 7, 'y': 7}, {'x': 7, 'y': 6}, {'x': 7, 'y': 5}], 'head': {'x': 7, 'y':7}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes =[{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 7, 'y': 7}, {'x': 7, 'y': 6}, {'x': 7, 'y': 5}], 'head': {'x': 7, 'y':7}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}], 'head': {'x':8, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)

        # Assert
        self.assertEqual(["down","left"], result_moves)

    def test_head_collision_bigger_snake(self):

        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'st', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'st', 'sb', 'sh', 'x', 'sh', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10},{'x':9,'y':10}], 'head': {'x': 8, 'y': 8}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10},{'x':9,'y':10}], 'head': {'x': 8, 'y': 8}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}], 'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 8}], 'head': {'x':6, 'y': 8}, 'length': 3, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)
        # Assert
        self.assertEqual(["up","down","left","right"], result_moves)

    def test_head_collision_up2(self):

        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'sh', 'sb', 'x'],
        ['x', 'x', 'sb', 'sb', 'x', 'sb', 'x'],
        ['x', 'x', 'sb', 'sb', 'sh', 'sb', 'x'],
        ['x', 'x', 'st', 'x', 'x', 'sb', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 4, 'y': 3}, {'x': 3, 'y': 3}, {'x': 3, 'y': 5}, {'x': 2, 'y': 5}, {'x': 2, 'y': 4}, {'x': 2, 'y': 3}], 'head': {'x': 4, 'y': 3}, 'length': 6, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95, 'body': [{'x': 4, 'y': 6}, {'x': 3, 'y': 3}, {'x': 3, 'y': 5}, {'x': 2, 'y': 5}, {'x': 2, 'y': 4}, {'x': 2, 'y': 3}], 'head': {'x': 4, 'y': 3}, 'length': 6, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93, 'body': [{'x': 4, 'y': 5}, {'x': 5, 'y': 5}, {'x': 5, 'y': 4}, {'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 5, 'y': 1}, {'x': 4, 'y': 1}, {'x': 3, 'y': 1}], 'head': {'x': 4, 'y': 5}, 'length': 8, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        possible_moves = ["up", "down", "left", "right"]

        # Act
        result_moves = moveLogic.checkForHeadCollision(my_snake,snakes,possible_moves,board)

        # Assert
        self.assertEqual(["down","left","right"], result_moves)

    def test_avoid_left_snake(self):
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'st', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'st', 'sb', 'sh', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
        'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}, {'x': 9, 'y': 10}],
        'head': {'x': 8, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
        'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
        'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}, {'x': 9, 'y': 10}],
        'head': {'x': 8, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
        'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
        {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
        'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}],
        'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '',
        'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
        {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93,
        'body': [{'x': 7, 'y': 9}, {'x': 7, 'y': 8}, {'x': 6, 'y': 8}], 'head': {'x': 7, 'y': 9}, 'length': 3,
        'shout': '', 'squad': '',
        'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_other_snakes(my_snake["head"],snakes,possible_moves)

        # Assert
        self.assertEqual(["down","right"], result_moves)

    def test_avoid_right_snake(self):
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'st', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sh', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb', 'st'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
        'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}, {'x': 9, 'y': 10}],
        'head': {'x': 8, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
        'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
        'body': [{'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}, {'x': 9, 'y': 10}],
        'head': {'x': 8, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
        'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
        {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
        'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}],
        'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '',
        'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
        {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93,
        'body': [{'x': 9, 'y': 9}, {'x': 9, 'y': 8}, {'x': 10, 'y': 8}], 'head': {'x': 7, 'y': 9},
        'length': 3,
        'shout': '', 'squad': '',
        'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_other_snakes(my_snake["head"], snakes, possible_moves)

        # Assert
        self.assertEqual(["down", "left"], result_moves)

    def test_avoid_above_snake(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'st', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}],
                   'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93,
                   'body': [{'x': 6, 'y': 9}, {'x': 7, 'y': 9}, {'x': 7, 'y': 10}], 'head': {'x': 6, 'y': 9},
                   'length': 3,
                   'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_other_snakes(my_snake["head"], snakes, possible_moves)

        # Assert
        self.assertEqual(["down", "left"], result_moves)

    def test_avoid_below_snake(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb', 'st', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}],
                   'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93,
                   'body': [{'x': 6, 'y': 7}, {'x': 7, 'y': 7}, {'x': 6, 'y': 8}], 'head': {'x': 6, 'y': 7},
                   'length': 3,
                   'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_other_snakes(my_snake["head"], snakes, possible_moves)

        # Assert
        self.assertEqual(["up", "left"], result_moves)

    def test_avoid_own_right(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}],
                   'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_other_snakes(my_snake["head"], snakes, possible_moves)

        # Assert
        self.assertEqual(["up","down", "left"], result_moves)

    def test_avoid_own_left(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sh', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 9, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 9, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 9, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 9, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}],
                   'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_other_snakes(my_snake["head"], snakes, possible_moves)

        # Assert
        self.assertEqual(["up","down", "right"], result_moves)

    def test_avoid_own_down(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 9}, {'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 9}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 9}, {'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 9}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}],
                   'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_other_snakes(my_snake["head"], snakes, possible_moves)

        # Assert
        self.assertEqual(["up", "left"], result_moves)

    def test_avoid_own_up(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'st', 'sb', 'sb', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 7}, {'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 7}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 7, 'y': 7}, {'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 8, 'y': 9}, {'x': 8, 'y': 10}],
                    'head': {'x': 7, 'y': 7}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 5, 'y': 3}, {'x': 5, 'y': 2}, {'x': 4, 'y': 2}, {'x': 3, 'y': 2}],
                   'head': {'x': 5, 'y': 4}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        possible_moves = ["up", "down", "left", "right"]
        # Act
        result_moves = moveLogic.avoid_other_snakes(my_snake["head"], snakes, possible_moves)

        # Assert
        self.assertEqual(["down", "left", "right"], result_moves)

    def test_generate_moves_top_right_corner(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sh', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x', 'sh'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 9, 'y': 9}, {'x': 9, 'y': 10}, {'x': 8, 'y': 10}, {'x': 8, 'y': 9}, {'x': 8, 'y': 7}],
                    'head': {'x': 9, 'y': 9}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 9, 'y': 9}, {'x': 9, 'y': 10}, {'x': 8, 'y': 10}, {'x': 8, 'y': 9}, {'x': 8, 'y': 7}],
                    'head': {'x': 9, 'y': 9}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 8}, {'x': 10, 'y': 9}, {'x': 10, 'y': 10}],
                   'head': {'x': 10, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        # Act
        result_moves = moveLogic.generateMoves(board,my_snake,snakes)

        # Assert
        self.assertEqual(["down"], result_moves)

    def test_generate_moves_bottom_right_corner(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 9, 'y': 0}, {'x': 9, 'y': 1}, {'x': 9, 'y': 2}],
                    'head': {'x': 9, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 9, 'y': 0}, {'x': 9, 'y': 1}, {'x': 9, 'y': 2}],
                    'head': {'x': 9, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 8}, {'x': 10, 'y': 9}, {'x': 10, 'y': 10}],
                   'head': {'x': 10, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        # Act
        result_moves = moveLogic.generateMoves(board,my_snake,snakes)

        # Assert
        self.assertEqual(["left", "right"], result_moves)

    def test_generate_moves_bottom_left_corner(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 2}],
                    'head': {'x': 1, 'y': 1}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 2}],
                    'head': {'x': 1, 'y': 1}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 8}, {'x': 10, 'y': 9}, {'x': 10, 'y': 10}],
                   'head': {'x': 10, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        # Act
        result_moves = moveLogic.generateMoves(board,my_snake,snakes)

        # Assert
        self.assertEqual(["left","up", "down"], result_moves)

    def test_generate_moves_top_left_corner(self):
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 1, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 1, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        # Act
        result_moves = moveLogic.generateMoves(board,my_snake,snakes)

        # Assert
        self.assertEqual(["up", "right"], result_moves)

class paranoidTestCases(unittest.TestCase):

    def test_paranoidAvoidEnemy(self):
        Board.resetGameBoard()
        Board.resetFood()
        # Arrange
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh'],
            ['x', 'x', 'x', 'f', 'x', 'st', 'sb', 'sb', 'x', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sh', 'sb', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'st', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'sb', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x'],
            ['x', 'f', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'f', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                    'body': [{'x': 8, 'y': 8}, {'x': 7, 'y': 8}, {'x': 7, 'y': 9}, {'x': 6, 'y': 9}, {'x': 5, 'y': 9}],
                    'head': {'x': 8, 'y': 8}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                   'body': [{'x': 8, 'y': 8}, {'x': 7, 'y': 8}, {'x': 7, 'y': 9}, {'x': 6, 'y': 9}, {'x': 5, 'y': 9}],
                   'head': {'x': 8, 'y': 8}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 10}, {'x': 10, 'y': 9}, {'x': 9, 'y': 9}, {'x': 9, 'y': 8},
                            {'x': 9, 'y': 7}], 'head': {'x': 10, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkqACDj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 6, 'y': 2}, {'x': 6, 'y': 3}, {'x': 5, 'y': 3}, {'x': 5, 'y': 4}, {'x': 5, 'y': 5},
                            {'x': 4, 'y': 5}], 'head': {'x': 6, 'y': 2}, 'length': 6, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{"x": 8, "y": 0}, {"x": 6, "y": 1}, {"x": 1, "y": 1}, {"x": 3, "y": 9}]
        Board.fillGameBoard(snakes, food, 11)

        pinf = float('inf')
        ninf = float('-inf')
        index = 0
        while index < 1:
            paranoid.timer = time.time()
            result = (paranoid.paranoid(ninf,pinf,4,"Max",board,board,snakes,snakes,"Initial",my_snake))
            self.assertEqual("down", result[1])
            index += 1

    def test_paranoidAvoidTrap(self):
        Board.resetGameBoard()
        Board.resetFood()
        # Arrange
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sh', 'sb', 'x'],
            ['x', 'sh', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'sb', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'sb', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'st', 'sb', 'x', 'sb', 'x'],
            ['f', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'sb', 'x'],
            ['sb', 'sb', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                   'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 0, 'y': 2}, {'x': 0, 'y': 3},
                            {'x': 0, 'y': 4}, {'x': 1, 'y': 4}], 'head': {'x': 1, 'y': 0}, 'length': 8, 'shout': '',
                   'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                   'body': [{'x': 1, 'y': 0}, {'x': 1, 'y': 1}, {'x': 1, 'y': 2}, {'x': 0, 'y': 2}, {'x': 0, 'y': 3},
                            {'x': 0, 'y': 4}, {'x': 1, 'y': 4}], 'head': {'x': 1, 'y': 0}, 'length': 8, 'shout': '',
                   'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 1, 'y': 8}, {'x': 1, 'y': 9}, {'x': 2, 'y': 9}, {'x': 3, 'y': 9}, {'x': 4, 'y': 9},
                            {'x': 5, 'y': 9}, {'x': 6, 'y': 9}, {'x': 7, 'y': 9}, {'x': 7, 'y': 8}, {'x': 7, 'y': 7},
                            {'x': 7, 'y': 6}, {'x': 6, 'y': 6}, {'x': 5, 'y': 6}], 'head': {'x': 1, 'y': 8},
                   'length': 13, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_VkYymmVCfGFSMMj3DSg7wYVV', 'name': 'Barry', 'latency': '59', 'health': 93,
                   'body': [{'x': 8, 'y': 9}, {'x': 9, 'y': 9}, {'x': 9, 'y': 8}, {'x': 9, 'y': 7}, {'x': 9, 'y': 6},
                            {'x': 9, 'y': 5}, {'x': 8, 'y': 5}], 'head': {'x': 8, 'y': 9}, 'length': 3, 'shout': '',
                   'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{"x": 0, "y": 5}]
        Board.fillGameBoard(snakes, food, 11)

        pinf = float('inf')
        ninf = float('-inf')
        index = 0
        # Assert
        while index < 50:
            paranoid.timer = time.time()
            result = (paranoid.paranoid(ninf,pinf,4,"Max",board,board,snakes,snakes,"initial",my_snake))
            self.assertEqual("right", result[1])
            index += 1

    def test_paranoidAvoidTrap2(self):
        Board.resetGameBoard()
        Board.resetFood()
        # Arrange
        board = [
            ['x', 'x', 'x', 'x', 'x', 'sb', 'sb', 'sb', 'sb', 'sb', 'sh'],
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'sb', 'sb', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'sb', 'sb', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'f', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'st', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                    'body': [{'x': 5, 'y': 9}, {'x': 5, 'y': 10}, {'x': 6, 'y': 10}, {'x': 7, 'y': 10},
                             {'x': 7, 'y': 9},
                             {'x': 7, 'y': 8}, {'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 7}, {'x': 5, 'y': 6}],
                    'head': {'x': 5, 'y': 9}, 'length': 10, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                   'body': [{'x': 5, 'y': 9}, {'x': 5, 'y': 10}, {'x': 6, 'y': 10}, {'x': 7, 'y': 10}, {'x': 7, 'y': 9},
                            {'x': 7, 'y': 8}, {'x': 6, 'y': 8}, {'x': 5, 'y': 8}, {'x': 5, 'y': 7}, {'x': 5, 'y': 6}],
                   'head': {'x': 5, 'y': 9}, 'length': 10, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 9, 'y': 10}, {'x': 8, 'y': 10}, {'x': 8, 'y': 9}, {'x': 9, 'y': 9},
                            {'x': 10, 'y': 9}, {'x': 10, 'y': 8}], 'head': {'x': 10, 'y': 10}, 'length': 14,
                   'shout': '',
                   'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{"x": 3, "y": 7}]
        Board.fillGameBoard(snakes, food, 11)

        pinf = float('inf')
        ninf = float('-inf')
        index = 0
        while index < 50:
            paranoid.timer = time.time()
            result = (paranoid.paranoid(ninf,pinf,4,"Max",board,board,snakes,snakes,"initial",my_snake))
            self.assertEqual("left", result[1])
            index += 1

    def test_paranoidAvoidTrap3(self):
        Board.resetGameBoard()
        Board.resetFood()
        # Arrange
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb', 'sb', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'sb'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'st', 'sb'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'sb', 'sb', 'sb', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'f'],
            ['sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                    'body': [{'x': 1, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 0, 'y': 2}, {'x': 1, 'y': 2},
                             {'x': 1, 'y': 3}, {'x': 1, 'y': 4}, {'x': 0, 'y': 4}, {'x': 0, 'y': 5},
                             {'x': 0, 'y': 6}, ], 'head': {'x': 1, 'y': 0}, 'length': 10, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                   'body': [{'x': 1, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 0, 'y': 2}, {'x': 1, 'y': 2},
                            {'x': 1, 'y': 3}, {'x': 1, 'y': 4}, {'x': 0, 'y': 4}, {'x': 0, 'y': 5}, {'x': 0, 'y': 6}, ],
                   'head': {'x': 1, 'y': 0}, 'length': 10, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 2}, {'x': 3, 'y': 2},
                            {'x': 4, 'y': 2}, {'x': 4, 'y': 3}, {'x': 4, 'y': 4}, {'x': 5, 'y': 4}, {'x': 6, 'y': 4},
                            {'x': 6, 'y': 5}, {'x': 6, 'y': 6}, {'x': 6, 'y': 7}, {'x': 6, 'y': 8}, {'x': 7, 'y': 8},
                            {'x': 8, 'y': 8}, {'x': 9, 'y': 8}, {'x': 9, 'y': 9}, {'x': 9, 'y': 10}, {'x': 10, 'y': 10},
                            {'x': 10, 'y': 9}, {'x': 10, 'y': 8}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6},
                            {'x': 9, 'y': 6}], 'head': {'x': 4, 'y': 1}, 'length': 14, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{"x": 3, "y": 7}]
        Board.fillGameBoard(snakes, food, 11)

        pinf = float('inf')
        ninf = float('-inf')
        index = 0
        while index < 50:
            paranoid.timer = time.time()
            result = (paranoid.paranoid(ninf,pinf,4,"Max",board,board,snakes,snakes,"initial",my_snake))
            self.assertEqual("right", result[1])
            index += 1

    def test_paranoidDetectWin(self):
        Board.resetGameBoard()
        Board.resetFood()
        # Arrange
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh'],
            ['x', 'x', 'x', 'f', 'st', 'sb', 'sb', 'sb', 'x', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sh', 'sb', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'f', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'f', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                    'body': [{'x': 8, 'y': 8}, {'x': 7, 'y': 8}, {'x': 7, 'y': 9}, {'x': 6, 'y': 9}, {'x': 5, 'y': 9},
                             {'x': 4, 'y': 9}],
                    'head': {'x': 8, 'y': 8}, 'length': 6, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                   'body': [{'x': 8, 'y': 8}, {'x': 7, 'y': 8}, {'x': 7, 'y': 9}, {'x': 6, 'y': 9}, {'x': 5, 'y': 9},
                            {'x': 4, 'y': 9}],
                   'head': {'x': 8, 'y': 8}, 'length': 6, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 10}, {'x': 10, 'y': 9}, {'x': 9, 'y': 9}, {'x': 9, 'y': 8},
                            {'x': 9, 'y': 7}], 'head': {'x': 10, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{"x": 8, "y": 0}, {"x": 6, "y": 1}, {"x": 1, "y": 1}, {"x": 3, "y": 9}]
        Board.fillGameBoard(snakes, food, 11)

        pinf = float('inf')
        ninf = float('-inf')
        index = 0
        while index < 50:
            paranoid.timer = time.time()
            result = (paranoid.paranoid(ninf,pinf,4,"Max",board,board,snakes,snakes,"initial",my_snake))
            self.assertEqual("up", result[1])
            index += 1

    def test_paranoidDetectWin2(self):
        Board.resetGameBoard()
        Board.resetFood()
        # Arrange
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'f', 'sh', 'sb', 'sb', 'st', 'f', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'sh', 'sb', 'x', 'x', 'f', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                    'body': [{'x': 2, 'y': 1}, {'x': 3, 'y': 1}, {'x': 4, 'y': 1}, {'x': 4, 'y': 2}],
                    'head': {'x': 2, 'y': 1}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                   'body': [{'x': 2, 'y': 1}, {'x': 3, 'y': 1}, {'x': 4, 'y': 1}, {'x': 4, 'y': 2}],
                   'head': {'x': 2, 'y': 1}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 4, 'y': 0}, {'x': 5, 'y': 0}, {'x': 5, 'y': 1}], 'head': {'x': 4, 'y': 0},
                   'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{"x": 8, "y": 0}, {"x": 6, "y": 1}, {"x": 1, "y": 1}, {"x": 3, "y": 9}]
        Board.fillGameBoard(snakes, food, 11)

        pinf = float('inf')
        ninf = float('-inf')
        index = 0
        while index < 50:
            paranoid.timer = time.time()
            result = (paranoid.paranoid(ninf,pinf,4,"Max",board,board,snakes,snakes,"Initial",my_snake))
            self.assertEqual("down", result[1])
            index += 1


    def test_paranoidDetectWin3(self):
        Board.resetGameBoard()
        Board.resetFood()
        # Arrange
        board = [
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['sb', 'sb', 'sb', 'st', 'x', 'x', 'f', 'x', 'x', 'x', 'x'],
        ['sh', 'sb', 'st', 'x', 'x', 'x', 'x', 'x', 'f', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
        'body': [{'x': 0, 'y': 3}, {'x': 0, 'y': 2}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 3, 'y': 1}],
        'head': {'x': 0, 'y': 3}, 'length': 6 ,'shout': '', 'squad': '',
        'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
        'body': [{'x': 0, 'y': 3}, {'x': 0, 'y': 2}, {'x': 0, 'y': 1}, {'x': 1, 'y': 1}, {'x': 2, 'y': 1}, {'x': 3, 'y': 1}],
        'head': {'x': 0, 'y': 3}, 'length': 6 ,'shout': '', 'squad': '',
        'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
        {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
        'body': [{'x': 0, 'y': 0}, {'x': 1, 'y': 0}, {'x': 2, 'y': 0}], 'head': {'x': 0, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
        'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
      {'id': 'gs_dVkqFCCj4av7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
       'body': [{'x': 0, 'y': 5}, {'x': 1, 'y': 5}, {'x': 1, 'y': 6}, {'x': 0, 'y': 6}, {'x': 0, 'y': 7}], 'head': {'x': 0, 'y': 5},
       'length': 5, 'shout': '', 'squad': '',
       'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{"x": 8, "y": 0},{"x": 6, "y": 1},{"x": 1, "y": 1},{"x": 3, "y": 9}]
        Board.fillGameBoard(snakes, food, 11)

        pinf = float('inf')
        ninf = float('-inf')
        index = 0
        while index < 50:
            paranoid.timer = time.time()
            result = (paranoid.paranoid(ninf,pinf,4,"Max",board,board,snakes,snakes,"Initial",my_snake))
            self.assertEqual("up", result[1])
            index += 1


class routeFinderTestCases(unittest.TestCase):

    def test_simulateMove(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 1, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                   'head': {'x': 1, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        Board.fillGameBoard(snakes, [], 11)

        possible_moves = moveLogic.generateMoves(board,my_snake,snakes)
        newCoordiantes = RouteFinder.simulateMove(my_snake["head"],possible_moves,board)
        self.assertEqual(newCoordiantes,[{'x':1,'y':10},{'x':2,'y':9}])

    def test_simulateMove2(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9},{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9},{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        Board.fillGameBoard(snakes, [], 11)

        possible_moves = moveLogic.generateMoves(board,my_snake,snakes)
        newCoordiantes = RouteFinder.simulateMove(my_snake["head"],possible_moves,board)
        self.assertEqual(newCoordiantes,[{'x':2,'y':10},{'x':2,'y':8},{'x':3,'y':9}])

    def test_findClosestFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'f'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9},{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9},{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x':5,'y':5},{'x':10,'y':2}]
        Board.fillGameBoard(snakes, food, 11)

        closestFood,distance = RouteFinder.findClosestFood(food,my_snake["head"])
        self.assertEqual(closestFood,{'x':5,'y':5})
        self.assertEqual(distance, 7)

    def test_findClosestEnemy(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9},{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9},{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5},{'x':10,'y':2}]
        Board.fillGameBoard(snakes, food, 11)
        snakeHeads = [snakes[1]["head"],snakes[2]["head"]]
        closestFood,distance = RouteFinder.findClosestFood(snakeHeads,my_snake["head"])
        self.assertEqual(closestFood,{'x':0,'y':9})
        self.assertEqual(distance, 2)

    def test_findClosestEnemy2(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9},{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9},{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5},{'x':10,'y':2}]
        Board.fillGameBoard(snakes, food, 11)
        snakeHeads = [snakes[1]["head"]]
        closestFood,distance = RouteFinder.findClosestFood(snakeHeads,my_snake["head"])
        self.assertEqual(closestFood,{'x':10,'y':0})
        self.assertEqual(distance, 17)

class boardClassTestCases(unittest.TestCase):

    def test_initaliseBoard11x11(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        self.assertEqual(Board.getBoard(), board)
        self.assertEqual(Board.getHeight(),11)
        self.assertEqual(Board.getWidth(),11)

    def test_fillGameBoard11x11(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb', 'sb', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'sb'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'st', 'sb'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'sb', 'sb', 'sb', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'f'],
            ['sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67, 'body': [{'x': 1, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 0, 'y': 2}, {'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 4}, {'x': 0, 'y': 4}, {'x': 0, 'y': 5}, {'x': 0, 'y': 6},], 'head': {'x': 1, 'y': 0}, 'length': 10, 'shout': '', 'squad': '', 'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}, {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95, 'body': [ {'x': 4, 'y':1}, {'x': 3, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 2}, {'x': 3, 'y': 2}, {'x': 4, 'y': 2}, {'x': 4, 'y': 3}, {'x': 4, 'y': 4}, {'x': 5, 'y': 4}, {'x': 6, 'y': 4}, {'x': 6, 'y': 5}, {'x': 6, 'y': 6}, {'x': 6, 'y': 7}, {'x': 6, 'y': 8}, {'x': 7, 'y': 8}, {'x': 8, 'y': 8}, {'x': 9, 'y': 8}, {'x': 9, 'y': 9}, {'x': 9, 'y': 10}, {'x': 10, 'y': 10}, {'x': 10, 'y': 9}, {'x': 10, 'y': 8}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6}, {'x': 9, 'y': 6}], 'head': {'x': 4, 'y': 1}, 'length': 14, 'shout': '', 'squad': '', 'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x':10,'y':1}]
        Board.fillGameBoard(snakes,food,Board.getHeight())
        self.assertEqual(Board.getBoard(),board)
        self.assertEqual(Board.getBoard()[9][10],"f")

    def test_getNumberOfFreeSquares(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'sb', 'sb', 'sb', 'sb', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'sb'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'st', 'sb'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'sb', 'sb', 'sb', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'f'],
            ['sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 67,
                   'body': [{'x': 1, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 1}, {'x': 0, 'y': 2}, {'x': 1, 'y': 2},
                            {'x': 1, 'y': 3}, {'x': 1, 'y': 4}, {'x': 0, 'y': 4}, {'x': 0, 'y': 5}, {'x': 0, 'y': 6}, ],
                   'head': {'x': 1, 'y': 0}, 'length': 10, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 4, 'y': 1}, {'x': 3, 'y': 1}, {'x': 2, 'y': 1}, {'x': 2, 'y': 2}, {'x': 3, 'y': 2},
                            {'x': 4, 'y': 2}, {'x': 4, 'y': 3}, {'x': 4, 'y': 4}, {'x': 5, 'y': 4}, {'x': 6, 'y': 4},
                            {'x': 6, 'y': 5}, {'x': 6, 'y': 6}, {'x': 6, 'y': 7}, {'x': 6, 'y': 8}, {'x': 7, 'y': 8},
                            {'x': 8, 'y': 8}, {'x': 9, 'y': 8}, {'x': 9, 'y': 9}, {'x': 9, 'y': 10}, {'x': 10, 'y': 10},
                            {'x': 10, 'y': 9}, {'x': 10, 'y': 8}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6},
                            {'x': 9, 'y': 6}], 'head': {'x': 4, 'y': 1}, 'length': 14, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        freeSquaresMe = Board.getNumberOfFreeSquares(board,snakes[0]["head"]["x"],snakes[0]["head"]["y"])
        freeSquaresOpp = Board.getNumberOfFreeSquares(board,snakes[1]["head"]["x"],snakes[1]["head"]["y"])
        self.assertEqual(freeSquaresMe,2)
        self.assertEqual(freeSquaresOpp,2)

    def test_getNumberOfFreeSquares2(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                   'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        freeSquaresMe = Board.getNumberOfFreeSquares(board,my_snake["head"]["x"],my_snake["head"]["y"])
        freeSquaresOpp = Board.getNumberOfFreeSquares(board,snakes[1]["head"]["x"],snakes[1]["head"]["y"])
        freeSquaresOpp2 = Board.getNumberOfFreeSquares(board,snakes[2]["head"]["x"],snakes[2]["head"]["y"])
        self.assertEqual(freeSquaresMe,3)
        self.assertEqual(freeSquaresOpp,1)
        self.assertEqual(freeSquaresOpp2,1)

    def test_getNumberOfFreeSquares3(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        freeSquaresMe = Board.getNumberOfFreeSquares(board,my_snake["head"]["x"],my_snake["head"]["y"])
        freeSquaresOpp = Board.getNumberOfFreeSquares(board,snakes[1]["head"]["x"],snakes[1]["head"]["y"])
        freeSquaresOpp2 = Board.getNumberOfFreeSquares(board,snakes[2]["head"]["x"],snakes[2]["head"]["y"])
        self.assertEqual(freeSquaresMe,1)
        self.assertEqual(freeSquaresOpp,0)
        self.assertEqual(freeSquaresOpp2,1)

    def test_updateSnakesUp(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctUpdatedSnake =  {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                    'body': [{'x': 2, 'y': 10},{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        updatedSnake = Board.updateSnakes(board,my_snake,"up",0,False)
        self.assertEqual(updatedSnake,correctUpdatedSnake)

    def test_updateSnakesDown(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctUpdatedSnake =  {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                    'body': [{'x': 2, 'y': 8},{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        updatedSnake = Board.updateSnakes(board,my_snake,"down",0,False)
        self.assertEqual(updatedSnake,correctUpdatedSnake)

    def test_updateSnakesLeft(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctUpdatedSnake =  {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                    'body': [{'x': 1, 'y': 10},{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}],
                    'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        updatedSnake = Board.updateSnakes(board,my_snake,"left",0,False)
        self.assertEqual(updatedSnake,correctUpdatedSnake)

    def test_updateSnakesRight(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctUpdatedSnake =  {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                    'body': [{'x': 3, 'y': 10},{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}],
                    'head': {'x': 3, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        updatedSnake = Board.updateSnakes(board,my_snake,"right",0,False)
        self.assertEqual(updatedSnake,correctUpdatedSnake)

    def test_updateSnakesRightAteFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'sh', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctUpdatedSnake =  {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                    'body': [{'x': 3, 'y': 10},{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9},{'x': 1, 'y': 9}],
                    'head': {'x': 3, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        updatedSnake = Board.updateSnakes(board,my_snake,"right",0,True)
        self.assertEqual(updatedSnake,correctUpdatedSnake)

    def test_updateSnakesLeftAteFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'f', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctUpdatedSnake =  {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                    'body': [{'x': 1, 'y': 10},{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9},{'x': 1, 'y': 9}],
                    'head': {'x': 1, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        updatedSnake = Board.updateSnakes(board,my_snake,"left",0,True)
        self.assertEqual(updatedSnake,correctUpdatedSnake)

    def test_updateSnakesDownAteFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctUpdatedSnake =  {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                    'body': [{'x': 2, 'y': 8},{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 8}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        updatedSnake = Board.updateSnakes(board,my_snake,"down",0,True)
        self.assertEqual(updatedSnake,correctUpdatedSnake)

    def test_updateSnakesUpAteFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctUpdatedSnake =  {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                    'body': [{'x': 2, 'y': 10},{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        updatedSnake = Board.updateSnakes(board,my_snake,"up",0,True)
        self.assertEqual(updatedSnake,correctUpdatedSnake)

    def test_calculateHeadCollisionLeftBigger(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]



        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
               'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
               'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
               'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
              {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
               'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
               'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
               'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
              {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
               'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
               'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
               'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                   'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board,snakes,0,"left")
        self.assertEqual(boardCopy,correctBoard)
        self.assertEqual(newSnakes,correctSnakes)
        self.assertEqual(survived,True)
        self.assertEqual(playerDead,False)
        self.assertEqual(deadIndexs,[1])

    def test_calculateHeadCollisionLeftSameSize(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]



        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
               'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
               'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
               'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
              {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
               'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
               'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
               'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
              {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
               'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
               'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
               'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board,snakes,0,"left")
        self.assertEqual(boardCopy,correctBoard)
        self.assertEqual(newSnakes,correctSnakes)
        self.assertEqual(survived,False)
        self.assertEqual(playerDead,True)
        self.assertEqual(deadIndexs,[0,1])

    def test_calculateHeadCollisionLeftSmaller(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]



        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
               'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
               'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
               'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
              {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
               'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
               'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
               'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
              {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
               'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
               'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
               'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
               'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
               'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
               'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board,snakes,0,"left")
        self.assertEqual(boardCopy,correctBoard)
        self.assertEqual(newSnakes,correctSnakes)
        self.assertEqual(survived,False)
        self.assertEqual(playerDead,True)
        self.assertEqual(deadIndexs,[0])

    def test_calculateHeadCollisionRightBigger(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board, snakes, 0, "right")
        self.assertEqual(boardCopy, correctBoard)
        self.assertEqual(newSnakes, correctSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(playerDead, False)
        self.assertEqual(deadIndexs, [1])

    def test_calculateHeadCollisionRightSameSize(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                   'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board, snakes, 0, "right")
        self.assertEqual(boardCopy, correctBoard)
        self.assertEqual(newSnakes, correctSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(playerDead, True)
        self.assertEqual(deadIndexs, [0,1])

    def test_calculateHeadCollisionRightSmaller(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                   'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                   'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board, snakes, 0, "right")
        self.assertEqual(boardCopy, correctBoard)
        self.assertEqual(newSnakes, correctSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(playerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_calculateHeadCollisionDownBigger(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8},{'x': 1, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8},{'x': 1, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board, snakes, 0, "down")
        self.assertEqual(boardCopy, correctBoard)
        self.assertEqual(newSnakes, correctSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(playerDead, False)
        self.assertEqual(deadIndexs, [1])

    def test_calculateHeadCollisionDownSmaller(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 1, 'y': 10}, {'x': 1, 'y': 9}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}, {'x': 0, 'y': 6}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}, {'x': 0, 'y': 6}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board, snakes, 0, "down")
        self.assertEqual(boardCopy, correctBoard)
        self.assertEqual(newSnakes, correctSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(playerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_calculateHeadCollisionDownSameSize(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}, {'x': 0, 'y': 6}],
                   'head': {'x': 0, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board, snakes, 0,
                                                                                              "down")
        self.assertEqual(boardCopy, correctBoard)
        self.assertEqual(newSnakes, correctSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(playerDead, True)
        self.assertEqual(deadIndexs, [0,1])

    def test_calculateHeadCollisionUpBigger(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}, {'x': 1, 'y': 6}],
                   'head': {'x': 1, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 0, 'y': 10}, {'x': 0, 'y': 9}],
                   'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}, {'x': 1, 'y': 6}],
                   'head': {'x': 1, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board, snakes, 0,
                                                                                              "up")
        self.assertEqual(boardCopy, correctBoard)
        self.assertEqual(newSnakes, correctSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(playerDead, False)
        self.assertEqual(deadIndexs, [1])

    def test_calculateHeadCollisionUpSmaller(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                   'head': {'x': 1, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board, snakes, 0,
                                                                                              "up")
        self.assertEqual(boardCopy, correctBoard)
        self.assertEqual(newSnakes, correctSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(playerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_calculcateHeadCollisionUpSameSize(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                   'head': {'x': 1, 'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 0, 'y': 10}, {'x': 0, 'y': 9}],
                   'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        boardCopy, newSnakes, survived, playerDead, deadIndexs = Board.calculateHeadCollision(board, snakes, 0,
                                                                                              "up")
        self.assertEqual(boardCopy, correctBoard)
        self.assertEqual(newSnakes, correctSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(playerDead, True)
        self.assertEqual(deadIndexs, [0,1])

    def test_doMoveRight(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                   'body': [{'x': 3, 'y': 9}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 3, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("right",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[])

    def test_doMoveRightAteFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 3, 'y': 9}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 8}],
                   'head': {'x': 3, 'y': 9}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5},{'x':3,'y':9}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("right",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[])

    def test_doMoveUp(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                   'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("up",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[])

    def test_doMoveUpAteFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 8}],
                   'head': {'x': 2, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5},{'x':2,'y':10}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("up",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[])

    def test_doMoveLeft(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                   'body': [{'x': 1, 'y': 10}, {'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("left",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[])

    def test_doMoveLeftAteFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'f', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 1, 'y': 10}, {'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 6, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5},{'x':1,'y':10}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("left",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[])

    def test_doMoveDown(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                   'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("down",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[])

    def test_doMoveDownAteFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2, 'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 8}],
                   'head': {'x': 2, 'y': 8}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5},{'x':2,'y':8}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("down",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[])

    def test_doMoveNone(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 2, 'y': 10}, {'x': 1, 'y':10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 2, 'y': 10}, {'x': 1, 'y':10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("none",my_snake,board,1,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[1])

    def test_doMoveLeftHeadCollisionBigger(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 1, 'y': 10}, {'x': 1, 'y':9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 1, 'y': 10}, {'x': 1, 'y':9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                    'body': [ {'x': 0, 'y': 10}, {'x': 1, 'y':10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("left",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[1])

    def test_doMoveLeftHeadCollisionSmaller(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 1, 'y': 10}, {'x': 1, 'y':9}, {'x': 1, 'y': 8}],
                    'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 1, 'y': 10}, {'x': 1, 'y':9}, {'x': 1, 'y': 8}],
                    'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("left",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead,True)
        self.assertEqual(deadIndexs,[0])

    def test_doMoveLeftHeadCollisionSameSize(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 1, 'y': 10}, {'x': 1, 'y':9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [ {'x': 1, 'y': 10}, {'x': 1, 'y':9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("left",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead,True)
        self.assertEqual(deadIndexs,[0,1])

    def test_doMoveRightHeadCollisionBigger(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}

        snakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}, {'x': 0, 'y': 7}],
                   'head': {'x': 0, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 94,
                   'body': [{'x': 1, 'y': 10},{'x': 0, 'y': 10}, {'x': 0, 'y': 9}, {'x': 0, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x':5,'y':5}]
        Board.fillGameBoard(snakes,food,11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("right",my_snake,board,0,snakes)
        self.assertEqual(correctBoard,newBoard)
        self.assertEqual(correctSnakes,newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead,False)
        self.assertEqual(deadIndexs,[1])

    def test_doMoveRightHeadCollisionSmaller(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
            {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 2, 'y': 8}, {'x':2, 'y': 7}],
                   'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                          'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 2, 'y': 8}, {'x':2, 'y': 7}],
                          'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("right", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_doMoveRightHeadCollisionSameSize(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'sh', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                   'body': [{'x': 1, 'y': 10}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                   'head': {'x': 1, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
            {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9}, {'x': 2, 'y': 8}],
                   'head': {'x': 2, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("right", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0,1])

    def test_doMoveUpHeadCollisionBigger(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['st', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2 ,'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2 ,'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 10}, {'x': 1, 'y': 10}, {'x': 0, 'y': 10}],
                   'head': {'x': 2, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                    'body': [{'x': 2, 'y': 10},{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("up", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead, False)
        self.assertEqual(deadIndexs, [1])

    def test_doMoveUpHeadCollisionSmaller(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['sb', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 10}, {'x': 1, 'y': 10}, {'x': 0, 'y': 10}, {'x': 0, 'y': 9}],
                   'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 10}, {'x': 1, 'y': 10}, {'x': 0, 'y': 10}, {'x': 0, 'y': 9}],
                   'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("up", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_doMoveUpHeadCollisionSameSize(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['st', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 10}, {'x': 1, 'y': 10}, {'x': 0, 'y': 10}],
                   'head': {'x': 2, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("up", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0,1])

    def test_doMoveUpDownCollisionBigger(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2 ,'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}, {'x': 1, 'y': 7}],
                    'head': {'x': 2 ,'y': 9}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 2, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 94,
                    'body': [{'x': 2, 'y': 8},{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("down", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, True)
        self.assertEqual(isPlayerDead, False)
        self.assertEqual(deadIndexs, [1])

    def test_doMoveUpDownCollisionSmaller(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}],
                   'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}],
                   'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("down", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_doMoveUpDownCollisionSameSize(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'st', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 95,
                    'body': [{'x': 2, 'y': 9}, {'x': 1, 'y': 9}, {'x': 1, 'y': 8}],
                    'head': {'x': 2 ,'y': 9}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkqFCCj4wv7StXwJP7TFdBG', 'name': 'Barry', 'latency': '60', 'health': 95,
                   'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 2, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [
                         {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("down", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0,1])

    def test_doMoveStarvationRight(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}],
                    'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}],
                    'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("right", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_doMoveStarvationLeft(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}],
                    'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}],
                    'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("left", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_doMoveStarvationUp(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}],
                    'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}, {'x': 2, 'y': 5}],
                    'head': {'x': 2, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("up", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_doMoveStarvationDown(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 3, 'y': 8},{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 3, 'y': 8},{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        correctSnakes = [{'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                          'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                          'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                          'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]

        food = [{'x': 5, 'y': 5}]
        Board.fillGameBoard(snakes, food, 11)
        newBoard, newSnakes, survived, isPlayerDead, deadIndexs = Board.doMove("down", my_snake, board, 0, snakes)
        self.assertEqual(correctBoard, newBoard)
        self.assertEqual(correctSnakes, newSnakes)
        self.assertEqual(survived, False)
        self.assertEqual(isPlayerDead, True)
        self.assertEqual(deadIndexs, [0])

    def test_removeSnake1(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                   'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 3, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 5, 'y': 5}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 3, 'y': 8},{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        newBoard= Board.removeSnake(board,my_snake)
        self.assertEqual(newBoard,correctBoard)

    def test_removeSnake2(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                   'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 5, 'y': 5}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 3, 'y': 8},{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        newBoard= Board.removeSnake(board,snakes[1])
        self.assertEqual(newBoard,correctBoard)

    def test_removeSnake3(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['sb', 'x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['sb', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['sb', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['sb', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'sb'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb', 'sb']]

        correctBoard = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                   'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 3}, {'x': 10, 'y': 2}, {'x': 10, 'y': 1},{'x': 10, 'y': 0}, {'x': 9, 'y': 0},
                            {'x': 8, 'y': 0},{'x': 7, 'y': 0}, {'x': 6, 'y': 0}, {'x': 5, 'y': 0},{'x': 4, 'y': 0},
                            {'x': 3, 'y': 0}, {'x': 2, 'y': 0},{'x': 1, 'y': 0}, {'x': 0, 'y': 0}, {'x': 0, 'y': 1},
                            {'x': 0, 'y': 2}, {'x': 0, 'y': 3}, {'x': 0, 'y': 4},{'x': 0, 'y': 5}, {'x': 0, 'y': 6},
                            {'x': 0, 'y': 7},{'x': 0, 'y': 8}, {'x': 0, 'y': 9}, {'x': 0, 'y': 10}, {'x': 1, 'y': 10},
                            {'x': 2, 'y': 10}, {'x': 3, 'y': 10}, {'x': 4, 'y': 10}, {'x': 5, 'y': 10}, {'x': 6, 'y': 10},
                            {'x': 7, 'y': 10}, {'x': 8, 'y': 10}, {'x': 9, 'y': 10}, {'x': 10, 'y': 10}, {'x': 10, 'y': 9},
                            {'x': 10, 'y': 8}, {'x': 10, 'y': 7}, {'x': 10, 'y': 6}, {'x': 10, 'y': 5}, {'x': 10, 'y': 4}],

                   'head': {'x': 10, 'y': 3}, 'length': 40, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 5, 'y': 5}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 3, 'y': 8},{'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        newBoard= Board.removeSnake(board,snakes[1])
        self.assertEqual(newBoard,correctBoard)

    def test_floodfillTrapped(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'sb', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                   'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 3, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6aP77WV6bbjqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 1,
                   'body': [{'x': 9, 'y': 1}, {'x': 9, 'y': 0}, {'x': 8, 'y': 0}],
                   'head': {'x': 9, 'y': 1}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 5, 'y': 5}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        xCoOrd = snakes[2]["head"]["x"]
        yCoOrd = snakes[2]["head"]["y"]
        floodFillScore = Board.floodFill(board,xCoOrd,yCoOrd)
        self.assertEqual(floodFillScore, 0)

    def test_floodfill(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sh', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st', 'sb', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                   'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 3, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6aP77WV6bbjqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 1,
                   'body': [{'x': 9, 'y': 1}, {'x': 9, 'y': 0}, {'x': 8, 'y': 0}],
                   'head': {'x': 9, 'y': 1}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 5, 'y': 5}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        xCoOrd = snakes[0]["head"]["x"]
        yCoOrd = snakes[0]["head"]["y"]
        floodFillScore = Board.floodFill(board,xCoOrd,yCoOrd)
        self.assertEqual(floodFillScore, 111)

    def test_floodfill2(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'st', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                   'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 3, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6aP77WV6bbjqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 1,
                   'body': [{'x': 5, 'y': 10}, {'x': 5, 'y': 9}, {'x': 5, 'y': 8},{'x': 5, 'y': 7},{'x': 5, 'y': 6},
                            {'x': 5, 'y': 5},{'x': 5, 'y': 4},{'x': 5, 'y': 3},{'x': 5, 'y': 2},
                            {'x': 5, 'y': 1},{'x': 5, 'y': 0},{'x': 6, 'y': 0}],
                   'head': {'x': 5, 'y': 10}, 'length': 12, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = []

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        xCoOrd = snakes[0]["head"]["x"]
        yCoOrd = snakes[0]["head"]["y"]
        floodFillScore = Board.floodFill(board,xCoOrd,yCoOrd)
        self.assertEqual(floodFillScore, 51)

    def test_floodfill3(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['sh', 'sb', 'sb', 'sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'st', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'st', 'x', 'x', 'x', 'x']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                   'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 3, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6aP77WV6bbjqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 1,
                   'body': [{'x': 5, 'y': 10}, {'x': 5, 'y': 9}, {'x': 5, 'y': 8},{'x': 5, 'y': 7},{'x': 5, 'y': 6},
                            {'x': 5, 'y': 5},{'x': 5, 'y': 4},{'x': 5, 'y': 3},{'x': 5, 'y': 2},
                            {'x': 5, 'y': 1},{'x': 5, 'y': 0},{'x': 6, 'y': 0}],
                   'head': {'x': 5, 'y': 10}, 'length': 12, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 0, 'y': 5}, {'x': 1, 'y': 5}, {'x': 2, 'y': 5},
                            {'x': 3, 'y': 5}, {'x': 4, 'y': 5}, {'x': 4, 'y': 4},],
                   'head': {'x': 0, 'y': 5}, 'length': 6, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = []

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 1,
                    'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        xCoOrd = snakes[0]["head"]["x"]
        yCoOrd = snakes[0]["head"]["y"]
        floodFillScore = Board.floodFill(board,xCoOrd,yCoOrd)
        self.assertEqual(floodFillScore, 21)

    def test_evaluateFunction(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'sh', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'sb', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'st', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'f', 'x', 'sb', 'st', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                   'head': {'x': 3, 'y': 8}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6aP77WV6bbjqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 1,
                   'body': [{'x': 5, 'y': 10}, {'x': 5, 'y': 9}, {'x': 5, 'y': 8},{'x': 5, 'y': 7},{'x': 5, 'y': 6},
                            {'x': 5, 'y': 5},{'x': 5, 'y': 4},{'x': 5, 'y': 3},{'x': 5, 'y': 2},
                            {'x': 5, 'y': 1},{'x': 5, 'y': 0},{'x': 6, 'y': 0}],
                   'head': {'x': 5, 'y': 10}, 'length': 12, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 3, 'y': 0}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                    'body': [{'x': 3, 'y': 8}, {'x': 2, 'y': 8}, {'x': 2, 'y': 7}, {'x': 2, 'y': 6}],
                    'head': {'x': 3, 'y': 8}, 'length': 3, 'shout': '', 'squad': '',
                    'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}
        evaluateScore = Board.evaluate(board,my_snake,snakes)
        self.assertEqual(evaluateScore, 245.0)

    def test_evaluateFunction2(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'st', 'sb', 'sh', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'sb', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'f', 'x', 'sb', 'st', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 4, 'y': 10}, {'x': 4, 'y': 9,}, {'x': 3, 'y': 9}, {'x': 3, 'y': 10}, {'x': 2, 'y': 10}],
                   'head': {'x': 4, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6aP77WV6bbjqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 1,
                   'body': [{'x': 5, 'y': 10}, {'x': 5, 'y': 9}, {'x': 5, 'y': 8},{'x': 5, 'y': 7},{'x': 5, 'y': 6},
                            {'x': 5, 'y': 5},{'x': 5, 'y': 4},{'x': 5, 'y': 3},{'x': 5, 'y': 2},
                            {'x': 5, 'y': 1},{'x': 5, 'y': 0},{'x': 6, 'y': 0}],
                   'head': {'x': 5, 'y': 10}, 'length': 12, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 3, 'y': 0}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 4, 'y': 10}, {'x': 4, 'y': 9}, {'x': 3, 'y': 9}, {'x': 3, 'y': 10}, {'x': 2, 'y': 10}],
                   'head': {'x': 4, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        evaluateScore = Board.evaluate(board,my_snake,snakes)
        self.assertEqual(evaluateScore, -51)

    def test_evaluateFunction3(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'st', 'sb', 'sh', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'sb', 'sb', 'sb', 'sh', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'sb', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'f', 'x', 'sb', 'st', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 4, 'y': 10}, {'x': 4, 'y': 9,}, {'x': 3, 'y': 9}, {'x': 3, 'y': 10}, {'x': 2, 'y': 10}],
                   'head': {'x': 4, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6aP77WV6bbjqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 1,
                   'body': [{'x': 6, 'y': 9}, {'x': 5, 'y': 9}, {'x': 5, 'y': 8},{'x': 5, 'y': 7},{'x': 5, 'y': 6},
                            {'x': 5, 'y': 5},{'x': 5, 'y': 4},{'x': 5, 'y': 3},{'x': 5, 'y': 2},
                            {'x': 5, 'y': 1},{'x': 5, 'y': 0},{'x': 6, 'y': 0}],
                   'head': {'x': 6, 'y': 9}, 'length': 12, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 3, 'y': 0}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 4, 'y': 10}, {'x': 4, 'y': 9}, {'x': 3, 'y': 9}, {'x': 3, 'y': 10}, {'x': 2, 'y': 10}],
                   'head': {'x': 4, 'y': 10}, 'length': 5, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        evaluateScore = Board.evaluate(board,my_snake,snakes)
        self.assertEqual(evaluateScore, 230)

    def test_evaluateFunction4(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'sb', 'sb', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'st', 'sh', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 5, 'y': 5}, {'x': 5, 'y': 6,}, {'x': 4, 'y': 6}, {'x': 4, 'y': 5}],
                   'head': {'x': 5, 'y': 5}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 3, 'y': 0},{'x':5, 'y': 4}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 5, 'y': 5}, {'x': 5, 'y': 6,}, {'x': 4, 'y': 6}, {'x': 4, 'y': 5}],
                   'head': {'x': 5, 'y': 5}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        evaluateScore = Board.evaluate(board,my_snake,snakes)
        self.assertEqual(evaluateScore, 243.5)

    def test_evaluateFunction5(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sh', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9,}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6jP77WV6bajqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 100,
                   'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9,}, {'x': 2, 'y': 8},{'x': 2, 'y': 8}],
                   'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6jP72WV6bajqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 100,
                   'body': [{'x': 1, 'y': 7}, {'x': 0, 'y': 7,}, {'x': 0, 'y': 6}],
                   'head': {'x': 1, 'y': 7}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 3, 'y': 0},{'x':5, 'y': 4}]

        Board.fillGameBoard(snakes, food, 11)
        my_snake = {'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9,}, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}}

        evaluateScore = Board.evaluate(board,my_snake,snakes)
        self.assertEqual(evaluateScore, 43)

    def test_resetBoard(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sh', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9, }, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6jP77WV6bajqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 100,
                   'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9, }, {'x': 2, 'y': 8}, {'x': 2, 'y': 8}],
                   'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6jP72WV6bajqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 100,
                   'body': [{'x': 1, 'y': 7}, {'x': 0, 'y': 7, }, {'x': 0, 'y': 6}],
                   'head': {'x': 1, 'y': 7}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 3, 'y': 0}, {'x': 5, 'y': 4}]

        self.assertEqual(Board.getBoard(),[['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']])

        Board.fillGameBoard(snakes, food, 11)
        self.assertNotEqual(Board.getBoard(),[])
        Board.resetGameBoard()
        self.assertEqual(Board.getBoard(),[['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']])

    def test_resetFood(self):
        Board.resetGameBoard()
        Board.resetFood()
        board = [
            ['sh', 'x', 'sh', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'sb', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['sb', 'sh', 'st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['st', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'st'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'sb'],
            ['x', 'x', 'x', 'f', 'x', 'x', 'x', 'x', 'x', 'x', 'sh']]

        snakes = [{'id': 'gs_6cKMCg9r6jP77WV6bbjqrFfX', 'name': 'ekans v1', 'latency': '147', 'health': 100,
                   'body': [{'x': 0, 'y': 10}, {'x': 0, 'y': 9, }, {'x': 0, 'y': 8}],
                   'head': {'x': 0, 'y': 10}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6jP77WV6bajqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 100,
                   'body': [{'x': 2, 'y': 10}, {'x': 2, 'y': 9, }, {'x': 2, 'y': 8}, {'x': 2, 'y': 8}],
                   'head': {'x': 2, 'y': 10}, 'length': 4, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_6cKMCg9r6jP72WV6bajqrFfX', 'name': 'ekans v2', 'latency': '147', 'health': 100,
                   'body': [{'x': 1, 'y': 7}, {'x': 0, 'y': 7, }, {'x': 0, 'y': 6}],
                   'head': {'x': 1, 'y': 7}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#800080', 'head': 'safe', 'tail': 'small-rattle'}},
                  {'id': 'gs_dVkaFCCj4wv7StXwJP7TFdBG', 'name': 'Barry2', 'latency': '60', 'health': 95,
                   'body': [{'x': 10, 'y': 0}, {'x': 10, 'y': 1}, {'x': 10, 'y': 2}],
                   'head': {'x': 10, 'y': 0}, 'length': 3, 'shout': '', 'squad': '',
                   'customizations': {'color': '#fb6900', 'head': 'default', 'tail': 'default'}}]
        food = [{'x': 3, 'y': 0}, {'x': 5, 'y': 4}]

        self.assertEqual(Board.getFood(),[])

        Board.fillGameBoard(snakes, food, 11)
        self.assertNotEqual(Board.getFood(),[])
        Board.resetFood()
        self.assertEqual(Board.getFood(),[])


if __name__ == "__main__":
    unittest.main()
