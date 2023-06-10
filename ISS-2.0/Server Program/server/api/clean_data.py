def clean(input_dict):
    input_dict['names'] = input_dict['names'][:2]
    input_dict['match'] = int(input_dict['match'])
    input_dict['teamnumber'] = int(input_dict['teamnumber'])
    input_dict['noshow'] = input_dict['noshow'].lower() in ['true']
    input_dict['mobility'] = input_dict['mobility'].lower() in ['true']
    input_dict['auto_pickup'] = input_dict['auto_pickup'].lower() in ['true']
    input_dict['early_endgame'] = input_dict['early_endgame'].lower() in ['true']
    input_dict['died'] = input_dict['died'].lower() in ['true']
    input_dict['tipped'] = input_dict['tipped'].lower() in ['true']
    input_dict['card'] = input_dict['card'].lower() in ['true']
    input_dict['damage'] = input_dict['damage'].lower() in ['true']
    