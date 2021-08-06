import requests
import argparse
import re
from crawlers import VultCrawler,DigitalOceanCrawler
import json

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

		ocean_crawler = DigitalOceanCrawler(url_digital)
		#dicionario com dados do digitalocean
		info_dict_ocean  = ocean_crawler.get_info()

		#dicionario com dados do vultr
		v_crawler = VultCrawler(url_vult)
		info_dict_vultr = v_crawler.get_info()

		#printa na tela
		if opt.print:
			print('\n\n')
			print("Informações do Site https://www.vultr.com:")
			print('\n\n')
			v_crawler.print(info_dict_vultr,10)
			print('\n\n')
			print("Informações do Site https://www.vultr.com:")
			print('\n\n')
			ocean_crawler.print(info_dict_ocean,6)
		#salva em json 
		elif opt.save_json:
			with open('vultr_json.txt', 'w') as outfile:
				json.dump(info_dict_vultr, outfile)
			with open('digital_ocean_json.txt', 'w') as outfile:
				json.dump(info_dict_ocean, outfile)
		else:	
		#salva em csv
			with open('vultr.csv', 'w') as outfile:
				v_crawler.write_csv_data(info_dict_vultr,outfile,10)
			with open('digital_ocean.csv', 'w') as outfile:
				ocean_crawler.write_csv_data(info_dict_ocean,outfile,6)
	else:
		print('Alguma opção deve ser fornecida ao crawler.')
