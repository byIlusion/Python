import json


def pars_firm(row):
    try:
        row = row.split()
        firm = {
            'name': row[0],
            'type': row[1],
            'revenue': float(row[2]),
            'costs': float(row[3])
        }
        return firm
    except:
        print(f"Не удалось распознать: {row!r}")
        return None


result = {
    'all_firms': [],
    'profit_firms': [],
    'loss_firms': [],
    'neutral_firms': [],
    'average_profit': 0,
    'average_loss': 0,
}
try:
    with open("files/text_7.txt") as f:
        for row in f:
            firm = pars_firm(row)
            if firm is not None:
                result['all_firms'].append(firm)
                if firm['revenue'] > firm['costs']:
                    result['profit_firms'].append(firm)
                    result['average_profit'] += firm['revenue'] - firm['costs']
                elif firm['revenue'] == firm['costs']:
                    result['neutral_firms'].append(firm)
                else:
                    result['loss_firms'].append(firm)
                    result['average_loss'] += firm['costs'] - firm['revenue']
except IOError:
    print("Ошибка чтения!")

if len(result['profit_firms']) > 0:
    result['average_profit'] /= len(result['profit_firms'])
if len(result['loss_firms']) > 0:
    result['average_profit'] /= len(result['loss_firms'])

try:
    with open("files/text_form_task_07.json", "w") as f:
        json.dump(result, f, indent=4)
except IOError:
    print("Ошибка сохранения!")
else:
    print("JSON файл сохранен")
