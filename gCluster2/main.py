from gClustering_f import Gcluster, readData, visualize


if __name__ == '__main__':
    txtData = input("請輸入檔案: ")
    cellSize = int(input("請輸入 Cell Size: "))
    minForce = float(input("請輸入 Min Force: "))
    minCells = int(input("請輸入 Min Cells: "))
    print()
    print('Waiting for data processing...')

    cells, numberOfCells = readData(txtData)
    Result = Gcluster(cells, cellSize, minForce, minCells, numberOfCells)
    visualize(Result)
