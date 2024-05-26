import numpy as np

arrayno1 = np.array([[1, 6, 3], [4, 2, 6], [7, 0, 9]])
arrayno2 = np.array([11, 21, 31, 41, 51])
arrayno3 = np.array([[31, 42], [53, 64], [75, 86]])

np.savetxt('array1.txt', arrayno1, delimiter=',')
print("Array1 saved to 'array1.txt'")

np.save('array2.npy', arrayno2)
print("Array2 saved to 'array2.npy'")

np.savez('arrays_compressed.npz', array1=arrayno1, array2=arrayno2, array3=arrayno3)
print("Arrays saved to 'arrays_compressed.npz'")

#loading the arrays
loaded_array1 = np.loadtxt('array1.txt', delimiter=',')
print("\nLoaded array1 from 'array1.txt':\n", loaded_array1)

loaded_array2 = np.load('array2.npy')
print("\nLoaded array2 from 'array2.npy':\n", loaded_array2)

with np.load('arrays_compressed.npz') as data:
    loaded_array1_from_npz = data['array1']
    loaded_array2_from_npz = data['array2']
    loaded_array3_from_npz = data['array3']
    print("\nLoaded arrays from 'arrays_compressed.npz':")
    print("array1:\n", loaded_array1_from_npz)
    print("array2:\n", loaded_array2_from_npz)
    print("array3:\n", loaded_array3_from_npz)
