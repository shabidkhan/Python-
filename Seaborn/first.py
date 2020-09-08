import seaborn as sns
import pandas as pd
data_={
    "price":[1,2,3,4,5,6,7,8,9,10],
    "profit":[11,22,33,22,55,66,44,55,22,44]

}
stock = pd.DataFrame(data_)
print(stock)
# sns.relplot('profit','price',data=stock)
# sns.show()
