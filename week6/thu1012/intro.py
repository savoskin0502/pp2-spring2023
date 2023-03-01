# ****
# Филиал Астана
# НДС 12%
# 001002003004 БИН адлырвдалыва ь оаывраолырваы аывралоырвлары 123 312443  аывордаыдвлоа 001002003004 алывралыдоа аыдвлраыдвоал
# ****

# pattern - правило по которому мы будем искать/то что мы ищем
# text - где мы ищем
# cat | cot | cit | ct
import re
pattern = '^c[aoi]?t$'  # * - 0 и более; number of rep; + - 1 and more; ? - 0 or 1
text = 'cot cot'
matching = re.search(pattern, text)
print(matching)
