from flask import jsonify
import yfinance as yf


class StockAnalysis(object):
	"""doc string"""
	def __init__(self, db):
		self.db = db

	def stock_analysis(self, request_data):
		"""doc string"""
		stock_name = request_data['stock_name']
		bought_qty = request_data['bought_qty']
		bought_qty_value = request_data['bought_qty_value']
		buying_date = request_data['buying_date']

		yf_resp = yf.Ticker(stock_name)
		yf_info = yf_resp.info
		prev_close = yf_info['previousClose']
		
		current_qty_value = prev_close * bought_qty

		data = {
			'profit_earned': None,
			'loss_incurred': None,
			'buying_discount': 0.80
		}

		if bought_qty_value > current_qty_value:
			data['loss_incurred'] = round(abs(bought_qty_value - current_qty_value), 3)
		elif bought_qty_value < current_qty_value:
			data['profit_earned'] = round(current_qty_value - bought_qty_value, 3)
		else:
			data['profit_earned'], data['loss_incurred'] = 0, 0
		
		return jsonify({'success': True, 'data': data}), 200