#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
		
s = Student('Bob',18,90)
print(json.dumps(s))
