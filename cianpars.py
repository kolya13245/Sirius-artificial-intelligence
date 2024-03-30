import cianparser

proxies = """kolyagnusov:uPzHKKw7Lr@149.126.216.231:59100	
kolyagnusov:uPzHKKw7Lr@149.126.217.254:59100	
kolyagnusov:uPzHKKw7Lr@149.126.218.230:59100	
kolyagnusov:uPzHKKw7Lr@149.126.219.224:59100	
kolyagnusov:uPzHKKw7Lr@149.126.220.214:59100	
kolyagnusov:uPzHKKw7Lr@212.8.229.17:59100	
kolyagnusov:uPzHKKw7Lr@94.137.91.94:59100	
kolyagnusov:uPzHKKw7Lr@194.110.14.222:59100	
kolyagnusov:uPzHKKw7Lr@45.95.67.87:59100	
kolyagnusov:uPzHKKw7Lr@46.3.133.65:59100
""".split('\n')

moscow_parser = cianparser.CianParser(location="Киров", proxies= None)
data = moscow_parser.get_flats(deal_type="sale", rooms=(3), with_saving_csv=False, additional_settings={"start_page":1, "end_page":50}, with_extra_data=False)

for i in data:
    i['date'] = None
    for j in i:
        if i[j] == -1:
            i[j] = None

import pandas as pd

df = pd.DataFrame(data)
df.to_excel(excel_writer = "test.xlsx")