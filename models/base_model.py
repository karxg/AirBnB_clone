#!/usr/bin/python3
#class BaseModel that defines all common attributes/methods for other classes


class BaseModel:
	def __str__(self):
		return [<type(self)>] (<self.id>) <self.__dict__>
	pass