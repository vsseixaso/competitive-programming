n_faces = {
	'Tetrahedron': 4,
	'Cube': 6,
	'Octahedron': 8,
	'Dodecahedron': 12,
	'Icosahedron': 20
}

n = int(raw_input())
sum = 0

for i in xrange(n):
	sum += n_faces[raw_input()]

print sum