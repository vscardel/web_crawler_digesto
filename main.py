import requests
import argparse
import regex

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
	#algum argumento foi fornecido
	if opt.print or opt.save_csv or opt.save_json:
		pass
	else:
		print('Alguma opção deve ser fornecida ao crawler.')
