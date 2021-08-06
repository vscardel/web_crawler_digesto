import requests
import argparse
import re
from crawlers import VultCrawler

#argumentos passados pelo terminal 
def parse_arguments(parser):
	parser.add_argument(
		'--print', 
		help="Imprime resultados na tela", 
		action='store_true'
	)
	parser.add_argument(
		'--save_csv', 
		help="Salva dados em arquivo csv", 
		action='store_true'
	)
	parser.add_argument(
		'--save_json', 
		help="Salva dados em arquivo json", 
		action='store_true'
	)
	
	args = parser.parse_args()
	return args

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="")
	opt = parse_arguments(parser)
	url_vult = "https://www.vultr.com/products/cloud-compute/#pricing"
	url_digital = "https://www.digitalocean.com/pricing/"
	#algum argumento foi fornecido
	if opt.print or opt.save_csv or opt.save_json:
		v_crawler = VultCrawler(url_vult)
		info_dict_vultr = v_crawler.get_info()
		if opt.print:
			print('\n\n')
			print("Informações do Site https://www.vultr.com:")
			print('\n\n')
			v_crawler.print(info_dict_vultr,10)

	else:
		print('Alguma opção deve ser fornecida ao crawler.')
