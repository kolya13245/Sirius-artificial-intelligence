import cianparser
import pandas as pd

moscow_parser = cianparser.CianParser(location = "Москва", proxies=None)
data = moscow_parser.get_flats(
    deal_type="sale",
    rooms=("all"),
    with_saving_csv=False,
    additional_settings={"start_page": 1, "end_page": 50},
    with_extra_data=False,
)

for i in data:
    i["date"] = None
    for j in i:
        if i[j] == -1:
            i[j] = None

df = pd.DataFrame(data)
df.to_excel(excel_writer="test.xlsx")
