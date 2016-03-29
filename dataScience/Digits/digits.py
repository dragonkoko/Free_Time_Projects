from sklearn import neighbors
import csv

f = open('train.csv')
csv_f = csv.reader(f)

x = []
y = []
i = -1

print 'reading training'
for row in csv_f:
    i += 1;
    if i == 0:
        continue
    record = row[1:]
    x.append(record)
    y.append(row[0])

print 'fitting'
clf = neighbors.KNeighborsClassifier(n_neighbors=1)
clf = clf.fit(x, y)

f = open('test.csv')
csv_f = csv.reader(f)
answers = []
i = -1
print 'predicting'
for row in csv_f:
    i += 1
    print i
    if i == 0:
        continue
    test_matrix = []
    test_matrix.append(row)
    answers.append(clf.predict(test_matrix))

myfile = open('submission.csv', 'wb')
myfile.write('ImageId,Label\n')
i = 0
for answer in answers:
    for digit in answer:
        i+=1
        myfile.write(str(i)+','+answer+'\n')
        print answer

myfile.close()
