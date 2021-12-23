import DataSum_fun

DataSum_fun.Config()

data, label = DataSum_fun.Sum()
E = DataSum_fun.get_epsilon()
data_size = DataSum_fun.get_data_size(data)
cell, data_cell = DataSum_fun.calcCell(E, data, data_size)

DataSum_fun.write_H_data(E, cell)
DataSum_fun.write_ori_data(data, label, data_cell, data_size)