class hs:
	def __init__(self,tham_so1,tham_so2):
		self.name = tham_so1
		self.classname = tham_so2
	def in_thong_tin(self):
		print("xin chào mình là", self.name, "minh lớp: ", self.classname)
a = hs("A","6a")
b = hs("B","7b")
a.in_thong_tin()
b.in_thong_tin()
