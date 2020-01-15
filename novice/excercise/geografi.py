class Geografi:
	def __init__(self, name, spesifik, spesial, kasus):
		self.name = name
		print("Name: " + self.name)
		self.spesifikasi = spesifik
		print("Specific major: " + self.spesifikasi)
		self.spesialisasi = spesial
		print("Specialization: " + self.spesialisasi)
		self.kasus = kasus
		print("Study case: " + self.kasus)

	def fisik(self):
		self.spesifik = "fisik"
		studi_kasus = ["Cyclone", "Erosi", "Banjir"]

		if self.kasus == studi_kasus[0]:
			template = "Mata kuliah yang harus " + self.name + " kuasai adalah: "
			master = "Meteorologi dan Klimatologi, Hidrometeorologi, dan Sistem Informasi Geografis"
			
			print(template, master)
		
		elif self.kasus == studi_kasus[1]:
			template = "Mata kuliah yang harus " + self.name + " kuasai adalah: "
			master = "Ilmu Tanah, Ilmu Ukur Tanah, Geomorfologi, serta Survey Tanah dan Konservasi"
			print(template, master)

		elif self.kasus == studi_kasus[2]:
			template = "Mata kuliah yang harus " + self.name + " kuasai adalah: "
			master = "Hidrometri, Geomorfologi, dan Hidrometeorologi"
			print(template, master)


	def sosial(self):
		self.spesifik = "sosial"
		studi_kasus = ["Inflasi", "Ketenagakerjaan", "Kemiskinan"]

		if self.kasus == studi_kasus[0]:
			template = "Mata kuliah yang harus " + self.name + " kuasai adalah: "
			master = "Geografi Ekonomi, Demografi, dan Geografi Kependudukan"
			print(template, master)

		elif self.kasus == studi_kasus[1]:
			template = "Mata kuliah yang harus " + self.name + " kuasai adalah: "
			master = "Geografi Kependudukan, Pembangunan Sumberdaya Manusia, Ketenagakerjaan, dan Geografi Ekonomi"
			print(template, master)

		elif self.kasus == studi_kasus[2]:
			template = "Mata kuliah yang harus " + self.name + " kuasai adalah: "
			master = "Geografi Kependudukan, Demografi, Pembangunan Sumberdaya Manusia, dan Geografi Ekonomi"
			print(template, master)

rin = Geografi("Rin", "Fisik", "Iklim", "Cyclone")
rin.fisik()
nanda = Geografi("Nanda", "Sosial", "Penduduk", "Ketenagakerjaan")
nanda.sosial()
