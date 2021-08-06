import requests
import re
#esse arquivo contém a lógica para realizar a captura das informações
#encapulada nas classes VultCrawler e DigitalOceanCrawler. Ambas herdam
#certos métodos em comum da classe Crawler
class Crawler():

	def __init__(self,url):
		self.url = url

	def get_html_text(self):
		response = requests.get(self.url)
		return response


class VultCrawler(Crawler):

	def get_info(self):
		html = self.get_html_text()
		#captura armazenamento,cpu e memória
		padrao_1 =r"""<div class="pt__cell">
		[\n,\t]*[<span>,<strong>]*[\n,\t]*<strong>([0-9]*[ ,A-Z,a-z]*)"""
		results_1 = [x.group(1) for x in re.finditer(padrao_1, html.text,re.MULTILINE)]
		#captura bandwith
		padrao_2 = r"""<span class="">
		[\s]*<strong>([0-9]*.[0-9]*[\ ]*[A-Z]*)</strong>[\s]*<span class="is-hidden-lg-up"> Bandwidth</span>"""
		results_2 = [x.group(1) for x in re.finditer(padrao_2, html.text,re.MULTILINE)]