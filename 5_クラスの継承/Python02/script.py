from food import Food
from drink import Drink

food1 = Food('サンドイッチ', 500)

print(food1.info())

drink1 = Drink('コーヒー', 300)

print(drink1.info())

# 継承をすると、子クラスは親クラスのインスタンスメソッドを引き継ぐ
# Foodクラスのインスタンスは、MenuItemクラス内に定義してある
#「__init__」メソッドや「info」メソッドを使うことができる。
