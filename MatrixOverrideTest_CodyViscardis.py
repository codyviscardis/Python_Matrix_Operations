import MatrixOverride_CodyViscardis
from datetime import datetime

start = datetime.now()

#matrix5x5 = MatrixOverride_CodyViscardis.myMatrix(5,5)
#matrix10x10 = MatrixOverride_CodyViscardis.myMatrix(10,10)
#matrix20x20 = MatrixOverride_CodyViscardis.myMatrix(20,20)
#matrix50x50 = MatrixOverride_CodyViscardis.myMatrix(50,50)
#matrix100x100 = MatrixOverride_CodyViscardis.myMatrix(100,100)
matrix250x250 = MatrixOverride_CodyViscardis.myMatrix(250,250)

#matrix5x5*matrix5x5
#matrix10x10*matrix10x10
#matrix20x20*matrix20x20
#matrix50x50*matrix50x50
#matrix100x100*matrix100x100
matrix250x250*matrix250x250

end = datetime.now()

total = end - start
print((total.microseconds)/1000)
#1 microsecond equals 0.0001 milliseconds

