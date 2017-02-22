# -*- coding: utf-8 -*-
import tornado.web
import tornado.websocket
import json

from .board_ws import BoardWebSocketHandler
from models import BoardGameMaster


class BoardHandler(tornado.web.RequestHandler):

    def get(self, borad_id):
        board = BoardWebSocketHandler.boards.get(board_id, BoardGameMaster())
        response = board.extract_data()

        self.write(json.dumps(response))
        self.set_header("Content-Type", "application/json")
